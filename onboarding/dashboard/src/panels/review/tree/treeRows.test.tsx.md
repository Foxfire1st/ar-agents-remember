# dashboard/src/panels/review/tree/treeRows.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Component cases for the intent-review tree's location layout and revision-standing tags.

## Code Commentary

Covered location rows keep three cells. A graded case puts the whole chip in the trailing cell,
and an ungraded case leaves that cell for the reason. Subject and family cases check the visible
candidate state tag, its writer in the title and accessible name where supplied, and the absence
of the tag for a subject that received no state.

## Boundaries

The component fixtures supply the record state and writer explicitly. One subject case supplies
`proposed` with a null writer and asserts a state-only tag. The cases exercise presentation of
supplied facts.

## Evidence

- The location cases check three cells, presence of the grade chip only where expected and the ungraded reason cell. [1]

- Subject cases cover state and writer in the trailing cell, accessible text, omitted state and a null writer. [2]
- The family case includes role and model in the title and accessible name alongside the visible state. [3]
