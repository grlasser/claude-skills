# Give Options: Adversarial Options Analysis

A Claude Code skill that generates multiple candidate solutions for a problem, subjects each one to rigorous adversarial stress-testing, and delivers a clear recommendation backed by evidence. Options go in raw, get hammered, and only the ones that hold up earn a recommendation.

## Why This Exists

When facing a decision with multiple valid paths (migration strategies, architecture choices, feature implementations, workarounds), Claude's default behavior is to present options that all sound reasonable. This skill forces a different process: generate genuinely distinct approaches, then try to destroy each one before recommending a winner. The result is options that have survived scrutiny, not options that merely sound plausible.

## How It Differs from Plan Review

**plan-review** audits an *existing* plan. **give-options** *generates* multiple candidate solutions from scratch, then stress-tests each one adversarially before doing a comparative assessment. It's the difference between reviewing a blueprint and forging the blueprint through adversarial pressure.

## How to Use It

With the skill installed, use natural language in any Claude Code session:

```
> give me 5 options for migrating to FalkorDB, with adversarial analysis
> what are my options for implementing real-time event correlation?
> propose approaches for replacing our current caching layer
> how should I tackle the SR Linux telemetry pipeline redesign?
> compare alternatives for the graph state persistence layer
> trade-off analysis: gRPC vs REST vs GraphQL for the agent API
```

## The 6-Phase Process

1. **Problem Frame** establishes constraints, current state, and success criteria before generating anything. Extracts context from your message first, only asks clarifying questions when critical information is genuinely missing.

2. **Research** (mandatory for significant decisions) searches for documentation, known limitations, community post-mortems, and benchmark data. Objectivity grounded in evidence, not just reasoning from training data.

3. **Option Generation** produces genuinely distinct approaches (not variations on a theme), each with concrete detail, effort estimates, and key dependencies. If fewer distinct options exist than requested, says so rather than padding.

4. **Adversarial Stress Test** selects relevant lenses per option from: assumption cracking, realistic failure modes, hidden costs, scaling/evolution pressure, evidence checks, and reversibility analysis. Dead options get eliminated, not carried forward.

5. **Synthesis** checks for productive hybrids (can elements of two survivors combine into something stronger?), then produces a side-by-side comparison matrix and explicit trade-off map.

6. **Recommendation** leads the output with a clear pick, runner-up, conditional triggers ("choose B instead if..."), a concrete first step, and early warning signals to watch for.

## Depth Calibration

The skill automatically scales its depth to match the decision's weight:

**Heavyweight** (architecture migrations, platform choices): Full process with active research and thorough stress testing.

**Midweight** (library selection, feature approach): Full process, focused stress tests on the 2-3 most relevant lenses per option.

**Lightweight** (tool selection, configuration choices): Abbreviated format with quick comparison table and recommendation.

## Installation

```bash
ln -s ~/Projects/claude-skills/give-options ~/.claude/skills/give-options
```

See the [repo README](../README.md) for full setup instructions.

## Works Well With

- Technology migration decisions
- Architecture and platform choices
- Feature implementation strategies
- Workaround and limitation mitigation
- Library, framework, and tooling selection
- Process and workflow design
- Build vs. buy evaluations
