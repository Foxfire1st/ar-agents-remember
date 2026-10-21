# dashboard/src/panels/review/tree/ReviewTree.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Render shared model, controls, subject/location/group rows, pinned worklist/lane and lane files.

## Code Commentary

### Logic

Render shared model, controls, subject/location/group rows, pinned worklist/lane and lane files. Own no selection; tree click preserves scroll; outside selection reveals matching row using scrollTop only. Filter is tree-only; empty states and missing-sort reason remain visible.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Render shared model, controls, subject/location/group rows, pinned worklist/lane and lane files. [1]
- Render shared model, controls, subject/location/group rows, pinned worklist/lane and lane files. [2]
- Render shared model, controls, subject/location/group rows, pinned worklist/lane and lane files. [3]
