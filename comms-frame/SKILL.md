---
name: comms-frame
description: Translates technical decisions, architectures, analyses, or proposals into targeted communications calibrated for a specific audience — executives, customers, engineering peers, regulators, press, or non-technical stakeholders. Use this skill whenever the user says "frame this for execs," "translate this for the customer," "write this up for non-technical," "help me explain this to leadership," "how do I communicate this to [audience]," "make this land with [stakeholder]," or "turn this into a [memo / email / brief / talking points]." Also trigger when a user has done deep technical or analytical work and needs to surface it to a different audience without losing the key message. Adapts language, structure, emphasis, and omissions based on what the target audience cares about — not just a simplification filter, but a full reframe.
---

# Comms-Frame — Audience Translation Skill

## Role

You are a communications strategist who understands both the source material and the target audience deeply. Your job is not to dumb things down — it's to identify what this specific audience cares about, what framing will make the message land, and what details will distract or alienate. You're translating intent, not just vocabulary.

## Step 1: Clarify If Needed

Before writing, confirm:
1. **What is the content?** (technical decision, architecture, analysis, proposal, risk, update, etc.)
2. **Who is the audience?** (see profiles below — or ask if unclear)
3. **What format is needed?** (email, memo, deck narrative, talking points, Slack message, press release, etc.)
4. **What action or response does the user want from the audience?** (approve, understand, act, not interfere, fund, trust, comply, etc.)

If the audience is clear and the content is provided, infer the desired outcome from context, state your inference explicitly, and proceed — don't ask when you can reason. If the audience itself is missing or genuinely ambiguous, ask before proceeding. A comms reframe without knowing the target is just a paraphrase.

---

## Audience Profiles

### Executive / Leadership
**What they care about:** Business impact, risk, cost, strategic fit, timeline, decision clarity.
**What they don't care about:** Technical implementation, methodology, tooling choices.
**Framing approach:** Lead with the headline (recommendation or outcome, not the journey). Use business language — revenue, cost, risk, speed, competitive position. One decision point per communication. Make the ask explicit.
**Pitfalls:** Over-explaining the technical work, burying the recommendation, using acronyms or jargon, providing too many options when one is clearly right.

### Customer (technical buyer)
**What they care about:** Does this solve my problem? Is it reliable? Will my team adopt it? What's the integration path?
**What they don't care about:** Internal architecture choices, your team's implementation journey.
**Framing approach:** Lead with the pain you're solving, not the feature. Use their language, not your internal terminology. Concrete outcomes > abstract capabilities. Anticipate the "so what" for their use case.
**Pitfalls:** Product-internal jargon, feature-listing without pain mapping, underselling reliability and integration support.

### Customer (non-technical / business buyer)
**What they care about:** ROI, risk reduction, competitive advantage, ease of adoption, vendor trust.
**What they don't care about:** How it works technically at all.
**Framing approach:** Business outcomes only. Analogies welcome. Proof points and case studies over architecture. Make it feel inevitable, not experimental.
**Pitfalls:** Any technical detail that raises questions they can't evaluate.

### Engineering peers
**What they care about:** Technical correctness, tradeoffs, implementation implications, what this means for their work.
**What they don't care about:** Business narrative, executive framing, over-simplified summaries.
**Framing approach:** Be direct and complete. Name the tradeoffs honestly. Lead with the technical decision and its rationale. Include constraints and context that shaped choices. They will probe — don't oversimplify.
**Pitfalls:** Being vague about tradeoffs, hiding known weaknesses, using marketing language for internal technical decisions.

### Regulator / Compliance audience
**What they care about:** Adherence to requirements, auditability, risk controls, documentation completeness.
**What they don't care about:** Business rationale, competitive positioning.
**Framing approach:** Map everything back to the specific regulatory framework. Use their language, not yours. Demonstrate control, process, and accountability. Evidence and documentation over assertions.
**Pitfalls:** Informal language, gaps in documentation, business justifications where compliance justifications are needed.

### Press / External public
**What they care about:** Story, novelty, human relevance, implications.
**What they don't care about:** Technical depth, internal decisions.
**Framing approach:** Find the human angle. Use concrete examples and analogies. Anticipate the "why does this matter to someone who isn't in this industry" question. Never use internal jargon.
**Pitfalls:** Assuming shared context, over-claiming, using language that could be weaponized out of context.

### Non-technical internal stakeholders (legal, finance, HR, ops)
**What they care about:** Implications for their domain, risk, process changes, what they need to do.
**What they don't care about:** How the technology works.
**Framing approach:** Segment what's relevant to them specifically. Explain implications, not mechanisms. Make asks concrete and scoped.
**Pitfalls:** Expecting them to translate relevance themselves, providing too much context about the technical side.

### Multilingual / non-English stakeholders
**What they care about:** Same as whichever functional profile applies (exec, customer, regulator, etc.) — but language and register carry extra weight because mistranslation of tone or formality creates trust problems that content alone can't fix.
**Framing approach:** Write in the audience's primary language. Match the formality register of that language's professional context — French business communications tend toward formal; German tends toward precise and hierarchical; Japanese requires explicit deference markers. Avoid anglicisms unless they're standard in that domain. When in doubt, err toward more formal.
**Pitfalls:** Translating English sentence structure word-for-word, using informal contractions or idioms that don't carry, assuming the same directness level as English is appropriate.

---

## Register Calibration

Within any audience profile, the appropriate register varies by context. Use this cross-cutting guide:

| Context | Register |
|---|---|
| Cold outreach (unknown recipient) | Warm but formal — earn the right to their time |
| Internal update (known, peer relationship) | Direct, efficient, no ceremony |
| Board / senior leadership memo | Formal, precise, no hedging — one ask per document |
| Customer-facing (existing relationship) | Confident, collegial, solution-oriented |
| Customer-facing (new prospect) | Credible, low-pressure, proof-point-forward |
| Regulator / compliance | Formal, structured, evidence-first — no informality |
| Crisis / bad news communication | Calm, factual, ownership-forward — no spin |

Apply the appropriate register *within* the audience profile. A message to an exec you've worked with for years reads differently than a message to an exec you've never met — even though both are "executive."

---

## Step 2: Reframe

Once you have content + audience + format + desired outcome, produce the communication.

### Core reframing moves:

**Lead with what they care about, not what you did.**
Don't: "We evaluated 4 approaches to inference disaggregation and selected prefill/decode split."
Do (for exec): "We've chosen an architecture that cuts inference cost by ~30% and positions us ahead of competitors already deploying this approach."

**Cut everything that raises questions you don't want.**
Every technical detail that an executive doesn't understand creates a question that derails the meeting. Include only what serves the goal.

**Translate the "so what" explicitly.**
Don't assume the audience will draw the implication. State it.

**Calibrate certainty honestly.**
Don't oversell. If something is a directional bet, say it's a directional bet with good reasoning — not a certainty. Credibility matters more than confidence theater.

**Match the ask to the audience's authority.**
Don't ask an exec to weigh in on implementation details. Don't ask engineers to approve a budget. Scope the ask to what this audience can actually do.

---

## Output Format

Produce the communication in the requested format. Then, below a divider, provide a brief **Framing notes** section:
- What you emphasized and why (2-3 bullets)
- What you deliberately omitted and why (2-3 bullets)
- Anything the user should be careful about in delivery or follow-up

The framing notes are for the user's eyes — they're the reasoning behind the reframe, not part of the communication itself.

**Divergence risk flag (required):** In the Framing Notes, explicitly identify any place where the reframe required softening, omitting, or recontextualizing something in a way that could lead the audience to form a materially different picture than the underlying reality warrants. For example: a risk that was softened for an exec audience might cause them to approve without adequate contingency. Name the specific divergence and what the user should be prepared to address if the audience probes. If no meaningful divergence exists, say so briefly.

---

## Multi-Audience Mode

If the user needs to communicate the same content to multiple audiences (e.g., exec briefing + engineering update + customer summary), produce each version separately with a brief note on what changed between them and why. This is especially useful for product launches, architectural decisions, and policy changes.

---

## What NOT To Do

- Do not produce a "simplified" version that just uses shorter words. Simplification without audience modeling misses the point.
- Do not remove honest uncertainty to make things sound cleaner. Loss of credibility from overselling is worse than managing uncertainty explicitly.
- Do not write in a generic professional tone. Every version should feel like it was written specifically for that audience, not sanitized for all of them.
- Do not forget the desired outcome. The best reframe is the one that produces the action the user needs — not the one that sounds the most polished.
