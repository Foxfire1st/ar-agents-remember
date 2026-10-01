# dashboard/src/data/sessionLifecycle.ts

## Governing Overview

[data overview](overview.md)

## Purpose

**Session lifecycle actions for the cockpit** (260715-FEUI-L6 R5): terminate/bulk-end flows that
keep the server's WHOLE answer instead of a bare boolean, plus the notice store for STOP
RESIDUALS. A `/terminate` response may carry `controlStopDetail` (the graceful control stop
failed on an already-dead bridge — e.g. "control command queue is stopped"): that is an
INFORMATIONAL fact about a session that terminated SUCCESSFULLY — never a "termination failed"
state, never discarded. Residuals live here (not on `perSession`) because the terminated row
becomes a tombstone the rail drops — the residual must outlive the row (worker decision 4).
**Retire note:** `POST /api/terminal/{id}/retire` requires an authorized ACTOR SESSION
(manager/orchestrator seat); the dashboard has no seat identity, so the cockpit's operator action
is terminate and retirement happens agent-side — the cockpit still RENDERS retire residuals
(`controlRaw.retireControlStopError`) with the same informational posture (reviewer-confirmed
against the retire route's authority checks).

## Code Commentary

### Logic

- **`lifecycleNoticeStore`** (cit:([`lifecycleNoticeStore`], dashboard/src/data/sessionLifecycle.ts:68-121)): newest-first `residuals: StopResidual[]`
  (`{sessionId, label, kind: terminate|retire, detail, at}` — detail is the server's words,
  verbatim), kept until explicitly dismissed; `cleanupOutcome` — the last bulk-cleanup result
  (closed/skipped honesty), null when none/dismissed; `sweptRetire` — sessionIds whose retire
  residual was already captured, so a dismissal STAYS dismissed across poll beats (the catalog
  row carries the fact forever). cit:([`sweepRetireResiduals`; "for (const session of sessions)"; "if (!changed)"; "residuals = [...residuals]"; "sweptRetire[session.id] = true"], dashboard/src/data/sessionLifecycle.ts:61-61; dashboard/src/data/sessionLifecycle.ts:87-87; dashboard/src/data/sessionLifecycle.ts:95-96; dashboard/src/data/sessionLifecycle.ts:110-110) captures
  `controlRaw.retireControlStopError` for EVERY row, once per sessionId, with copy-on-write only
  when something actually changes.
- **`startRetireResidualSweep()`** (cit:([`startRetireResidualSweep`], dashboard/src/data/sessionLifecycle.ts:136-154), review F1 sev-3 fix): the refcounted,
  FOCUS-INDEPENDENT capture path. Retired rows tombstone out of the rail, so a focused-handoff
  capture silently dropped unfocused retirements (and reloads); this subscription sweeps every
  `sessionStore` change (poll hydrates AND direct patches) and sweeps rows already present at
  subscribe time (the reload path — the catalog serves retired rows forever). Release is
  idempotent (`released` flag); refs 0 unsubscribes and nulls the handle — StrictMode
  double-mount safe, with dedup living in the STORE, not module state.
- **`terminateSessionDetailed(sessionId)`** (cit:([`terminateSessionDetailed`], dashboard/src/data/sessionLifecycle.ts:169-197)): the terminate POST keeping the body —
  `{ok:true, controlStopDetail?}` on success; on failure `{ok:false, error}` with the server's
  words verbatim (response body or `HTTP <status>` or the network error message — review finding
  4: a failed POST is never silent). Deliberately duplicates the POST instead of calling
  `terminateTerminalSession` (the boolean-only helper drops the body; untouched for Chats).
- **`endSessionDetailed(session)`** (cit:([`endSessionDetailed`], dashboard/src/data/sessionLifecycle.ts:203-224)): the cockpit terminate flow — POST, then mirror
  the store (`setStatus("terminated")` + `close` + `notifySessionCatalogChanged`), then record
  any stop residual for the informational surfaces. A failed POST returns early: no tombstone, no
  fake state.
- **`endLandedDetailed(sessions)`** (cit:([`endLandedDetailed`], dashboard/src/data/sessionLifecycle.ts:230-251)): bulk-end via the landed-cleanup route, keeping
  the route's OWN outcome (closed + skipped WITH reasons) in `cleanupOutcome` instead of dropping
  the skips; closes the closed rows locally and re-hydrates excluding them.

### Invariants And Boundaries

- Residual copy is informational by construction — rendering goes through `lifecycleCopy`'s
  `terminateResidualCopy`/`retireResidualCopy` and tests assert the word "fail" never appears.
- Residuals/outcomes are never auto-dropped; only an explicit dismiss removes them, and a
  dismissed retire residual never resurrects within the JS session (`sweptRetire`). A reload
  deliberately resurfaces undismissed retire residuals — the catalog row still carries the fact.
- Store state is in-memory: reload persistence is the catalog row itself, not this store.

### 2026-07-24 Curator Delta

Successful terminate and landed cleanup now explicitly disconnect the active conversation runtime.
Focus changes keep healthy projections warm, but a terminated seat must not retain its SSE runtime until
later LRU pressure.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The notice store and residual sweep. [1]
- The detailed terminate and bulk-end flows preserve server outcomes. [2]
- The centralized terminate confirmation copy. [3]
- The stage renderer of residual notices (dismissable `role="status"` lines). [4]
- The rail consumers keep immediate single End and confirmed bulk End. [5]
- The cleanup outcome notice is rendered by the dedicated landed-cleanup component. [6]
- The view mounts the focus-independent sweep. [7]
- `terminateTerminalSession` is the boolean-only predecessor. [8]
- `subscribeSessionCatalogChanges` registers catalog-change listeners. [9]
- The focused `endLandedDetailed (bulk cleanup honesty)` test covers the landed cleanup path. [10]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

Adds `cleanupFailure` alongside authoritative cleanup outcomes. When no result is available, the exact action-boundary target snapshot remains visible and retryable; a real outcome replaces failure, and neither state fabricates success.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
