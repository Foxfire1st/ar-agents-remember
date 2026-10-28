# dashboard/src/panels/review/reading/LaneSection.counts.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin the signed lane-file line counts and their declared presentation.

## Code Commentary

### Logic

Renders the composed L181 page with first-paint intersection, waits for its added lane file to load, and asserts the exact text +45 −0. Each signed number is a direct child of the count wrapper; the wrapper declares 0.72rem and the children use mint and alarm colours.

### Invariants And Boundaries

The fixture supplies one 45-line added file. These DOM/text/class assertions do not measure rendered colour or font size.

## Evidence

- The mounted lane file retains both signed counts and the declared size/colour classes.

- Retired at the fifth freeze d59c3493: dashboard/src/panels/review/reading/LaneSection.counts.test.tsx:20-37 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 10e466b17feee2530c06b2670fef496c6c9e755f. Retired means the anchor no longer stands, not that the cited subject was deleted.
