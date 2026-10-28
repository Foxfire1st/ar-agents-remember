# dashboard/src/panels/review/reading/ReadingColumn.headFocus.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin the sticky reading head's protection against native focus scrolling.

## Code Commentary

### Logic

Mounts the composed page, confirms the tree toggle is inside the sticky reading head, and checks the head and all descendants declare a 1,000,000px bottom scroll margin.

### Invariants And Boundaries

jsdom does not perform native scrolling on focus. This case pins the scroll-margin declaration, while actual browser focus/scroll behavior requires separate evidence.

## Evidence

- The head contains the toggle and declares the large scroll margin on itself and descendants.

- Retired at the fifth freeze d59c3493: dashboard/src/panels/review/reading/ReadingColumn.headFocus.test.tsx:17-25 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 10e466b17feee2530c06b2670fef496c6c9e755f. Retired means the anchor no longer stands, not that the cited subject was deleted.
