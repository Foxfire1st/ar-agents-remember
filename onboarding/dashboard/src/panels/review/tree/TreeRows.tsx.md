# dashboard/src/panels/review/tree/TreeRows.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Render accessible one-line family, invariant, changed-location and group rows.

## Code Commentary

### Logic

Render accessible one-line family, invariant, changed-location and group rows. Tooltip retains full title; plain reason and signs survive color; proper current occurrence shares page identity. Group button opens column group, not a tree disclosure.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Render accessible one-line family, invariant, changed-location and group rows. [1]
- Render accessible one-line family, invariant, changed-location and group rows. [2]
- Render accessible one-line family, invariant, changed-location and group rows. [3]

LocationRow now inserts the model's Ungraded (n) heading before the first ungraded row and renders JudgmentChip before its location label. A chip names the active grade or graded state, carries stale/category/grade attributes and the full inference/reason hover text; stale chips use dashed amber styling. The location tooltip appends those reasons while the existing accessible location/role/reason label and selection callbacks remain intact.

- LocationRow now inserts the model's Ungraded (n) heading before the first ungraded row and renders JudgmentChip before its location label. A chip names the active grade or graded state, carries stale/category/grade attributes and the full inference/reason hover text; stale chips use dashed amber styling. The location tooltip appends those reasons while the existing accessible location/role/reason label and selection callbacks remain intact. [4]
