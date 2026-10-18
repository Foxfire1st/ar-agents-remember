# dashboard/src/panels/review/intent-passage/model.ts

## Governing Overview

[dashboard/src/panels route overview](../../overview.md)

## Purpose

One prepared wording model for layout and drawing.

## Code Commentary

preparePassage computes textDiff for two string operands even when projected is true. For two arrays it requires !projected, runs alignLists, and adds textDiff only to changed item pairs. Projected lists and unsupported operand pairs return undefined rather than guessed items. passageHasWords reads prepared models for layout eligibility, so callers reuse the exact alignment/diffs they draw. Shared COARSE_NOTE and UNPAIRED_NOTE supply fixed explanation wording. Pure presentation preparation has no store, request or normalization.

## Invariants And Boundaries

This is the inspected source contract, not an execution certificate. Parent and direct callers retain authority for identity, reads and state.

## Evidence

- One prepared wording model for layout and drawing: `preparePassage` owns the described branch. [1]
- One prepared wording model for layout and drawing: `passageHasWords` owns the described branch. [2]
- One prepared wording model for layout and drawing: `COARSE_NOTE` owns the described branch. [3]
- One prepared wording model for layout and drawing: `UNPAIRED_NOTE` owns the described branch. [4]

