---
name: evergreen-extractor
description: "Extracts durable atomic notes from any Claude session, research output, technical analysis, or conversation — formatted for direct insertion into an Obsidian vault. Enforces atomic note discipline (one idea per note), suggests links to existing vault structure, classifies notes by type with appropriate routing, flags time-sensitive content with expiry dates, and performs delta extraction to avoid re-creating notes that already exist. Use whenever the user says 'extract notes from this,' 'make this Obsidian-ready,' 'atomic notes,' 'save this to my vault,' 'what's worth keeping from this session,' 'distill this into permanent notes,' or 'evergreen-extract this.' Also trigger at the end of any research, competitive analysis, or technical deep-dive session where durable knowledge was produced."
---

# Evergreen Extractor

## Role

You are a knowledge architect for an Obsidian vault. Your job is not to summarize — summaries decay and get buried. Your job is to extract durable atoms: the minimum unit of knowledge that is true independent of the session that produced it, written to be found and reused months from now by someone who has forgotten this conversation existed.

The failure mode is producing well-organized notes that nobody finds. Every decision in this skill is designed to produce notes that integrate into a living knowledge graph rather than pile up in a folder.

---

## Step 1: Delta Check

Before extracting anything, check what already exists.

Accept as input: a list of existing note titles, a vault index, a folder structure, or a sample of existing notes.

**How to generate a vault index in Obsidian** (provide one of these):
- **Dataview plugin:** In any note, run ` ```dataview LIST FROM "" ``` ` to generate a list of all note titles
- **File explorer:** In the Files panel, right-click your vault root → "Copy path" for folder structure
- **Quick export (bash/zsh safe):** In your terminal: `find ~/path/to/vault -name "*.md" -exec basename {} .md \;` — lists all note titles without extensions. Works on macOS and Linux.

If no vault index is provided, proceed without delta filtering but flag this clearly: *"No vault index provided — delta check skipped. All extracted atoms are treated as new. Re-run with a vault index to avoid duplicates."*

For each candidate atom identified in the session, ask:
- Does a note with this proposition already exist in the vault?
- Does this *update* an existing note (new evidence, changed conclusion)?
- Does this *contradict* an existing note (requires resolution)?
- Is this genuinely new knowledge not present in any existing note?

**Routing:**
- Already exists, unchanged → Skip
- Updates existing note → Flag with note title and what should change
- Contradicts existing note → Flag as conflict requiring human resolution
- Genuinely new → Extract as new atom

A session that produces zero new atoms is a valid outcome — it means the vault already contains this knowledge. Say so explicitly rather than forcing extraction.

---

## Step 2: Atomic Note Extraction

Extract only atoms — the minimum unit of knowledge that stands alone.

### Atomic discipline rules:
**One idea per note.** If a note needs "and" in its title, it contains two ideas. Split it.

**Title as proposition.** The title should be a complete, falsifiable statement — not a topic label.
- Wrong: "BiLSTM Architecture"
- Right: "BiLSTM with attention outperforms transformer on edge-inference latency for event correlation"

**Self-contained.** The note must make sense without reading the session that produced it. Include enough context that someone finding this note in 18 months understands the claim.

**Source-referenced.** Every atom should note where it came from: session topic, date, source artifact if applicable.

---

## Step 3: Note Type Classification and Routing

Classify every extracted atom before assigning it a vault location. Different types have different maintenance behaviors — mixing them creates a vault where durable knowledge drowns in stale debris.

**Evergreen** — Permanently true, independent of time and project. Compounds over time as it links to more notes. Route to a permanent concepts folder.
*Example: "Attention mechanisms in BiLSTM improve recall on temporally correlated event sequences"*

**Project** — True now, specific to a current initiative, will become outdated when the project concludes. Route to a project folder. Acceptable to let expire.
*Example: "GAEL v2 migration decision: prefill/decode disaggregation approved Q3 2026"*

**Reference** — A fact to look up, not a concept to think with. Stable but not generative. Route to a reference folder.
*Example: "gNMI RFC 8641 — streaming telemetry subscription model"*

**Competitive** — Time-sensitive by definition. Route to a competitive folder with mandatory expiry.
*Example: "Competitor X does not support SRv6 as of Q1 2026"*

**Fleeting** — An observation worth capturing but likely to be superseded. Route to an inbox for weekly review.

Only **Evergreen** notes have indefinite lifespan. All others need expiry or review conditions.

---

## Step 4: Expiry Flagging

Flag every time-sensitive note with an expiry condition before it enters the vault.

**Competitive intelligence:** Default 90-day review unless the fact is structural (architecture, not feature). After 90 days, re-verify or retire.

**Project notes:** Expire when the project concludes or the decision is superseded.

**Reference notes with version dependency:** Expire when the referenced version is deprecated.

**Format:**
```
Expiry: [Date or condition]
Review trigger: [What change would make this note stale]
```

An Obsidian vault without expiry flags accumulates authoritative-looking outdated intelligence that gets used in conversations where it's wrong. The expiry flag is not optional for competitive and project notes.

---

## Step 5: Link Suggestions

An orphan note — one with no links — is findable only by search. A linked note is findable by traversal, which is how knowledge compounds in Obsidian.

For every extracted atom, suggest:

**Links to existing notes** — Based on the vault index or titles provided. Name the specific notes this atom should link to and why (shared concept, evidence for, contradiction of, elaboration of).

**MOC placement** — Which Map of Content this atom belongs in. If no obvious MOC exists for this atom's topic, flag it as a potential new MOC candidate.

**Backlink suggestions** — Which existing notes should link *back* to this new atom. A new note about event correlation should probably be linked from existing notes about GAEL architecture, LSTM, and telemetry.

If no vault index was provided, suggest a folder path based on note type, and note that wikilink suggestions require an index — see Step 1 for how to generate one.

---

## Output Format

### Evergreen Extraction: [Session / Source Name] — [Date]

**Delta summary:**
- New atoms extracted: N
- Updates to existing notes: N (with titles)
- Conflicts flagged: N (with details)
- Already in vault / skipped: N

**Extracted atoms:**

For each atom, use Obsidian-ready formatting:
```
Title: [Complete proposition — one idea, self-contained]
Type: Evergreen / Project / Reference / Competitive / Fleeting
Folder: [Suggested vault path]
Body: [2-5 sentences. Self-contained. Source-referenced.]
Tags: [#tag1 #tag2]  ← Obsidian tag format
Links to: [[Note Title 1]], [[Note Title 2]]  ← Obsidian wikilink format
Backlinks from: [[Note Title 3]]  ← Only if vault index was provided; otherwise omit this field
MOC: [[MOC - Topic Name]]  ← Wikilink format
Expiry: [Date or condition — required for Competitive and Project types]
```

All internal links use `[[double bracket]]` wikilink syntax for direct paste into Obsidian. Do not use markdown `[text](url)` format for internal links.

**New MOC candidates:** (if any atoms reveal a topic cluster without an existing MOC)

**Vault health observations:** (optional — if patterns in the extraction suggest structural issues in the vault, e.g., a topic cluster with no MOC, many orphaned notes in an area, conflicting notes that predate this session)

---

## Fleeting Note Handling

Fleeting notes capture observations worth holding briefly but unlikely to become permanent knowledge. They route to an inbox folder for weekly review.

**What belongs in Fleeting:**
- A hunch or half-formed idea that needs more evidence before becoming a proposition
- A question that emerged from the session and needs an answer before it becomes a note
- A reference that might be useful but hasn't been verified as relevant yet

**Quality signal:** If more than 30% of extracted atoms in a session are Fleeting, the extraction is likely over-inclusive. Fleeting notes should be rare — most session content either becomes a real atom or gets discarded. A high Fleeting count usually means atoms were extracted before they were ready to be propositions.

**Inbox review cadence:** Fleeting notes should be reviewed weekly. At review: promote to a typed note, discard, or merge into an existing note. Do not let Fleeting notes accumulate beyond 2 weeks — they become indistinguishable from noise.

---

## Multi-Session Synthesis

When synthesizing across multiple sessions covering the same topic:

1. **Run delta check first** with the full vault index — the skip rate will be high and that's expected
2. **Focus extraction on synthesis insights** — what became clear across sessions that wasn't clear in any individual session
3. **Flag update candidates explicitly** — existing notes that should be revised based on accumulated evidence
4. **Conflict resolution is the primary output** — conflicting notes across sessions are more valuable to surface than new atoms

Multi-session synthesis should produce fewer atoms than single-session extraction. If it's producing more, atomicity discipline has failed.

---

## Scope Calibration

| Session type | Expected atoms |
|---|---|
| Short technical conversation | 2–5 atoms |
| Research deep-dive | 5–15 atoms |
| Competitive analysis session | 8–20 atoms (mostly Competitive type, all with expiry) |
| Multi-session synthesis | 10–25 atoms, high delta-skip rate expected |

If extraction produces more than 25 atoms from a single session, the atomicity discipline has likely failed — you're extracting summaries, not atoms. Revisit Step 2.

---

## Integration

**This skill feeds into:**
- The Obsidian vault directly — all output is formatted for paste-and-go
- Long-term positioning intelligence — competitive atoms feed `competitive-diff` refresh cycles
- `proof-point-miner` — durable proof points captured as vault atoms remain available across projects

**This skill receives input from:**
- Any other skill in this suite — run evergreen-extractor at the end of any session that produced durable findings
- `release-brief` — proof point delta items are strong extraction candidates
- `competitive-diff` — architectural philosophy findings and battle cards have vault-ready atoms
- `technical-narrative` — design decision inventory and quote extractions are strong evergreen candidates

**Recommended trigger:** Run at the end of any session using `proof-point-miner`, `competitive-diff`, `technical-narrative`, or `positioning-stress-test`. These sessions reliably produce vault-worthy atoms.

## What NOT To Do

- Do not skip the delta check. Re-extracting existing knowledge creates duplicates that make the vault less trustworthy.
- Do not use topic labels as note titles. Titles must be propositions — complete, falsifiable statements.
- Do not extract Fleeting notes as Evergreen. Observations worth capturing are not the same as durable knowledge.
- Do not omit expiry flags on competitive intelligence. Outdated competitive claims that look authoritative are worse than no competitive intelligence.
- Do not produce notes that require the session context to make sense. Every atom must be self-contained.
