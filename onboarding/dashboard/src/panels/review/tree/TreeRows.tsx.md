# dashboard/src/panels/review/tree/TreeRows.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Render accessible one-line family, invariant, changed-location and group rows.

## Code Commentary

### Logic

Render accessible one-line family, invariant, changed-location and group rows. The family or invariant
row's button title retains the full subject title. When the candidate supplies a revision state, a
state tag shares the trailing cell with the reason. The tag's title and the row's accessible name
include the writer's role and model when supplied. Plain reasons and signs survive colour, and the
current occurrence shares page identity. Group buttons open their groups in the reading column.

### Invariants And Boundaries

LocationRow displays the supplied ungraded-group heading before its row when there is a positive
count. A graded location draws its chip before the reason inside the trailing cell. The chip carries
the supplied caption, stale flag, category, grade and hover text. Stale chips use dashed amber
styling. The location tooltip appends the supplied judgment hover text. Its accessible label still
names the location, role and reason.

This file displays supplied comparison and record facts. Knowledge authoring and task acceptance
stay with their server-side owners.

## Evidence

- The family row keeps one trailing cell for the reason, optional kept label and state tag. Its accessible name includes supplied standing. [1]
- The subject button keeps the whole-title tooltip and appends supplied standing to its accessible name. [2]
- A counted group opens the matching reading-column group via the supplied callback. [3]
- A graded location puts its chip before the reason in the trailing cell. The row tooltip carries supplied hover text. [4]

- The optional tag shows candidate revision state and names its writer in the title when supplied. The subject tail keeps one cell. [5]
