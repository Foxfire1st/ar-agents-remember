# dashboard/src/panels/GateResponder.tsx

## Governing Overview

[panels overview](overview.md)

## Purpose

Shared **Gate Respond** control for durable lifecycle gates. It renders one `Respond` button, shows a
human-readable request preview with raw JSON tucked behind diagnostics, and keeps only gate-decision
paths in this task-local surface: `Yes` / `No` record gate decisions through
`data/actions.postGateDecision`, and `Dismiss` cancels/deletes the current gate. The old message-only
`Chat` response path was removed in L8; conversational follow-up belongs in the adjacent leaf chat.

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
agent notification. Delivery first uses `deliverToSession` when `findSessionForLifecycle(lifecycleId)`
returns a hosted chat; otherwise it calls `postOperatorInbox` with the lifecycle id, gate id, human
preview text, and trimmed response.
The visible status distinguishes decision recording, stale/no-open gate failures, hosted delivery,
external-inbox queueing, unconfirmed hosted delivery, and inbox-post failure.

Successful approve/reject/dismiss submissions close the dialog immediately after the server accepts
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
- No message-only response box lives here after L8; revision instructions and follow-up questions go to
  the adjacent leaf chat, while this component keeps durable gate decisions explicit.
- `Dismiss` is not a decision outcome like approve/reject; it maps to backend `cancel`, which deletes
  the gate interaction so the attention row disappears server-side.
- `compact` only changes presentation so the same routing/control logic is used in Detail, Hangar, and
  Engine Room diagnostics.

## Evidence

### Repo-Internal References

- Dashboard gate decision client used by Yes/No. [1]
- Hosted session identity and delivery helpers. [2]
- External inbox helper used when no hosted session is attached. [3]
- Request/status formatting helpers extracted from this component. [4]
- Canonical lifecycle detail surface that renders this only when a durable gate exists. [5]
- Engine Room diagnostics secondary surface. [6]
- Hangar secondary surface for worktree-bound gates. [7]
- Projection gate and lifecycle shapes. [8]

#### 260713-PHA-L5 Adapter Interaction Context

Gate responses render adapter-owned interaction prompt, choices, and identity, and submit the chosen
response through the durable gate path. Completion or acceptance does not consume an inbox row.

## Current L5I Maintenance

A reopened hosted-interaction gate can carry `packet.adapterDecisionFailure`. This renderer now
shows the prior decision/note, the proven delivery certainty, and its reason before offering a
fresh response. It distinguishes `not-sent` (safe to decide again) from `unknown` (the harness may
already hold the decision) and preserves unfamiliar wire values verbatim rather than guessing.
