# dashboard/src/cockpit/PaseoChatFrame.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Own one embedded native chat document and its separate frame, control, agent and plugin notices.

## Code Commentary

The descriptor is fetched on first activation or an explicit preload, then on explicit Retry. Ordinary selection changes do not fetch it again. Preload is opt-in for a closed review chat column: if the pane is still hidden when the descriptor answers, the controller starts the application without naming an agent. Other panes retain first-show startup. [2]

One stable controller receives a changed target in a layout effect before paint and re-syncs an unshown target without reload when `active` flips from false to true. The iframe is keyed only by load generation so a ready message switch retains its DOM identity, and its `onLoad` callback notifies the controller to anchor post-load readiness timing. The container
also carries `data-scope`, the steered selection's role-and-document identity, which changes without a remount. The component reports whether the descriptor provides an available native frame. [1] [3]

While the document's agent is unknown, `holding` keeps the current native screen visible but inert. Otherwise `frameWait` holds input until the selected agent is shown or on-chat, or an explicitly URL-only plugin loaded its URL; when control is unavailable without an explicit non-`open-agent` plugin report, an unconfirmed URL-landed agent is not in reach and keeps a waiting notice with Retry. On-chat releases input while the bottom-edge waiting line remains until the conversation is drawn or the native failed-load pane is reported. An older plugin may end the line earlier; its capability notice names that limit. A held focused frame is blurred, inert and pointer-disabled. An agent-problem notice renders an explicit Retry button that asks the controller to resend `ar.open` without reload while control is ready, or reloads the frame while control is unavailable. [3] [4]

Document mode is passed to the controller. `FrameUnavailable` is exported for a shared unavailable notice with Retry. The native application's navigation and Parent control remain inside the embedded page: the existing document policy retains Parent on the wide frame and suppresses it in the narrow document layout.

## Invariants And Boundaries

Normal view and responsive selection switches retain the frame. Recovery loading follows the controller's unanswered open-request ping boundary, explicit Retry while unavailable, and host return; post-load readiness and cold-load cap timeouts settle unavailable without reloading, and a plugin explicitly lacking `open-agent` retains URL navigation. A slow host or drawing answer does not itself replace a generation. Ready document switches carry the agent and workspace through `ar.open`, with page mode announced separately by the controller.

Clipboard read and write permission is limited to the configured embedded origin. Native failure text and native Retry remain the application's. The dashboard draws neither another conversation frame nor a frozen image of the previous conversation. [3]


## Evidence

- First activation, opt-in preload and Retry own descriptor reads; hidden startup names no agent. [2]

- The stable controller dispatches changed targets before paint, re-syncs unshown targets on reveal without reload, and receives frame messages. [1]
- The frame component forwards the steered selection scope and onLoad/Retry handlers into EmbeddedFrame and FrameNotices; generation keys the iframe, clipboard permission names the embedded origin, held input is blurred and inert, and agent-problem Retry resends ar.open when ready or reloads when unavailable. [3]
- Shown, on-chat, control availability and explicit urlOnly state determine input reachability and the waiting notice with Retry. [4]
