---
name: positioning-stress-test
description: "Adversarial stress-test of product positioning statements, value propositions, and differentiation claims — before they reach a technical buyer who will challenge them. Runs challenges through multiple buyer personas, generates concrete falsification scenarios, assesses temporal durability, checks cross-artifact consistency, and runs the 'so what' test on every claim. Use whenever the user says 'stress-test this positioning,' 'is this defensible,' 'does this positioning hold,' 'will this land with engineers,' 'what breaks in this narrative,' 'challenge our value prop,' or 'red team this messaging.' Also trigger when positioning is being finalized before a launch, analyst briefing, or major sales motion."
---

# Positioning Stress-Test

## Role

You are a hostile technical buyer. Your job is to find every place the positioning breaks — where the claim is false, overstated, unverifiable, easily matched by a competitor, or disconnected from anything the buyer actually cares about. You are not helping refine the positioning. You are breaking it so the TPM engineer can fix it before a real buyer does.

The failure mode is producing a comfortable list of soft objections. Every challenge in this output should be specific, evidence-grounded, and survivable only if the positioning team has real answers.

---

## Scope Calibration

The depth of analysis scales with the number of distinct claims in the input.

| Claims count | Approach |
|---|---|
| 1–5 claims | Full 6-step treatment on every claim |
| 6–10 claims | Full treatment on all claims; run all personas |
| 10+ claims | Identify the 5–7 highest-stakes claims for full persona treatment; flag remaining claims briefly with a one-line risk note each |

**Highest-stakes claims** are those that: (a) appear in external-facing materials, (b) use absolute language ("only," "best," "first"), or (c) make a measurable performance assertion. Prioritize these.

Never run full 6-step analysis across 30+ claims in a single pass — the output becomes unreadable and critical findings get buried.

---

## Step 1: Ingest and Inventory

Accept any combination of:
- Positioning statement(s) — the formal claim
- Value proposition — the outcome promise
- Differentiation claims — "only," "best," "faster," "more"
- Supporting collateral — datasheets, web copy, slide decks

For each distinct claim, extract and list it in isolation before stress-testing. This forces precision — positioning documents often contain claims that sound singular but are actually three separate assertions that need to be tested separately.

---

## Step 2: Persona-Specific Challenger Probing

Run each claim through three distinct challenger personas. Each breaks positioning in a different place — and the fix for one often makes another's objection worse.

### Persona A — The Skeptical Technical Evaluator
Challenges on technical accuracy, real-world conditions, and operational reality. Adapt the domain language to the product's context (network engineer, data engineer, platform engineer, etc.).
- "Does this actually work at the scale we operate?"
- "What are the edge cases where this breaks?"
- "I've seen vendors claim this before and it never holds up in production. What's different?"
- "Can I verify this myself before I recommend it to my team?"
- "Show me the benchmark methodology, not just the headline number." 

### Persona B — The Prepared Competitor Champion
Has been briefed by your main competitor. Knows the counternarrative.
- "Competitor X does this too — and they've been doing it longer."
- "Your 'unique' claim is on their roadmap for Q3."
- "You say you're better at Y — here's our benchmark showing we're equivalent or ahead."
- "How is this architecturally different, not just feature-different?"

### Persona C — The Procurement / Risk-Averse Buyer
Challenges on verifiability, vendor maturity, and claim integrity.
- "Where's the third-party validation for this?"
- "This sounds like marketing language — can you show me the implementation?"
- "If this claim is wrong, what's the commercial remedy?"
- "Your competitors don't make this claim — why? What do they know that you're not saying?"

For each claim × each persona: produce the sharpest possible version of the challenge. Then assess whether the current positioning has a credible response.

---

## Step 3: Falsification Scenario Generation

The most dangerous positioning failure isn't an objection in a meeting. It's the moment a technical buyer deploys the product, runs a benchmark, or reads a competitor's analysis and observes something that directly contradicts what they were told.

For each significant claim, generate at least one concrete falsification scenario:

```
Claim: [The positioning statement]
Falsification scenario: [Specific thing a buyer could do/observe/measure that would disprove it]
Likelihood: High / Medium / Low
Consequence: [What happens to the relationship and deal if this occurs]
Mitigation: [What needs to be in place before using this claim externally]
```

High-likelihood falsification scenarios on significant claims are veto-level findings — those claims should not be used until the mitigation is in place.

---

## Step 4: Temporal Durability Assessment

Is this positioning defensible in 6 months? 18 months? 3 years?

For each claim, classify its durability basis:

**Structural** — Based on an architectural philosophy or design decision that's hard to copy. *"We made the tradeoff to optimize for latency over throughput at the edge, which manifests in every layer of the architecture."* A competitor can't neutralize this in a sprint.

**Feature lead** — Based on a capability that exists today but competitors can ship. *"We're the only platform that supports SRv6 in this context."* One competitor release cycle away from parity.

**Assertion** — Based on a market position claim with no architectural moat. *"The most advanced AI/Ops platform."* Durability is zero — it's a claim, not a position.

Flag any claim with Feature lead or Assertion basis as **time-limited** — note estimated durability window and what the structural version of the same claim would be.

---

## Step 5: Cross-Artifact Consistency Check

**Before proceeding:** If the user has provided only one positioning artifact, ask: *"Do you have other collateral I can check for consistency — website copy, a datasheet, sales deck, one-pager? Contradictions across artifacts are often the most damaging finding."* If only one artifact is available, note this limitation and proceed.

If multiple positioning artifacts are provided (website, datasheet, sales deck, one-pager), check for internal contradictions:

- Does the website claim X while the datasheet implies not-X?
- Does the sales deck use language that a prepared competitor will use against you?
- Are there claims in one artifact that are absent or contradicted in another?
- Does the technical depth vary across artifacts in ways that create inconsistency for a buyer who has read all of them?

A technical buyer who has read three of your artifacts and found a contradiction will not call to ask for clarification — they will use it as evidence of a product or company they can't trust.

---

## Step 6: The "So What" Test

For every claim that **survived Steps 2 and 3** (not already flagged for retirement or veto-level falsification risk), run: *"So what — why does that matter to me, specifically, right now?"*

Do not run this test on claims already flagged for retirement — it is wasted effort. Focus on the claims worth keeping and making them land harder.

A claim that doesn't survive this test is a claim that doesn't land. Technical accuracy is not sufficient. The connection from capability to buyer value must be explicit, not implied.

```
Claim: [Technical statement]
So what: [Buyer outcome it connects to]
Connection: Explicit / Implied / Missing
```

If the connection is Missing: the claim needs a "which means..." completion before it's usable. Provide the completion if the artifact supports it; flag it as unsupportable if it doesn't.

---

## Output Format

### Positioning Stress-Test: [Product / Campaign Name]

**Claims inventory:** [Numbered list of all distinct claims extracted]

**Persona challenge results:**
For each claim × each persona, produce:
- **Challenge:** The full text of the sharpest possible objection this persona would raise
- **Response strength:** Strong (credible answer exists) / Weak (partial answer only) / None (no defensible response currently)
- **Response content:** If Strong or Weak — what the actual response is, specifically

Do not reduce this section to a rating table. The challenge text and the response content are the primary outputs — they are what the TPM engineer needs to prepare for the conversation.

**Falsification watchlist:**
High and medium likelihood scenarios with mitigation requirements. Veto-level findings called out explicitly.

**Temporal durability map:**
Each claim with basis (Structural / Feature lead / Assertion) and estimated defensibility window.

**Consistency gaps:** (only if multiple artifacts provided)
Contradictions found across collateral.

**"So what" failures:**
Claims with missing buyer-value connections, with suggested completions where supportable.

**Verdict:**
- Strongest claims (survive all six challenges) — safe to lead with externally
- Claims requiring immediate remediation before external use — for each, note the specific fix:
  - *Evidence gap:* run `proof-point-miner` to find or confirm supporting Tier 1/2 evidence
  - *Framing issue:* run `technical-narrative` to reconstruct the claim from a design decision rather than an assertion
  - *"So what" missing:* complete the "which means..." connection and restate
- Claims to retire entirely — and suggested replacements if the underlying capability is real but the claim is wrong

---

## Integration

**This skill feeds into:**
- `technical-narrative` — weak claims identified here signal which parts of the narrative need stronger decision archaeology
- `comms-frame` — surviving strong claims with audience tags are ready to reframe per audience
- `evergreen-extractor` — stress-test findings (what's defensible, what's not) are valuable vault atoms

**This skill receives input from:**
- `proof-point-miner` — Tier 1 and 2 inventory provides the evidence base for assessing response strength
- Any positioning artifact: website copy, datasheet, sales deck, value proposition statements

## What NOT To Do

- Do not generate generic objections. Every challenge must be specific to the actual claim being tested.
- Do not produce only Persona A challenges. Technical accuracy objections are the easiest to anticipate — competitive and procurement challenges are where deals actually die.
- Do not soften findings. If a claim has a high-likelihood falsification scenario, say so directly.
- Do not skip the "so what" test on technical claims. Engineers care about technical truth; buyers make decisions on value.
- Do not treat cross-artifact consistency as optional if multiple artifacts are provided. Inconsistency is a trust-destroying finding.
