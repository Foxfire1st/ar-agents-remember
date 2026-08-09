# dashboard/src/data/actions.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/actions.ts`                  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `fb0296562ceb29929a3675a1b0195700d23bc56a`       |
| lastVerifiedCommitDate | 2026-08-09T20:35:49+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The serving route this POSTs to (records the developer/dashboard gate decision). | "def _gate_decision_response(" | mcp/src/agents_remember/serving/_app_routes.py:242-242 |
| The gate responder that calls `postGateDecision` and maps failure outcomes into rendered status. | `GateResponder` | dashboard/src/panels/GateResponder.tsx:720-780 |
| The attention queue that calls `postAttentionDismiss`. | `AttentionQueueImpl` | dashboard/src/panels/AttentionQueue.tsx:271-323 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-09T00:00+02:00 — 260713-TES-L5F2 reference correction: interaction answers no longer
  consume this gate-action client; removed the obsolete cross-reference.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T11:35:04+02:00 — 260731-EFA-L6 S18-B10 curator: source-first semantic citation curation; repaired this card's scoped citation findings with frozen-source evidence and corrected stale or pooled claims where needed.

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 4 citation entries (8 findings); no Tier-3 findings.

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
