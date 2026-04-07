# assumption-mapper

Surfaces and stress-ranks the unstated assumptions embedded in any plan, decision, strategy, or technical design — before you commit.

## What It Does

Most plans fail not because of bad execution, but because they were built on assumptions nobody stopped to examine. This skill runs a structured excavation across six assumption categories, identifies which assumptions are load-bearing for others (clusters), ranks everything by confidence × consequence-if-wrong, and specifies the fastest path to validate each risk.

The output is an **Assumption Map**: a prioritized view of what has to be true for the plan to work, ranked by how badly things break if any of it turns out to be wrong.

## Trigger Phrases

- "what are we assuming here"
- "map the assumptions"
- "what are we taking for granted"
- "what has to be true for this to work"
- "what are our hidden dependencies"
- "assumption check this"

Also triggers proactively when a plan, architecture, or proposal is presented before a major commitment or stakeholder review.

## Output Structure

```
Assumption Map: [Plan/Decision Name]

Excavation summary       — dominant risk zone identified
🔴 Immediate Risks       — low/medium confidence + critical impact
                           with: assumption | confidence gap | failure mode | validation action
🟠 Validate Soon         — low/medium confidence + major impact
🟡 Monitor               — high confidence + critical impact (watch if context shifts)
Bottom line              — overall assumption profile + single most dangerous assumption
```

Each 🔴 and 🟠 item specifies a validation type: **Conversation**, **Data pull**, **Desk research**, **Experiment/spike**, or **Decision forcing**.

## Scope Calibration

| Input size | Assumptions surfaced |
|---|---|
| Simple decision / short proposal | 5–8 |
| Medium plan or architecture | 10–15 |
| Complex program or system design | Up to 20 (hard cap) |

## How It Fits

```
give-options → assumption-mapper → plan-review → pre-mortem
   (generate)      (excavate)        (audit)      (stress narrative)
```

`assumption-mapper` fills the gap between generating options and auditing a plan. Where `plan-review` evaluates whether a plan is structurally sound, `assumption-mapper` surfaces what the plan silently takes for granted — before anyone has committed to a direction.

## Example

**Input:** A proposal to migrate a service to a new infrastructure provider in Q3.

**Output highlights:**
- 🔴 *"The new provider's SLA will match current latency requirements"* — Low confidence. Failure means SLA breach for downstream customers. Validate via: **Experiment/spike** — run a 48-hour load test against the provider's staging environment.
- 🔴 *"Finance has approved the migration budget"* — Low confidence. This assumption props up three others (headcount, tooling, timeline). Validate via: **Decision forcing** — budget owner needs to confirm by [date] before architecture decisions are made.
- 🟠 *"The team has capacity alongside the current roadmap"* — Medium confidence. Validate via: **Conversation** — capacity review with engineering leads.
