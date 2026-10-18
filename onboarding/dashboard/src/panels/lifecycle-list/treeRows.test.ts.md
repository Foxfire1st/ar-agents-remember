# dashboard/src/panels/lifecycle-list/treeRows.test.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Pure regression tests for need ordering, completed folds and selection reach in the Operations repository tree.

## Code Commentary

Pure native tree assertions keep a completed master folded despite an active child and open its ancestors to a selected descendant until an explicit release. Additional pure cases supply a released fold key or released parent key and require the fold/parent to close over the chosen child. These explicit TreeView inputs prove release precedence, not the React hook's selection-episode lifetime. At 109/300 terminal-child history sizes closed folds construct no child rows; opening preserves authored entry order. Supplied roots for unlisted/missing-parent tasks and their declared children are reached exactly once. No browser-side creation-order/parent reconstruction or legacy cycle algorithm is claimed; React Aria keyboard/click behavior remains outside this pure suite.

A new case orders the started band by host time: a working master first, then the paused rows the host timed newest first, then the untimed rows in the server's order; a missing time is never read as epoch zero or as now, so untimed rows are not reordered against each other.

## Evidence

- The started band puts host-timed paused rows newest first and leaves untimed rows in the server's order. [3]

- Native parent/children, lazy terminal folds, selected reach and authored root/child order are the current pure assertions. [1]

- Pure tree inputs show a released fold or ancestor staying closed over the chosen child; no mounted keyboard or hook-lifetime execution is inferred. [2]
