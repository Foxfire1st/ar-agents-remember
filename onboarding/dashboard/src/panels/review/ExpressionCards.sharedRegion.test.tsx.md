# dashboard/src/panels/review/ExpressionCards.sharedRegion.test.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Specify one rendered card per shared region while keeping each entry’s rationale, tray reference and selection identity.

## Code Commentary

### Logic

The captured L181 triple at one before/after region yields thirteen cards for fifteen changed entries. The shared card renders three voices and one excerpt; each entry’s add control produces its own exact block identity.

Selecting any entry of the shared region marks that same single card selected, and blockElement finds a scroll target within it.

### Invariants And Boundaries

It mounts SubjectGroupSection under an explicit ReadingContext over retained L181 data, not the complete served review page. Assertions were read; tests were not run.

## Evidence

- Shared rendering with entry-specific voices/picks [1]
- Selection and scroll target per retained identity [2]
