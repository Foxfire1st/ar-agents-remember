# dashboard/src/panels/review/reading/ReadingColumn.crumb.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Keep the reading-head breadcrumb aligned with the explicit subject, block or lane-file selection.

## Code Commentary

### Logic

Opens the composed comparison #8 and clicks three different tree positions. It checks the exact comparison-only opening, the selected invariant text ID, the block's basename and after range, and the lane-file basename without a range. Every selected form has one bold ink/600-weight part; the block case also checks the selected card is inside the named subject section.

### Invariants And Boundaries

These cases cover the fixed L181 fixture identities and a selected entry's after range; they do not make the breadcrumb follow scrolling.

## Evidence

- Subject, block and lane-file clicks produce exact breadcrumb text and one bold subject/lane part. [4]
