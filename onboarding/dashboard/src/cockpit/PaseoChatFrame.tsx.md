# dashboard/src/cockpit/PaseoChatFrame.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The component owns one native embedded chat document, with distinct frame/control/agent notices; the dashboard draws no chat navigation of its own.

## Code Commentary

The descriptor is read on first activation and explicit Retry — never on an ordinary selection change. A stable controller consumes execution targets and trusted plugin messages. The iframe generation rises by exactly one per document load and is exposed as `data-generation` for tests; ready selection switches never touch it, while the fallback load, Retry and host return still replace the frame. The dashboard's own sidebar, its grouping memo and its catalog/problem notices are removed with rule 7; the host's own list is the navigation (MIK-R75 rules 7 to 9).

## Invariants And Boundaries

Normal view switches preserve the frame; Retry and the existing unavailable-control URL path may replace a generation. The frame loads again only for the MIK-R121 fallback load, Retry, and host return. The host's list, not a dashboard rail, is the chat navigation on this page.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- One stable controller consumes execution targets and trusted plugin messages. [1]
- The descriptor is fetched on first activation and each explicit Retry. [2]
- The mounted pane exposes the load count and keys the frame element by generation only. [3]

## MIK-R95 Document Page Mode

The frame takes `page` and reports availability to its host. In document mode the controller announces `ar.page`, carries `arPage=document` in the frame URL, moves a ready frame by `ar.open` with the exact agent and workspace (so the same element and `performance.timeOrigin` survive a ready target switch) and does not reload for a selection change; the unavailable path and explicit Retry still replace a generation. `FrameUnavailable` is exported so the document panel shows the same Retry notice. The wide embedded frame keeps the working Parent control; the narrow document frame shows none (D86).
