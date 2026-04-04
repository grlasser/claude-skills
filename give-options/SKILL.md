---
name: give-options
description: "Adversarial options analysis for decisions, migrations, feature designs, workarounds, and architectural choices. Use this skill whenever the user asks to propose, compare, or evaluate multiple options or approaches. Trigger phrases include: 'give me options', 'propose approaches', 'what are my options', 'how should I approach', 'how would you tackle', 'compare approaches', 'pros and cons', 'what's the best way to', 'help me decide', 'evaluate alternatives', 'trade-off analysis', 'migration options', 'workaround ideas', 'give me alternatives', 'what's the best approach', or any request that involves generating and comparing multiple candidate solutions. Also trigger when the user asks for a recommendation on HOW to do something where multiple valid paths exist, even if they don't explicitly say 'options'. Trigger for migrations, technology choices, architectural decisions, feature implementation strategies, and process/workflow design. Do NOT trigger for reviewing an existing plan (use plan-review instead) or for simple factual questions with one answer."
---

# Give Options: Adversarial Options Analysis

## Purpose

Generate multiple candidate solutions for a problem, stress-test each one adversarially, then deliver a clear recommendation backed by evidence. Options that enter this process raw must survive scrutiny to earn a recommendation. Fight the instinct to defend your own proposals.

## Depth Calibration

Not every decision deserves the same analytical weight. Before starting, assess the decision's weight:

**Heavyweight** (architecture migrations, platform choices, multi-month initiatives): Run the full process. Research actively. Stress-test thoroughly.

**Midweight** (library selection, feature implementation approach, workflow design): Run the full process but keep stress tests focused on the 2-3 most relevant lenses per option. Skip lenses that don't apply.

**Lightweight** (tool selection, configuration choices, minor design decisions): Abbreviate. Generate options with brief rationale, do a quick comparative table, give a recommendation. Skip the full stress-test phase.

State the calibration level at the start so the user knows what depth to expect.

## Process

### Phase 1: Problem Frame

Establish the decision space. Extract as much as possible from the user's message and conversation history before asking anything. Only ask clarifying questions if critical information is genuinely missing (not for information you can reasonably infer).

State:
- **The core problem or goal** (restate to confirm understanding)
- **Hard constraints** (non-negotiables the user stated or that are obvious from context)
- **Current state** (what exists today)
- **Success criteria** (what "this worked" looks like)

If the user provided rich context, do not slow them down with a questionnaire. Frame and proceed.

### Phase 2: Research

**This phase is mandatory for heavyweight and midweight decisions.** Before generating options, search for:

- Official documentation for the technologies involved
- Known limitations, open issues, and community-reported problems
- Migration guides, post-mortems, or case studies from teams who have done similar transitions
- Benchmark data or performance comparisons where relevant
- Recent developments (version changes, deprecations, roadmap shifts) that affect viability

Do not generate options from training data alone when current information is available. The user asked for objectivity, which requires evidence.

For lightweight decisions, a quick search is sufficient. For heavyweight decisions, invest several searches to ground the analysis in reality.

### Phase 3: Option Generation

Generate the requested number of options (default: 4-5). If fewer genuinely distinct approaches exist, generate fewer and say why. Do not pad.

Each option must be:

- **Distinct in approach.** Different strategies, tools, architectures, or sequencing. If three options are variations on the same idea, you failed. Push for genuine diversity: different trade-off profiles, different risk postures, different levels of ambition.
- **Concretely specified.** Enough detail to start executing. "Use a microservices approach" is not an option. "Decompose into three services communicating via gRPC, deployed on K8s" is.
- **Honestly scoped.** State effort, expertise, infrastructure, and time requirements. Do not lowball to make an option look attractive.

For each option, provide:
1. **Name**: Short, descriptive label
2. **Approach**: 3-5 sentence summary of what this entails
3. **Key mechanism**: The core technical or strategic lever this option pulls
4. **Effort estimate**: Order of magnitude (days/weeks/months, team size)
5. **Key dependency**: The single most critical thing this depends on

### Phase 4: Adversarial Stress Test

For each option, select and apply the stress-test lenses that are relevant to this type of decision. Do not mechanically apply all lenses to every option. Choose 3-4 from:

**Assumption Cracking**: Identify the 2-3 most fragile assumptions. For each, describe a realistic scenario where it fails and the consequence.

**Realistic Failure Mode**: The single most likely way this option fails in practice. Not edge cases. The thing that actually goes wrong when teams try this.

**Hidden Costs**: Operational overhead, cognitive load, tech debt, vendor lock-in, migration pain later, debugging difficulty, monitoring gaps. Costs that aren't obvious at first glance.

**Scaling & Evolution**: What happens at 10x load/scope? What if a key technology gets deprecated? How hard is it to pivot away once committed? *(Most relevant for architecture and platform decisions.)*

**Evidence Check**: Do the research results support or contradict this option's viability? Have other teams succeeded or failed with this approach? What did they learn? *(Most relevant when real-world data was found in Phase 2.)*

**Reversibility**: How deep is the commitment? What's the cost of unwinding this if it doesn't work after 3 months? *(Most relevant for migrations and platform choices.)*

After each option's stress test, state a clear verdict:
- **Survived intact**: Minor concerns, no structural problems. Note mitigations.
- **Survived with modifications**: Real issues found, but patchable. State the modifications and how they change the effort/complexity profile.
- **Eliminated**: Fundamental flaw exposed. State the flaw clearly and remove from final consideration. Do not carry dead options forward.

### Phase 5: Synthesis

This is where the analysis earns its value.

#### Hybrid Check
Before comparing survivors, ask: can elements of two options be combined into something stronger than either alone? If yes, propose the hybrid as an additional candidate and briefly stress-test it.

#### Comparative Matrix
Compare surviving options across relevant dimensions. Choose dimensions that matter for THIS decision (not a generic checklist). Common useful dimensions:

- Implementation effort / Time to first value
- Operational complexity / Maintenance burden
- Reversibility / Commitment depth
- Risk profile (worst-case downside)
- Future flexibility
- Team skill alignment

Use a clear rating: Strong / Adequate / Weak. Commit to ratings. Do not hedge everything to "Adequate."

#### Trade-off Map
For the top 2-3 survivors, state the core trade-off crisply: "Option A optimizes for X at the cost of Y. Option B does the reverse." Frame it so the user can decide based on what they value most.

### Phase 6: Recommendation

Lead with the answer. Do not bury it.

1. **Primary recommendation**: Which option and why, in 2-3 sentences
2. **Runner-up**: The best alternative and what would have to change to make it the better choice
3. **Conditional triggers**: "Choose Option B instead if [specific condition]"
4. **First concrete step**: What the user should do in the next 48 hours
5. **What to watch for**: Early signals (within the first 2 weeks) that the chosen approach is working or failing

If two options are genuinely close, say so, but still pick one and explain the margin. "It depends" is not a recommendation.

## Output Structure

For heavyweight and midweight decisions, structure as:

```
## Recommendation (Lead with this)
[Phase 6: Primary pick, runner-up, conditional triggers, next step]

## Problem Frame
[Phase 1]

## Options Considered
### Option 1: [Name]
[Phase 3 detail]
**Stress Test**: [Phase 4 findings]
**Verdict**: [Survived / Modified / Eliminated]

### Option 2: [Name]
...

## Comparative Assessment
[Phase 5: Matrix, trade-off map, hybrid if applicable]
```

Note: Recommendation comes FIRST. The supporting analysis follows for those who want to dig in. The user should be able to read the first section and have a clear answer, then read further only if they want to understand the reasoning.

For lightweight decisions, use an abbreviated format: brief options list, quick comparison table, recommendation. No stress-test section.

## Calibration Rules

- **Do not manufacture options to hit a count.** If only 3 distinct approaches exist, generate 3.
- **Do not equivocate in the recommendation.** Pick one. Explain the margin if it's close.
- **Weight practical experience over theoretical elegance.** An option that is technically beautiful but that teams routinely fail to execute is worse than a boring option that reliably ships.
- **Name specific technologies, tools, and patterns.** Vague options are useless.
- **Respect the user's context.** Every option must be evaluated against the user's real constraints (stack, team size, timeline), not an ideal scenario.
- **Ground claims in evidence.** When research turned up relevant data, cite it. When you're reasoning without evidence, say so.
- **Stress-test your own recommendation.** Before finalizing, ask yourself: "What's the strongest argument against my pick?" If it's strong enough to change your mind, change it.

## What NOT To Do

- Do not generate obviously non-viable options to pad the list.
- Do not give every option the same "it has trade-offs" verdict. Some options are better. Say which.
- Do not skip the research phase for heavyweight decisions. Objectivity without evidence is just confident speculation.
- Do not apply every stress-test lens to every option regardless of relevance. Select the lenses that matter.
- Do not bury the recommendation at the bottom of a 3,000-word analysis. Lead with it.
- Do not present stress-test findings and then ignore them in the recommendation.
- Do not soften the elimination of weak options. If it failed, it's out.
- Do not treat all options as mutually exclusive without checking for productive hybrids.
