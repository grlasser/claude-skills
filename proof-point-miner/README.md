# proof-point-miner

Systematically mines a codebase, documentation set, or technical artifact for claims that can become proof points — concrete, specific, technically grounded statements that land with technical buyers.

## What It Does

Marketing claims that collapse under the first technical question destroy credibility faster than saying nothing. This skill reads what's actually in code and docs, surfaces every defensible claim, rates each by credibility tier, detects gaps where positioning outpaces reality, assesses how easily each claim can be challenged, maps each to the audience most likely to care, and rates competitive differentiation value.

The gap detection is often the most valuable output — it tells you exactly where the narrative is ahead of the evidence.

## Trigger Phrases

- "find proof points in this"
- "what claims can we make"
- "mine this for marketing material"
- "what do we actually have to show"
- "what can I back up"
- "ground our positioning in the code"

Also trigger when preparing for a technical buyer conversation and wanting to know what's defensible.

## Credibility Tier System

| Tier | Type | Description |
|---|---|---|
| **1** | Measured / Benchmarked | Specific number under defined test conditions. Fully defensible. |
| **2** | Architectural Decision | Specific design choice with documented reason. Credible and specific. |
| **3** | Design Intent | Stated goal that manifests in the architecture. Usable with care. |
| **4** | Assertion | Claim in docs with no Tier 1/2 support. Flag for elevation or retirement. |

This tier system is the canonical credibility scale used across `proof-point-miner`, `technical-narrative`, and `release-brief`.

## Output Structure

```
Proof Point Inventory: [Project Name]

Tier 1 — Measured/Benchmarked     claim | audience | competitive rating | falsification risk | source
Tier 2 — Architectural Decisions  same format
Tier 3 — Design Intent            same format, briefer
Gaps — Claims not supported        positioning claim | evidence gap | remediation needed
Falsification assessment           all Tier 1+2, grouped: High (veto) / Medium / Low
Tier 4 — Unsupported Assertions    claim | elevation path | recommended action

Summary: counts, top 3 claims, any table-stakes items in current positioning
```

## How It Fits

```
[codebase + docs] → proof-point-miner → positioning-stress-test
                          ↓                      ↓
                   competitive-diff          technical-narrative
                          ↓
                    release-brief (proof point delta updates this inventory)
```

Run this before any positioning work. Its Tier 1 and 2 inventory is the evidence base for every other skill in the suite.
