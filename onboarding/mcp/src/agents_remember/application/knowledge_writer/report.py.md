# mcp/src/agents_remember/application/knowledge_writer/report.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/report.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T10:05:46+02:00 |
| lastVerifiedCommitHash | `cd3e943d740b490d391722389af0a6bca0ccf93e`|
| lastVerifiedCommitDate | 2026-09-29T10:38:08+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**What one writer operation reports.** A written or planned operation lists every record, entry and
history row with its ID and action, every entry's evidence and where it is stored, and the validator's
report-only findings; a refused one lists every problem and refusing violation. `to_document` is the
`--json` form (`"operation": "knowledge-write"`), `render` the text form.

## Code Commentary

### Logic

- `Action` is `created`, `updated`, `unchanged` or `removed`; `WriteState` is `written`, `planned` or
  `refused`; `EvidenceState` is `proof_written`, `needs_facet` or `unresolvable`.
- `EvidenceOutcome.stored_in` names the records whose `origin.handoff` holds the evidence, or
  `knowledge/history/<owner>.json#<record ID>` for evidence stored in a history row. An empty `stored_in`
  renders "nothing: the entry authored no record".
- `authorization` is carried because the file format has no field for it.

### Conventions

- JSON keys are camelCase (`memoryRoot`, `codeTree`, `historyRows`, `handoffEntry`, `storedIn`).

### Invariants And Boundaries

- The report is the product, as for the database `knowledge-ingest`; nothing else records the operation.

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

The report shapes.

| Finding | Anchor | Source |
| --- | --- | --- |
| The outcome of one evidence-bearing entry. | `EvidenceOutcome` | mcp/src/agents_remember/application/knowledge_writer/report.py:59-66 |
| The report and its refused flag. | `WriteReport` | mcp/src/agents_remember/application/knowledge_writer/report.py:69-140 |
| The JSON form. | `to_document` | mcp/src/agents_remember/application/knowledge_writer/report.py:91-109 |
| The text form. | `render` | mcp/src/agents_remember/application/knowledge_writer/report.py:111-140 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
