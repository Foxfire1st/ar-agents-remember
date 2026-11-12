# dashboard/src/cockpit/reviewPage.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Compose the review’s main slot and the existing right rail as the task-chat column.

## Code Commentary

### Logic

ReviewMain passes the target’s optional selector and live/recorded history to ReviewSurface. At 40rem and narrower its main element supplies the stacked page’s vertical scrolling.

reviewRailView always identifies this rail as chat, hides it while closed or full bleed, requests preload while closed, and supplies the task binding and explicit unbound state.

columnPlacement changes the same rail element between grid, absolute overlay and fixed narrow overlay. ReviewChatClose places the shared toggle at the overlay’s edge.

### Invariants And Boundaries

This module supplies layout and props; chat state belongs to reviewChat.ts and the right-rail/frame owners retain the mounted chat element. A historical target asks for its recorded comparison.

## Evidence

- Target forwarding and main-slot composition [1]
- Reachable overlay close control [3]

reviewRailView also forwards column.explainer to the shared DocumentChat. The rail's preload, explicit unbound task state, closed/full-bleed visibility and placement/resize owners remain the same; the optional target changes which chrome and seat the retained frame displays.

- reviewRailView also forwards column.explainer to the shared DocumentChat. The rail's preload, explicit unbound task state, closed/full-bleed visibility and placement/resize owners remain the same; the optional target changes which chrome and seat the retained frame displays. [4]

- reviewRailView forwards the document reference, preload, explicit unbound state and optional leaf explainer target to the retained right rail; placement and resize behavior keep their existing owner. [2]
