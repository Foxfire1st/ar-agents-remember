# dashboard/src/cockpit/PaseoChatFrame.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The component owns one native embedded chat document, with distinct frame/control/agent notices; the dashboard draws no chat navigation of its own.

## Code Commentary

The descriptor is fetched on first activation and explicit Retry, never for an ordinary selection change. One stable controller publishes the frame's load generation and current request state. A layout effect sends a known target change before paint; the iframe is keyed only by generation, so a message switch preserves its DOM identity.

While the document's agent is unknown, `holding` keeps the current native screen visible but inert. Otherwise `frameWait` holds input until the application reports the selected agent as shown or on-chat, or the loaded URL already names it. With the current plugin, on-chat releases input while the waiting line remains until drawing or the native failed-load pane is reported. The line lies at the bottom edge, away from native header controls. An older plugin's earlier answer ends it at that plugin's boundary, which the capability notice names. A held focused frame is blurred and excludes pointer input as well as keyboard reach.

## Invariants And Boundaries

Normal view and responsive selection switches preserve the frame. Recovery loading follows the controller's unanswered-ping boundary, explicit Retry and host return, with URL-only navigation retained for a plugin explicitly lacking open-agent. A slow host/drawing answer does not itself replace a generation. The pane shows the application's own screen, not a second frame or a frozen copy of the previous conversation. Native failure text and native Retry remain the application's, never fabricated dashboard content. The host's list remains the only chat navigation.

## Evidence

These assertions name source ownership; no native installation proof or test rerun is claimed.

- One stable controller dispatches selection changes before paint and consumes only its trusted frame messages. [1]
- The descriptor is fetched on first activation and explicit Retry, not selection changes. [2]
- Generation alone keys the iframe; held input is inert, pointer-disabled and blurred, with a bottom-edge waiting line. [3]
- On-chat or shown confirms selected-screen input ownership; an unanswered request remains visibly waiting. [4]

## MIK-R95 Document Page Mode

The frame takes `page` and reports availability to its host. In document mode the controller announces `ar.page`, carries `arPage=document` in the frame URL, moves a ready frame by `ar.open` with the exact agent and workspace (so the same element and `performance.timeOrigin` survive a ready target switch) and does not reload for a selection change; the unavailable path and explicit Retry still replace a generation. `FrameUnavailable` is exported so the document panel shows the same Retry notice. The wide embedded frame keeps the working Parent control; the narrow document frame shows none (D86).
