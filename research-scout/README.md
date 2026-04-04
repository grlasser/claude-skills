# research-scout

A Claude Code skill that analyzes your code, searches for cutting-edge research papers and engineering techniques, and produces a structured **Research Upgrade Report** mapping each finding to a specific code location with a concrete implementation proposal.

## What It Does

Most code reviews tell you what's wrong with your code. Research Scout tells you what the field has learned since you wrote it — and shows you how to apply it.

It runs in four phases:

1. **Code Archaeology** — reads your code and produces a visible Pattern Catalog: every architectural pattern, AI/ML technique, concurrency model, state management approach, and anti-pattern found, mapped to the file and function where it lives.

2. **Research Discovery** — translates each pattern into research vocabulary and searches arXiv, Papers With Code, Semantic Scholar, and major AI lab engineering blogs (Anthropic, Google DeepMind, Meta AI, Hugging Face). Applies a credibility filter — only surfaces papers from top venues, with active open-source implementations, or from recent major lab publications.

3. **Relevance Mapping** — scores each finding by impact potential, implementation cost, and evidence strength. Filters out weak or speculative results before writing anything.

4. **Research Upgrade Report** — one section per finding: current code location, what the paper proposes, why it applies here, a code sketch in your actual language, compatibility notes, effort estimate, and risk rating. Ends with a prioritized summary table.

## Two Modes

**`quick-scan`** — a compact Research Radar table. Fast, high-level, no code sketches. Good for "what areas should I look into?"

```
RESEARCH RADAR — my-agent
─────────────────────────────────────────────────────
Area                  | Pattern Found        | Research Direction to Explore
─────────────────────────────────────────────────────
Context management    | Full ctx every call  | Prompt caching, KV reuse (Anthropic, 2024)
Retrieval             | Cosine sim RAG       | ColBERT, HyDE, late chunking
Agent loop            | Sequential tools     | Parallel tool execution (function call batching)
─────────────────────────────────────────────────────
```

**`deep-dive`** — full Research Upgrade Report with per-finding analysis, code sketches, effort estimates, and a decision-logger hook. Default mode.

## Triggers

Say any of:

- `research-scout this`
- `find new techniques for this code`
- `are there better patterns for this agent loop`
- `what does recent research say about this implementation`
- `scout this for improvements`
- `what would a 2025 version of this look like`

Also triggers automatically when you share a substantial codebase and ask for a deep review or optimization pass.

## Example Output (Deep-Dive)

```
RESEARCH UPGRADE REPORT
Codebase: ReasonGrid agent harness
Language: Python 3.11
Findings: 5 upgrade opportunities across 3 categories

FINDING #1 — Prompt Caching for Agent Context

Code Location: agent/harness.py > ReasoningAgent.call_llm()

What the Code Currently Does:
  Reconstructs the full system prompt and conversation history on every
  LLM call, including static tool definitions and reasoning instructions
  that never change between turns.

Research Finding:
  Anthropic Prompt Caching (2024) — Anthropic Engineering Blog
  Allows marking stable prefix content (system prompts, tool schemas,
  few-shot examples) as cacheable. The inference layer reuses the KV
  cache for those tokens across calls, reducing latency and cost on
  repeated content by up to 90%.

Why This Applies Here:
  Your system prompt and tool definitions are identical across every
  turn of the agent loop. They are being re-encoded from scratch on
  every call — exactly the pattern prompt caching is designed to eliminate.

Proposed Implementation:
  # Before
  messages = [{"role": "user", "content": user_input}]

  # After — mark stable prefix with cache_control
  system = [
      {"type": "text", "text": STATIC_SYSTEM_PROMPT,
       "cache_control": {"type": "ephemeral"}},
      {"type": "text", "text": TOOL_DEFINITIONS,
       "cache_control": {"type": "ephemeral"}}
  ]

Compatibility Notes: Requires Anthropic SDK >= 0.28. No infrastructure change needed.
Estimated Effort: 2-4 hours
Risk: Low — purely additive, no behavioral change
```

## What It Won't Do

- Invent papers. If nothing credible surfaces for a pattern, it says so.
- Reproduce findings for techniques you already use or have already evaluated — tell it what you've tried and it skips those.
- Suggest generic best practices without a specific paper or production deployment backing them.
- Undersell implementation cost — infrastructure changes are flagged explicitly.

## Bundled Reference

Includes `references/pattern-research-map.md` — a curated 40+ row lookup table mapping common code patterns to research domains and search terms, covering AI agents, RAG pipelines, inference optimization, networking/ops, and security.

## Composes With

- **decision-logger** — each finding includes a prompt to capture the adoption/rejection decision with rationale
- **plan-review** — use plan-review to stress-test the proposed redesign before implementing
- **pre-mortem** — use pre-mortem to pressure-test the migration plan for a high-effort finding

## Installation

```bash
ln -s ~/Projects/claude-skills/research-scout ~/.claude/skills/research-scout
```

Restart your Claude Code session and it's live.
