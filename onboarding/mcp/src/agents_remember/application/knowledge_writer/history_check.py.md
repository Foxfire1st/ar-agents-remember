# mcp/src/agents_remember/application/knowledge_writer/history_check.py

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
- **L37.** The file checked is the owner's writable history file (`state.history_target(owner)`), so a reopened
  leaf's rows are checked in its latest attempt and its closed file is not a refusal reason. A `changed` row's
  revision counts from `_base_revision`: the higher merge side's revision while a merge leaves the record unmerged
  (MIK-R24 rule 8 step 4), else the base's. So the writer accepts a crossing's resolution at maximum plus one.
- **A `changed` row at an unchanged revision (L37, INV-XN0FG8).** `_earlier_attempts` reads the owner's earlier
  attempt files from the writer's base, latest first; these are the leaf's frozen files, and a wave or a crossing
  has none. `_restated_revision` returns the revision of the latest earlier row about the subject when that row is
  a `changed` row, else nothing. `_row_messages` hands it to `invariant_revision_violation`, which accepts a
  `changed` row whose revision equals the base revision only when it equals that restated revision: the leaf
  closed out, was not integrated, and corrects the row's effect, because or reason, or does entry work under it.
  The record is not edited.

### Conventions

- A history file that does not parse is skipped here; the render step reports its shape.

### Invariants And Boundaries

- The writer refuses rather than refreshing `after` on its own (MIK-R07's failure rule).

### Todos

- The module docstring still says "The remedy is always the same", although a closed file gets the
  `_FROZEN` remedy; the code is right and the sentence is stale.
- Open question to the architect from the worker: `reanchor_mismatches` and `unknown_subjects` could also
  run as a registered validator rule over open history files (owner MIK-R09 or R22).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The check and its per-row messages.

- The two remedies. [1]

- Every row of the owner's file, as problems. [2]
- Invariant and family row checks. [3]

- A contradicted row refuses until it is named again; a closed file is frozen. [4]

- The revision a row's change counts from: the higher merge side's for an unmerged record. [5]

- The owner's earlier attempts as the base holds them. [6]
- The revision a changed row may restate: the leaf's latest earlier row, when it is a changed row. [7]
- A changed row cannot restate a revision once a later row of another disposition is the latest earlier row. [8]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
