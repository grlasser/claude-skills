---
name: research-lineage
description: >
  Analyzes code to identify which patterns, algorithms, and techniques map to existing published
  research papers, engineering breakthroughs, and well-known academic contributions. Produces a
  structured "Research Lineage Report" that maps specific code locations to the papers, techniques,
  and intellectual heritage they embody — turning a codebase into an annotated bibliography.

  Use this skill whenever a user asks to: "what research is this code based on", "map this code
  to papers", "what techniques does this implement", "research-lineage this", "annotate this code
  with references", "what algorithms am I using", "which papers describe this approach",
  "trace the academic roots of this code", "find the papers behind this implementation", or any
  request to identify the published research a codebase already implements. Also useful for
  writing related-work sections, building bibliographies for technical documentation, or preparing
  patent prior-art searches based on a codebase.
---

# Research Lineage

Analyzes code to identify which established research papers, algorithms, and engineering techniques
are already embodied in the implementation. Produces a structured **Research Lineage Report**
mapping code locations to their academic and engineering roots.

---

## Phase 1 — Code Archaeology (Catalog What's Implemented)

Read all provided code carefully. For each file or module, identify **techniques in use** — not
what could be improved, but what IS there.

### Technique Inventory

Build a list of every identifiable technique, algorithm, or pattern:

| Category | What to Detect |
|---|---|
| **Algorithms** | Sorting, search, graph traversal, optimization (gradient descent, LP, DP), hashing, scheduling |
| **ML/AI techniques** | Attention mechanisms, transformer blocks, tokenization schemes, embedding methods, loss functions, training loops, RL algorithms, inference strategies |
| **Architectural patterns** | ReAct loops, RAG pipelines, chain-of-thought, self-consistency, reflection, tool-use patterns, multi-agent frameworks, DAG orchestration |
| **Data structures** | KV caches, ring buffers, bloom filters, skip lists, tries, priority queues, knowledge graphs |
| **Retrieval methods** | BM25, TF-IDF, dense retrieval, hybrid search, reranking, late interaction, HyDE |
| **Networking/systems** | Congestion control algorithms, routing protocols, consensus mechanisms, load balancing strategies, telemetry approaches |
| **Statistical methods** | Bayesian inference, hypothesis testing, time-series decomposition, anomaly detection methods, confidence intervals |
| **Security patterns** | Cryptographic primitives, access control models, input sanitization approaches, differential privacy |

### Granularity Rules
- Tag at the **function or class level**, not the file level
- If a function implements a well-known algorithm, name it precisely (e.g., "Dijkstra's shortest path" not "graph search")
- If a pattern combines multiple techniques, list each one separately
- Note any modifications or adaptations to standard algorithms

### Existing Citation Scan
Before searching, scan the codebase for citations already present:
- Docstrings or comments referencing paper titles, arXiv IDs, or DOIs
- README sections with references or bibliography
- Variable/class names that reference papers (e.g., `rotary_embedding`, `dpo_loss`)
- License files or NOTICE files citing upstream research

Collect these as "claimed citations" — they will be verified in Phase 2 and reported in
Coverage Notes.

---

## Phase 2 — Research Discovery (Find the Papers)

For each identified technique, search for the **canonical paper** and any **key follow-up papers**.

### What Constitutes a Match

A code→paper match must satisfy at least ONE of:

1. **Direct Implementation** — the code implements the algorithm described in the paper
2. **Close Variant** — the code adapts or modifies the technique with recognizable differences
3. **Architectural Pattern** — the code follows the system-level design proposed in the paper
4. **Influenced By** — the code uses ideas from the paper without a direct implementation

### Search Strategy

For each technique, search in this priority order:

1. **Canonical/seminal paper** — the original publication that introduced the technique
2. **Survey papers** — that cover the technique as part of a taxonomy (helps confirm lineage)
3. **Implementation papers** — that describe production deployments of the technique
4. **arXiv / conference proceedings** — for the specific variant used in the code

### Concrete Search Guidance

Since this skill identifies **known** techniques (confirmatory search, not discovery), use
targeted queries:

- **If you know the paper name:** search `<paper title> <first author> <year>`
- **If you know the technique but not the paper:** search `<technique name> original paper`
  or `<technique name> seminal paper <domain>`
- **To confirm venue/year:** search `<first author> <short title> conference year`
- **For RFCs/standards:** search `RFC <number>` or `<protocol name> IETF RFC`
- **For networking techniques:** also search with IEEE Xplore, ACM Digital Library terms

Avoid quoted phrases in search queries — most search tools don't support exact-match syntax.

Do NOT waste searches on techniques you can map from the reference file
(`references/technique-paper-map.md`). Search only when the reference file doesn't cover
the technique or you need to verify/update a citation.

### Search Query Construction

Translate code implementations into research vocabulary. A few examples of the pattern:

| Code Implementation | Research Search Terms |
|---|---|
| `attention(Q, K, V)` with masking | Attention Is All You Need Vaswani 2017 |
| RAG pipeline (retrieve→augment→generate) | Retrieval-Augmented Generation Lewis NeurIPS 2020 |
| ReAct-style observe→think→act loop | ReAct Synergizing Reasoning Acting Yao ICLR 2023 |
| LSTM event correlation | Long Short-Term Memory Hochreiter Schmidhuber 1997 |

For 50+ more mappings, load `references/technique-paper-map.md` before searching.

### Verification

For each match, verify by checking:
- Does the code's logic structurally match the paper's pseudocode or algorithm description?
- Are the same mathematical operations present (loss functions, scoring formulas, update rules)?
- Does the code use terminology from the paper (variable names, class names, comments referencing the technique)?

---

## Phase 3 — Lineage Mapping

For each confirmed match, build a lineage entry:

```
MATCH CONFIDENCE (internal, not shown verbatim):
  Match type:          Direct Implementation / Close Variant /
                       Architectural Pattern / Influenced By
  Evidence strength:   Strong (code matches pseudocode or equations) /
                       Moderate (pattern matches, details differ) /
                       Circumstantial (same general approach)

Include as "Direct Implementation" if: code structurally matches paper AND Evidence=Strong
Include as "Close Variant" if: code adapts technique with modifications AND Evidence≥Moderate
Include as "Architectural Pattern" if: code follows system-level design from paper AND Evidence≥Moderate
Include as "Influenced By" if: code uses ideas from paper without direct implementation AND Evidence≥Moderate
Drop if: Evidence=Circumstantial only
```

Map each match to a **specific code location**:
- File name + function/class name + line range (if available)
- Or structural description ("the retrieval pipeline in module X")

---

## Phase 4 — Research Lineage Report (Output Format)

Produce the report in this exact structure.

---

### RESEARCH LINEAGE REPORT

**Codebase:** [name/description]
**Analysis Date:** [date]
**Mappings Found:** [N] technique→paper mappings across [M] categories

---

#### MAPPING #N — [Technique Name]

**Code Location:** `file.py > ClassName.method_name()` or structural description

**What the Code Implements:**
> Concise description of the technique as implemented — what it does, key operations,
> data flow.

**Canonical Paper:**
> **[Paper Title]** — [Authors, Venue, Year] — [URL]
> One-paragraph plain-English explanation of the paper's contribution and how it relates
> to the implementation.

**Match Type:** Direct Implementation | Close Variant | Architectural Pattern | Influenced By

**Key Correspondences:**
> Specific mapping between code constructs and paper concepts. E.g.:
> - `score = dot(Q, K) / sqrt(d_k)` → Equation 1 in Vaswani et al. (scaled dot-product attention)
> - `retrieved_docs + query → augmented_prompt` → Section 3.1 of Lewis et al. (RAG pipeline)

**Variant Notes:** (if applicable)
> How the implementation deviates from or extends the paper. E.g., "Uses RoPE instead of
> sinusoidal positional encoding from the original Transformer."

**Related Papers:** (optional, max 2-3)
> - [Follow-up Paper Title] — [Authors, Year] — [URL] — [one-line description of relevance]

---

[Repeat for each mapping]

---

### LINEAGE SUMMARY TABLE

| # | Technique | Code Location | Canonical Paper | Year | Match Type |
|---|-----------|--------------|-----------------|------|------------|
| 1 | [name] | `file > func` | [Author et al.] | YYYY | Direct |
| ... | | | | | |

### TECHNIQUE TIMELINE

List mappings chronologically by paper publication year to show the intellectual evolution:

- **1997** — LSTM (Hochreiter & Schmidhuber) → `model/encoder.py`
- **2017** — Transformer (Vaswani et al.) → `model/attention.py`
- **2020** — RAG (Lewis et al.) → `retrieval/pipeline.py`
- ...

### COVERAGE NOTES

- **Well-documented techniques:** [list any with clear comments/docstrings citing papers — verify citations are correct]
- **Incorrect citations:** [list any code citations that reference wrong paper, wrong year, or wrong authors]
- **Uncited implementations:** [list any that implement known techniques without attribution]
- **Novel/custom components:** [list any code that doesn't map to known published work — these
  may be original contributions worth documenting or publishing]

### DEPENDENCY LINEAGE (optional, if dependencies are visible)

Key libraries in the dependency tree and their research heritage:

| Dependency | Research Origin | Citation |
|---|---|---|
| e.g. `faiss` | Billion-scale similarity search | Johnson et al., IEEE TBD 2019 |
| e.g. `vllm` | PagedAttention / continuous batching | Kwon et al., SOSP 2023 |

*Only include dependencies that embody specific published research. Skip generic utilities.*

---

## Output

Save the report as `RESEARCH-LINEAGE.md` in the root of the analyzed codebase (or the
working directory if analyzing a snippet). If the codebase already has a `docs/` directory,
save there instead.

---

## Behavioral Guidelines

### Depth Calibration
- **Small code snippet (<100 lines):** 1-3 mappings, focus on the primary technique
- **Module or service (100-1000 lines):** 3-8 mappings across multiple categories
- **Full codebase (1000+ lines):** 5-15 mappings; group by subsystem

### Tone and Honesty
- Never fabricate paper references. If unsure, search. If search returns nothing, say "likely
  implements [technique] but canonical paper could not be confirmed via search."
- Distinguish clearly between: "this IS algorithm X" vs "this resembles the pattern from paper Y"
- When code comments or variable names reference a paper, verify the reference is correct
- If code implements something genuinely novel (no known paper), flag it explicitly in
  Coverage Notes — this is valuable information

### Domain Sensitivity
When analyzing domain-specific code (networking, telecom, AI-Ops):
- Search IEEE Xplore, ACM Digital Library, IETF RFCs, and 3GPP specs
- Check relevant vendor research labs and published technical reports
- Map any YANG models or gNMI patterns to their RFC origins
- Note protocol-specific techniques and their standards lineage (MPLS RFCs, EVPN, SR, etc.)
- For AI-Ops code: also search SIGCOMM, INFOCOM, and IEEE JSAC proceedings

### What NOT to Include
- Generic language features (using a for loop is not "implementing iteration theory")
- Standard library calls (using `sorted()` is not implementing Timsort research)
- Trivial patterns (basic CRUD, simple REST endpoints, config file parsing)
- Techniques the code merely *calls* via a library — focus on what the code *implements*

### Library vs. Implementation Distinction
- If code calls `torch.nn.MultiheadAttention` → note it uses attention but don't map it as
  "implementing" the Transformer paper — the library does that
- If code has a custom attention implementation with the actual `Q @ K.T / sqrt(d)` math →
  that IS an implementation worth mapping
- Borderline: if code orchestrates library calls in a pattern from a paper (e.g., a RAG pipeline
  using LangChain components), map the orchestration pattern, not the individual library calls

---

## Quick Reference: Common Implementation → Paper Mappings

See `references/technique-paper-map.md` (relative to this SKILL.md file) for a curated table
of 50+ code techniques mapped to their canonical papers with exact citations. **Load this file
first** before searching — it covers the most common mappings and saves unnecessary web searches.
In Claude Code CLI context, read it with: `cat <skill-path>/references/technique-paper-map.md`
