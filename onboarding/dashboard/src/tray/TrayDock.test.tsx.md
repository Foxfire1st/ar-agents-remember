# dashboard/src/tray/TrayDock.test.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks single-dock geometry, reserved height and minimized/full/closed transitions.

## Code Commentary

### Logic

Supplied composer/frame boxes produce the exact above-box placement, measured reservation and bounded height; unavailable composer yields one notice below frame; new picks show only attached counter; explicit expansion and minimization remain stable; close preserves pill; outcomes/refusals remain readable.

Mocked getBoundingClientRect and frameTrayStore, with class assertions for min-height,38vh pick scrolling and overscroll containment.

### Invariants And Boundaries

Rectangles and CSS classes are fixture inputs; no browser pixel measurement is newly established.

## Evidence

- Checks single-dock geometry, reserved height and minimized/full/closed transitions. [1]
- Checks single-dock geometry, reserved height and minimized/full/closed transitions. [2]
- Checks single-dock geometry, reserved height and minimized/full/closed transitions. [3]
- Checks single-dock geometry, reserved height and minimized/full/closed transitions. [4]
- Checks single-dock geometry, reserved height and minimized/full/closed transitions. [5]
- Checks single-dock geometry, reserved height and minimized/full/closed transitions. [6]
- Checks single-dock geometry, reserved height and minimized/full/closed transitions. [7]
- Checks single-dock geometry, reserved height and minimized/full/closed transitions. [8]
- Checks single-dock geometry, reserved height and minimized/full/closed transitions. [9]
