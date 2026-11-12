# dashboard/src/tray/TrayDock.test.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks single-dock geometry, including the message box's own column, reserved height and minimized/full/closed transitions.

## Code Commentary

### Logic

Supplied composer/frame boxes produce the exact above-box placement, measured reservation and bounded height; the placement takes the message box's own left and width with the frame only as their origin and leaves the width unclamped, while a composer edge without the pair keeps the frame-wide left and width; unavailable composer yields one notice below frame; new picks show only attached counter; explicit expansion and minimization remain stable; close preserves pill; outcomes/refusals remain readable.

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

- Three geometry cases pin the box's own column: the exact box-origin formula with an unclamped width, the drawn dock inside a frame wider than its chat, and the frame-wide fallback when no extent is reported. [10]

Two new DOM cases press the minimized docked line's head to expand the full tray and press its Close control to retain the closed pill without expanding. The fixture supplies the native composer location; these cases prove event composition and collection retention, not fresh browser geometry.

- Two new DOM cases press the minimized docked line's head to expand the full tray and press its Close control to retain the closed pill without expanding. The fixture supplies the native composer location; these cases prove event composition and collection retention, not fresh browser geometry. [11]
