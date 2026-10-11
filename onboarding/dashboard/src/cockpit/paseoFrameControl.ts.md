# dashboard/src/cockpit/paseoFrameControl.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The controller steers one existing frame and owns its bounded native control-channel lifetime.

## Code Commentary

Wanted/seen, pending/settled and URL-loaded IDs distinguish launch intent, unanswered control and an already loaded route. Ready navigation posts ar.open without replacement; transient options absence does not resend a seen actor. Receive checks exact configured origin/current iframe window. Start/stop reset the selected-ID set for the next frame lifetime; the controller no longer holds a catalog. The message switch keeps `selection` and `navigation-error`; the `hierarchy`/`hierarchy-error` kinds and the deliberate chat-navigation click went with the dashboard sidebar (MIK-R75 rules 7 to 9), and Parent errors still require a currently selected source child. Since MIK-R122 a selection change while the channel is unavailable clears and re-arms one trailing settle window (`PASEO_UNAVAILABLE_QUIET_MS`); a change while ready invokes sync and can post `ar.open` at once, while a change while waiting invokes sync but forwards nothing until the ready report or deadline, with no timer elsewhere. The window's expiry brings its latest selection forward; the ready report, Retry, host return or a new deadline also syncs, while a superseding display while unavailable only cancels and re-arms the window. Each expiry may load its latest changed URL once; two settled windows with different latest URLs bring each forward, so no per-episode one-load cap or total-burst bound is claimed.

## Invariants And Boundaries

The existing 10-second unavailable path keeps the frame and may load the requested actor URL once; explicit Retry changes generation. A trailing settle window coalesces bursts first: each settled window forwards only its latest selection, and the deadline still names the latest unanswered target. Shown replies never establish selected rows. The dashboard draws no other chat navigation; no fallback is proposed.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- A selection change while ready invokes sync and can post ar.open at once; while waiting it invokes sync but forwards nothing until the ready report or deadline; while unavailable it clears and re-arms one trailing settle window for the latest selection. [1]
- The settle window's expiry brings its latest selection forward; the ready report, Retry, host return or a new deadline also syncs, while a superseding display while unavailable only cancels and re-arms the window. [2]
- The switch posts ar.open by message while ready and loads a changed latest URL when its settle window expires while unavailable. [3]
- A document load raises the generation by exactly one. [4]
- Only the embedded application's messages from the exact origin and window are admitted. [5]

## MIK-R95 Document Steering

The pane descriptor carries `page`. In document mode a ready target switch posts `ar.open` with the exact agent and workspace (not a bare agent), the frame URL carries the page mode, and the pane re-announces `ar.page`; the initial document load is forced through the wanted target so a fresh frame opens on the selection. Ready navigation still retains the frame element and never reloads for a same-generation move.
