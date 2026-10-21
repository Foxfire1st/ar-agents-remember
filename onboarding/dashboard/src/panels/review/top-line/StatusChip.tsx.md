# dashboard/src/panels/review/top-line/StatusChip.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Render the top-line branch-status button and its measured-facts popover.

## Code Commentary

### Logic

The chip uses the supplied label/tone in a fixed 13.5rem place, including while the label reads reading….

Its popover anchors to the comparison button when supplied, otherwise its own trigger; it renders the supplied rows and optional owner reason, names the shown comparison and points to Technical details.

### Invariants And Boundaries

StatusChip presents ChipFacts and computes no branch movement, staleness, comparison identity or semantic acceptance.

## Evidence

- Fixed place and tone presentation [1]
- Accessible button, supplied fact rows and popover anchor [2]
