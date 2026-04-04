---
name: research-scout
description: >
  Analyzes code to identify patterns, architectures, and techniques in use, then searches for
  recent academic research papers and engineering breakthroughs that could improve or optimize
  the code. Produces a structured "Research Upgrade Report" that maps each finding to specific
  code locations, explains the technique, and proposes a concrete new design or implementation.
  Use this skill whenever a user asks to "find research that could improve this code", "look for
  better techniques", "are there new papers on this pattern", "research-scout this", "scout this
  code for improvements", or any request to cross-reference code with academic or engineering
  state-of-the-art. Also trigger proactively when the user shares a substantial codebase and
  asks for a deep review or optimization pass — research-backed suggestions are almost always
  valuable in that context.
---

# Research Scout

Analyzes code to surface cutting-edge research and engineering techniques that could materially
improve or optimize it. Produces a structured, actionable **Research Upgrade Report**.

---

## Step 0 — Intake (Do This Before Anything Else)

Before reading any code, collect the following from the user or infer from context:

**Mode** — ask if not obvious:
- `quick-scan`: High-level radar only — what areas are worth researching? (no deep report)
- `deep-dive`: Full Research Upgrade Report with code sketches and effort estimates (default)

**Focus area** (optional) — e.g., "focus on latency", "focus on the agent loop", "focus on memory"
If provided, weight Phase 1 and Phase 2 toward that area. Still note other critical findings briefly.

**Already tried** (optional) — e.g., "we already evaluated ColBERT", "we use RAG"
Record these explicitly. Do NOT produce findings for techniques already in use or already evaluated
and rejected. If a finding is adjacent to something already tried, flag it as "related to your
existing work on X" rather than treating it as new.

**Language and runtime** — infer from code, confirm if ambiguous.
All code sketches in Phase 4 must use the actual language of the codebase.

---

## Phase 1 — Code Archaeology (Produce a Written Catalog)

**Do not proceed to Phase 2 until this catalog is written out explicitly.**
The catalog is a visible artifact, not internal notes. Show it to the user before searching.

### 1a — Large Codebase Fast-Scan Strategy

If the input exceeds ~500 lines:
1. Read entry points, main loops, and orchestration layers first
2. Sample 2-3 representative modules or classes
3. Note which subsystems you have NOT read — be explicit about coverage gaps
4. Ask user if any unread subsystem is the actual focus before proceeding

### 1b — Pattern Catalog (Write This Out)

For each identified pattern, write one line per entry:

```
PATTERN CATALOG
───────────────────────────────────────────────────────
[Category]         | [Pattern observed]         | [File/location]
───────────────────────────────────────────────────────
Architectural      | Agent loop with tool use   | agent/harness.py > run()
AI/ML              | Full context passed every  | agent/harness.py > call_llm()
                   | LLM call, no caching       |
Concurrency        | Synchronous tool calls,    | tools/executor.py
                   | no parallelism             |
State management   | In-memory dict, lost on    | session/state.py
                   | restart                    |
...
```

Categories to check:

| Category | What to Look For |
|---|---|
| **Architectural** | Agent loops, harnesses, orchestrators, pipelines, DAGs, FSMs |
| **AI/ML** | Prompt construction, context management, embedding usage, RAG, fine-tuning hooks |
| **Data structures** | How state is stored, passed, and mutated across calls |
| **I/O and latency** | API calls, DB queries, file I/O — anything batchable, cacheable, or deferrable |
| **Concurrency** | Sync vs async, thread/process pools, event loops |
| **Memory management** | How context windows, buffers, queues are managed |
| **Evaluation/feedback** | How the system measures or corrects its own output |
| **Security surface** | Input sanitization, secrets handling, trust boundaries |
| **Networking/protocol** | gNMI streaming, YANG models, BGP/EVPN handlers, telemetry pipelines |

### 1c — Anti-Pattern Flags

Flag anything that is:
- Reinventing a solved problem (custom tokenizers, hand-rolled attention, bespoke schedulers)
- Using a technique with well-known 2024+ replacements
- Creating unnecessary overhead (full context re-serialization, redundant embedding recomputation)
- Missing a feedback or correction mechanism now considered standard
- Blocking where async/parallel execution is straightforward

---

## Phase 2 — Research Discovery (Search With Budget)

**Search budget:** 2-3 searches per catalog entry, max 12 searches total for a deep-dive.
For quick-scan mode, max 6 searches across the highest-priority patterns.

If a pattern matches the inline tables below, use those search terms directly — no need to load
the reference file. Load `references/pattern-research-map.md` only when you encounter a pattern
NOT covered by the inline tables.

### Search Targets (in priority order)
1. **arXiv** — `site:arxiv.org <pattern> <domain> 2024 OR 2025`
2. **Papers With Code** — `paperswithcode.com <technique>`
3. **Engineering blogs** — Google DeepMind, Anthropic, OpenAI, Meta AI, Hugging Face, Mistral
4. **Semantic Scholar** — for citation networks around a found paper
5. **GitHub trending / releases** — for implementation-ready libraries
6. **ACL Anthology / NeurIPS / ICML / ICLR proceedings** — for reviewed results

For networking/ops/telemetry domains, also search:
IEEE Xplore, IFIP, IETF RFCs, Nokia Bell Labs, Cisco Research, Juniper AI

### Search Query Construction

| Code Pattern Observed | Research Search Terms |
|---|---|
| Agent loop with tool use | "ReAct agent efficiency 2024", "agentic tool use optimization" |
| Large context passed every call | "KV cache reuse LLM", "prompt caching inference", "context compaction" |
| RAG with cosine similarity | "ColBERT late interaction", "HyDE hypothetical document", "RAG retrieval 2024" |
| Multi-agent orchestration | "multi-agent LLM coordination 2024", "agent communication protocol" |
| Repeated LLM calls for reasoning | "chain of thought compression", "speculative decoding", "self-consistency efficient" |
| Embedding re-computation | "embedding caching", "dense retrieval batching" |
| Sequential tool calls | "parallel function calling LLM", "concurrent tool execution agents" |
| Fine-tuning loop | "DPO direct preference optimization", "GRPO", "RLHF alternatives 2024" |
| Prompt templates hardcoded | "DSPy automatic prompting", "APE prompt engineering", "meta-prompting 2024" |
| In-memory state only | "MemGPT long-term memory", "persistent agent state", "episodic memory LLM" |
| No output validation | "structured generation LLM", "outlines library", "instructor constrained decoding" |
| Log parsing with regex | "LogBERT", "drain log parsing", "neural log analysis 2024" |
| Threshold-based alerting | "adaptive threshold anomaly detection", "online learning network monitoring" |

### Credibility Filter

Surface research that meets at least ONE of:
- Published at a top venue (NeurIPS, ICML, ICLR, ACL, EMNLP, SIGIR)
- On arXiv with 50+ citations — **exception: papers from the last 12 months pass on venue or
  lab origin alone** (recent work will not have citation counts yet)
- Implemented in production at a major lab (cite the engineering post)
- Has a working open-source implementation with active maintenance

If search returns nothing credible for a pattern, say so explicitly and suggest where the user
could look manually. Do not fill the gap with weak sources.

---

## Phase 3 — Relevance Mapping

For each research finding, apply this filter before writing the report:

```
RELEVANCE SCORE (internal):
  Impact potential:    High / Medium / Low
  Implementation cost: Low / Medium / High
  Evidence strength:   Strong / Moderate / Speculative

Keep if:  (Impact = High OR Medium) AND (Evidence = Strong OR Moderate)
Drop if:  (Impact = Low) OR (Evidence = Speculative AND no open-source implementation)
```

Also map each finding to a specific code location:
- File + class/function + line range if available
- Structural description if line numbers are not provided ("the agent harness loop in harness.py")

Note any finding that:
- Requires a runtime or language version upgrade (flag the version requirement)
- Has EU AI Act compliance implications (explainability, auditability, human oversight)
- Requires cloud infrastructure vs. can run fully on-premise
- Is adjacent to something the user said they already tried (flag as "related to your work on X")

---

## Phase 4 — Output

### Quick-Scan Mode Output

If mode is `quick-scan`, produce only this:

```
RESEARCH RADAR — [Codebase name]
─────────────────────────────────────────────────────
Area                  | Pattern Found        | Research Direction to Explore
─────────────────────────────────────────────────────
Context management    | Full ctx every call  | Prompt caching, KV reuse (Anthropic, 2024)
Retrieval             | Cosine sim RAG       | ColBERT, HyDE, late chunking
Agent loop            | Sequential tools     | Parallel tool execution (function call batching)
...
─────────────────────────────────────────────────────
Run in deep-dive mode for full analysis and implementation proposals.
```

---

### Deep-Dive Mode Output

Produce the full report in this structure:

---

#### RESEARCH UPGRADE REPORT

**Codebase:** [name/description]
**Language:** [language(s) detected]
**Analysis Date:** [date]
**Coverage:** [files/modules read] — [any gaps noted]
**Findings:** [N] upgrade opportunities across [M] categories

---

#### FINDING #N — [Short Title]

**Code Location:** `filename > ClassName.method_name()` or structural description

**What the Code Currently Does:**
> Concise description of the current pattern and its limitations.

**Research Finding:**
> **[Paper/Technique Name]** — [Authors, Venue, Year] — [URL]
> Plain-English explanation of what this technique does and why it matters.

**Why This Applies Here:**
> Specific reasoning connecting the paper to the code's limitation.
> Include measured improvements from the paper when available.

**Proposed New Design:**
> High-level description of what changes — architecture, data flows, new components.

**Proposed Implementation:**
```[language]
# Concrete sketch in the codebase's actual language.
# Focus on the novel part — does not need to be complete.
# Show before/after if it clarifies the change.
```

**Compatibility Notes:** [runtime version, dependencies, on-premise vs cloud, EU AI Act flags]
**Estimated Effort:** [hours/days]
**Risk:** [Low / Medium / High] — [one sentence on what could go wrong]

---

[Repeat for each finding]

---

#### SUMMARY TABLE

| # | Finding | Category | Impact | Effort | Risk |
|---|---------|----------|--------|--------|------|
| 1 | [title] | [AI/Perf/Security/etc] | High | 2d | Low |

#### RECOMMENDED PRIORITY ORDER

1. **Quick wins:** [finding numbers] — high impact, low effort
2. **High-value investments:** [finding numbers] — high impact, higher effort
3. **Exploratory / R&D:** [finding numbers] — promising but uncertain

#### DECISION LOG PROMPT

If any finding leads to an architectural decision, capture it with:
> "Log this decision: [finding title] — we are/are not adopting [technique] because [reason]"
> (triggers the decision-logger skill)

---

## Behavioral Guidelines

### Depth Calibration
- **Snippet (<100 lines):** 2-4 findings, dominant pattern only
- **Module (100-1000 lines):** 4-8 findings across multiple categories
- **Full codebase (1000+ lines):** 6-12 findings grouped by subsystem; note coverage gaps

### Tone and Honesty
- Never invent papers. If nothing credible surfaces, say so.
- Distinguish "deployed at scale by [org]" from "promising preprint."
- Do not undersell implementation cost — flag infrastructure changes explicitly.
- Do not produce findings for techniques the user already uses or has already evaluated.

### Domain Customization
This skill is domain-agnostic by default. Adjust searches based on the codebase domain:
- **Networking/AI-Ops:** IEEE, IFIP, IETF, vendor research blogs (Nokia Bell Labs, Cisco, Juniper)
- **Finance/trading:** SSRN, Journal of Financial Data Science
- **Healthcare:** PubMed, NEJM AI, FDA guidance documents
- **Robotics:** IEEE RA-L, ICRA, RSS proceedings

---

## Quick Reference: Pattern-to-Research Map

The inline tables above cover the most common patterns. For unfamiliar patterns not covered
there, load `references/pattern-research-map.md` — it contains 40+ additional mappings across
AI agents, RAG, inference optimization, networking/ops, and security domains.
