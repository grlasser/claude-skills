# Pre-Mortem — Narrative Failure Analysis

A Claude Code skill that generates realistic failure stories for your project before you start building. Instead of listing risks analytically (that's what [plan-review](../plan-review/) does), pre-mortem imagines the project has already failed and works backward through the causal chain.

## Why Pre-Mortem ≠ Plan Review

| | Plan Review | Pre-Mortem |
|---|---|---|
| **Approach** | Analytical decomposition | Narrative imagination |
| **Output** | Risk assessment table | Three failure stories + fragility map |
| **Catches** | Structural flaws (assumptions, gaps, contradictions) | Dynamic failures (timing, politics, compounding delays) |
| **Perspective** | Engineer auditing a blueprint | War-gamer reconstructing a defeat |

## How to Use

```
> pre-mortem this plan
> imagine this project fails — tell me why
> what kills this project?
> war-game this
> write the post-mortem before we start
```

## What You Get

1. **Three failure narratives** — distinct stories covering technical, organizational, and timing/external failures, each with a specific causal chain and intervention point
2. **Fragility map** — the 3-4 moments in your timeline where the project is most vulnerable, with early warning signals and preventive actions
3. **Epitaph** — a single uncomfortable sentence: "This project died because ___"

## What It Uniquely Surfaces

- Sequence-dependent risks that look fine in isolation
- Organizational dynamics (champion leaves, competing initiative, political shifts)
- Motivation decay over multi-week efforts
- Success traps (partial success worse than clean failure)
- Compounding delays that cascade through dependencies

## Installation

```bash
ln -s ~/Projects/claude-skills/pre-mortem ~/.claude/skills/pre-mortem
```
