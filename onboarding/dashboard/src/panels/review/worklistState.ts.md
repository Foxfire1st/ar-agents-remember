# dashboard/src/panels/review/worklistState.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Display server gate verdicts, never derive them.

## Code Commentary

itemAnswer returns item_states only for a bound worklist. itemAnswerText states measured answered witness, open reason, stale row reason, undecided reason or missing measurement. openCount requires non-absent source, complete state, no incompleteness, bound context, an item_states map and decisive verdicts for every relevant item. worklistAnswer then returns N open/all answered; fileAnswers groups unexplained_hunk/unexplained_file facts by path once and returns N open/answered only for admitted measurements. Neither satisfied_by nor presence of history substitutes for the gate. This module cannot satisfy or waive a worklist item.

## Invariants And Boundaries

This is the inspected source contract, not an execution certificate. Parent and direct callers retain authority for identity, reads and state.

## Evidence

- Display server gate verdicts, never derive them: `itemAnswer` owns the described branch. [1]
- Display server gate verdicts, never derive them: `itemAnswerText` owns the described branch. [2]
- Display server gate verdicts, never derive them: `openCount` owns the described branch. [3]
- Display server gate verdicts, never derive them: `worklistAnswer` owns the described branch. [4]
- Display server gate verdicts, never derive them: `fileAnswers` owns the described branch. [5]

