# dashboard/src/cockpit/paseoFrameControl.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The controller steers one existing frame and owns its bounded native control-channel lifetime.

## Code Commentary

Wanted/seen, pending/settled and URL-loaded IDs distinguish launch intent, unanswered control and an already loaded route. Ready navigation posts ar.open without replacement; transient options absence does not resend a seen actor. Receive checks exact configured origin/current iframe window. Start/stop reset the selected-ID set for the next frame lifetime; the controller no longer holds a catalog. The message switch keeps `selection` and `navigation-error`; the `hierarchy`/`hierarchy-error` kinds and the deliberate chat-navigation click went with the dashboard sidebar (MIK-R75 rules 7 to 9), and Parent errors still require a currently selected source child.

## Invariants And Boundaries

The existing 10-second unavailable path keeps the frame and may load the requested actor URL once; explicit Retry changes generation. Shown replies never establish selected rows. The dashboard draws no other chat navigation; no fallback is proposed.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `receive` | `dashboard/src/cockpit/paseoFrameControl.ts:122-129` |
| Current source owner or exact assertion described above. | `onMessage` | `dashboard/src/cockpit/paseoFrameControl.ts:131-158` |
| Current source owner or exact assertion described above. | `sync` | `dashboard/src/cockpit/paseoFrameControl.ts:163-175` |
| Unloaded, unknown and hidden DOM IDs are not published; plural visible IDs are intersected after load and recomputed on SDK removals, reconnect snapshots and teardown. | `validates visible selections against current SDK IDs, recovering after catalog load and clearing removed or reconnected IDs` | `dashboard/src/cockpit/paseoHierarchy.test.ts:244-274` |
| Deferred lookup is ignored after tab/relation changes; a still-visible split-pane caller can open its current parent, and missing/archived parents or root transitions do not replace the child. | `checks current visible caller and parent relation, including deferred navigation, unavailable parents and root transitions` | `dashboard/src/cockpit/paseoHierarchy.test.ts:134-164` |
