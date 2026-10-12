# dashboard/src/panels/lifecycle-list/treeRows.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

A pure flattening of one repository task tree into task rows and in-place completed/abandoned folds.

## Code Commentary

Parents inherit the most pressing need in their subtree. treeItems composes subtree-need order before the chronological tie-break; compareRows itself compares only createdAt and then fallbackOrder. Over-state subtrees fold behind a scoped count. The selected descendant holds ancestors and its fold open without rewriting persisted reader choices. A completed parent with active descendants stays out of the over fold. Cycle guards and a final orphan sweep keep each input row reachable once; an unopened parent hides descendants rather than losing them. This helper changes presentation, never the selected document or task state.

## Evidence

- The tree walk combines subtree need, selection containment, fold state and one-time row emission. [1]


- Chronological comparison is separate from subtree-need ordering and held-selection flattening. [2]
