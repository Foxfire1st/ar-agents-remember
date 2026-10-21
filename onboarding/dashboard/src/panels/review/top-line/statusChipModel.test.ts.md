# dashboard/src/panels/review/top-line/statusChipModel.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Specify local recorded-time formatting and its appearance in the status popover’s comparison row.

## Code Commentary

### Logic

One case expects local month/day/hour/minute for the supplied current year, includes the year for another year and preserves invalid input.

The second case expects the same short local time in Bound comparison for comparison 8.

### Invariants And Boundaries

The date is passed to the formatter; this source neither reads a live clock for acceptance nor covers all chip tones. Tests were inspected, not run.

## Evidence

- The two exact formatting cases [1]
