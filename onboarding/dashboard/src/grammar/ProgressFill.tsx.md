# dashboard/src/grammar/ProgressFill.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`ProgressFill` is a retained presentational bottom-up cyan charge fill inside an outline (note 08 progress grammar). Its source comment names former task-step and provider-seed uses; it has no current caller under `dashboard/src`. The comment does not restore provider-seed progress.

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



- The retained component renders completed/total progress; former detail-panel and provider-seed uses are named by its source comment, not by a current caller. [1]

## Historical former uses

These former current claims are retained as history, not as instructions or present implementation evidence.

> `ProgressFill` is the bottom-up cyan charge fill inside an outline (note 08 progress grammar) — reused by the detail panel's task-step progress and the engine room's provider-seed progress.
>
> The detail panel renders this for task-step progress.
