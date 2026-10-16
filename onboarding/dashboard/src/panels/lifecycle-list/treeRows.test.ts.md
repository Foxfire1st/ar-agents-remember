# dashboard/src/panels/lifecycle-list/treeRows.test.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Pure regression tests for need ordering, completed folds and selection reach in the Operations repository tree.

## Code Commentary

Pure native tree assertions keep a completed master folded despite an active child and open its ancestors to a selected descendant. At 109/300 terminal-child history sizes closed folds construct no child rows; opening preserves authored entry order. Supplied roots for unlisted/missing-parent tasks and their declared children are reached exactly once. No browser-side creation-order/parent reconstruction or legacy cycle algorithm is claimed; React Aria keyboard/click behavior remains outside this pure suite.

## Evidence

- Native parent/children, lazy terminal folds, selected reach and authored root/child order are the current pure assertions. [1]
