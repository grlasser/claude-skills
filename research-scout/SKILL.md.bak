---
name: research-scout
description: >
  Analyzes code to identify patterns, architectures, and techniques in use, then searches for
  recent academic research papers and engineering breakthroughs that could improve or optimize
  the code. Produces a structured "Research Upgrade Report" that maps each finding to specific
  code locations, explains the technique, and proposes a concrete new design or implementation.

  Use this skill whenever a user asks to: "find research that could improve this code",
  "look for better techniques for this implementation", "are there new papers on this pattern",
  "can AI agent context caching improve this", "what does recent research say about X in my code",
  "research-scout this", "scout this code for improvements", or any request to cross-reference
  code with academic or engineering state-of-the-art. Also trigger proactively when the user
  shares a substantial codebase and asks for a deep review or optimization pass — research-backed
  suggestions are almost always valuable in that context.
---

# Research Scout

Analyzes code to surface cutting-edge research and engineering techniques that could materially
improve or optimize it. Produces a structured, actionable **Research Upgrade Report**.

---

## Phase 1 — Code Archaeology (Understand Before Searching)

Read all provided code carefully. For each file or module, identify:

### Pattern Catalog
Build a mental or written inventory of:

| Category | What to Look For |
|---|---|
| **Architectural patterns** | Agent loops, harnesses, orchestrators, pipelines, DAGs, FSMs |
| **AI/ML techniques** | Prompt construction, context management, embedding usage, RAG, fine-tuning hooks |
| **Data structures** | How state is stored, passed, and mutated across calls |
| **I/O and latency** | API calls, DB queries, file I/O — anything that could be batched, cached, or deferred |
| **Concurrency model** | Sync vs async, thread/process pools, event loops |
| **Memory management** | How context windows, buffers, queues are managed |
| **Evaluation/feedback loops** | How the system measures or corrects its own output |
| **Security surface** | Input sanitization, secrets handling, trust boundaries |

### Anti-Pattern Flags
Highlight anything that is:
- Reinventing a solved problem (custom tokenizers, hand-rolled attention, bespoke schedulers)
- Using a 2021-era technique for a problem that has 2024 solutions
- Creating unnecessary overhead (full context re-serialization, redundant embedding recomputation)
- Missing a feedback or correction mechanism where one is now standard practice

---

## Phase 2 — Research Discovery (Search Strategically)

For each identified pattern or anti-pattern, conduct targeted web searches. Prioritize:

### Search Targets (in order of priority)
1. **arXiv** — `site:arxiv.org <pattern> <domain> 2024 OR 2025`
2. **Papers With Code** — `paperswithcode.com <technique>`
3. **Semantic Scholar** — for citation networks around a core paper
4. **Engineering blogs** — Google DeepMind, Anthropic, OpenAI, Meta AI, Hugging Face, Mistral
5. **GitHub trending / releases** — for implementation-ready libraries
6. **ACL Anthology / NeurIPS / ICML / ICLR proceedings** — for rigorously reviewed results

### Search Query Construction
Translate code patterns into research vocabulary:

| Code Pattern Observed | Research Search Terms |
|---|---|
| Agent loop with tool use | "agentic AI tool use optimization", "ReAct agent efficiency 2024" |
| Large context passed every call | "KV cache reuse LLM inference", "context compaction techniques", "prompt caching" |
| RAG with cosine similarity | "RAG retrieval optimization 2024", "ColBERT late interaction", "HyDE hypothetical document" |
| Multi-agent orchestration | "multi-agent coordination LLM 2024", "agent communication protocols" |
| Repeated LLM calls for reasoning | "chain of thought efficiency", "speculative decoding", "self-consistency sampling" |
| Embedding re-computation | "embedding caching", "dense retrieval batching" |
| Sequential tool calls | "parallel tool use LLM", "tool call batching agents" |
| Fine-tuning loop | "RLHF alternatives 2024", "DPO direct preference optimization", "GRPO" |
| Prompt templates hardcoded | "dynamic prompting", "meta-prompting", "automatic prompt optimization APE" |

### Credibility Filter
Only surface research that meets at least ONE of:
- Published at a top venue (NeurIPS, ICML, ICLR, ACL, EMNLP, SIGIR) OR arXiv with 50+ citations
- Implemented in a production system at a major lab (cite the engineering post)
- Has a working open-source implementation linked

---

## Phase 3 — Relevance Mapping

For each research finding, score and filter before writing the report:

```
RELEVANCE SCORE (internal, not shown to user):
  Impact potential:    High / Medium / Low
  Implementation cost: Low / Medium / High
  Evidence strength:   Strong / Moderate / Speculative
  
Keep if: (Impact=High OR Impact=Medium) AND Evidence=Strong OR Moderate
Drop if: Impact=Low OR Evidence=Speculative with no implementation
```

Also map each finding to a **specific code location**:
- File name + function/class name + line range (if provided)
- Or a structural description ("the agent harness loop in module X")

---

## Phase 4 — Research Upgrade Report (Output Format)

Produce the report in this exact structure. Be specific, not generic.

---

### RESEARCH UPGRADE REPORT

**Codebase:** [name/description]
**Analysis Date:** [date]
**Findings:** [N] upgrade opportunities across [M] categories

---

#### FINDING #N — [Short Title]

**Code Location:** `file.py > ClassName.method_name()` or structural description

**What the Code Currently Does:**
> Concise description of the current pattern and its limitations

**Research Finding:**
> **[Paper/Technique Name]** — [Authors, Venue, Year] — [URL]
> One-paragraph plain-English explanation of what this technique does and why it matters.

**Why This Applies Here:**
> Specific reasoning connecting the paper's contribution to the code's current limitation.
> Include measured improvements from the paper (e.g., "reduces inference latency by 40% on
> comparable workloads") when available.

**Proposed New Design:**
> High-level description of what changes — architectural decisions, new data flows, new components.

**Proposed Implementation:**
```python
# Concrete code sketch showing the key change.
# This does NOT need to be complete — focus on the novel part.
# Show before vs after if helpful.
```

**Estimated Effort:** [hours/days estimate]
**Risk:** [Low / Medium / High] — [one sentence on what could go wrong]

---

[Repeat for each finding]

---

### SUMMARY TABLE

| # | Finding | Category | Impact | Effort | Risk |
|---|---------|----------|--------|--------|------|
| 1 | [title] | [AI/Perf/Security/etc] | High | 2d | Low |
| ... | | | | | |

### RECOMMENDED PRIORITY ORDER

Based on impact-to-effort ratio:

1. **Quick wins (do first):** [finding numbers]
2. **High-value investments:** [finding numbers]
3. **Exploratory / R&D:** [finding numbers]

---

## Behavioral Guidelines

### Depth Calibration
- **Small code snippet (<100 lines):** 2-4 findings, focus on the dominant pattern
- **Module or service (100-1000 lines):** 4-8 findings across multiple categories
- **Full codebase (1000+ lines):** 6-12 findings; group by subsystem

### Tone and Honesty
- Never invent papers. If search returns nothing credible, say so and suggest where to look.
- Distinguish clearly between: "this is deployed at scale by [org]" vs "this is a promising preprint"
- Flag when a technique requires significant infrastructure change (e.g., switching to a different
  inference backend) — don't undersell the cost

### Domain Sensitivity
For Nokia/networking/AI-Ops code specifically:
- Also search IEEE, IFIP, IETF RFCs, and vendor research blogs (Nokia Bell Labs, Cisco Research,
  Juniper AI)
- Flag any technique that has EU AI Act compliance implications (explainability, auditability)
- Note when a technique requires cloud inference vs. can run on-premise

### What NOT to Include
- Generic "best practices" that aren't research-backed
- Techniques the code already uses correctly
- Papers that are only tangentially related
- Vague suggestions like "consider using caching" without a specific mechanism and citation

---

## Quick Reference: Common Code-to-Research Mappings

See `references/pattern-research-map.md` for a curated table of 40+ code patterns mapped
to relevant research areas and suggested search terms. Load this file when you need to quickly
identify search terms for an unfamiliar pattern.
