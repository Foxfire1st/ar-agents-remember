# dashboard/src/panels/review/top-line/ComparisonSelector.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Render the review’s numbered comparison menu and the change-set tray-pick control.

## Code Commentary

### Logic

The controlled menu lists every integer from latest down to 1, marks the shown number current, labels latest versus read-only and invokes onChoose only for a different number after closing.

Only the shown comparison receives its recorded time because the supplied answer does not list other comparisons’ times. The menu names the leaf and states the older-number read-only boundary.

The comparison label and tray-add slot reserve width from first paint; a supplied pick renders AddToTray next to the label. The optional button ref also serves the status popover anchor.

### Invariants And Boundaries

It derives available number rows from the supplied latest number and owns no comparison fetch, candidate resolution or recording operation.

## Evidence

- Reserved widths [1]
- Shown time, current row and latest/read-only labels [2]
- Descending menu, selection callback and tray pick [3]
