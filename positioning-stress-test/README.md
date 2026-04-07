# positioning-stress-test

Adversarial stress-test of product positioning statements, value propositions, and differentiation claims — before they reach a technical buyer who will challenge them.

## What It Does

Positioning fails in two ways: in the meeting when a buyer challenges it, or after the meeting when a buyer deploys the product and observes something that contradicts what they were told. This skill surfaces both failure modes before either happens.

It runs each claim through three distinct challenger personas, generates concrete falsification scenarios, assesses how long the positioning will hold before competitors neutralize it, checks for contradictions across collateral, and runs a "so what" test to ensure every claim connects to buyer value.

## Trigger Phrases

- "stress-test this positioning"
- "is this defensible"
- "does this positioning hold"
- "will this land with engineers"
- "what breaks in this narrative"
- "challenge our value prop"
- "red team this messaging"

Also trigger when positioning is being finalized before a launch, analyst briefing, or major sales motion.

## Three Challenger Personas

**Persona A — Skeptical Technical Evaluator**
Challenges on technical accuracy, real-world performance, and verifiability. "Show me the benchmark methodology, not just the headline number."

**Persona B — Prepared Competitor Champion**
Has been briefed by your main competitor. Challenges on differentiation. "Competitor X does this too — how is yours architecturally different?"

**Persona C — Procurement / Risk-Averse Buyer**
Challenges on vendor maturity and claim integrity. "This sounds like marketing language — can you show me the implementation?"

The fix for one persona's objection often creates another's. Running all three is the only way to find the claims that survive all challenges.

## Output Structure

```
Positioning Stress-Test: [Product / Campaign Name]

Claims inventory           numbered list of all distinct claims
Persona challenge results  for each claim × persona: full challenge text + response strength + response content
Falsification watchlist    concrete scenarios a buyer could use to disprove each claim
Temporal durability map    Structural / Feature lead / Assertion — with durability window estimates
Consistency gaps           contradictions across multiple artifacts (if provided)
"So what" failures         claims missing buyer-value connection, with suggested completions
Verdict                    strongest claims / remediation needed / retire entirely — with routing to fix each
```

## Scope

| Claims count | Approach |
|---|---|
| 1–5 | Full treatment on every claim |
| 6–10 | Full treatment on all claims |
| 10+ | Full treatment on 5–7 highest-stakes claims; brief flag on remainder |

## How It Fits

```
proof-point-miner → positioning-stress-test → technical-narrative (rebuild weak claims)
                                            → comms-frame (use strong claims per audience)
```

Runs after `proof-point-miner` (evidence base) and before `comms-frame` (audience translation). Weak claims identified here signal where `technical-narrative` needs to do deeper design decision archaeology.
