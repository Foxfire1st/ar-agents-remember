# dashboard/src/panels/review/explainer/MovedNotice.test.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Measures the moved notice's line, its note and the presence or absence of the Update control for the published, page-model and no-work shapes.

## Code Commentary

- The cases render the real notice with hand-built notices and read the line, the note and whether the control exists.
- The watcher's own text, rather than a re-derivation, is the required line, and the note must still say the explainer was not woken.
- The no-work case is required to state the renewed state and offer no Update, and a press in flight is required to be disabled and to call nothing.

## Evidence

- The published line is shown with its block count, and the note says the explainer was not woken [1]
- A master move offers Update even before any page exists [2]
- A leaf with no explainer work states that the view renewed itself and offers no control [3]
