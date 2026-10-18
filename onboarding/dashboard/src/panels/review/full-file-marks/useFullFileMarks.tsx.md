# dashboard/src/panels/review/full-file-marks/useFullFileMarks.tsx

## Governing Overview

[dashboard/src/panels route overview](../../overview.md)

## Purpose

Reach every classified hunk in served full-file text.

## Code Commentary

Use the same marker-scope classification acquisition as the source pane; sourceMarks requires active scope and exact classified before/after blobs. MarksList enumerates classified hunk ranges, class and deduplicated linked realization/proof invariant names independently of editor viewport. Membership in pane marks determines reachability. Unplaceable hunks stay listed with a disabled action: truncated content names beyond the first 2 MiB, otherwise not in shown text. A placed choice supplies pane.reveal and clears it after reveal; existing pane behavior owns scroll/focus and collapsed-run expansion. A non-hunk/file-level classification adds no hunk list. This is presentation, not a second classifier or larger source provider.

## Invariants And Boundaries

This is the inspected source contract, not an execution certificate. Parent and direct callers retain authority for identity, reads and state.

## Evidence

- Reach every classified hunk in served full-file text: `sourceMarks` owns the described branch. [1]
- Reach every classified hunk in served full-file text: `MarksList` owns the described branch. [2]
- Reach every classified hunk in served full-file text: `revealingPane` owns the described branch. [3]
- Reach every classified hunk in served full-file text: `useFullFileMarks` owns the described branch. [4]

