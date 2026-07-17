# dashboard/src/data/sessionLifecycle.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionLifecycle.ts`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

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

- **`lifecycleNoticeStore`** (L30-L86): newest-first `residuals: StopResidual[]`
  (`{sessionId, label, kind: terminate|retire, detail, at}` — detail is the server's words,
  verbatim), kept until explicitly dismissed; `cleanupOutcome` — the last bulk-cleanup result
  (closed/skipped honesty), null when none/dismissed; `sweptRetire` — sessionIds whose retire
  residual was already captured, so a dismissal STAYS dismissed across poll beats (the catalog
  row carries the fact forever). `sweepRetireResiduals(sessions)` (L57-L83) captures
  `controlRaw.retireControlStopError` for EVERY row, once per sessionId, with copy-on-write only
  when something actually changes.
- **`startRetireResidualSweep()`** (L97-L118, review F1 sev-3 fix): the refcounted,
  FOCUS-INDEPENDENT capture path. Retired rows tombstone out of the rail, so a focused-handoff
  capture silently dropped unfocused retirements (and reloads); this subscription sweeps every
  `sessionStore` change (poll hydrates AND direct patches) and sweeps rows already present at
  subscribe time (the reload path — the catalog serves retired rows forever). Release is
  idempotent (`released` flag); refs 0 unsubscribes and nulls the handle — StrictMode
  double-mount safe, with dedup living in the STORE, not module state.
- **`terminateSessionDetailed(sessionId)`** (L133-L150): the terminate POST keeping the body —
  `{ok:true, controlStopDetail?}` on success; on failure `{ok:false, error}` with the server's
  words verbatim (response body or `HTTP <status>` or the network error message — review finding
  4: a failed POST is never silent). Deliberately duplicates the POST instead of calling
  `terminateTerminalSession` (the boolean-only helper drops the body; untouched for Chats).
- **`endSessionDetailed(session)`** (L156-L172): the cockpit terminate flow — POST, then mirror
  the store (`setStatus("terminated")` + `close` + `notifySessionCatalogChanged`), then record
  any stop residual for the informational surfaces. A failed POST returns early: no tombstone, no
  fake state.
- **`endLandedDetailed(sessions)`** (L178-L191): bulk-end via the landed-cleanup route, keeping
  the route's OWN outcome (closed + skipped WITH reasons) in `cleanupOutcome` instead of dropping
  the skips; closes the closed rows locally and re-hydrates excluding them.

### Invariants And Boundaries

- Residual copy is informational by construction — rendering goes through `lifecycleCopy`'s
  `terminateResidualCopy`/`retireResidualCopy` and tests assert the word "fail" never appears.
- Residuals/outcomes are never auto-dropped; only an explicit dismiss removes them, and a
  dismissed retire residual never resurrects within the JS session (`sweptRetire`). A reload
  deliberately resurfaces undismissed retire residuals — the catalog row still carries the fact.
- Store state is in-memory: reload persistence is the catalog row itself, not this store.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Notice store, sweep, and the detailed terminate/bulk-end flows. | L21-L191 | [sessionLifecycle.ts](sessionLifecycle.ts) |
| The centralized residual/confirm copy (informational wording lives there). | L14-L47 | [../panels/session-cockpit/lifecycleCopy.ts](../panels/session-cockpit/lifecycleCopy.ts) |
| The stage renderer of residual notices (dismissable `role="status"` lines). | L42-L43 | [../panels/session-cockpit/StopResidualNotes.tsx](../panels/session-cockpit/StopResidualNotes.tsx) |
| The rail consumers: End arm→confirm→execute + the cleanup-outcome note. | L347-L355; L386-L427 | [../panels/session-cockpit/SessionRail.tsx](../panels/session-cockpit/SessionRail.tsx) |
| The view mounting the sweep (one effect; the focus-coupled capture was removed). | L229; L279 | [../panels/session-cockpit/SessionsView.tsx](../panels/session-cockpit/SessionsView.tsx) |
| The boolean-only predecessors this module deliberately does not reuse. | — | [terminal.ts](terminal.ts) |
| The registry the sweep subscribes to (hydrates keep the full list incl. terminated rows). | — | [sessions.ts](sessions.ts) |
| The unit suite: residual kept/clean/verbatim-failure, sweep capture-once + reload path, bulk outcome, copy honesty. | L34-L185 | [sessionLifecycle.test.ts](sessionLifecycle.test.ts) |

## Update History

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R5 (incl. fix round 1 findings 1 and 4):
  the lifecycle notice store (stop residuals that outlive tombstoned rows, dismissal that sticks
  via the swept-set), the refcounted focus-independent retire-residual sweep, and the detailed
  terminate/landed-cleanup flows keeping `controlStopDetail`, verbatim POST failures, and the
  route's own closed+skipped outcome. Retire is render-only from the cockpit (no actor seat) —
  the operator action is terminate. Verification metadata pinned to the leaf base until closeout
  stamps the L6 code commit.
