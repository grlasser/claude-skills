# evergreen-extractor

Extracts durable atomic notes from any Claude session, research output, or technical analysis — formatted for direct paste into an Obsidian vault, with link suggestions, type routing, expiry flags, and delta checking to avoid duplicates.

## What It Does

Session outputs that don't get captured are lost when context compacts. Summaries that do get captured decay — they're too dense to reuse and too vague to link. This skill extracts atoms: the minimum unit of knowledge that is true independent of the session that produced it, written to be found and reused months later by someone who has forgotten this conversation.

Every atom gets: a proposition title (not a topic label), a type classification with routing, expiry conditions for time-sensitive content, Obsidian-ready `[[wikilink]]` formatting, and link suggestions to integrate it into the existing knowledge graph rather than pile it in a folder.

## Trigger Phrases

- "extract notes from this"
- "make this Obsidian-ready"
- "atomic notes"
- "save this to my vault"
- "what's worth keeping from this session"
- "distill this into permanent notes"
- "evergreen-extract this"

Also trigger automatically at the end of any session using `proof-point-miner`, `competitive-diff`, `technical-narrative`, or `positioning-stress-test`.

## Note Types

| Type | Lifespan | Routing | Expiry |
|---|---|---|---|
| **Evergreen** | Indefinite | `/concepts` | None |
| **Project** | Until project ends | `/projects/[name]` | When project concludes |
| **Reference** | Until deprecated | `/reference` | When version deprecated |
| **Competitive** | 90 days default | `/competitive` | Mandatory — 90-day review |
| **Fleeting** | 1–2 weeks | `/inbox` | Review weekly |

Only Evergreen notes compound over time. All others require expiry conditions.

## Output Format (Obsidian-ready)

```
Title: [Complete proposition — one idea, self-contained]
Type: Evergreen / Project / Reference / Competitive / Fleeting
Folder: [Vault path]
Body: [2-5 sentences. Self-contained. Source-referenced.]
Tags: [#tag1 #tag2]
Links to: [[Note Title 1]], [[Note Title 2]]
Backlinks from: [[Note Title 3]]  (only if vault index provided)
MOC: [[MOC - Topic Name]]
Expiry: [Date or condition]
```

All links use `[[double bracket]]` wikilink syntax for direct paste.

## Generating a Vault Index

To enable delta checking and link suggestions, provide a note list. Three options:

**Dataview plugin:** Run ` ```dataview LIST FROM "" ``` ` in any note.

**File explorer:** Copy the folder tree from Obsidian's Files panel.

**Terminal:** `find ~/path/to/vault -name "*.md" -exec basename {} .md \;`

## Scope

| Session type | Expected atoms |
|---|---|
| Short technical conversation | 2–5 |
| Research deep-dive | 5–15 |
| Competitive analysis session | 8–20 (mostly Competitive type) |
| Multi-session synthesis | 10–25, high skip rate expected |

If extraction produces >25 atoms from one session, atomicity has failed — you're extracting summaries, not atoms.

## How It Fits

```
[any skill output] → evergreen-extractor → Obsidian vault
                           ↑
Best inputs: proof-point-miner (Tier 1/2 items),
             competitive-diff (architectural findings, battle cards),
             technical-narrative (design decisions, quotes),
             positioning-stress-test (what's defensible)
```
