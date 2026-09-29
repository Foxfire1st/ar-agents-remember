# mcp/src/agents_remember/memory/conversion/inputs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/conversion/inputs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Reads a memory tree to convert, from a working directory or a Git tree, and writes a finished
conversion (MIK-R24 rule 6).** Both readers return the same `MemoryInput`: the exact bytes of every file
under `knowledge/` and `onboarding/`, read by the validator's own tree readers (so the route-index cache
is excluded the same way), plus a readable path to the tree's `knowledge.sqlite` when it has one.

## Code Commentary

### Logic

- `memory_from_directory(root)` reads the working tree through `knowledge_tree_from_directory`, and
  takes `root/knowledge.sqlite` when it is a file.
- `memory_from_git(repository, treeish, scratch)` reads the tree through `knowledge_tree_from_git`. The
  database blob, if `<treeish>:knowledge.sqlite` exists, is copied to `scratch/<blob>.sqlite` (once per
  blob), because SQLite opens files, not blobs.
- `write_changed(root, changed)` writes each changed file through a sibling temporary file
  (`.<name>.converting`) and a rename, in path order.

### Conventions

- `DATABASE_NAME = "knowledge.sqlite"`, the legacy database's committed name.

### Invariants And Boundaries

- The database copy is only ever opened read-only (`legacy_db` opens with `SQLITE_OPEN_READONLY`).
- `write_changed` is called only after the whole converted tree validated, so a refused conversion writes
  nothing.

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

The two readers and the writer.

| Finding | Anchor | Source |
| --- | --- | --- |
| A working tree and its database. | `memory_from_directory` | mcp/src/agents_remember/memory/conversion/inputs.py:29-36 |
| A Git tree, with its database blob copied to scratch. | `memory_from_git` | mcp/src/agents_remember/memory/conversion/inputs.py:39-57 |
| Writing a finished conversion through a temporary file and a rename. | `write_changed` | mcp/src/agents_remember/memory/conversion/inputs.py:60-72 |

## Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
