---
name: code-prep
description: >
  Prepares Python code for optimal Claude Code comprehension. Generates a CONTEXT.md companion
  file containing an architecture map, class/function inventory, dependency graph, call chains,
  and a change risk map — so Claude Code can orient instantly without reading every file from
  scratch. Optionally enriches source docstrings in place. Use this skill whenever the user
  wants to make a Python file, module, or codebase easier to work with in Claude Code, says
  things like "prep this code", "document this for Claude Code", "map out this codebase",
  "make this easier to debug", "generate a context file", "help Claude Code understand this",
  or asks to annotate/document Python code before a review, refactor, or debugging session.
  Also trigger when the user shares Python code and says it is messy, undocumented, or hard
  to navigate.
---

# Code Prep

Prepares Python codebases for AI-assisted work. Produces a `CONTEXT.md` companion file and
optionally a Repomix-packed source bundle — giving Claude Code everything it needs to orient
itself without reading every source file from scratch.

## Two modes

### Mode A — Context Map (default, non-destructive)
Generates `CONTEXT.md`. Does not touch source files.
Best for: production code, unfamiliar codebases, pre-review orientation.

### Mode B — Deep Annotate
Generates `CONTEXT.md` + rewrites thin/missing docstrings in place.
Best for: work-in-progress or personal projects with poor docstring coverage.
**Always confirm with the user before modifying source files.**

---

## Step 1 — Clarify scope and mode

If not already clear from context, ask:
1. Target path? (single file, directory/module, or project root)
2. Mode A (CONTEXT.md only) or Mode B (CONTEXT.md + enrich docstrings)?

If the user pasted code, write it to a temp file (`/tmp/code_prep_input.py`) before running
the extractor.

---

## Step 2 — Run the structure extractor (Tree-sitter based)

```bash
python <skill_dir>/scripts/extract_structure.py <target_path> [--depth N] [--no-gitignore]
```

**Important**: The script requires `tree-sitter` and `tree-sitter-python`. If not installed:
```bash
pip install tree-sitter tree-sitter-python --break-system-packages
```

The extractor is error-tolerant — files with syntax errors are parsed partially and flagged,
not skipped. It respects `.gitignore` by default.

**Key output fields:**
- `total_tokens_approx` — estimated token count of source code across all files
- `files_with_parse_errors` — files that had syntax issues (still partially parsed)
- `modules[]` — per-file: docstring, imports, globals, classes (with dataclass fields,
  decorator roles), functions
- `call_graph` — namespace-qualified edges (`file.py::Class.method -> file.py::fn`)
- `dependency_map` — relative import relationships between files
- `documentation_gaps` — public functions/methods/classes missing docstrings

**Scale guidance based on `total_tokens_approx`:**
- < 20k tokens: analyse all files in full depth
- 20k–80k tokens: summarize leaf utilities, focus depth on core logic
- > 80k tokens: ask the user to confirm scope or suggest focusing on a subdirectory.
  Also consider running Repomix with compression (see Step 2b).

---

## Step 2b — Optional: Repomix compressed bundle (for large codebases or full-context sessions)

For codebases over 30k tokens, optionally generate a compressed Repomix bundle that
Claude Code can load as supplementary context. This gives full source access at ~70% fewer
tokens than raw files.

```bash
npx repomix <target_path> --compress --output repomix-output.xml
```

Repomix handles `.gitignore` awareness, token counting per file, and secret scanning
automatically. The compressed output uses Tree-sitter to strip whitespace and comments
while preserving structure.

Tell the user: "You can load `repomix-output.xml` in Claude Code for full source access.
`CONTEXT.md` gives the semantic map; Repomix gives the raw compressed source."

---

## Step 3 — Generate CONTEXT.md

Read `references/context-format.md` for the exact section definitions and format templates.

Using the JSON from the extractor plus selective reading of key source files, produce a
`CONTEXT.md` covering:

1. **Purpose and Responsibility** — what this code does and explicitly does NOT do
2. **Architecture Overview** — structure, patterns, key abstractions, ASCII diagram if useful
3. **Module / File Summaries** — per-file: purpose, exports, change sensitivity (HIGH/MED/LOW)
4. **Class and Function Inventory** — precise signatures, roles, gotchas, hidden coupling
5. **Dependency Map** — internal file dependencies + external third-party packages
6. **Call Graph Summary** — entry points, hot paths, recursive calls
7. **Change Risk Map** — blast radius table for realistic change scenarios (highest-value section)
8. **Known Gaps and TODOs** — from `documentation_gaps`, TODO/FIXME/HACK comments, dead code
9. **Claude Code Session Priming** — ready-to-paste context block (see below)

Place `CONTEXT.md` at the root of the target directory (or alongside the file if single-file).

### Token budget for CONTEXT.md

CONTEXT.md should target **under 6,000 tokens** (approximately 24,000 characters).
If it would exceed this:
- Abbreviate Method Inventory for private methods (one-liners only)
- Summarize utility/leaf files in Module Summaries as one sentence each
- Split into `CONTEXT.md` (overview + risk map) + `CONTEXT-inventory.md` (full class/function list)

### Claude Code Session Priming block (Section 9)

This is a ready-to-copy block the user pastes at the top of a Claude Code session or adds
to their project's `CLAUDE.md` file:

```markdown
## Code Context

See `CONTEXT.md` for architecture map, change risk guide, and function inventory.
Before making any changes to this module, read CONTEXT.md — especially the Change Risk Map.

Key constraint: <single most important thing not to break>
Current focus: <what the user is about to do>
```

**Recommend CLAUDE.md injection**: Tell the user: "For persistent loading, add this block to
your project's `.claude/CLAUDE.md` — Claude Code reads it at the start of every session,
so you won't need to re-paste it."

### Quality bar

- Every public class and function must appear in the inventory
- Change Risk Map needs at least 4 rows covering realistic scenarios
- Flag hidden coupling, mutable defaults, and thread-safety issues explicitly
- Write for an AI reader: precise and dense, exact names not vague references
- Never say "appears to" when the code is unambiguous

---

## Step 4 — Mode B: Enrich docstrings (only if confirmed)

For each function/method/class identified in `documentation_gaps` (public, no docstring):

Write a new docstring covering:
- **Purpose**: one sentence
- **Args**: each param with type (if not annotated) and meaning
- **Returns**: what the return value represents
- **Raises**: exceptions that can propagate to the caller
- **Side effects**: I/O, state mutation, network calls

Rules:
- Do not alter logic, code formatting, or variable names
- Preserve existing docstrings if they are substantive (3+ meaningful lines)
- Process file by file, confirming with the user after each file if more than 3 files

---

## Step 5 — Deliver and advise

After generating outputs:

1. Report what was created: `CONTEXT.md` path, token count estimate, Repomix bundle if generated
2. Report any files with parse errors from `files_with_parse_errors`
3. Tell the user how to use it:
   - Inject into `.claude/CLAUDE.md` for persistent loading
   - Or load per-session: start Claude Code with `claude --context CONTEXT.md`
   - Or tell Claude Code inline: "Read CONTEXT.md before making any changes"
4. Suggest regenerating after major refactors or adding new modules

---

## Reference files

- `references/context-format.md` — Full CONTEXT.md section definitions, format templates,
  quality guidelines, and tone notes. Read this before generating CONTEXT.md.
- `scripts/extract_structure.py` — Tree-sitter based extractor. Requires `tree-sitter` and
  `tree-sitter-python`. Outputs JSON to stdout. Error-tolerant, gitignore-aware, token-counting.

---

## Dependencies

- `tree-sitter` + `tree-sitter-python` (pip) — required for extractor
- `repomix` (npx, no install needed) — optional, for compressed source bundles

---

## Edge cases

- **No Python files found**: Report and ask if they meant a different path or a non-Python project
- **Pasted code (no file path)**: Write to `/tmp/code_prep_input.py`, run extractor, clean up after
- **Files with parse errors**: Note each in CONTEXT.md Section 8 (Known Gaps). Do not skip them
- **Codebase > 80k tokens**: Ask user to confirm scope or suggest subdirectory focus
- **Already good docstrings in Mode B**: Skip those functions; report count of functions already covered
- **`__init__.py` files**: Always include — they define the public API surface of a package
- **Dynamic patterns** (metaclasses, `__getattr__`, heavy use of `getattr()`): Note these
  explicitly in Section 2 (Architecture) as "runtime behaviour not captured by static analysis"
- **`CONTEXT.md` exceeds 6,000 tokens**: Split into `CONTEXT.md` + `CONTEXT-inventory.md`
