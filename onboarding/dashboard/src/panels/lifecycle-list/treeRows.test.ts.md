# dashboard/src/panels/lifecycle-list/treeRows.test.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Pure regression tests for need ordering, completed folds and selection reach in the Operations repository tree.

## Code Commentary

The synthetic tree assertions cover sibling creation order, scoped in-place folds, completed parents with open work, held selected descendants and both active/completed parent cycles. Flattened keys and depths must retain rows once; the suite does not render React Aria or prove keyboard and click behavior.

## Evidence

- The tests protect ordering, fold scope, selected reach and cyclic parent handling. [1]
