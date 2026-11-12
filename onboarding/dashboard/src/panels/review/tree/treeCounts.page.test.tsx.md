# dashboard/src/panels/review/tree/treeCounts.page.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin signed line-count labels for page tree location and lane-file rows.

## Code Commentary

### Logic

Mounts the composed page and checks a location row's reason retains its role plus signed counts, with separate mint/alarm children at 0.7rem and the same counts in its accessible label. Once the lane diff reads, it checks the lane-file tree row shows +45 −0 with the same structure and accessible counts.

### Invariants And Boundaries

The case checks one matching location row and one composed lane file, using DOM/class assertions. It does not measure the rendered colours or line-count font size.

## Evidence

- Location and loaded lane-file rows retain signed text, colour classes and accessible counts. [3]
