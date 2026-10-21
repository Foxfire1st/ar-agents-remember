# dashboard/src/panels/review/reading/SummaryLine.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Count changed records, locations/files, lane files, folded locations and active sort from the model/reads.

## Code Commentary

### Logic

Count changed records, locations/files, lane files, folded locations and active sort from the model/reads. Loading usesellipsis; unavailable is named, never zero. Summary's counted lane totals can answer before lane files; ready lane is used when those counts absent.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Count changed records, locations/files, lane files, folded locations and active sort from the model/reads. [1]
- Count changed records, locations/files, lane files, folded locations and active sort from the model/reads. [2]
- Count changed records, locations/files, lane files, folded locations and active sort from the model/reads. [3]
