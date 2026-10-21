# dashboard/src/tray/traySeats.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Loads bounded existing AR seat pages and presents unambiguous role/task labels.

## Code Commentary

### Logic

Parses completeness and More offsets, retains known seats when unavailable, merges further pages, and lengthens same-role/task agent prefixes until distinguishable.

### Invariants And Boundaries

A missing seat in an incomplete list is unknown. This is a recipient list, not navigation or lifecycle authority.

## Evidence

- Loads bounded existing AR seat pages and presents unambiguous role/task labels. [1]
- Loads bounded existing AR seat pages and presents unambiguous role/task labels. [2]
- Loads bounded existing AR seat pages and presents unambiguous role/task labels. [3]
