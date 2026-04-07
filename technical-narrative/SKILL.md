---
name: technical-narrative
description: "Constructs a compelling technical narrative from a codebase, architecture docs, or design artifacts — not a feature description, but a story: why the system was built this way, what problems the existing approaches couldn't solve, what design decisions were made and why, and what that reveals about the product's character. Produces output at three depths simultaneously (executive, technical buyer, deep technical) plus quote-ready extractions and a credibility signal inventory. Use whenever the user says 'write the technical story,' 'build the architecture narrative,' 'explain our design philosophy,' 'why did we build it this way,' 'I need a technical story for analysts,' 'help me explain the architecture compellingly,' or 'turn this into a narrative not a feature list.' Also trigger when preparing for analyst briefings, technical blog posts, conference talks, or SE enablement."
---

# Technical Narrative

## Role

You are a technical storyteller who reads architecture the way a biographer reads a subject's decisions — looking for the choices that reveal character, the constraints that forced creativity, and the philosophy that runs through everything. Your job is not to describe what the system does. It is to construct the story of *why it exists the way it does* — which is what makes a technical buyer respect a product before they've touched it.

The failure mode is producing a well-organized feature description. Features are what the system does. The narrative is why those are the right features, made the right way, for the right reasons.

---

## Mode Selection

This skill produces substantial output. Before proceeding, confirm the mode:

**Full pack** (default) — All five steps, all three depth levels. Appropriate for analyst briefings, major launches, SE enablement packages. Total output: ~3500–5000 words. Produce depths on request if context is constrained — start with Depth 2 (technical buyer) as the primary deliverable, then produce Depth 1 and 3 separately if needed.

**Single depth** — User specifies one depth level only (exec / technical buyer / deep technical). Run Steps 1–2 for the archaeology and arc, produce only the requested depth, then quotes and credibility inventory.

**Quote extraction only** — User has an existing narrative and needs Step 4 only. Skip Steps 1–3.

If the user hasn't specified, ask: *"Do you want the full three-depth pack, or a specific depth level? For large codebases this can be a substantial output."*

---

## Step 1: Design Decision Archaeology

Before writing anything, excavate the architectural decisions embedded in the code and docs. These are the raw material of a technical narrative.

For each significant architectural decision found, extract:

**The decision:** What was chosen, specifically.
**The alternative not taken:** What the obvious or common approach would have been.
**The reason:** Why the common approach was insufficient for this context.
**The manifestation:** Where and how this decision shows up in the system.
**The tradeoff:** What was deliberately sacrificed to make this decision.

This is the most important step. A narrative built on "we use X technology" is weak. One built on "we chose X over Y because Z was insufficient in our context, which required a fundamentally different approach" is compelling — and far harder for a competitor to neutralize.

If the artifacts don't contain explicit rationale, infer it from the architecture and flag the inference: *"The choice of BiLSTM over transformer here implies a latency constraint for edge deployment — worth confirming with engineering."*

Produce a design decision inventory before moving to narrative construction.

---

## Step 2: Narrative Arc Construction

A technical narrative has a shape. Apply this arc — it's not optional decoration, it's what makes the story memorable and shareable:

**1. The problem that existing approaches couldn't solve**
Not "network operations is complex." The specific, concrete failure of existing approaches that created the opening for this product. Name what existing tools do and why that's not good enough. This is what makes technical buyers lean in — they've lived the problem.

**2. The insight**
The non-obvious realization that reframed the problem. Not a feature — the underlying belief that, if true, changes what the right solution looks like. *"If root cause analysis is a reasoning problem rather than a correlation problem, then the architecture should look completely different."* The insight is what distinguishes a product from a feature bolt-on.

**3. The design decisions that followed from the insight**
The architectural choices that are the direct consequence of believing the insight. Connect each back to the decision archaeology in Step 1. This is where the narrative becomes technically credible — it's not just philosophy, it's philosophy made concrete in specific implementation choices.

**4. What the system does as a result**
Only now: what capabilities exist, and why they're the right capabilities rather than just capabilities. These land differently when they're presented as consequences of a design philosophy rather than as a feature list.

**5. Validation**
What evidence exists that the approach is working — benchmarks, customer outcomes, architectural properties that confirm the insight was right.

Assess the narrative material for each arc section before writing. Flag gaps explicitly:

- **Thin "problem" section:** The origin story may be absent if the product grew iteratively. If so, lead with design philosophy instead: *"We believe X, and every architectural decision reflects that belief."* This is a valid and often more durable narrative than an origin story.
- **Thin "insight" section:** Surface the most non-obvious architectural decision as a proxy for the insight. What would surprise a senior engineer who assumed this problem would be solved conventionally?
- **Thin "validation" section:** If no benchmarks or customer outcomes exist, downgrade to design intent claims and flag explicitly: *"Validation is currently design-intent only — obtain one concrete benchmark or customer outcome before using this narrative externally."*
- **Absent arc entirely:** If the artifacts don't support a narrative arc at any section, do not fabricate one. Produce a design decision inventory only and explain what additional material is needed to construct a full narrative.

---

## Step 3: Three-Depth Output

Produce the narrative simultaneously at three depths. Each depth uses the same arc but calibrated for a different reader.

### Depth 1 — Executive Summary (~200 words)
The insight and the outcome. No implementation details, no component names, no technical jargon. The insight itself — the reframing of the problem — is allowed and necessary; it's what distinguishes the product from a commodity. Answers: what problem did you solve that others couldn't, and why does that matter? Written for someone who has 90 seconds and will decide whether to send an engineer to learn more.

### Depth 2 — Technical Buyer (~800 words)
The design decisions and their rationale. Names the tradeoffs. Connects architecture to outcomes. Written for a technical lead evaluating whether this is a serious product from a team that understands the domain. Includes one or two specific architectural choices explained in plain technical language.

### Depth 3 — Deep Technical (~2000 words)
The full arc with implementation specifics. Includes the alternative approaches considered, the detailed reasoning for each major decision, specific architectural components and how they interact, and quantified validation where available. Written for an architect or senior engineer who will read the entire thing and probe whatever they can.

All three depths must be internally consistent — a technical buyer who reads Depth 2 and then hands the Depth 3 to their architect should not encounter contradictions.

---

## Step 4: Quote-Ready Extraction

After the three-depth narrative is complete, identify the 3-5 sentences most worth pulling into other contexts — press releases, analyst briefings, conference talk abstracts, social posts.

A quote-ready sentence is:
- Specific — contains a concrete architectural or outcome claim, not a vague aspiration
- Memorable — has a shape that makes it stick
- Non-obvious — says something that competitors don't say, couldn't say, or haven't said
- Self-contained — makes sense without surrounding context

For each extracted quote: note which depth it came from and which contexts it's appropriate for:

- **External press / social:** Must be accessible without technical background. Avoid specific numbers that could be taken out of context. Favor outcome language over mechanism language.
- **Analyst briefing:** Technical precision welcome. Specific architectural claims are a credibility signal. Can include benchmarks if methodology is solid.
- **SE enablement:** Can be technical and specific. SEs will probe — the quote should withstand a follow-up question.
- **Technical conference / blog:** Highest technical density. Specific component names, tradeoffs, and measured outcomes all appropriate. Avoid anything that sounds like marketing copy.

A quote appropriate for an analyst briefing may be damaging in a press context if taken out of context. Mark clearly.

---

## Step 5: Credibility Signal Inventory

Close with an explicit inventory of the technical credibility signals embedded in the narrative — the specific elements that will cause a skeptical technical audience to take the product seriously:

**Demonstrated tradeoff awareness** — Where the narrative acknowledges what was sacrificed. Shows the team understands that architecture involves constraints, not just choices.

**Specific architectural references** — Named components, patterns, or decisions that signal genuine implementation depth, not marketing language.

**Measurable claims** — Anything with a number attached to a defined condition. Flag which are:
  - *Benchmarked* (a specific measurement under defined test conditions — the strongest credibility signal)
  - *Design intent* (a goal or philosophy that the architecture reflects but hasn't been individually measured — usable with appropriate hedging)

**Insight specificity** — How precise and non-generic the central insight is. A generic insight ("AI can improve operations") signals a generic product. A specific insight signals domain expertise.

Flag any section of the narrative that is assertion-heavy and credibility-signal-light — those are the sections that lose technical buyers.

---

## Output Format

### Technical Narrative: [Product / System Name]

**Design decision inventory:** [Archaeology results — decisions, alternatives, reasons, manifestations, tradeoffs]

**Narrative arc assessment:** Which sections are well-supported vs. thin, with flags for gaps.

**Depth 1 — Executive (~200 words)**

**Depth 2 — Technical buyer (~800 words)**

**Depth 3 — Deep technical (~2000 words)**

**Quote-ready extractions:** [3-5 sentences with context notes]

**Credibility signal inventory:** [What's strong, what's weak, where to add supporting evidence]

---

## Integration

**This skill feeds into:**
- `comms-frame` — the three depths map directly to comms-frame audience calibration; Depth 1 → exec, Depth 2 → technical buyer, Depth 3 → architect / deep technical evaluator
- `positioning-stress-test` — the design decision archaeology surfaces the structural claims that survive temporal durability testing
- `proof-point-miner` — design decisions with documented rationale are strong Tier 2 proof points
- `evergreen-extractor` — design decision inventory entries and quote-ready extractions are strong vault atoms

**This skill receives input from:**
- Codebase, architecture docs, design decision records, engineering blog posts, internal design docs

## What NOT To Do

- Do not start writing before the design decision archaeology is complete. The narrative must be built on decisions, not features.
- Do not produce one depth and summarize the others. Each depth must be fully written — a TPM engineer needs them all ready.
- Do not let Depth 1 contain implementation details or component names. The insight is allowed — it's what distinguishes the product. Implementation mechanics are not.
- Do not skip the arc assessment. A narrative with a weak "problem" section or a thin "validation" section will fail with technical audiences who probe both.
- Do not confuse quote-ready with summary sentences. Quote-ready sentences are surprising and specific. Summaries are neither.
