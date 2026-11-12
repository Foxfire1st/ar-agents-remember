# dashboard/src/panels/review/reading/ReadingColumn.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Render sticky reading head plus permanently mounted notes, active subjects, lane, retained canvas slot and provenance.

## Code Commentary

### Logic

Render sticky reading head plus permanently mounted notes, active subjects, lane, retained canvas slot and provenance. One remembered code-context switch. Measure head for scroll padding; page-level pending reads do not tear down the column. Worklist replaces summary/subjects/lane when selected.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Render sticky reading head plus permanently mounted notes, active subjects, lane, retained canvas slot and provenance.
- Render sticky reading head plus permanently mounted notes, active subjects, lane, retained canvas slot and provenance. [2]

- The page-level Code context control selects Changes only or Full context through the persisted code-context store; the old ExpressionControls callbacks are retired. 
- ReadingColumn renders the shared model's subject groups and lane under its page-level control; the retired ReviewExpressions file accordion is not this composition. 

- Retired at the fifth freeze d59c3493: dashboard/src/panels/review/reading/ReadingColumn.tsx:25-41 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 10e466b17feee2530c06b2670fef496c6c9e755f; dashboard/src/panels/review/reading/ReadingColumn.tsx:70-92 - the region it cited is not in the file at the candidate and no re-point was possible; dashboard/src/panels/review/reading/ReadingColumn.tsx::CodeContextSwitch - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 10e466b17feee2530c06b2670fef496c6c9e755f; dashboard/src/panels/review/reading/ReadingColumn.tsx::ReadingColumn - the bytes it recorded now occur 4 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
