# dashboard/src/panels/review/markerUnknown.task.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerUnknown.task.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent` task-context review of the MIK-L34 scratch leaf on comparison 3** (14,990 bytes; test
evidence for `ReviewSurface.markers.test.tsx`).

## Code Commentary

### Logic

- No subject selected; the limitations name `review:trees:3` and `knowledge-index:after:partial`; the same four-path inventory.

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

The body describes the scratch copies under `/tmp/mik-l34-real` (code `59daf505` with the scratch leaf's edits; memory `76f5e91e1` converted with the L34 worktree's `knowledge-convert` and committed as scratch `main` `2e3810ed`), not current project knowledge; its line numbers, blobs and keys are the scratch tree's.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The comparison token and the partial after index. | "review:trees:3"; "knowledge-index:after:partial" | dashboard/src/panels/review/markerUnknown.task.captured.json:186-193 |
| The receipt row for this body. | "src/panels/review/markerUnknown.task.captured.json" | dashboard/src/panels/review/markerUnknown.capture-provenance.json:15-15 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new captured task-context review (comparison 3). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
