---
name: decision-logger
description: Captures key project decisions with full context — alternatives considered, rationale, accepted risks, and revisit triggers — into a persistent decisions.md log. Use this skill whenever the user says "log this decision," "capture that choice," "record this," "remember why we chose," "decision log," or "add to decisions." Also trigger when the user says "show me decisions," "what did we decide about," "why did we choose," or "review decisions" — these activate review mode. Trigger proactively at the end of any conversation where a meaningful technical, architectural, or strategic choice was made and the user might benefit from capturing it. If a significant decision just happened in conversation and the user hasn't explicitly asked to log it, suggest it: "Want me to log that decision?"
---

# Decision Logger — Structured Decision Capture & Review

## Purpose

Decisions made during planning and implementation sessions evaporate when the conversation ends. This skill captures them in a structured, queryable format so they survive across sessions and serve as an auditable trail for executive reviews, onboarding, and retrospectives.

## Two Modes

### Capture Mode

Triggered by: "log this decision," "capture that choice," "record why we chose X," or proactive suggestion after a meaningful decision.

#### What to Capture

Extract from the conversation context and write a structured entry. Every entry must include:

- **Decision**: One-line statement of what was decided. Be specific. Not "chose a threshold" but "Set training data filter threshold at 70% root_cause_accuracy."
- **Date**: Today's date in YYYY-MM-DD format.
- **Context**: 1-2 sentences on what prompted this decision. What problem or question led here?
- **Alternatives considered**: Brief list of other options evaluated, with one-line reason each was rejected. This is the most valuable field in hindsight — it answers "why didn't you just do X?"
- **Rationale**: Why this choice over the alternatives. Reference specific evidence, data, prior art, or constraints that drove the decision.
- **Risks accepted**: What you're knowingly trading off. Every decision has a cost — name it explicitly.
- **Revisit trigger**: What conditions would make you reconsider this decision. Frame as concrete, observable signals, not vague "if things change." Example: "If training data rejection rate exceeds 25%" not "if quality becomes an issue."
- **Phase/Component**: Which part of the project this relates to (for filtering during review).

#### Entry Format

Append to the decisions log file using this exact format:

```markdown
### [DECISION-NNN] Decision title
**Date:** YYYY-MM-DD  
**Phase:** [phase or component name]  
**Context:** [what prompted this decision]  
**Decision:** [specific statement of what was chosen]  
**Alternatives considered:**
- [Option A] — rejected because [reason]
- [Option B] — rejected because [reason]
- [Option C] — rejected because [reason]

**Rationale:** [why this choice]  
**Risks accepted:** [known tradeoffs]  
**Revisit trigger:** [concrete conditions for reconsideration]
```

#### Numbering

Read the existing log file first. Continue numbering from the last entry. If no log exists, start at DECISION-001.

#### Where to Write

Check for an existing decisions log in this order:
1. `.claude/plans/decisions.md` (preferred — next to other planning artifacts)
2. `.claude/decisions.md` (fallback)
3. If neither exists, create `.claude/plans/decisions.md`

If the file already has a header, append after the last entry. If creating new, add this header:

```markdown
# Decision Log

Structured record of key project decisions, alternatives considered, and rationale.  
Generated and maintained via the decision-logger skill.

---
```

#### What Qualifies as a Decision Worth Logging

Not every small choice needs logging. Capture decisions that:
- Affect architecture, data flow, or system design
- Choose between meaningfully different approaches
- Accept known risks or tradeoffs
- Would be questioned by a stakeholder, reviewer, or future-you
- Close off alternative paths that would be expensive to revisit

Don't log: formatting preferences, variable naming, minor refactors, tool version bumps, or anything easily reversible in under an hour.

#### Proactive Suggestion

If a significant decision was just made in conversation and the user hasn't asked to log it, offer briefly:

> "That [threshold/architecture/approach] decision seems worth capturing. Want me to log it?"

Don't be pushy. Offer once, then move on.

### Review Mode

Triggered by: "show me decisions," "what did we decide about X," "why did we choose X," "review decisions," "decision history."

#### Capabilities

- **Show all**: Display the full log, most recent first
- **Filter by phase/component**: "show me decisions about training data" — scan entries and return matches
- **Filter by date range**: "decisions from this week" or "decisions in March"
- **Search by keyword**: match against decision titles, rationale, and context fields
- **Revisit check**: "any decisions due for revisit?" — scan revisit triggers against current project state and flag any that may have been activated

When presenting entries in review mode, keep the full structured format. Don't summarize or compress — the value is in the details, especially the alternatives and rationale fields.

## What NOT To Do

- Do not invent or infer decisions that weren't actually made. Only log what was explicitly discussed and chosen.
- Do not editorialize the rationale. Capture the reasoning as it happened, even if you'd recommend differently.
- Do not skip the "alternatives considered" field. It's tempting when the decision seems obvious, but obvious decisions are exactly the ones people question later.
- Do not create a new file if one already exists. Always append.
- Do not log the same decision twice. Check for existing entries about the same topic before appending.
