# dashboard/src/panels/review/reading/useReviewPage.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Own walk, selection, model, scroll and traversal composition.

## Code Commentary

### Logic

Own walk, selection, model, scroll and traversal composition. Walk scope is repo/master/leaf/history; lane facts reset by comparison; not-yet-read lane paths still keep traversal position; comparison switch unselects; tree group action opens the reading group and arms one landing.

The page's comparison choice is expressed against the comparison the page resolved, so choosing it again clears the explicit number. `chooseDelivered` is the delivered view's action, taken by the mismatch line and by the menu's delivered row: it leaves any recorded frame the target opened and then clears the number, because the delivered view is the page's default rather than a second comparison.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance. The delivered action starts no model and no role.

## Evidence

- Own walk, selection, model, scroll and traversal composition. [1]
- Own walk, selection, model, scroll and traversal composition. [2]
- Own walk, selection, model, scroll and traversal composition. [3]

- Choosing the resolved comparison clears the explicit number, so one meaning of "shown" serves the note, the selector and the subject reads. [4]
- The delivered action leaves the recorded frame and clears the chosen number. [5]
