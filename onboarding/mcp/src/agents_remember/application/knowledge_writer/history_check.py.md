# mcp/src/agents_remember/application/knowledge_writer/history_check.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/history_check.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T10:05:46+02:00 |
| lastVerifiedCommitHash | `cd3e943d740b490d391722389af0a6bca0ccf93e`|
| lastVerifiedCommitDate | 2026-09-29T10:38:08+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Every row of the owner's history file agrees with the candidate the operation produces (MIK-R07;
architect ruling F1).** After all edits, `owner_history_problems` checks every row of
`knowledge/history/<owner>.json`, not only this run's rows, with L07's writer-support checks.

## Code Commentary

### Logic

- `unknown_subjects`: the subject names a record of the candidate.
- `reanchor_mismatches`: each covered entry's `after` equals its anchor in the candidate (`absent` when
  gone), MIK-R07 rule 4; candidate anchors come from `sidecar_entry_anchors` over the edited sidecars.
- `invariant_revision_violation`: an invariant row's revision is the candidate revision and binds the base
  revision, rule 2.
- `stale_examined_members`: a family row examined each member at its candidate revision, rule 5.
- The remedy is "name this row again in 'history' so the writer rewrites it"; on a **closed** file it is
  `_FROZEN` ("closed and frozen (MIK-R07 rule 7) … a correction belongs to a new leaf's rows").

### Conventions

- A history file that does not parse is skipped here; the render step reports its shape.

### Invariants And Boundaries

- The writer refuses rather than refreshing `after` on its own (MIK-R07's failure rule).

### Todos

- The module docstring still says "The remedy is always the same", although a closed file gets the
  `_FROZEN` remedy; the code is right and the sentence is stale.
- Open question to the architect from the worker: `reanchor_mismatches` and `unknown_subjects` could also
  run as a registered validator rule over open history files (owner MIK-R09 or R22).

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

The check and its per-row messages.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two remedies. | `_FROZEN` | mcp/src/agents_remember/application/knowledge_writer/history_check.py:43-46 |
| Every row of the owner's file, as problems. | `owner_history_problems` | mcp/src/agents_remember/application/knowledge_writer/history_check.py:49-72 |
| Invariant and family row checks. | `_row_messages` | mcp/src/agents_remember/application/knowledge_writer/history_check.py:75-102 |
| A contradicted row refuses until it is named again; a closed file is frozen. | `test_a_row_the_candidate_contradicts_refuses_until_it_is_named_again` | mcp/tests/test_knowledge_writer.py:491-528 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
