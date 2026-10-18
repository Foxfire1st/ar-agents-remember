# dashboard/src/panels/review/treeScroll.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Reveal a row within its tree panel only.

## Code Commentary

Find the closest data-review-tree-panel; missing row/panel is a no-op. Reset its max-height before measuring viewport changes, clip the bottom to window and review-surface bounds, constrain a clipped scrollport, and move its visible top below sticky triage controls. Adjust only that panel.scrollTop until the selected row fits. No ancestor scrollIntoView, focus move or selection occurs here. This keeps j/k reveal local rather than sending the page to its top.

## Invariants And Boundaries

This is the inspected source contract, not an execution certificate. Parent and direct callers retain authority for identity, reads and state.

## Evidence

- Reveal a row within its tree panel only: `revealTreeRow` owns the described branch. [1]
- Reveal a row within its tree panel only: `visiblePanelBounds` owns the described branch. [2]
- Reveal a row within its tree panel only: `belowControls` owns the described branch. [3]

