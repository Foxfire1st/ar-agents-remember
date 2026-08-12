# dashboard/src/panels/GateResponder.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/GateResponder.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`       |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Dashboard gate decision client used by Yes/No. | "export type GateDecisionStatus" | dashboard/src/data/actions.ts:7-7 |
| Hosted session identity and delivery helpers. | "export interface OpenSession" | dashboard/src/data/sessions.ts:29-29 |
| External inbox helper used when no hosted session is attached. | "export interface OperatorInboxPostRequest" | dashboard/src/data/operatorInbox.ts:4-4 |
| Request/status formatting helpers extracted from this component. | "export function humanKey" | dashboard/src/panels/GateResponderText.ts:20-20 |
| Canonical lifecycle detail surface that renders this only when a durable gate exists. | "export const DetailPanel" | dashboard/src/panels/detail-panel/DetailPanel.tsx:75-75 |
| Engine Room diagnostics secondary surface. | "export function DiagnosticsPanel" | dashboard/src/panels/engine-room/DiagnosticsPanel.tsx:40-40 |
| Hangar secondary surface for worktree-bound gates. | "export function Hangar" | dashboard/src/panels/Hangar.tsx:72-72 |
| Projection gate and lifecycle shapes. | "export interface GateNode" | dashboard/src/types/projection.ts:231-231 |

### 260713-PHA-L5 Adapter Interaction Context

Gate responses render adapter-owned interaction prompt, choices, and identity, and submit the chosen
response through the durable gate path. Completion or acceptance does not consume an inbox row.

## Current L5I Maintenance

A reopened hosted-interaction gate can carry `packet.adapterDecisionFailure`. This renderer now
shows the prior decision/note, the proven delivery certainty, and its reason before offering a
fresh response. It distinguishes `not-sent` (safe to decide again) from `unknown` (the harness may
already hold the decision) and preserves unfamiliar wire values verbatim rather than guessing.

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-24T13:17:17Z — Curator: corrected the reopened-gate contract to surface the failed prior
  delivery with evidence-bounded copy; verification fields remain pre-commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: refreshed adapter interaction rendering and response boundary.

- 2026-07-02T16:18+02:00 — L8: removed the message-only `Chat` mode and its textarea/send path from
  the gate responder. The component still records explicit approve/reject/cancel decisions and notifies
  the agent after successful approve/reject; non-decision conversation now belongs in the adjacent leaf
  chat.
- 2026-06-25T13:10+02:00 — Task 23/24: added Dismiss/cancel, close-on-success response behavior, and extracted request/status formatting to `GateResponderText.ts`.
- 2026-06-25T07:17+02:00 — Task 19: split Gate Respond into durable decision paths (`Yes` approves, `No` rejects with required reason) and message-only `Chat`, added targeted stale-gate handling, rendered gate requests as human-readable previews with diagnostics JSON collapsed, and added the 480px resizable request panel. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: Gate Respond now queues a developer response in the external operator inbox when `findSessionForLifecycle` finds no hosted chat, and exposes queued/error status text instead of disabling the response path. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T13:45+02:00 — Created for Task 11: shared chat-routed Gate Respond control with
  Yes/No/Chat modes, full request display, hosted-session lookup by lifecycle id, missing-session
  status, and active untagged chat attach.
