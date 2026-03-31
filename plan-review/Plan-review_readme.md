# Plan Review — Adversarial Audit Skill

A Claude Code skill that transforms Claude from a helpful collaborator into a skeptical, independent auditor. Built for anyone who needs honest stress-testing of plans, strategies, architectures, or proposals — not just validation.

## Why This Exists

Claude has a natural tendency to be agreeable, especially when it helped create the plan being reviewed. This skill forces a deliberate role shift into adversarial analysis mode, ensuring real problems get surfaced instead of buried in reassurance.

## How to Use It

With the skill installed, just use natural language in any Claude Code session:

```
> red team this plan
> stress-test this architecture
> is this plan solid? what am I missing?
> play devil's advocate on this proposal
> review this critically — what could go wrong?
```

You can reference a plan file directly:

```
> cat plans/q3-roadmap.md
> red team this — what's going to break?
```

Or use it after co-creating a plan in the same session — the skill explicitly breaks out of collaborator mode.

## The 7-Lens Framework

The skill runs a structured analysis through these lenses:

1. **Assumptions Audit** — Surfaces unstated assumptions, flags cascade risks where a single wrong assumption brings down the whole plan
2. **Failure Mode Analysis** — Identifies the 3-5 most realistic failure scenarios with likelihood and severity ratings
3. **Gaps & Blind Spots** — Finds what the plan doesn't address: missing dependencies, unaccounted stakeholders, resource constraints
4. **Internal Consistency Check** — Catches contradictions: misaligned timelines, resource conflicts, metrics that don't measure what they claim to
5. **Second-Order Effects** — Explores unintended consequences of the plan succeeding exactly as written
6. **Strongest Counterargument** — The sharpest possible objection a skeptical executive would use to kill this plan
7. **Verdict & Recommendations** — Direct assessment with the top 3 priority actions

## What It Won't Do

- Summarize the plan back to you (you already know what it says)
- Generate generic risks that apply to any plan
- Soften findings with excessive hedging
- Rewrite the plan — it flags issues and lets you decide

## Installation

```bash
ln -s ~/Projects/claude-skills/plan-review ~/.claude/skills/plan-review
```

See the [repo README](../README.md) for full setup instructions.

## Works Well With

- Product roadmaps and PRDs
- Technical architecture proposals
- Go-to-market strategies
- Business cases and investment proposals
- Project plans and timelines
- AI/ML deployment strategies
- Competitive positioning frameworks
