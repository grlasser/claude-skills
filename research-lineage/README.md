# Research Lineage

Analyzes code to identify which established research papers, algorithms, and engineering techniques are already embodied in the implementation. Produces a structured **Research Lineage Report** mapping specific code locations to their academic and engineering roots — turning a codebase into an annotated bibliography.

## What It Does

Where [research-scout](../research-scout) looks *forward* ("what research could improve this code?"), research-lineage looks *backward* ("what research does this code already implement?").

It scans your code for recognizable algorithms, architectural patterns, ML techniques, and protocol implementations, then maps each one to its canonical paper or specification — with match type, key correspondences, and variant notes.

## When to Use It

- **Documentation:** auto-generate a references section for your codebase
- **Related work:** build a bibliography for a paper or technical report based on your implementation
- **Prior art:** identify published techniques for patent searches
- **Onboarding:** help new team members understand the intellectual heritage behind the code
- **Citation hygiene:** verify that existing code comments cite the right papers

## Trigger Phrases

```
"what research is this code based on"
"map this code to papers"
"what techniques does this implement"
"research-lineage this"
"annotate this code with references"
"which papers describe this approach"
"trace the academic roots of this code"
"find the papers behind this implementation"
```

## Output

A `RESEARCH-LINEAGE.md` file saved alongside the analyzed code, containing:

- **Per-technique mappings** — code location → canonical paper, match type, key correspondences, variant notes
- **Lineage summary table** — all mappings at a glance
- **Technique timeline** — chronological view showing intellectual evolution (e.g., 1997 LSTM → 2017 Transformer → 2020 RAG)
- **Coverage notes** — well-cited code, uncited implementations, incorrect citations, and genuinely novel components
- **Dependency lineage** — research heritage of key libraries in the dependency tree

## Match Types

| Type | Meaning |
|---|---|
| **Direct Implementation** | Code structurally matches the paper's algorithm or equations |
| **Close Variant** | Code adapts the technique with recognizable modifications |
| **Architectural Pattern** | Code follows the system-level design proposed in the paper |
| **Influenced By** | Code uses ideas from the paper without direct implementation |

## Structure

```
research-lineage/
├── SKILL.md                            # Main skill definition (4 phases)
├── README.md                           # This file
└── references/
    └── technique-paper-map.md          # 50+ technique → canonical paper lookup table
```

The reference map covers: Transformer & Attention, Training & Optimization, Retrieval & RAG, Agentic / Reasoning Patterns, Sequence Models, Networking & Systems (incl. RFCs), and Anomaly Detection & AIOps.

## Example

Given a file with a custom attention implementation and a RAG pipeline, the report might include:

```
#### MAPPING #1 — Scaled Dot-Product Attention

**Code Location:** `model/attention.py > SelfAttention.forward()`

**What the Code Implements:**
> Custom multi-head attention with scaled dot-product scoring and causal masking.

**Canonical Paper:**
> **Attention Is All You Need** — Vaswani et al., NeurIPS 2017
> Introduced the Transformer architecture and the scaled dot-product attention mechanism.

**Match Type:** Direct Implementation

**Key Correspondences:**
> - `scores = Q @ K.T / math.sqrt(d_k)` → Equation 1 (scaled dot-product attention)
> - `attn = softmax(scores + mask)` → Section 3.2.1 (masked attention)

**Variant Notes:**
> Uses RoPE (Su et al., 2021) instead of sinusoidal positional encoding from the original paper.
```

## Installation

```bash
ln -s ~/Projects/claude-skills/research-lineage ~/.claude/skills/research-lineage
```

## See Also

- [research-scout](../research-scout) — the forward-looking complement: finds research that could *improve* your code
