# dashboard/src/panels/review/reading/LaneSection.look.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin the lane heading, file label and quiet control structure.

## Code Commentary

### Logic

After the composed page reads its lane file, checks the boxed lane/count/status labels, the Changed files explanation before the first file, and the Unexplained Full page label. Reconstructs the shared button selector to verify it excludes the quiet full-page and hunk buttons, whose own transparency, border and size classes are asserted.

### Invariants And Boundaries

The selector and class checks run without a CSS cascade or visual geometry; they preserve declared structure rather than certify a match to a screenshot.

## Evidence

- The mounted case checks heading/file labels, shared-selector exclusion and quiet control classes. [2]
