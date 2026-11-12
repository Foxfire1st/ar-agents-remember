# dashboard/src/panels/review/reading/useChangeSet.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Own the page's numbered reads and sole model.

## Code Commentary

### Logic

Own the page's numbered reads and sole model. Summary key `review-page` is separate from the task-entry request. `useComparisonNumbers` separates three numbers: the comparison the task context resolved (a landed leaf's delivered pair), the number on screen (`chosen` or the resolved one), and the older-comparison state, which now means the reader chose a number other than the resolved one. The menu's own list comes from the trees answer's `latest`, the leaf's highest recorded number, which is a different fact from the resolved comparison.

Cards read only active-view invariant IDs after read 4/catalogue settle; a missing or non-tree comparison is explicitly unavailable. `deliveredOf` states delivery from the trees answer when the leaf-wide read answered, and states an explicit unavailable line, with no delivered control, when that read refused or failed: silence used to read on the page exactly like a matching pair.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance. A delivered notice is a statement about which pair is on screen, never a review of it.

## Evidence

- Own the page's numbered reads and sole model. [1]
- Own the page's numbered reads and sole model. [2]
- Own the page's numbered reads and sole model. [3]

- The resolved comparison, the shown number and the older-comparison state are three separate facts. [4]
- An unreadable delivery is stated explicitly with no delivered control instead of collapsing to silence. [5]
- The menu's number list comes from the highest recorded number, kept apart from the resolved comparison. [6]

Per-leaf judgment state is now published separately from comparison facts and consumed by the sole change-set model. It stores categories/grades under repository/master/leaf, emits only when their serialized content changes and deletes empty judgment payloads. A live no-work move increments a leaf generation and re-reads the numbered leaf facts and currently asked invariant cards, while retaining the opening-set card-read owner. This publication carries inference data; it does not author knowledge or convert a grade into a recorded fact.

- Per-leaf judgment state is now published separately from comparison facts and consumed by the sole change-set model. It stores categories/grades under repository/master/leaf, emits only when their serialized content changes and deletes empty judgment payloads. A live no-work move increments a leaf generation and re-reads the numbered leaf facts and currently asked invariant cards, while retaining the opening-set card-read owner. This publication carries inference data; it does not author knowledge or convert a grade into a recorded fact. [7]
