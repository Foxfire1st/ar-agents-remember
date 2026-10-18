# dashboard/src/panels/review/ReviewDestinations.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Comparison-bound navigation destinations.

## Code Commentary

Render Changes without an invariant, Changes of unknown attribution, All changes and Worklist. Change-set buttons use the existing navigation context and held lane counts; loading is an ellipsis, unread/unavailable is not zero. All changes includes listed and unrepresentable paths only for a measured inventory, otherwise names the unmeasured change set. Worklist uses only a matching leaf read and worklistAnswer, displaying N open/all answered when admitted, not item count as a gate verdict. No fetch or local gate rule is introduced.

## Invariants And Boundaries

This is the inspected source contract, not an execution certificate. Parent and direct callers retain authority for identity, reads and state.

## Evidence

- Comparison-bound navigation destinations: `laneCounts` owns the described branch. [1]
- Comparison-bound navigation destinations: `ReviewDestinations` owns the described branch. [2]

