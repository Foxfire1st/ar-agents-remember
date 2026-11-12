# dashboard/src/panels/review/treeScroll.ts

## Governing Overview

[review route overview](overview.md)

## Purpose

Reveal a selected row by changing only the nearest tree panel's scrollTop, accounting for its pinned bottom rows.

## Code Commentary

`revealTreeRow` finds the nearest data-review-tree-panel scroller, measures it and the selected row, and adjusts scrollTop only when the row is above or below its visible bounds. If the pinned Worklist/lane block follows the row and does not contain it, its top limits the row's visible bottom. Rows inside or after that block use the panel bottom. Missing row/panel is a no-op.

The helper changes no height/style, focus, selection or ancestor scroll coordinate. CSS owns the scroller's height and the caller owns focus eligibility.

## Evidence

- treeScroll.ts current behavior at this source owner. [5]
