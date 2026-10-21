# dashboard/src/panels/review/reading/ReviewPage.opening.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Guard the opening request schedule, closed location groups and single whole-comparison route.

## Code Commentary

### Logic

Counts exactly six page-opening request kinds with no selected subject or block. Holding the card answer prevents lane-file reads; once opening completes, an in-view lane file reads its classification and text without a gesture, while card marks additionally wait for engagement and intersection. The file-task gate is checked against READ_BATCH. Other cases pin the 31/28 closed groups and four-row previews, tree-triggered group opening with one column scroll, trailing-newline-safe added-file caps, one tree All changes control, absent per-card Full file controls, and the code-only-change count wording.

### Invariants And Boundaries

Fetch, intersections and group geometry are controlled by fixtures. READ_BATCH is tested as queued file tasks, not as a global count of network requests; the All changes cases inspect control ownership rather than an opened viewer.

## Evidence

- Opening reads, intersection/gesture admission and the queued file-task limit. [4]
- Closed-group counts/previews and tree-triggered group opening. [5]
- Added-file newline caps, the one All changes route and code-only-change wording. [6]
