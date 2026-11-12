# dashboard/src/panels/review/reading/readerAnchor.editors.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Exercise document-line anchoring inside real editors under deterministic layout changes.

## Code Commentary

### Logic

Places real EditorView instances in the anchored mock column. It checks a line near the view top remains within 1px through line-height changes above/below, editor rebuild and surrounding growth; asks only newly visible unmeasured editors to measure; restores a line initially hidden in an editor gap; and observes both simulated side-by-side lanes and held-box relayouts after animation callbacks.

### Invariants And Boundaries

CodeMirror instances are real, but block/line heights, visibility, alignment stimulus and frame observations are controlled by the test harness. These are not browser screenshot/paint measurements or a fresh full MergeView acceptance run.

## Evidence

- Real editors retain the addressed line and only newly visible unmeasured editors receive a measurement request. [4]
- A line initially in an editor gap remains stable while later lines grow. [5]
- Both controlled side-by-side lanes and held-box relayouts retain the sampled line positions. [6]
