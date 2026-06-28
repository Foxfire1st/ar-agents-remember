# dashboard/src/grammar/ProgressFill.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/ProgressFill.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-15T17:00                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`ProgressFill` is the bottom-up cyan charge fill inside an outline (note 08 progress grammar) —
reused by the detail panel's task-step progress and the engine room's provider-seed progress.

## Code Commentary

### Logic

Computes `pct = round(completed/total*100)` (guarded for `total===0`) and sets the inner fill's
`height` to `${pct}%` via inline style (the only dynamic value). Three Panda `css()` boxes:
`fillBox` (outline), `fillLevel` (the rising cyan), `fillPct` (the count). `role="img"` + an
`aria-label`.

### Invariants And Boundaries

Presentational; the only inline style is the dynamic fill height. Cyan = the progress/charge grammar.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The detail panel renders this for task-step progress. | L200-L208 | [panels/DetailPanel.tsx](../panels/DetailPanel.tsx) |

## Update History

- 2026-06-15T17:00 — Created for slice 5d: `ProgressFill` migrated to Panda `css()` (was `.fill*`).
  Verification metadata pinned until closeout stamps the 5d code commit.
