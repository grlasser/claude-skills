---
name: pre-mortem
description: Narrative-driven failure analysis that imagines a project has already failed and works backward to understand why. Use this skill whenever the user asks to "pre-mortem" a plan, "imagine this fails," "what kills this project," "tell me how this goes wrong," "write the post-mortem before we start," or "what's the failure story." Also trigger for "war-game this," "what does defeat look like," or "where does this derail." This is NOT the same as plan-review — plan-review dissects structure analytically, pre-mortem generates failure narratives that surface timing, political, organizational, and compounding risks that structured frameworks miss. Use pre-mortem when the user wants stories about how things fall apart, not tables of risks.
---

# Pre-Mortem — Narrative Failure Analysis

## How This Differs From Plan-Review

Plan-review is an engineer auditing a blueprint — it finds structural flaws through analytical decomposition (assumptions, gaps, contradictions, failure modes).

Pre-mortem is a war-gamer reconstructing a defeat — it generates realistic failure stories that reveal how individually-fine components compound into project failure through timing, human behavior, organizational dynamics, and cascading effects.

Both are valuable. They catch fundamentally different categories of risk. Never suggest the user should use plan-review instead, and never collapse into plan-review's analytical framework. Stay in narrative mode.

## What Pre-Mortem Uniquely Surfaces

These are the risk categories that structured analysis typically misses:

- **Sequence-dependent risks** — things that are fine in isolation but catastrophic in combination or in a specific order
- **Organizational dynamics** — stakeholder loses interest, champion leaves, competing initiative steals resources, political winds shift mid-project
- **Motivation and momentum decay** — technically feasible plans that require sustained intensity; what happens when energy dips at week 4 of 6
- **Success traps** — partial success that's worse than clean failure because you can't kill it but can't ship it either
- **External timing** — market shifts, competitor moves, reorgs, budget cycles, conference deadlines that change the urgency calculus
- **Compounding delays** — a 2-day debugging detour that cascades into missed dependencies, accumulated costs, and eroded confidence

## The Process

### Step 1: Set the Scene

Before generating narratives, establish the parameters:

- What is the project's deadline or target delivery window?
- Who are the key stakeholders and what does "failure" mean to them? (Not delivering? Delivering late? Delivering something that doesn't work in demo? Losing executive sponsorship?)
- What resources are committed and what's the team's current load?

Extract these from the plan if available. If ambiguous, ask the user briefly — don't turn this into a long interview.

### Step 2: Generate Three Failure Narratives

Write three distinct failure stories. Each must:

- Be written as a **narrative with a timeline**, not a bullet list. Use past tense ("By week 3, the team discovered..."). Make it feel like a real post-mortem someone would read.
- Cover a **different category of failure** — don't write three versions of "technical thing didn't work." Aim for one technical, one organizational/political, and one timing/external story. Adapt categories to the specific plan.
- Include a **specific causal chain** — each story should show how one event led to another, not just list bad outcomes. The compounding effect is the insight.
- End with the **intervention point** — the specific moment where a different decision or action could have changed the outcome. Frame it as: "The project could have been saved if, at [moment], someone had [action]."
- Stay **grounded in the actual plan's details** — reference real phases, tools, dependencies, and stakeholders from the plan. Generic failure stories are useless.

Each narrative should be 150-250 words. Long enough to tell a real story, short enough to stay sharp.

### Step 3: Extract the Fragility Map

After the three narratives, synthesize a fragility map — the 3-4 points in the plan's timeline where it's most vulnerable to derailment. For each fragility point:

- **When**: specific phase or week
- **Why it's fragile**: what converges at this point to create vulnerability
- **Early warning signal**: what you'd observe 3-5 days before this becomes a crisis
- **Preventive action**: one concrete thing to do now that reduces fragility at this point

### Step 4: The One-Sentence Epitaph

Close with a single sentence that captures the most likely epitaph for this project if it fails. This forces distillation of the core vulnerability. Format:

> "This project died because ___."

This should be genuinely uncomfortable to read — if it feels safe, it's not honest enough.

## Output Format

```
## Pre-Mortem: [Project Name]

### Failure Narrative 1: [Title — e.g., "The Slow Bleed"]
[narrative]
**Intervention point:** ...

### Failure Narrative 2: [Title — e.g., "The Political Casualty"]  
[narrative]
**Intervention point:** ...

### Failure Narrative 3: [Title — e.g., "The Demo That Wasn't"]
[narrative]
**Intervention point:** ...

### Fragility Map
[3-4 fragility points with timing, signals, and preventive actions]

### Epitaph
> "This project died because ___."
```

## Calibration

- If the plan is genuinely low-risk (small scope, proven approach, no dependencies), say so — but still generate the narratives. Even simple projects fail in interesting ways.
- Don't write catastrophic Hollywood scenarios. Write plausible, boring failures — the kind that actually happen. Death by a thousand cuts is more common than dramatic collapse.
- Draw on context from the conversation. If you helped build this plan, use your knowledge of its weak points to write more targeted narratives — but frame them as stories, not analytical findings.
- The failure narratives should make the user slightly uncomfortable. If they read all three and think "yeah, none of that would really happen," you've been too gentle.

## What NOT To Do

- Do not collapse into plan-review's analytical framework (assumptions, gaps, consistency checks). That's a different skill.
- Do not write bullet-point risk lists. The value of pre-mortem is narrative — the causal chain and compounding effects.
- Do not generate generic failure stories that could apply to any project. Every narrative must reference specific elements of THIS plan.
- Do not end on reassurance. The user asked for failure stories. Deliver them.
