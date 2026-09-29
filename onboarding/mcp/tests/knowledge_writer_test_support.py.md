# mcp/tests/knowledge_writer_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/knowledge_writer_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T10:05:46+02:00 |
| lastVerifiedCommitHash | `cd3e943d740b490d391722389af0a6bca0ccf93e`|
| lastVerifiedCommitDate | 2026-09-29T10:38:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The world the MIK-R12 writer tests run in.** `build_world` creates two real Git repositories under
`tmp_path`: **code** (a small package `pkg/landing.py` and `tests/test_landing.py`, committed) and a
converted **memory** tree whose committed `HEAD` is the writer's base, holding `INV-BASE01` realized by
`land_pair` (`RLZ-BASE01`) and the family `FAM-FAM001` with that member; plus a task root with `task.json`
and a leaf contract naming both worktrees, so the command line runs exactly as a leaf runs it.

## Code Commentary

### Logic

- `CODE` defines `land_pair`, `Helper` and `Other` (same-named methods, for the qualified-symbol rule).
- `entry(...)` builds a producer entry with curator keys; `SCOPE`, `ADMISSION` and `target(...)` are the
  shared curator values.
- `tree_bytes` and `read_json` read the memory tree for byte-identity and content assertions.

### Conventions

- Git runs through `git(root, *args)` with a fixed identity; `canonical` renders fixtures canonically.

### Invariants And Boundaries

- A support module (no collected cases).

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

The world.

| Finding | Anchor | Source |
| --- | --- | --- |
| The base memory: one invariant, one realization, one family. | `base_memory` | mcp/tests/knowledge_writer_test_support.py:114-167 |
| The leaf contract naming both worktrees. | `contract_text` | mcp/tests/knowledge_writer_test_support.py:170-206 |
| Both repositories and the task root. | `build_world` | mcp/tests/knowledge_writer_test_support.py:209-220 |
| A producer entry with curator keys. | `entry` | mcp/tests/knowledge_writer_test_support.py:223-241 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
