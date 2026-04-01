# Decision Logger — Structured Decision Capture & Review

A Claude Code skill that captures key project decisions with full context so they survive beyond the conversation where they were made. Builds an auditable trail of what was decided, what alternatives were considered, why, and what would trigger reconsideration.

## The Problem

During a Claude session, you make a meaningful choice — 70% threshold instead of 60%, Opus instead of Gemini as teacher model, flatten correlation instead of multi-turn distillation. The reasoning is solid, the alternatives were weighed. Then the session ends, and all of that context evaporates.

Three weeks later: "Why didn't you just use 60%?" and you're reconstructing rationale from memory.

## How to Use

### Capture Mode

After making a decision in any session:

```
> log this decision
> capture that choice
> record why we chose Opus over Gemini
```

The skill extracts the decision from conversation context and appends a structured entry to `.claude/plans/decisions.md`.

It also suggests proactively — after a significant choice is made, it may offer: "That threshold decision seems worth capturing. Want me to log it?"

### Review Mode

```
> show me decisions about training data
> what did we decide about the teacher model?
> review decisions from this phase
> any decisions due for revisit?
```

## What Gets Captured

Each entry records:

- **Decision** — specific one-line statement
- **Alternatives considered** — what else was on the table and why it was rejected (the most valuable field in hindsight)
- **Rationale** — evidence and constraints that drove the choice
- **Risks accepted** — known tradeoffs
- **Revisit trigger** — concrete conditions that would reopen the decision

## Where It Creates Value

- **Executive reviews** — "Why didn't you just do X?" You have the receipts.
- **Onboarding** — compressed history of every fork in the road
- **Retrospectives** — systematic review of which decisions held up
- **Self-continuity** — across weeks of implementation, prevents re-litigating settled decisions

## Installation

```bash
ln -s ~/Projects/claude-skills/decision-logger ~/.claude/skills/decision-logger
```
