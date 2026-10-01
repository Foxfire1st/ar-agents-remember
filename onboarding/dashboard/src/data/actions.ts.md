# dashboard/src/data/actions.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The dashboard's **action POST client**: `postGateDecision` POSTs a targeted gate decision to the
serving layer's `POST /api/actions/{verb}`, `postGateDecisionDetailed` (260715-FEUI-L6) is the
same POST keeping the server's words for verbatim-error surfaces, and `postAttentionDismiss`
POSTs lifecycle-bound attention dismissals to `POST /api/actions/dismiss`. The read-only zustand
store stays read-only; these are fire-and-report actions, not optimistic local state.

## Code Commentary

### Logic

`postGateDecision(lifecycleId, verb, options)` `fetch`es `POST /api/actions/{verb}` with a JSON
body containing `{ target: lifecycleId, gateId?, note? }` when a lifecycle id is present, or
`{ gateId, note? }` for gate-id-only cancel cleanup. It maps the HTTP outcome to a
`GateDecisionStatus`:
`202` → `recorded`; `409 {"status":"stale-gate"}` → `stale-gate`; other `409` → `no-open-gate`;
anything else → `error`; a network throw is caught → `error`. No retry, no optimistic state — callers
render the returned status honestly.

`postGateDecisionDetailed(lifecycleId, verb, options)` (260715-FEUI-L6 R4, L40-L83) sends the
SAME body to the same route but returns `{status, detail?}` — `detail` carries the server's own
words (response body / `HTTP <status>` line / network error message) instead of collapsing
everything past 202 into a bare status. The 409 mapping (`stale-gate` vs `no-open-gate`) is
preserved WITH the raw body attached. Consumers are the verbatim-error + retry surfaces: the
InteractionBar's answer path renders POST failures in the server's words (design §7.3 F7). The
original `postGateDecision` is untouched for its existing callers.

`postAttentionDismiss(item)` sends `{itemId, kind, target?, gateId?}` to `/api/actions/dismiss`.
The caller only uses it for lifecycle-bound attention rows or gate-open rows; `target` is omitted when
`lifecycleId` is null, preserving the gate-id-only cleanup path. It maps `202` to `dismissed`, anything
else or a network throw to `error`.

### Invariants And Boundaries

Same-origin POST (the dashboard is served by the FastAPI app that owns `/api/actions`). The UI never
decides safety — the gate's state, lifecycle-scoped acknowledgement rules, and server-side closeout
enforcement are the boundary; this helper only transports the request. Never reports a fake "sent":
only `202` reads as successful.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The serving route this POSTs to (records the developer/dashboard gate decision). [1]
- The gate responder that calls `postGateDecision` and maps failure outcomes into rendered status. [2]
- The attention queue that calls `postAttentionDismiss`. [3]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
