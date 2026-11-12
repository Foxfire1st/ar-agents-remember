# dashboard/src/panels/review/reading/LaneSection.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Keep long added-file links on a destination that actually lists the chosen lane file.

## Code Commentary

### Logic

Builds one synthetic 45-line added file in each attribution bucket. After the text stub answers, each file exposes 15 more added lines; clicking it calls the comparison navigator exactly once with that file path and its matching unexplained or unknown filter. The same fixture is passed through the change-set destination selector to assert that filter contains the path.

### Invariants And Boundaries

The test observes the navigation callback and destination file list. It does not mount or inspect the opened comparison viewer.

## Evidence

- Synthetic lane and text fixtures contain one file per bucket. [2]
- The cap link preserves both the chosen path and a filter whose list contains it. [3]
