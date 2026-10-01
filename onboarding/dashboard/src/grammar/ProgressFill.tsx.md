# dashboard/src/grammar/ProgressFill.tsx

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

## Evidence

### Repo-Internal References

- The detail panel renders this for task-step progress. [1]
