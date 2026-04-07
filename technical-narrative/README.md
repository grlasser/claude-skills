# technical-narrative

Constructs a compelling technical narrative from a codebase, architecture docs, or design artifacts — not a feature description, but a story: why the system was built this way, what problems existing approaches couldn't solve, and what the design decisions reveal about the product's character.

## What It Does

Features are what a system does. A technical narrative is why those are the right features, made the right way, for the right reasons. That distinction is what causes a senior engineer to respect a product before they've touched it — and it's what separates a product with a real architecture story from a feature list dressed up as positioning.

This skill starts with design decision archaeology: excavating every significant architectural choice, the alternative not taken, the reason, and the deliberate tradeoff. It then constructs a narrative arc and produces output at three depths simultaneously.

## Trigger Phrases

- "write the technical story"
- "build the architecture narrative"
- "explain our design philosophy"
- "why did we build it this way"
- "I need a technical story for analysts"
- "help me explain the architecture compellingly"
- "turn this into a narrative not a feature list"

Also trigger when preparing for analyst briefings, technical blog posts, conference talks, or SE enablement.

## Three Output Depths

| Depth | Audience | Length | Content |
|---|---|---|---|
| **1 — Executive** | Executives, non-technical decision makers | ~200 words | Insight + outcome. No implementation details. Creates interest. |
| **2 — Technical buyer** | Technical leads, architects evaluating the product | ~800 words | Design decisions + rationale. Names tradeoffs. Connects architecture to outcomes. |
| **3 — Deep technical** | Senior engineers, architects who will probe | ~2000 words | Full arc with alternatives considered, detailed reasoning, component interactions, quantified validation. |

All three depths are internally consistent — a buyer who reads Depth 2 and hands Depth 3 to their architect will not find contradictions.

## Modes

- **Full pack** — All three depths + design decision inventory + quotes + credibility inventory (~3500–5000 words total)
- **Single depth** — Specify exec / technical buyer / deep technical
- **Quote extraction only** — Extract quote-ready sentences from an existing narrative

The skill will ask which mode if not specified.

## Output Structure

```
Technical Narrative: [Product / System Name]

Design decision inventory    decisions, alternatives not taken, reasons, tradeoffs
Narrative arc assessment     which sections are strong vs thin — flags gaps explicitly
Depth 1 — Executive
Depth 2 — Technical buyer
Depth 3 — Deep technical
Quote-ready extractions      3-5 sentences with per-context routing (press / analyst / SE / conference)
Credibility signal inventory what will land with skeptical technical audiences; what needs support
```

## How It Fits

```
[codebase + docs] → technical-narrative → comms-frame (Depth 1 → exec, Depth 2 → technical buyer)
                          ↓
                  positioning-stress-test (design decisions → structural claims)
                          ↓
                   proof-point-miner (design decisions = Tier 2 proof points)
                          ↓
                   evergreen-extractor (decision inventory → vault atoms)
```
