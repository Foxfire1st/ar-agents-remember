# dashboard/src/panels/detail-panel/taskSwitchAbort.test.tsx

## Governing Overview

[panels overview](../overview.md)

## Purpose

Pin the mounted task-switch rule: the left page's change-set bar, changed-intent summary and full
body reads end with the selection, and the new page shows its own loading state with no error.

## Tested Boundary

The case mounts the three page readers for one leaf, switches the selection, and asserts that each
in-flight request signal is aborted, the new page's own read is loading, and no error text appears.
It is a mounted component assertion, not an installed page timing.

## Evidence

- The mounted case named `aborts the change set, the review summary and the body, and shows no error`.
- The production `ChangeSetButton`, `useIntentReviewSummary` and `useTaskDocumentBody` abort paths.
