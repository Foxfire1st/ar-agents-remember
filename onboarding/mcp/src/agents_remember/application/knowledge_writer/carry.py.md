# mcp/src/agents_remember/application/knowledge_writer/carry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/carry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `e40c314ca55305f7e4334b4e8e16a10297f6f175`|
| lastVerifiedCommitDate | 2026-09-29T18:13:06+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The writer's mechanical carry-forward of `carried` entries (MIK-R08 definition 4, MIK-R12).** An entry is
`carried` when its path's blob at C differs from the entry's `blob` while the range its locator names at C
holds identical content. Such an entry needs no disposition; every writer operation re-records it at C here.

## Code Commentary

### Logic

- `carry_entries(state, snapshot, owner)` walks every sidecar of the memory state and every `realizes` and
  `proves` entry whose anchor `blob` differs from the source's blob in the code snapshot.
  `_carried_anchor` resolves the anchor at the new blob through `CodeTrees.resolve` (the worklist's own
  resolution); only when it resolves **and** its content identity equals the recorded `content` does it
  return the new anchor: `blob` set to C's blob and, for a `line_range`, the mapped `start` and `end`. The
  sidecar is marked touched, and the IDs are returned sorted (the report's `carried`).
- `_carry_rows` then updates the owner's own history file: a row's `covers` element whose `after` equals a
  carried entry's old anchor (with its path) gets the new anchor. It returns without editing when nothing
  was carried, the file is missing, or the file is `closed`.

### Conventions

- The carry runs after authoring and before the owner-history check in `writer.write_knowledge`, over the
  whole tree, not only the leaf's changed paths, because `carried` is defined relative to C.

### Invariants And Boundaries

- **Nothing authored changes.** The locator kind, a symbol's name and `content` are never modified; an
  entry whose content differs at C, or whose locator does not resolve there, is left for the curator's item.
- **Carrying only updates this leaf's own open row (architect ruling 5).** Another owner's rows and a closed
  (frozen) history file are never edited, per the MIK-R07 freeze; with the leaf's own file closed, L12's
  whole-file row check then refuses the write, naming "closed and frozen".
- A read failure of a blob is treated as "not carried", never as an error of the write.

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| What carried means and what the writer changes. | "Nothing else changes: not the locator kind, not the name" | mcp/src/agents_remember/application/knowledge_writer/carry.py:1-18 |
| The new anchor only for identical content. | `_carried_anchor` | mcp/src/agents_remember/application/knowledge_writer/carry.py:33-44 |
| Every carried entry of the tree is re-recorded. | `carry_entries` | mcp/src/agents_remember/application/knowledge_writer/carry.py:47-72 |
| Only the owner's open row with the old `after` is updated. | `_carry_rows`; `history_path` | mcp/src/agents_remember/application/knowledge_writer/carry.py:75-87 |
| The call in every writer operation. | `write_knowledge`; `carry_entries` | mcp/src/agents_remember/application/knowledge_writer/writer.py:81-125 |
| Blobs and covering rows are carried. | `test_the_writer_carries_moved_blobs_and_the_rows_that_cover_them` | mcp/tests/test_knowledge_worklist_leaf.py:329-385 |
| Another owner's row and a closed file are untouched. | `test_carrying_never_edits_another_owners_row_or_a_closed_history_file` | mcp/tests/test_knowledge_worklist_leaf.py:473-495 |

## Cross-Repo References

No meaningful cross-repo references found: the carry edits the in-memory state of one memory tree against
one code snapshot.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
