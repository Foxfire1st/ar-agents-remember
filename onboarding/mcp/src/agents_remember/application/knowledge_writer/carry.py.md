# mcp/src/agents_remember/application/knowledge_writer/carry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/carry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:13:48+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
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
  `_carried_anchor` is `mapped_anchor` plus the carry's own condition: only when the anchor resolves **and** its
  content identity equals the recorded `content` does it return the new anchor: `blob` set to C's blob and, for a
  `line_range`, the mapped `start` and `end`. The sidecar is marked touched, and the IDs are returned sorted (the
  report's `carried`).
- **`mapped_anchor(code, source, anchor, blob)` (public since MIK-R14, review F1).** The mapping itself: the anchor
  is resolved at the new blob through `CodeTrees.resolve` (the worklist's own resolution: a `line_range` is mapped
  through the zero-context diff from its recorded blob, a symbol is re-bound), and the new anchor records `blob`,
  the mapped span and the `content` the range holds there. It returns `None` when the blob is unknown, the read
  fails, or the locator does not resolve (a range with no image, a symbol not bound once, a file gone). It does
  **not** require identical content: MIK-R14's `still_rejected` refresh re-anchors a link target through it
  (`knowledge_writer/reconsideration.py`), and applies its own content checks. The carry's behaviour is unchanged
  (removing its content condition fails an existing carry test, review R2).
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
| The carry keeps the mapping only when the content is identical. | `_carried_anchor` | mcp/src/agents_remember/application/knowledge_writer/carry.py:58-62 |
| The mapping at a new blob, with the mapped span and the content there; `None` when it does not resolve (reused by MIK-R14's refresh). | `mapped_anchor` | mcp/src/agents_remember/application/knowledge_writer/carry.py:33-55 |
| The refresh maps a line range through the diff with this function. | `test_the_refresh_maps_a_line_range_and_refreshes_only_the_fired_links` | mcp/tests/test_reconsideration_surfacing.py:781-810 |
| Every carried entry of the tree is re-recorded. | `carry_entries` | mcp/src/agents_remember/application/knowledge_writer/carry.py:65-90 |
| Only the owner's open row with the old `after` is updated. | `_carry_rows`; `history_path` | mcp/src/agents_remember/application/knowledge_writer/carry.py:93-105 |
| The call in every writer operation. | `write_knowledge`; `carry_entries` | mcp/src/agents_remember/application/knowledge_writer/writer.py:98-155 |
| Blobs and covering rows are carried. | `test_the_writer_carries_moved_blobs_and_the_rows_that_cover_them` | mcp/tests/test_knowledge_worklist_leaf.py:330-386 |
| Another owner's row and a closed file are untouched. | `test_carrying_never_edits_another_owners_row_or_a_closed_history_file` | mcp/tests/test_knowledge_worklist_leaf.py:478-500 |

## Cross-Repo References

No meaningful cross-repo references found: the carry edits the in-memory state of one memory tree against
one code snapshot.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): **body updated for MIK-R14 (review F1, ruling 2026-09-30T05:31:11).** The carry's mapping is now the public `mapped_anchor` (records the mapped span and the content at the new blob, `None` when it does not resolve), which MIK-R14's `still_rejected` refresh reuses; `_carried_anchor` is `mapped_anchor` plus the identical-content condition, so the carry is unchanged. **Reopened claim re-read and reworded:** the `_carried_anchor` row (the function changed structurally) now cites it as the mapping plus the condition; I removed this pass's generated bullet for it. Two rows added; the `history_path` row the fixer declined was re-pointed by the exact line shift. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
