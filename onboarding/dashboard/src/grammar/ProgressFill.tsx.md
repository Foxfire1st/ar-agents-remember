# dashboard/src/grammar/ProgressFill.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/ProgressFill.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-15T17:00                                 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The detail panel renders this for task-step progress. | `ProgressFill` | dashboard/src/grammar/ProgressFill.tsx:27-45 |

## Update History

- 2026-08-04T17:52+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the single Repo-Internal row —
  rebound the detail-panel render claim to the exact `ProgressFill` JSX mount line with a fixer-verified
  range. Claim wording unchanged.
- 2026-06-15T17:00 — Created for slice 5d: `ProgressFill` migrated to Panda `css()` (was `.fill*`).
  Verification metadata pinned until closeout stamps the 5d code commit.
