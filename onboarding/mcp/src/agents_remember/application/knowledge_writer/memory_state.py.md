# mcp/src/agents_remember/application/knowledge_writer/memory_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/memory_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T10:05:46+02:00 |
| lastVerifiedCommitHash | `cd3e943d740b490d391722389af0a6bca0ccf93e`|
| lastVerifiedCommitDate | 2026-09-29T10:38:08+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The memory tree one writer operation reads and edits, and the base it compares against.** The
candidate K_C is every file under `knowledge/` and `onboarding/`, read once as bytes
(`knowledge_tree_from_directory`). The operation edits parsed copies of the JSON documents it touches;
nothing reaches disk until `MemoryState.write` is called with the validated result.

## Code Commentary

### Logic

- `Owner(task, kind, id)`: the task and the leaf or wave that owns the history file. `origin()` is
  `{task, leaf|wave}`; `authored(document, handoff_entry)` says whether a record's or entry's origin names
  this owner and this hand-off entry (entries carry only `leaf`, so a wave's entries carry the wave ID in
  `leaf`, architect ruling 2).
- **The base** is the memory worktree's `HEAD` (`read_base`); a root that is not a Git work tree has no
  base. It answers a record's revision before this leaf (`base_record`) and an entry's anchor before this
  leaf (`base_entry_anchor`, a history row's `before`). The exact K_B resolver of MIK-R07 rule 0 is the
  gate's (MIK-R08/R09).
- `known_ids` is every record ID, minted ID, sidecar entry ID and history row ID of every history file, so
  minting never collides.
- `record_by_origin` and `entries_by_origin` find what this owner wrote from a hand-off entry, which is how
  a rerun reuses IDs.
- `put_record` keeps a record's file name unless a new slug renames it, carrying the paired `.md` along.
- `file_sidecar` creates an empty sidecar for a source file that has none.
- `write` writes each changed file through a temporary sibling and `replace`, then unlinks removed files.

### Conventions

- `deep_copy` and `canonical_equal` (sorted-key JSON equality) are the helpers `authoring.py` uses.

### Invariants And Boundaries

- A refused operation leaves every file exactly as it was, because edits live only in `documents` until
  `write`.
- The file writer writes only a converted tree: `converted` is the layout-marker test over the candidate
  files.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The candidate, the owner, the base and the write.

| Finding | Anchor | Source |
| --- | --- | --- |
| Who authors the operation, and whether a document names it. | `Owner` | mcp/src/agents_remember/application/knowledge_writer/memory_state.py:49-67 |
| The base is the memory worktree's `HEAD`, or none. | `read_base` | mcp/src/agents_remember/application/knowledge_writer/memory_state.py:121-129 |
| Every ID the tree holds, including history row IDs. | `known_ids` | mcp/src/agents_remember/application/knowledge_writer/memory_state.py:191-204 |
| Rerun ID reuse by origin. | `record_by_origin` | mcp/src/agents_remember/application/knowledge_writer/memory_state.py:214-223 |
| A record keeps its file unless a new slug renames it. | `put_record` | mcp/src/agents_remember/application/knowledge_writer/memory_state.py:225-244 |
| Entries this owner wrote for an invariant from a hand-off entry. | `entries_by_origin` | mcp/src/agents_remember/application/knowledge_writer/memory_state.py:279-288 |
| A record as the base holds it. | `base_record` | mcp/src/agents_remember/application/knowledge_writer/memory_state.py:303-313 |
| An entry's anchor as the base holds it. | `base_entry_anchor` | mcp/src/agents_remember/application/knowledge_writer/memory_state.py:315-328 |
| The atomic per-file write and the removals. | `write` | mcp/src/agents_remember/application/knowledge_writer/memory_state.py:350-366 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
