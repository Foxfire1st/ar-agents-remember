# dashboard/src/cockpit/RoleChatsView.shownChat.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Specify which observed Chats-frame agent becomes the first object pick’s tray target.

## Code Commentary

### Logic

A native selection from A to B updates the shown-chat store and supplies B to a fresh tray, without a new ar.open request.

A plugin with showing reports supplies the visible chat in compact layout even while selection remains empty; null clears the default target. Foreign-origin reports change nothing.

An unreachable-frame placeholder supplies no shown chat even when the launcher retains an architect execution.

### Invariants And Boundaries

These mounted, stubbed native-channel cases observe the displayed chat rather than treating a launcher receipt as the displayed agent; a fourth case pins that a requested but unacknowledged chat publishes nothing, so a request and a receipt are separated too. No tests were run for this analysis.

## Evidence

- Observed default target without steering [1]
- Showing capability, null and origin boundaries [2]
- Unavailable display supplies no default [3]
