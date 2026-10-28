# dashboard/src/panels/review/reading/SelectedWorklist.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The leaf worklist in the reading column, where the reviewer chooses it over the change set.

## Code Commentary

A reviewer who chooses the worklist sees their leaf's paths in the reading column instead of the change set, and every path still opens. A path the conversion has not covered is shown as such rather than disappearing from the list.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- A path the conversion has not reached is still listed and still opens, rather than vanishing from the worklist. [1]
