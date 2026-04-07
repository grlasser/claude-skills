# comms-frame

Translates technical decisions, architectures, analyses, and proposals into targeted communications calibrated for a specific audience — without losing the substance or creating misalignment.

## What It Does

Deep technical or analytical work rarely speaks for itself. The same content needs to land differently depending on who's reading it: an executive needs the business headline and a clear ask; an engineering peer needs the tradeoffs named honestly; a regulator needs everything mapped to a compliance framework; a customer needs their pain addressed, not your architecture explained.

This skill is not a simplification filter. It's a full reframe — identifying what each audience actually cares about, what framing makes the message land, what to cut, and what register to use. It also produces **Framing Notes** for the author: what was emphasized, what was deliberately omitted, and where the reframe might create divergence between what the audience infers and what the underlying reality actually is.

## Trigger Phrases

- "frame this for execs"
- "translate this for the customer"
- "write this up for non-technical"
- "help me explain this to leadership"
- "how do I communicate this to [audience]"
- "make this land with [stakeholder]"
- "turn this into a [memo / email / brief / talking points]"

Also triggers when deep technical or analytical work needs to be surfaced to a different audience.

## Audience Profiles

| Audience | Leads with | Cuts |
|---|---|---|
| Executive / Leadership | Business impact, risk, clear ask | Technical implementation, methodology |
| Customer (technical buyer) | Pain solved, reliability, integration path | Internal architecture, your team's journey |
| Customer (business buyer) | ROI, competitive advantage, vendor trust | How it works technically |
| Engineering peers | Tradeoffs, constraints, decision rationale | Business narrative, marketing language |
| Regulator / Compliance | Regulatory mapping, controls, auditability | Business rationale, competitive positioning |
| Press / External public | Story, human relevance, implications | Technical depth, internal decisions |
| Internal non-technical (legal, finance, HR) | Implications for their domain, what they need to do | How the technology works |
| Multilingual stakeholders | Same as functional profile + language/register calibration | Anglicisms, English sentence structure, assumed directness |

## Register Calibration

Within any audience, the right tone varies by context:

| Context | Register |
|---|---|
| Cold outreach | Warm but formal — earn the right to their time |
| Internal update (known relationship) | Direct, efficient, no ceremony |
| Board / senior leadership memo | Formal, precise, one ask per document |
| Customer (existing relationship) | Confident, collegial, solution-oriented |
| Customer (new prospect) | Credible, low-pressure, proof-point-forward |
| Regulator / compliance | Formal, structured, evidence-first |
| Crisis / bad news | Calm, factual, ownership-forward — no spin |

## Output Structure

```
[Communication in requested format]

---

Framing Notes (for author only):
• What was emphasized and why
• What was deliberately omitted and why
• Divergence risk: where the reframe may cause the audience to form a
  materially different picture than the underlying reality warrants,
  and what to be ready to address if they probe
```

## Multi-Audience Mode

Pass the same content with multiple target audiences and the skill produces each version separately with a note on what changed between them and why — useful for product launches, architectural decisions, and policy changes that need to be communicated across the organization simultaneously.

## How It Fits

```
[analysis / decision] → comms-frame → [stakeholder communication]
                              ↑
                    works on output from any other skill:
                    give-options, plan-review, assumption-mapper, retro
```

Any output from the decision intelligence suite — options analysis, plan review, assumption maps, retros — can be passed to `comms-frame` to produce a version tailored for a specific audience.

## Example

**Input:** A technical decision to move from a monolithic inference stack to a disaggregated prefill/decode architecture.

**For exec (email):**
> "We've selected a new inference architecture that reduces our serving cost by approximately 30% at scale and positions us ahead of the industry shift already underway at [competitors]. The change requires a one-time migration effort of roughly [X] engineer-weeks. I'm requesting approval to begin in Q3."

**Framing Notes:**
- *Emphasized:* Cost reduction and competitive timing — the two things that drive exec decisions on infrastructure.
- *Omitted:* Prefill/decode disaggregation mechanics, DPU/LPU placement tradeoffs, migration complexity details.
- *Divergence risk:* "30% cost reduction" is a projection at scale, not a current realized number. If the exec asks "when do we see this in the P&L," be ready to explain the scale dependency — the number doesn't materialize until traffic volume reaches [threshold].
