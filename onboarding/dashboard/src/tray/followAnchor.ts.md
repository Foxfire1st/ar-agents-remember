# dashboard/src/tray/followAnchor.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Keeps small fixed tray popups attached to their anchor.

## Code Commentary

### Logic

Measures on activation/render and follows observed element resize, window resize and captured scroll; cleans all observers/listeners on release.

### Invariants And Boundaries

It supplies geometry tracking only; callers own placement and popup semantics.

## Evidence

- Keeps small fixed tray popups attached to their anchor. [1]
