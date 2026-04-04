#!/usr/bin/env python3
"""
extract_structure.py — Tree-sitter based Python code structure extractor.

Improvements over AST-based version:
  - Error-tolerant: parses files with syntax errors instead of skipping them
  - Captures decorators properly (@property, @classmethod, @staticmethod)
  - Namespace-aware call graph (no false cross-module edges from name collisions)
  - Token counting per file and total
  - .gitignore support
  - Dataclass field detection

Usage:
    python extract_structure.py <path>           # file or directory
    python extract_structure.py <path> --depth 2 # limit directory recursion
    python extract_structure.py <path> --no-gitignore  # ignore .gitignore rules
"""

import json
import sys
import os
import re
import argparse
from pathlib import Path
from collections import defaultdict

try:
    import tree_sitter_python as tsp
    from tree_sitter import Language, Parser
    PY_LANGUAGE = Language(tsp.language())
    _parser = Parser(PY_LANGUAGE)
    TREE_SITTER_AVAILABLE = True
except ImportError:
    TREE_SITTER_AVAILABLE = False
    import ast  # fallback


# ---------------------------------------------------------------------------
# Token counting (approximation: 1 token ≈ 4 chars for code)
# ---------------------------------------------------------------------------

def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


# ---------------------------------------------------------------------------
# .gitignore reader
# ---------------------------------------------------------------------------

def load_gitignore_patterns(root: Path) -> list:
    """Return compiled regex patterns from .gitignore."""
    patterns = []
    gitignore = root / ".gitignore"
    if not gitignore.exists():
        return patterns
    for line in gitignore.read_text(errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Convert glob to regex (basic)
        regex = line.replace(".", r"\.").replace("*", ".*").replace("?", ".")
        if not regex.startswith("/"):
            regex = "(^|/)" + regex
        if regex.endswith("/"):
            regex = regex + ".*"
        try:
            patterns.append(re.compile(regex))
        except re.error:
            pass
    return patterns


def is_gitignored(path: Path, root: Path, patterns: list) -> bool:
    try:
        rel = str(path.relative_to(root))
    except ValueError:
        rel = str(path)
    return any(p.search(rel) for p in patterns)


# ---------------------------------------------------------------------------
# Tree-sitter helpers
# ---------------------------------------------------------------------------

def get_text(node, src: bytes) -> str:
    return src[node.start_byte:node.end_byte].decode("utf-8", errors="replace")


def first_child_of_type(node, *types):
    for child in node.children:
        if child.type in types:
            return child
    return None


def all_children_of_type(node, *types):
    return [c for c in node.children if c.type in types]


def extract_docstring_ts(body_node, src: bytes) -> str | None:
    """Extract docstring from a body node (class body or function body)."""
    if body_node is None:
        return None
    for child in body_node.children:
        if child.type == "expression_statement":
            for sub in child.children:
                if sub.type == "string":
                    text = get_text(sub, src).strip()
                    # Strip quotes
                    for q in ['"""', "'''", '"', "'"]:
                        if text.startswith(q) and text.endswith(q) and len(text) > 2 * len(q):
                            return text[len(q):-len(q)].strip()
                    return text
        elif child.type not in ("comment", "\n"):
            break
    return None


def extract_decorators(node, src: bytes) -> list[dict]:
    """Extract decorators from a decorated_definition or function/class node."""
    result = []
    for child in node.children:
        if child.type == "decorator":
            text = get_text(child, src).strip()
            name = text.lstrip("@").split("(")[0].strip()
            result.append({"text": text, "name": name})
    return result


def extract_params_ts(params_node, src: bytes) -> list[dict]:
    """Extract parameter list from a parameters node."""
    if params_node is None:
        return []
    params = []
    for child in params_node.children:
        if child.type in (",", "(", ")", "comment"):
            continue
        if child.type == "identifier":
            params.append({"name": get_text(child, src), "annotation": None, "default": None, "kind": "regular"})
        elif child.type == "typed_parameter":
            name_node = first_child_of_type(child, "identifier")
            ann_node = first_child_of_type(child, "type")
            name = get_text(name_node, src) if name_node else "?"
            ann = get_text(ann_node, src) if ann_node else None
            params.append({"name": name, "annotation": ann, "default": None, "kind": "regular"})
        elif child.type == "default_parameter":
            name_node = first_child_of_type(child, "identifier")
            # Default value is after the = sign
            parts = get_text(child, src).split("=", 1)
            name = parts[0].strip()
            default = parts[1].strip() if len(parts) > 1 else None
            params.append({"name": name, "annotation": None, "default": default, "kind": "regular"})
        elif child.type == "typed_default_parameter":
            name_node = first_child_of_type(child, "identifier")
            ann_node = first_child_of_type(child, "type")
            name = get_text(name_node, src) if name_node else "?"
            ann = get_text(ann_node, src) if ann_node else None
            text = get_text(child, src)
            default = text.split("=", 1)[1].strip() if "=" in text else None
            params.append({"name": name, "annotation": ann, "default": default, "kind": "regular"})
        elif child.type == "list_splat_pattern":
            inner = first_child_of_type(child, "identifier")
            name = "*" + (get_text(inner, src) if inner else "")
            params.append({"name": name, "annotation": None, "default": None, "kind": "var_positional"})
        elif child.type == "dictionary_splat_pattern":
            inner = first_child_of_type(child, "identifier")
            name = "**" + (get_text(inner, src) if inner else "")
            params.append({"name": name, "annotation": None, "default": None, "kind": "var_keyword"})
        elif child.type == "keyword_separator":
            pass  # bare *
    return params


def collect_calls(body_node, src: bytes) -> list[str]:
    """Collect all function call targets within a node."""
    calls = set()
    if body_node is None:
        return []

    def walk(node):
        if node.type == "call":
            fn_node = node.child_by_field_name("function")
            if fn_node:
                text = get_text(fn_node, src)
                # Only collect simple identifiers and attribute calls (foo.bar)
                if re.match(r'^[\w][\w.]*$', text):
                    calls.add(text)
        for child in node.children:
            walk(child)

    walk(body_node)
    return sorted(calls)


def collect_raises(body_node, src: bytes) -> list[str]:
    if body_node is None:
        return []
    raises = []

    def walk(node):
        if node.type == "raise_statement":
            for child in node.children:
                if child.type not in ("raise", "comment"):
                    raises.append(get_text(child, src).split("(")[0].strip())
        for child in node.children:
            walk(child)

    walk(body_node)
    return list(set(raises))


def is_async(node) -> bool:
    return node.type == "function_definition" and any(
        c.type == "async" for c in (node.parent.children if node.parent else [])
    ) or node.type == "async_function_definition" or (
        node.parent and node.parent.type == "async_statement"
    )


def extract_function_ts(fn_node, src: bytes, decorators: list[dict] | None = None) -> dict:
    """Extract metadata from a function_definition node."""
    name_node = fn_node.child_by_field_name("name")
    params_node = fn_node.child_by_field_name("parameters")
    return_node = fn_node.child_by_field_name("return_type")
    body_node = fn_node.child_by_field_name("body")

    name = get_text(name_node, src) if name_node else "?"
    params = extract_params_ts(params_node, src)
    return_ann = get_text(return_node, src).lstrip("->").strip() if return_node else None
    doc = extract_docstring_ts(body_node, src)
    calls = collect_calls(body_node, src)
    raises = collect_raises(body_node, src)

    # Decorator semantic roles
    dec_names = {d["name"] for d in (decorators or [])}
    role = "method"
    if "property" in dec_names or "cached_property" in dec_names:
        role = "property"
    elif "classmethod" in dec_names:
        role = "classmethod"
    elif "staticmethod" in dec_names:
        role = "staticmethod"
    elif name == "__init__":
        role = "constructor"
    elif name.startswith("__") and name.endswith("__"):
        role = "dunder"
    elif name.startswith("_"):
        role = "private"

    # Check for async — tree-sitter represents async differently
    fn_text = get_text(fn_node, src)
    fn_is_async = fn_text.lstrip().startswith("async ")

    # Check for generator
    is_generator = False
    def check_yield(node):
        nonlocal is_generator
        if node.type in ("yield", "yield_from"):
            is_generator = True
        for c in node.children:
            check_yield(c)
    if body_node:
        check_yield(body_node)

    return {
        "name": name,
        "line": fn_node.start_point[0] + 1,
        "end_line": fn_node.end_point[0] + 1,
        "role": role,
        "is_async": fn_is_async,
        "is_generator": is_generator,
        "decorators": [d["text"] for d in (decorators or [])],
        "params": params,
        "return_annotation": return_ann,
        "docstring": doc,
        "raises": raises,
        "calls_made": calls,
        "has_docstring": doc is not None,
    }


def _extract_class_var(assignment_node, src: bytes, class_vars: list, parent_node) -> None:
    """Parse a tree-sitter assignment node inside a class body into a class_var entry."""
    children = assignment_node.children
    name = None
    annotation = None
    value_preview = None
    # Parse: identifier [: type] [= value]
    i = 0
    while i < len(children):
        c = children[i]
        if c.type == "identifier" and name is None:
            name = get_text(c, src)
        elif c.type == "type":
            annotation = get_text(c, src)
        elif c.type == "=" and i + 1 < len(children):
            value_preview = get_text(children[i + 1], src)[:60]
            break
        i += 1
    if name:
        class_vars.append({
            "name": name,
            "annotation": annotation,
            "value_preview": value_preview,
            "line": parent_node.start_point[0] + 1,
        })


def extract_class_ts(cls_node, src: bytes, decorators: list[dict] | None = None) -> dict:
    """Extract metadata from a class_definition node."""
    name_node = cls_node.child_by_field_name("name")
    body_node = cls_node.child_by_field_name("body")
    superclasses_node = cls_node.child_by_field_name("superclasses")

    name = get_text(name_node, src) if name_node else "?"

    # Base classes
    bases = []
    if superclasses_node:
        for child in superclasses_node.children:
            if child.type not in (",", "(", ")"):
                bases.append(get_text(child, src))

    doc = extract_docstring_ts(body_node, src)

    # Is dataclass?
    dec_names = {d["name"] for d in (decorators or [])}
    is_dataclass = "dataclass" in dec_names

    methods = []
    class_vars = []

    if body_node:
        for child in body_node.children:
            fn_node = None
            fn_decorators = []

            if child.type == "decorated_definition":
                fn_decorators = extract_decorators(child, src)
                fn_node = first_child_of_type(child, "function_definition")
            elif child.type == "function_definition":
                fn_node = child

            if fn_node:
                m = extract_function_ts(fn_node, src, fn_decorators)
                m["class"] = name
                methods.append(m)

            # Class-level variable assignments — in tree-sitter these are
            # expression_statement > assignment nodes (not top-level assignment nodes)
            elif child.type == "expression_statement":
                inner = child.children[0] if child.children else None
                if inner and inner.type == "assignment":
                    _extract_class_var(inner, src, class_vars, child)

    return {
        "name": name,
        "line": cls_node.start_point[0] + 1,
        "end_line": cls_node.end_point[0] + 1,
        "bases": bases,
        "decorators": [d["text"] for d in (decorators or [])],
        "is_dataclass": is_dataclass,
        "docstring": doc,
        "has_docstring": doc is not None,
        "class_vars": class_vars,
        "methods": methods,
    }


def extract_imports_ts(root_node, src: bytes) -> list[dict]:
    imports = []
    for node in root_node.children:
        if node.type == "import_statement":
            for name_node in node.children:
                if name_node.type in ("dotted_name", "aliased_import"):
                    text = get_text(name_node, src)
                    module = text.split(" as ")[0].strip()
                    alias = text.split(" as ")[1].strip() if " as " in text else None
                    imports.append({
                        "type": "import",
                        "module": module,
                        "alias": alias,
                        "line": node.start_point[0] + 1,
                        "is_stdlib": _is_likely_stdlib(module),
                    })
        elif node.type == "import_from_statement":
            module_node = node.child_by_field_name("module_name")
            module = get_text(module_node, src) if module_node else ""
            # Count leading dots for relative imports
            level = 0
            for child in node.children:
                if child.type == ".":
                    level += 1
                elif child.type == "relative_import":
                    level_text = get_text(child, src)
                    level = len(level_text) - len(level_text.lstrip("."))
            for child in node.children:
                if child.type in ("dotted_name", "identifier"):
                    if child == module_node:
                        continue
                    imports.append({
                        "type": "from_import",
                        "module": module,
                        "name": get_text(child, src),
                        "alias": None,
                        "level": level,
                        "line": node.start_point[0] + 1,
                        "is_stdlib": _is_likely_stdlib(module),
                    })
                elif child.type == "aliased_import":
                    text = get_text(child, src)
                    name = text.split(" as ")[0].strip()
                    alias = text.split(" as ")[1].strip() if " as " in text else None
                    imports.append({
                        "type": "from_import",
                        "module": module,
                        "name": name,
                        "alias": alias,
                        "level": level,
                        "line": node.start_point[0] + 1,
                        "is_stdlib": _is_likely_stdlib(module),
                    })
    return imports


_KNOWN_STDLIB = {
    "os", "sys", "re", "io", "math", "json", "time", "datetime", "pathlib",
    "typing", "collections", "itertools", "functools", "operator", "abc",
    "copy", "dataclasses", "enum", "logging", "traceback", "warnings",
    "threading", "multiprocessing", "asyncio", "subprocess", "socket",
    "http", "urllib", "email", "csv", "hashlib", "hmac", "secrets",
    "unittest", "contextlib", "inspect", "importlib", "pkgutil", "types",
    "string", "textwrap", "pprint", "struct", "array", "queue", "heapq",
    "bisect", "weakref", "gc", "platform", "shutil", "glob", "fnmatch",
    "tempfile", "stat", "zipfile", "tarfile", "gzip", "configparser",
    "argparse", "signal", "atexit", "builtins", "concurrent", "selectors",
}

def _is_likely_stdlib(module_name):
    root = module_name.split(".")[0] if module_name else ""
    return root in _KNOWN_STDLIB


def extract_globals_ts(root_node, src: bytes) -> list[dict]:
    globals_list = []
    for node in root_node.children:
        if node.type in ("assignment", "annotated_assignment", "typed_assignment"):
            lhs = (node.child_by_field_name("left")
                   or node.child_by_field_name("name"))
            ann = (node.child_by_field_name("type")
                   or node.child_by_field_name("annotation"))
            rhs = (node.child_by_field_name("right")
                   or node.child_by_field_name("value"))
            if lhs:
                globals_list.append({
                    "name": get_text(lhs, src),
                    "annotation": get_text(ann, src) if ann else None,
                    "value_preview": get_text(rhs, src)[:80] if rhs else None,
                    "line": node.start_point[0] + 1,
                })
    return globals_list


# ---------------------------------------------------------------------------
# File parser
# ---------------------------------------------------------------------------

def parse_file(filepath: Path, root: Path) -> dict:
    try:
        src_text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return {"file": str(filepath), "relative_path": str(filepath.relative_to(root)),
                "error": str(e), "parse_failed": True, "token_count": 0}

    src = src_text.encode("utf-8", errors="replace")
    line_count = src_text.count("\n") + 1
    token_count = estimate_tokens(src_text)

    try:
        rel = str(filepath.relative_to(root))
    except ValueError:
        rel = str(filepath)

    if not TREE_SITTER_AVAILABLE:
        return _parse_file_ast_fallback(filepath, src_text, rel, line_count, token_count)

    tree = _parser.parse(src)
    root_node = tree.root_node

    has_errors = root_node.has_error
    module_docstring = None

    # Module docstring: first expression_statement with a string
    for child in root_node.children:
        if child.type == "expression_statement":
            for sub in child.children:
                if sub.type == "string":
                    module_docstring = get_text(sub, src).strip("\"'").strip()
            break
        elif child.type not in ("comment", "\n"):
            break

    classes = []
    functions = []

    for child in root_node.children:
        if child.type == "decorated_definition":
            decs = extract_decorators(child, src)
            inner = first_child_of_type(child, "class_definition")
            if inner:
                classes.append(extract_class_ts(inner, src, decs))
                continue
            inner = first_child_of_type(child, "function_definition")
            if inner:
                fn = extract_function_ts(inner, src, decs)
                functions.append(fn)
        elif child.type == "class_definition":
            classes.append(extract_class_ts(child, src))
        elif child.type == "function_definition":
            functions.append(extract_function_ts(child, src))

    imports = extract_imports_ts(root_node, src)
    globals_list = extract_globals_ts(root_node, src)

    return {
        "file": str(filepath),
        "relative_path": rel,
        "line_count": line_count,
        "token_count": token_count,
        "has_parse_errors": has_errors,
        "module_docstring": module_docstring,
        "imports": imports,
        "globals": globals_list,
        "classes": classes,
        "functions": functions,
    }


def _parse_file_ast_fallback(filepath, src_text, rel, line_count, token_count):
    """Minimal AST fallback when tree-sitter is unavailable."""
    import ast
    try:
        tree = ast.parse(src_text, filename=str(filepath))
    except SyntaxError as e:
        return {"file": str(filepath), "relative_path": rel, "error": f"SyntaxError: {e}",
                "parse_failed": True, "token_count": token_count}
    return {
        "file": str(filepath),
        "relative_path": rel,
        "line_count": line_count,
        "token_count": token_count,
        "has_parse_errors": False,
        "module_docstring": ast.get_docstring(tree),
        "imports": [],
        "globals": [],
        "classes": [{"name": n.name, "line": n.lineno} for n in ast.walk(tree) if isinstance(n, ast.ClassDef)],
        "functions": [{"name": n.name, "line": n.lineno} for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)],
        "fallback": True,
    }


# ---------------------------------------------------------------------------
# Call graph — namespace-aware
# ---------------------------------------------------------------------------

def build_call_graph(modules: list[dict]) -> dict:
    """
    Build a call graph with namespaced keys to avoid false cross-module edges.

    Keys use the format:  relative/path.py::ClassName.method  or  path.py::fn
    Edges only connect to names actually defined in this project.
    """
    # Build a registry: short_name -> [qualified_name]
    defined = defaultdict(list)  # short name -> list of qualified names

    for mod in modules:
        rp = mod.get("relative_path", mod["file"])
        for fn in mod.get("functions", []):
            qname = f"{rp}::{fn['name']}"
            defined[fn["name"]].append(qname)
        for cls in mod.get("classes", []):
            for method in cls.get("methods", []):
                short = f"{cls['name']}.{method['name']}"
                qname = f"{rp}::{short}"
                defined[short].append(qname)
                defined[method["name"]].append(qname)

    edges = {}
    for mod in modules:
        rp = mod.get("relative_path", mod["file"])
        for fn in mod.get("functions", []):
            caller = f"{rp}::{fn['name']}"
            callees = []
            for call in fn.get("calls_made", []):
                # Resolve: check exact match first, then short name
                matches = defined.get(call) or defined.get(call.split(".")[-1]) or []
                # Filter out self-reference
                callees.extend(m for m in matches if m != caller)
            if callees:
                edges[caller] = sorted(set(callees))

        for cls in mod.get("classes", []):
            for method in cls.get("methods", []):
                caller = f"{rp}::{cls['name']}.{method['name']}"
                callees = []
                for call in method.get("calls_made", []):
                    matches = defined.get(call) or defined.get(call.split(".")[-1]) or []
                    callees.extend(m for m in matches if m != caller)
                if callees:
                    edges[caller] = sorted(set(callees))

    return edges


def build_dependency_map(modules: list[dict]) -> dict:
    """Internal import relationships (relative imports only)."""
    dep_map = {}
    for mod in modules:
        deps = []
        for imp in mod.get("imports", []):
            if imp.get("level", 0) > 0:
                deps.append({
                    "module": imp.get("module", ""),
                    "name": imp.get("name"),
                    "type": "relative",
                })
        if deps:
            dep_map[mod.get("relative_path", mod["file"])] = deps
    return dep_map


def build_documentation_gaps(modules: list[dict]) -> list[dict]:
    """Identify public functions/methods missing docstrings."""
    gaps = []
    for mod in modules:
        rp = mod.get("relative_path", mod["file"])
        for fn in mod.get("functions", []):
            if not fn.get("has_docstring") and not fn["name"].startswith("_"):
                gaps.append({"file": rp, "type": "function", "name": fn["name"], "line": fn["line"]})
        for cls in mod.get("classes", []):
            if not cls.get("has_docstring"):
                gaps.append({"file": rp, "type": "class", "name": cls["name"], "line": cls["line"]})
            for m in cls.get("methods", []):
                if not m.get("has_docstring") and m["role"] not in ("dunder", "private"):
                    gaps.append({"file": rp, "type": "method",
                                 "name": f"{cls['name']}.{m['name']}", "line": m["line"]})
    return gaps


# ---------------------------------------------------------------------------
# File collection
# ---------------------------------------------------------------------------

SKIP_DIRS = {
    "__pycache__", ".git", ".venv", "venv", "env", ".env", "node_modules",
    ".eggs", "dist", "build", ".mypy_cache", ".pytest_cache", ".tox",
    "htmlcov", ".cache", ".ruff_cache", "site-packages",
}


def collect_python_files(root: Path, max_depth: int | None, gitignore_patterns: list,
                         use_gitignore: bool, current_depth: int = 0) -> list[Path]:
    files = []
    if max_depth is not None and current_depth > max_depth:
        return files
    try:
        for item in sorted(root.iterdir()):
            if use_gitignore and is_gitignored(item, root, gitignore_patterns):
                continue
            if item.is_file() and item.suffix == ".py":
                files.append(item)
            elif (item.is_dir() and item.name not in SKIP_DIRS
                  and not item.name.startswith(".")):
                files.extend(collect_python_files(
                    item, max_depth, gitignore_patterns, use_gitignore, current_depth + 1
                ))
    except PermissionError:
        pass
    return files


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Extract Python code structure (Tree-sitter based).")
    ap.add_argument("path", help="File or directory to analyse")
    ap.add_argument("--depth", type=int, default=None, help="Max directory recursion depth")
    ap.add_argument("--no-gitignore", action="store_true", help="Ignore .gitignore rules")
    args = ap.parse_args()

    target = Path(args.path).resolve()
    if not target.exists():
        print(json.dumps({"error": f"Path not found: {target}"}))
        sys.exit(1)

    use_gitignore = not args.no_gitignore

    if target.is_file():
        files = [target]
        root = target.parent
    else:
        root = target
        gitignore_patterns = load_gitignore_patterns(root) if use_gitignore else []
        files = collect_python_files(root, args.depth, gitignore_patterns, use_gitignore)

    modules = [parse_file(f, root) for f in files]

    call_graph = build_call_graph(modules)
    dependency_map = build_dependency_map(modules)
    documentation_gaps = build_documentation_gaps(modules)

    total_tokens = sum(m.get("token_count", 0) for m in modules)
    parse_errors = [m["relative_path"] for m in modules if m.get("has_parse_errors")]

    output = {
        "extractor": "tree-sitter" if TREE_SITTER_AVAILABLE else "ast-fallback",
        "root": str(root),
        "total_files": len(modules),
        "total_lines": sum(m.get("line_count", 0) for m in modules),
        "total_tokens_approx": total_tokens,
        "files_with_parse_errors": parse_errors,
        "modules": modules,
        "call_graph": call_graph,
        "dependency_map": dependency_map,
        "documentation_gaps": documentation_gaps,
    }

    print(json.dumps(output, indent=2, default=str))


if __name__ == "__main__":
    main()
