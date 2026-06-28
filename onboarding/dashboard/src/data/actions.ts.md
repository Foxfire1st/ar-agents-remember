# dashboard/src/data/actions.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/actions.ts`                  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-28T03:05+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The dashboard's **action POST client**: `postGateDecision` POSTs a targeted gate decision to the
serving layer's `POST /api/actions/{verb}`, and `postAttentionDismiss` POSTs lifecycle-bound attention
dismissals to `POST /api/actions/dismiss`. The read-only zustand store stays read-only; these are
fire-and-report actions, not optimistic local state.

## Code Commentary

### Logic

`postGateDecision(lifecycleId, verb, options)` `fetch`es `POST /api/actions/{verb}` with a JSON
body containing `{ target: lifecycleId, gateId?, note? }` when a lifecycle id is present, or
`{ gateId, note? }` for gate-id-only cancel cleanup. It maps the HTTP outcome to a
`GateDecisionStatus`:
`202` → `recorded`; `409 {"status":"stale-gate"}` → `stale-gate`; other `409` → `no-open-gate`;
anything else → `error`; a network throw is caught → `error`. No retry, no optimistic state — callers
render the returned status honestly.

`postAttentionDismiss(item)` sends `{itemId, kind, target?, gateId?}` to `/api/actions/dismiss`.
The caller only uses it for lifecycle-bound attention rows or gate-open rows; `target` is omitted when
`lifecycleId` is null, preserving the gate-id-only cleanup path. It maps `202` to `dismissed`, anything
else or a network throw to `error`.

### Invariants And Boundaries

Same-origin POST (the dashboard is served by the FastAPI app that owns `/api/actions`). The UI never
decides safety — the gate's state, lifecycle-scoped acknowledgement rules, and server-side closeout
enforcement are the boundary; this helper only transports the request. Never reports a fake "sent":
only `202` reads as successful.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The serving route this POSTs to (records the developer/dashboard gate decision). | — | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The drawer that calls this + renders the status. | — | [panels/DetailPanel.tsx](../panels/DetailPanel.tsx) |
| The attention queue that calls `postAttentionDismiss`. | — | [panels/AttentionQueue.tsx](../panels/AttentionQueue.tsx) |

## Update History

- 2026-06-28T03:05+02:00 — Task 28 S5.2: added/updated `postAttentionDismiss` semantics for lifecycle-scoped attention acknowledgements and gate-open consumption through `/api/actions/dismiss`. Verification metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: `postGateDecision` now accepts a null lifecycle id and omits `target`, used by attention Clear to cancel stale gate-only rows.
- 2026-06-25T07:17+02:00 — Task 19: `postGateDecision` now accepts `gateId` and optional `note`, sends them in the action body, and distinguishes stale-gate 409 responses from no-open-gate. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-18T15:00 — Created for task 6 slice 6c Part B: `postGateDecision` — the dashboard's first write path (POST a gate decision to `/api/actions`, honest status mapping). Verification metadata pinned to the task base until closeout stamps the 6c Part B code commit.
