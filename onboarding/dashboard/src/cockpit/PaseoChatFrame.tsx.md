# dashboard/src/cockpit/PaseoChatFrame.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Own one embedded native chat document and its separate frame, control, agent and plugin notices.

## Code Commentary

The descriptor is fetched on first activation or an explicit preload, then on explicit Retry. Ordinary selection changes do not fetch it again. Preload is opt-in for a closed review chat column: if the pane is still hidden when the descriptor answers, the controller starts the application without naming an agent. Other panes retain first-show startup. [2]

One stable controller receives a known target change in a layout effect before paint. The iframe is keyed only by load generation, so a ready message switch retains its DOM identity. The component reports whether the descriptor provides an available native frame. [1] [3]

While the document's agent is unknown, `holding` keeps the current native screen visible but inert. Otherwise `frameWait` holds input until the selected agent is shown or on-chat, or the loaded URL already names it. On-chat releases input while the bottom-edge waiting line remains until the conversation is drawn or the native failed-load pane is reported. An older plugin may end the line earlier; its capability notice names that limit. A held focused frame is blurred, inert and pointer-disabled. [3] [4]

Document mode is passed to the controller. `FrameUnavailable` is exported for a shared unavailable notice with Retry. The native application's navigation and Parent control remain inside the embedded page: the existing document policy retains Parent on the wide frame and suppresses it in the narrow document layout.

## Invariants And Boundaries

Normal view and responsive selection switches retain the frame. Recovery loading follows the controller's unanswered-ping boundary, explicit Retry and host return; a plugin explicitly lacking `open-agent` retains URL navigation. A slow host or drawing answer does not itself replace a generation. Ready document switches carry the agent and workspace through `ar.open`, with page mode announced separately by the controller.

Clipboard read and write permission is limited to the configured embedded origin. Native failure text and native Retry remain the application's. The dashboard draws neither another conversation frame nor a frozen image of the previous conversation. [3]


## Evidence

- The stable controller dispatches known target changes before paint and receives frame messages. [1]
- First activation, opt-in preload and Retry own descriptor reads; hidden startup names no agent. [2]
- Generation keys the iframe; clipboard permission names the embedded origin and held input is blurred and inert. [3]
- The selected screen's shown/on-chat/loaded state determines input reachability and its waiting line. [4]
