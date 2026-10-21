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
- Preload and in-place rail placement [2]
- Reachable overlay close control [3]
