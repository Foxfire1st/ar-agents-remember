# dashboard/src/panels/review/reading/blockCards.test-utils.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Render supplied card-read entries through the production block-card component for tests.

## Code Commentary

### Logic

Synthesizes one outlined invariant per supplied entry owner, builds the Priority/All change-set model with ready cards and no selection, then flattens changed, unchanged and not-comparable locations. BlockCards draws each location with the production ReviewBlockCard, an empty planning map, default split layout and collapsed context, and an inert selection callback.

### Invariants And Boundaries

This helper does not issue a card read or provide a real navigation/selection owner. Its synthetic outline marks every supplied subject changed; callers must supply the comparison and entries whose behavior they intend to exercise.

## Evidence

- The helper creates its synthetic outline and flattens all three location classes. [4]
- BlockCards supplies fixed/default test context to the production card component. [5]
