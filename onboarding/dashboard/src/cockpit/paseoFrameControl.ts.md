# dashboard/src/cockpit/paseoFrameControl.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The controller steers one existing frame and owns its bounded native control-channel lifetime.

## Code Commentary

Wanted, pending, settled and URL-loaded identities distinguish the selected agent, its unanswered request, a completed answer and the frame's current route. `receive` admits only the configured origin and exact iframe window. Selection and source-scoped Parent errors retain their independent native selected-set authority.

A ready selection sends `ar.open` immediately. Every document load awaits a ready report for ten seconds, then asks one ping; only ten more seconds without that ping's answer mark the channel unavailable. A pong during that wait is a ready report. Selections made while a load's report is awaited are held, not loaded again, and the latest goes out by message when readiness returns. A ready request past its own ten-second deadline is late, not a dead channel: answered pings keep it waiting without resending the open, and a newer selection still switches by message.

When control really is unavailable and no load's ready report is pending, the existing trailing settle window coalesces unavailable selections and forwards the latest URL. That is a per-window bound, not a lifetime one-load cap. Explicit Retry and a returned host start the frame again. A plugin explicitly lacking `open-agent` uses agent URLs; one that merely names fewer abilities, or names none as the older plugin does, still switches by message.

## Invariants And Boundaries

An initial load establishes the frame. Subsequent recovery loads require an unanswered application ping, explicit Retry, or host return; a plugin explicitly unable to open an agent retains the URL-only exception. Missing ready or a slow agent answer alone never justifies a recovery load. Each load increments generation exactly once.

`navigated` distinguishes host lookup from application drawing; `on-chat` permits input to the selected agent's native screen before drawing completes. `shown` and the application's own `load-failed` pane both end the pending request. The latter leaves native failure text/Retry in reach without a dashboard-invented failure. Replies for another or superseded pending agent have no settlement consequence. Navigation acknowledgement never establishes native selected rows.

## Evidence

These are source contracts, not a claim of test execution in this pass.

- A ready change switches immediately; a change during a load's readiness wait is held, while unavailable changes use the trailing settle window. [1]
- Readiness ends the load wait and sends the latest held target through the negotiated channel. [2]
- URL loading is allowed only while unavailable and outside an outstanding load-readiness wait. [3]
- A document load raises generation once and then awaits its own readiness. [4]
- Only the configured frame origin and actual iframe window supply control messages. [5]
- A missing readiness report asks a ping before control is unavailable. [6]
- A late request is probed, not automatically reloaded. [7]
- Drawing and the application's own failed-load pane both settle only the pending agent. [8]

## MIK-R95 Document Steering

The pane descriptor carries `page`. In document mode a ready target switch posts `ar.open` with the exact agent and workspace (not a bare agent), the frame URL carries the page mode, and the pane re-announces `ar.page`; the initial document load is forced through the wanted target so a fresh frame opens on the selection. Ready navigation still retains the frame element and never reloads for a same-generation move.
