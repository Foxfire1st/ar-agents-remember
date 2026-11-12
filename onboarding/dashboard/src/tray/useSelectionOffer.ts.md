# dashboard/src/tray/useSelectionOffer.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Observes dashboard panel selections without taking focus or changing copy.

## Code Commentary

### Logic

Reads the selection synchronously on mouseup, optionally runs native copy, names the nearest panel, and only takes on the offer click; dismisses on collapsed selection, Escape or scrolling.

### Invariants And Boundaries

Editable inputs, tray, offer and iframe are excluded. Copy failure leaves the clipboard unchanged and the offer usable. No removeAllRanges or focus transfer.

## Evidence

- Observes dashboard panel selections without taking focus or changing copy. [1]
- Observes dashboard panel selections without taking focus or changing copy. [2]
- Observes dashboard panel selections without taking focus or changing copy. [3]
