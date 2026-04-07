# competitive-diff

Produces a technically grounded competitive differentiation analysis — going below features to architectural philosophy, design tradeoffs, and structural constraints — with an asymmetric honest map and a field-ready battle card.

## What It Does

Feature-level competitive analyses get neutralized by the next release. Architectural comparisons don't. This skill compares your product's actual code and architecture against competitor public documentation at the layer that matters: what each product is fundamentally optimized for, what tradeoffs were made, and what problems each architecture is structurally bad at solving.

The output includes an asymmetric win/loss/draw map — including an honest "where you lose" section with structured handling strategies — and a battle card formatted for field use by an SE in a live conversation.

## Trigger Phrases

- "how do we compare to X"
- "what is our real differentiation"
- "competitive brief"
- "battle card for X"
- "what do we win on"
- "where are we weaker"
- "prepare me for a competitive conversation"
- "analyze X vs us"

## Evidence Tier System

Claims about competitors are tagged by source reliability — distinct from the Tier 1/2/3/4 system used for your own product:

| Tag | Meaning | External use |
|---|---|---|
| **V** | Verified from observable implementation | Safe |
| **S** | Stated in competitor's own docs (may be aspirational) | Safe with caveat |
| **I** | Inferred from architectural patterns | Hedge explicitly |
| **A** | Assumed from market position | Internal only |

Your own product claims use the Tier 1/2/3/4 system from `proof-point-miner`.

## Output Structure

```
Competitive Analysis: [Your Product] vs [Competitor]

Evidence inventory            sources used, with V/S/I/A tags
Architectural philosophy      optimization targets, tradeoffs, structural constraints — for both
Asymmetric map                Where you win (Tier 1/2 evidence) | Where you lose (with handling strategies) | Draws (with discovery questions)
Narrative integrity issues    incoherences between your claims and your architecture
Battle card                   field-ready: orientation, their strengths, your differentiators,
                              discovery questions, landmines, if-they-say/we-say
```

## "Where You Lose" Handling Strategies

The skill doesn't leave SEs without a response for losses. Five structured options:
- **Acknowledge and reframe** — name the deliberate tradeoff
- **Redirect** — shift to a dimension you win on
- **Qualify the context** — when the gap doesn't apply to your target scenario
- **Flag as roadmap** — honest gap with current mitigation
- **Accept and move on** — some losses have no good response; know them internally

## Scope

| Task | Scope |
|---|---|
| Single competitor | Full 5-step analysis + battle card |
| Quick battle card update | Steps 1 and 5 only |
| Full landscape (3+ competitors) | Steps 1–3 per competitor + individual battle cards |
| Analyst briefing | Full analysis, emphasis on Step 2 (architectural philosophy) |

## How It Fits

```
proof-point-miner → competitive-diff → comms-frame (competitive framing per audience)
                          ↓
                  positioning-stress-test (Persona B challenges come from here)
                          ↓
                   evergreen-extractor (battle cards → vault, 90-day expiry)
```
