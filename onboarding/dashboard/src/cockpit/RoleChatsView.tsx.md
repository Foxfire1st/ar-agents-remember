# dashboard/src/cockpit/RoleChatsView.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Render the shared role launcher, receipt-selected native chat frame, tray dock and report reader.

## Code Commentary

The view threads one native TaskEntry array into the launcher, derives the frame target from the current scoped execution, and supplies launch readiness, progress, current errors and actions from their control owners. Report display hides the existing role pane and renders the shared report reader alongside it. A bound document row renders its launcher without a second native frame. [1]

For an active unbound Chats page outside the report reader, the view publishes the chat actually named by the frame channel. Before that channel has reported a value after a load, it uses the launcher's native target only while the frame is available. An explicit `null` from the frame means no named shown chat and does not restore the launcher target. This permits native chat-list navigation to change the tray's initial recipient.

The Chats tray dock is placed after the shared frame in the pane and is visible only with that active unbound chat page. Bound launcher rows add no dock. [1]

## Invariants And Boundaries

Presentation owns neither launch HTTP, options adoption, storage nor request identity guards. Those stay in the controls and transport owners. The view recreates neither a native chat list nor a report reader.

The frame's shown-chat report is separate from the launcher's current execution. While the native frame is absent or unavailable, the view publishes no shown chat. Hidden report takeover and bound launcher presentation preserve their distinct ownership. [1]


## Evidence

- RoleChatsView composes the shared launcher, optional native frame, conditional dock and report reader. [1]
- The presentation hook derives the scoped execution, frame target and launcher actions. [2]
- An available frame uses its explicit shown-chat report, with the launcher target only before any report. [3]
