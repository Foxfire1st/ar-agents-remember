# dashboard/src/data/actions.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/actions.ts`                  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview | `overview.md` |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The serving route this POSTs to (records the developer/dashboard gate decision). | — | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The drawer that calls this + renders the status. | — | [panels/DetailPanel.tsx](../panels/DetailPanel.tsx) |
| The attention queue that calls `postAttentionDismiss`. | — | [panels/AttentionQueue.tsx](../panels/AttentionQueue.tsx) |
| The interaction answer path riding `postGateDecisionDetailed` (approve + note). | L119-L129 | [interactionAnswer.ts](interactionAnswer.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (R4): added `postGateDecisionDetailed` — the additive
  gate-decision POST variant that keeps the server's words (body / HTTP status / network error)
  for the cockpit's verbatim-error + retry surfaces (the InteractionBar answer path); existing
  helpers untouched. Verification metadata pinned to the leaf base until closeout stamps the L6
  code commit.
- 2026-06-28T03:05+02:00 — Task 28 S5.2: added/updated `postAttentionDismiss` semantics for lifecycle-scoped attention acknowledgements and gate-open consumption through `/api/actions/dismiss`. Verification metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: `postGateDecision` now accepts a null lifecycle id and omits `target`, used by attention Clear to cancel stale gate-only rows.
- 2026-06-25T07:17+02:00 — Task 19: `postGateDecision` now accepts `gateId` and optional `note`, sends them in the action body, and distinguishes stale-gate 409 responses from no-open-gate. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-18T15:00 — Created for task 6 slice 6c Part B: `postGateDecision` — the dashboard's first write path (POST a gate decision to `/api/actions`, honest status mapping). Verification metadata pinned to the task base until closeout stamps the 6c Part B code commit.
