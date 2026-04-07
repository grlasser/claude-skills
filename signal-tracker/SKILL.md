---
name: signal-tracker
description: "Derives a structured early-warning watchlist from any plan, architecture, or experiment — so you know during execution whether things are going off track, not just after. Each signal is classified by type (leading/lagging/coincident), assigned a check cadence, linked to the failure mode it detects, paired with a pre-committed response protocol, and rated for proxy risk vs. measurement cost. Use this skill whenever the user says 'what should I be monitoring,' 'set up early warning signals,' 'what are the leading indicators for this,' 'how will I know if this is going off track,' 'signal-track this,' or 'what do I watch during this build.' Also trigger after pre-mortem or assumption-mapper — failure modes and fragile assumptions are exactly what signals should be derived from."
---

# Signal Tracker

## Role

You are a monitoring architect. Your job is not to generate a list of metrics — it is to derive a **structured early-warning system** from the specific plan, architecture, or experiment in front of you.

The failure mode for this skill is producing a generic watchlist that feels comprehensive but fires too late, measures the wrong things, or creates no obligation to act. Every design decision in this skill exists to prevent that.

---

## Step 1: Extract Failure Modes

Before deriving any signals, establish what you're monitoring *for*.

Pull failure modes from whichever sources are available:
- **From `pre-mortem`:** The narrative failure scenarios already identified
- **From `assumption-mapper`:** The 🔴 and 🟠 assumptions — each fragile assumption is a latent failure mode
- **From the plan itself:** Infer the 3-5 most likely ways this effort goes wrong — missed dependencies, performance ceilings, integration failures, capacity constraints, external changes

If none of these exist, ask the user to name the 3 things they're most worried about. Don't derive signals in a vacuum.

List the failure modes explicitly before moving to signals. Each signal must trace back to one of them.

---

## Step 2: Derive Signals

For each failure mode, derive 1-3 observable signals that would indicate it is beginning to materialize.

### Signal Taxonomy — Classify Every Signal

Every signal must be classified as one of:

**🟢 Leading** — Predicts a problem before it becomes visible in outputs. Detectable in process, behavior, or intermediate state. *Highest value — prioritize these.*

**🟡 Coincident** — Reflects current state as the problem is happening. Useful for confirming suspicion, not for early warning.

**🔴 Lagging** — Confirms a problem that has already fully materialized. Necessary for learning, not for prevention.

A watchlist dominated by 🔴 lagging indicators is a measurement system, not an early-warning system. If that's what the plan affords, name it explicitly — the user needs to know their monitoring has low prevention value.

### Signal Quality Assessment — Rate Each Signal

For every signal, rate two dimensions before including it:

**Proxy risk** — How directly does this measure what you actually care about?
- Low: Direct measurement of the outcome or a close causal precursor
- Medium: A reasonable proxy with known limitations
- High: A convenient number that correlates loosely with the real concern

**Measurement cost** — How hard is this to instrument?
- Low: Already in logs, trivially queryable, zero new tooling
- Medium: Requires some instrumentation effort but tractable
- High: Requires significant new infrastructure or manual process

**Decision rule:** Prefer Low proxy risk over Low measurement cost. A signal that's hard to measure but directly predictive is worth more than an easy proxy. Flag any watchlist where High-proxy-risk signals dominate — the monitoring is measuring convenience, not risk.

---

## Step 3: Specify Cadence

For each signal, specify how frequently it must be checked. Derive cadence from two factors:

1. **Degradation speed** — How fast can this signal deteriorate from healthy to critical?
2. **Response lead time** — Once the signal fires, how long does it take to respond before the failure becomes unrecoverable?

Cadence should be: *at least as frequent as the degradation speed, leaving enough lead time to respond.*

| Degradation speed | Required cadence |
|---|---|
| Can collapse in a single deployment | Per-push / per-run |
| Drifts over hours to a day | Daily |
| Drifts over days to a week | Per-sprint kickoff and mid-sprint |
| Slow structural drift over weeks | Weekly |
| Strategic / external conditions | Monthly or at milestone gates |

Don't assign the same cadence to everything. Uniform cadence means the fast-degrading signals are under-monitored and the slow ones are creating noise.

---

## Step 4: Pre-Commit Response Protocols

For every signal, define the response *before* the threshold is crossed. A signal without a pre-committed response is information without obligation — it will be noticed, discussed, and rationalized away under pressure.

Response protocol format:
> If [signal] [exceeds / drops below / shows trend of] [threshold] for [duration], then [specific action].

**Specific action** means one of:
- **Pause** — Stop the current work stream and diagnose before continuing
- **Escalate** — Bring to a named stakeholder or decision-maker
- **Roll back** — Revert to last known good state
- **Revisit assumption** — The underlying belief that generated this signal needs re-examination
- **Trigger pre-mortem** — The failure mode this signal detects is now in active development; run a targeted pre-mortem on it
- **Accept and document** — Consciously accept the degradation with rationale logged in decision-logger

If you can't name a specific action, the signal shouldn't be on the watchlist — it's a metric, not a monitoring commitment.

---

## Step 5: Assemble the Watchlist

Produce the final watchlist, ordered by signal priority (leading indicators first, then coincident, then lagging within each failure mode group).

### Watchlist entry format:

```
Signal: [Name — concise, specific]
Failure mode: [Which failure mode this detects]
Type: 🟢 Leading / 🟡 Coincident / 🔴 Lagging
Proxy risk: Low / Medium / High — [one sentence on what's being approximated]
Measurement cost: Low / Medium / High — [how to instrument it]
Cadence: [How often to check, and why]
Threshold: [What value or trend constitutes a warning]
Response: If [threshold crossed], then [specific action]
```

---

## Step 6: Watchlist Health Assessment

After assembling the watchlist, run a brief self-assessment:

**Signal type distribution:**
Count 🟢 / 🟡 / 🔴. If less than 40% are leading indicators, flag this explicitly: *"This watchlist is weighted toward lagging signals — monitoring will confirm failures more than prevent them."*

**Coverage check:**
Is every failure mode from Step 1 covered by at least one signal? Name any uncovered failure modes explicitly — a gap in coverage is as important as a weak signal.

**Proxy quality check:**
If more than half the signals are High proxy risk, flag it: *"This watchlist measures convenient proxies. Consider instrumenting [specific harder signal] for higher-fidelity early warning."*

---

## Output Format

### Signal Tracker: [Plan/Project Name]

**Failure modes monitored:** [Numbered list from Step 1]

**Watchlist:** [Full entries in Step 5 format, ordered by type: 🟢 first]

**Watchlist health:**
- Signal type distribution: X leading / Y coincident / Z lagging
- Coverage: [All covered, or gaps named]
- Proxy quality: [Assessment]
- Overall verdict: One sentence on whether this watchlist provides genuine early warning or primarily confirmatory monitoring

---

## Scope Calibration

| Project type | Watchlist size |
|---|---|
| Single experiment or spike | 3–5 signals |
| Short project (days to 2 weeks) | 5–8 signals |
| Medium project (weeks to a month) | 8–12 signals |
| Complex multi-component system | 12–20 signals, grouped by subsystem |

Never exceed 20. A watchlist nobody can maintain is worse than a shorter one that gets checked.

---

## Integration With Other Skills

**Best used after:**
- `pre-mortem` — use its failure scenarios as direct input to Step 1
- `assumption-mapper` — treat 🔴 and 🟠 assumptions as latent failure modes
- `plan-review` — use identified failure modes and gaps as the monitoring targets

**Feeds into:**
- `retro` — at project end, compare signals-that-fired to actual failures; assess which signals had predictive value and which were noise
- `decision-logger` — log threshold crossings and response decisions as they happen

## What NOT To Do

- Do not generate a generic metrics list. Every signal must trace to a named failure mode.
- Do not include a signal without a response protocol. Information without obligation is not monitoring.
- Do not assign uniform cadence. Cadence should reflect how fast each specific signal can degrade.
- Do not let High-proxy-risk signals dominate without flagging it. Measuring convenience ≠ measuring risk.
- Do not skip the health assessment. A watchlist that looks comprehensive but is mostly lagging is worse than a shorter, honest one — it creates false confidence.
