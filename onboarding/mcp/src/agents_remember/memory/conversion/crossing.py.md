# mcp/src/agents_remember/memory/conversion/crossing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/conversion/crossing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The structural three-way merge of a crossing sync (MIK-R24 rule 8 steps 3 and 4).** Once every
unconverted side is converted, the three converted trees merge file by file. Markdown merges by line,
sidecars and records by key, and mechanical anchor fields never cause a conflict.

## Code Commentary

### Logic

- `merge_trees(base, ours, theirs, *, repository)` goes path by path. A file only one side changed is
  taken from that side (a deletion included, counted `own`, `incoming` or `same`). A JSON file both sides
  changed is merged by key (`_merge_json_file`), and any other file three-way by line (`_merge_text_file`,
  through `kernel/git_command.merge_file_bytes`). A text file deleted on one side and changed on the other
  is a `(file)` conflict.
- **Keys (`_merge_json`, `_merge_collection`).** `references` merge by number, `realizes` and `proves` by
  entry `id`, and every other field by name.
- **Items (`merge_item`).** A reference, an entry or a record field is one item. Its mechanical fields are
  an anchor's `blob`, `content` and line numbers (`authored` strips them), and everything else is authored.
  - An item only one side changed is taken from that side, whole.
  - If one side changed authored fields and the other only mechanical ones, the authored side's item is
    taken, whole.
  - If both sides changed only mechanical fields, the incoming side's item is taken.
  - An item deleted on one side and changed only mechanically on the other is deleted.
  - Authored fields changed differently on both sides are a **conflict**. So is an item added on both
    sides with different authored content. A reference number both sides added with different targets is
    reported as `renumber one side`, even when the Markdown merged cleanly.
- **Conflict markers (`CONFLICT_MARKER`, `_conflicted`).** A conflicted JSON item, or a whole JSON file,
  is written as an explicit `{"crossing-conflict": {item, reason, base, own, incoming}}` marker. No
  knowledge-file model admits that key, so the validator refuses the file until the curator replaces the
  marker. Markdown conflicts keep Git's conflict hunks.
- `Conflict.to_document` gives each conflict's path, item, reason and the three sides' values for the
  crossing report.

### Conventions

- Merged JSON is written in the canonical format (`canonical_text`).

### Invariants And Boundaries

- **Mechanical anchor fields never conflict in a crossing** (rule 8 step 3).
- **A conflicted item is never committed as a silent "ours"** (review R1 finding 1, resolved by the
  markers).
- **No anchor is re-resolved.** Staleness is reported later by MIK-R03 wherever the knowledge is read.
- On the real ONT fork, 615 conflict items fell in 32 cards, all within the 46 cards both lines changed.
  503 of them are renumbering effects of references merged by number, which the packet allows and the
  architect left as they are.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The item rules, the keyed merge and the markers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The explicit conflict marker the validator refuses. | `CONFLICT_MARKER`; `_conflicted` | mcp/src/agents_remember/memory/conversion/crossing.py:43-43; mcp/src/agents_remember/memory/conversion/crossing.py:69-78 |
| Mechanical fields stripped for comparison. | `authored` | mcp/src/agents_remember/memory/conversion/crossing.py:94-110 |
| The item rules: one side, authored beats mechanical, incoming for mechanical-only, delete versus mechanical. | `merge_item`; `_absent_on_a_side`; `_both_changed` | mcp/src/agents_remember/memory/conversion/crossing.py:113-124; mcp/src/agents_remember/memory/conversion/crossing.py:127-137; mcp/src/agents_remember/memory/conversion/crossing.py:140-149 |
| References by number, entries by id, fields by name; a reference number added on both sides. | `_merge_json`; `_merge_collection` | mcp/src/agents_remember/memory/conversion/crossing.py:161-184; mcp/src/agents_remember/memory/conversion/crossing.py:191-213 |
| Markdown three-way by line. | `_merge_markdown`; `_merge_text_file` | mcp/src/agents_remember/memory/conversion/crossing.py:216-230; mcp/src/agents_remember/memory/conversion/crossing.py:252-270 |
| The file-by-file merge and its provenance counts. | `merge_trees` | mcp/src/agents_remember/memory/conversion/crossing.py:273-299 |
| The item rules on mechanical and authored fields. | `test_items_merge_by_their_mechanical_and_authored_fields` | mcp/tests/test_knowledge_crossing.py:93-110 |
| A reference number both sides added conflicts even when the Markdown merges. | `test_a_reference_number_both_sides_added_conflicts_even_when_the_markdown_merges` | mcp/tests/test_knowledge_crossing.py:124-152 |

## Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
