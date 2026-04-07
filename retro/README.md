# retro

Structured post-execution retrospective that extracts causal chains, decision quality, and forward-learning from real outcomes — whether the result was a success, failure, or mixed.

## What It Does

Most retros produce comfortable summaries: a list of what went well, what could improve, and vague action items nobody revisits. This skill takes a different approach. It works backward from the actual outcome to surface the real causal chain, audits the quality of decisions made during execution (separating good decisions from good luck), and converts findings into durable, specific forward-learning rather than generic principles.

It's the mirror of `pre-mortem`: where `pre-mortem` imagines failure before it happens, `retro` analyzes what actually happened after.

## Trigger Phrases

- "retro this"
- "debrief this"
- "what did we learn"
- "post-mortem this"
- "what actually happened"
- "why did this go wrong"
- "why did this work"
- "what should we take forward"

Also triggers when a project, sprint, launch, experiment, or significant decision has concluded.

## Output Structure

```
Retro: [Project/Decision Name] — [Date or period]

Outcome summary          — intended vs. actual (2-3 sentences)
Causal chain             — narrative working backward from effect to root cause
Decision quality audit   — table: Decision | Alternative | Info available | Process quality | Outcome | Verdict
Signals that were there  — what was visible early that predicted the outcome
Forward-learning         — carry forward / stop / watch-for (specific, not generic)
One-sentence verdict     — what this retro most wants the team to remember in 6 months
```

### Decision Verdict Taxonomy

| Verdict | Meaning |
|---|---|
| Good process / good outcome | Intentional — repeat it |
| Good process / bad outcome | Bad luck — don't abandon the process |
| Bad process / good outcome | **Got lucky** — highest priority to flag |
| Bad process / bad outcome | Expected — identify the root cause |

The **got-lucky** cases are where false confidence gets built. Encoding luck as method is the most common failure mode of success retros.

## Scope Calibration

| Project type | Depth |
|---|---|
| Sprint / experiment / single decision | Phases 2 + 5 only. Under one page. |
| Medium project (weeks to a few months) | All 5 phases at moderate depth |
| Major program (multi-month, multi-team) | Full depth — causal chain and decision audit get the most attention |

## How It Fits

```
pre-mortem → [execution] → retro → decision-logger
 (imagines)                (analyzes)    (captures)
```

`pre-mortem` runs before execution to surface failure modes. `retro` runs after to extract what actually happened. `decision-logger` captures decisions made during the retro itself — revisit triggers, changes to process, choices about what to carry forward.

## Example

**Input:** A feature launch that shipped 3 weeks late with reduced scope.

**Causal chain (excerpt):** The launch slipped not because of the integration complexity discovered in week 6, but because the team assumed the vendor API contract was frozen — a belief no one had verified. That single unvalidated assumption cascaded into a mid-sprint redesign that consumed the schedule buffer.

**Got-lucky flag:** The reduced scope actually tested better with users than the full feature would have. The team nearly encoded "ship incrementally" as a deliberate strategy — but the reduction was forced, not planned. Don't carry forward what was a constraint as if it were a principle.

**One-sentence verdict:** "We were saved by a lucky scope cut, but the real problem — assuming external contracts without verification — will surface again on the next integration project."
