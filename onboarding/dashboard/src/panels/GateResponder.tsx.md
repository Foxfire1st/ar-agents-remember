# dashboard/src/panels/GateResponder.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/GateResponder.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-25T13:10+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

Shared **Gate Respond** control for lifecycle gates and proto `ask` packets. It renders one `Respond`
button, shows a human-readable request preview with raw JSON tucked behind diagnostics, and splits
developer response paths by meaning: `Yes` / `No` record gate decisions through
`data/actions.postGateDecision`, `Dismiss` cancels/deletes the current gate, and `Chat` is message-only
and routes text either to the AR-hosted chat attached to that lifecycle or, when no hosted session
exists, to the external operator inbox.

## Code Commentary

### Logic

Props are `lifecycleId`, optional `gateNode`, optional `ask`, optional `compact`, and an optional
`testId`. The component subscribes to `data/sessions` for open sessions and the active id. It resolves
the destination by `findSessionForLifecycle(lifecycleId)`, so the route is
`gate.lifecycleId -> OpenSession.lifecycleId -> deliverToSession(session.id, package)`.

The dialog is inline React Aria `Dialog` content. `requestText` converts gate packets and `ask`
objects into operator-readable lines (`Gate`, `State`, `Decision options`, `Request`, and contextual
fields such as changed paths); `diagnosticText` keeps the original JSON in a collapsed diagnostics
block. The request preview has a 480px default/minimum height and a keyboard/pointer resize handle
that adjusts only the preview height, bounded by measured content height plus margin.

For a durable `gateNode`, `Yes` first calls `postGateDecision(lifecycleId, "approve",
{gateId})`; `No` requires non-empty reason text and calls `postGateDecision(lifecycleId, "reject",
{gateId, note})`; `Dismiss` calls `postGateDecision(lifecycleId, "cancel", {gateId, note})`, which the
backend treats as a physical gate delete. None of these paths asks the agent to set the decision
itself. After a successful recorded approve/reject decision the component notifies the agent with a
short message through the hosted chat or operator inbox; after a successful dismiss it closes without
agent notification. `Chat` never calls `postGateDecision`; it only sends the free-form message. Delivery first uses
`deliverToSession` when `findSessionForLifecycle(lifecycleId)` returns a hosted chat; otherwise it
calls `postOperatorInbox` with the lifecycle id, gate id, human preview text, and trimmed response.
The visible status distinguishes decision recording, stale/no-open gate failures, hosted delivery,
external-inbox queueing, unconfirmed hosted delivery, and inbox-post failure.

Successful approve/reject/chat/dismiss submissions close the dialog immediately after the server accepts
the write/delivery, so the developer is not left staring at a completed prompt. Formatting helpers moved
to `GateResponderText.ts` so this component remains behavior-focused.

If no session is attached but the active hosted session is untagged, `Attach <session>` calls
`sessionStore.setLifecycle(activeSession.id, lifecycleId)`. It does not retag a chat already attached
to another lifecycle; one chat works one lifecycle, and one lifecycle route resolves to one chat.
`isWorktreeGateKind(kind)` is exported for secondary engine-room/hangar surfaces and currently matches
the worktree-bound gate families: closeout, push, integration, and cleanup.

### Invariants And Boundaries

- Hosted chat injection remains preferred because it gives immediate conversational context.
- The external operator inbox is the fallback when no hosted session is attached; missing session is no
  longer a disabled response path.
- Durable gate decisions are recorded by the dashboard (`/api/actions/{approve,reject}`) and targeted
  by `gateId`; stale gates surface as errors and do not notify the agent.
- `Chat` is deliberately message-only: it cannot approve/reject/cancel a gate and exists for revision
  instructions or follow-up questions.
- `Dismiss` is not a decision outcome like approve/reject; it maps to backend `cancel`, which deletes
  the gate interaction so the attention row disappears server-side.
- `compact` only changes presentation so the same routing/control logic is used in Detail, Hangar, and
  Engine Room diagnostics.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Dashboard gate decision client used by Yes/No. | — | [data/actions.ts](../data/actions.ts) |
| Hosted session identity and delivery helpers. | — | [data/sessions.ts](../data/sessions.ts) |
| External inbox helper used when no hosted session is attached. | L1-L25 | [data/operatorInbox.ts](../data/operatorInbox.ts) |
| Request/status formatting helpers extracted from this component. | — | [GateResponderText.ts](GateResponderText.ts) |
| Canonical lifecycle detail surface that renders this for gates and asks. | — | [DetailPanel.tsx](DetailPanel.tsx) |
| Engine Room diagnostics secondary surface. | — | [engine-room/DiagnosticsPanel.tsx](engine-room/DiagnosticsPanel.tsx) |
| Hangar secondary surface for worktree-bound gates. | — | [Hangar.tsx](Hangar.tsx) |
| Projection gate and lifecycle shapes. | — | [types/projection.ts](../types/projection.ts) |

## Update History

- 2026-06-25T13:10+02:00 — Task 23/24: added Dismiss/cancel, close-on-success response behavior, and extracted request/status formatting to `GateResponderText.ts`.
- 2026-06-25T07:17+02:00 — Task 19: split Gate Respond into durable decision paths (`Yes` approves, `No` rejects with required reason) and message-only `Chat`, added targeted stale-gate handling, rendered gate requests as human-readable previews with diagnostics JSON collapsed, and added the 480px resizable request panel. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: Gate Respond now queues a developer response in the external operator inbox when `findSessionForLifecycle` finds no hosted chat, and exposes queued/error status text instead of disabling the response path. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T13:45+02:00 — Created for Task 11: shared chat-routed Gate Respond control with
  Yes/No/Chat modes, full request display, hosted-session lookup by lifecycle id, missing-session
  status, and active untagged chat attach.
