# dashboard/src/panels/review/tree/treeStyles.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin tree layout and control style declarations at their ruled breakpoints.

## Code Commentary

### Logic

Inspects generated class strings for a 45dvh scroller cap only at 40rem and narrower; one-line flexible controls with a 5rem filter minimum, fixed view switch and ellipsized sort; tightened 320px-container heading/control spacing; signed count colours; a sticky bottom Worklist/lane block; and the 350px Sort popup's rows, rule and explanatory styles.

### Invariants And Boundaries

These are declaration-level assertions without mounting a tree or running a CSS layout engine. They do not measure overflow, actual row geometry or whether the controls fit a real viewport.

## Evidence

- Scroller cap and responsive control/heading declarations. [4]
- Signed count colours, pinned block and Sort popup declarations. [5]
