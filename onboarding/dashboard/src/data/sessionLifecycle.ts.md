# dashboard/src/data/sessionLifecycle.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionLifecycle.ts`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                   |

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
| The notice store and residual sweep. | `lifecycleNoticeStore`; `sweepRetireResiduals`; `startRetireResidualSweep`; "for (const session of sessions)"; "if (!changed)" | dashboard/src/data/sessionLifecycle.ts:61-61; dashboard/src/data/sessionLifecycle.ts:68-121; dashboard/src/data/sessionLifecycle.ts:136-154 |
| The detailed terminate and bulk-end flows preserve server outcomes. | `terminateSessionDetailed`; `endSessionDetailed`; `endLandedDetailed` | dashboard/src/data/sessionLifecycle.ts:169-197; dashboard/src/data/sessionLifecycle.ts:203-224; dashboard/src/data/sessionLifecycle.ts:230-251 |
| The centralized terminate confirmation copy. | `terminateConfirmCopy` | dashboard/src/panels/session-cockpit/lifecycleCopy.ts:13-22 |
| The stage renderer of residual notices (dismissable `role="status"` lines). | `StopResidualNotes` | dashboard/src/panels/session-cockpit/StopResidualNotes.tsx:41-72 |
| The rail consumers keep immediate single End and confirmed bulk End. | `endSession`; `endLanded`; `SessionRail` | dashboard/src/panels/session-cockpit/SessionRail.tsx:33-35; dashboard/src/panels/session-cockpit/SessionRail.tsx:39-43; dashboard/src/panels/session-cockpit/SessionRail.tsx:155-235 |
| The cleanup outcome notice is rendered by the dedicated landed-cleanup component. | `LandedCleanupNotice` | dashboard/src/panels/session-cockpit/LandedCleanupNotice.tsx:48-113 |
| The view mounts the focus-independent sweep. | "useEffect(() => startRetireResidualSweep()" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:812-812 |
| `terminateTerminalSession` is the boolean-only predecessor. | `terminateTerminalSession` | dashboard/src/data/terminal.ts:442-451 |
| `subscribeSessionCatalogChanges` registers catalog-change listeners. | `subscribeSessionCatalogChanges` | dashboard/src/data/sessions.ts:128-138 |
| The focused `endLandedDetailed (bulk cleanup honesty)` test covers the landed cleanup path. | "endLandedDetailed (bulk cleanup honesty)" | dashboard/src/data/sessionLifecycle.test.ts:146-213 |

## FEUI-L8 Reviewed Candidate Delta

Adds `cleanupFailure` alongside authoritative cleanup outcomes. When no result is available, the exact action-boundary target snapshot remains visible and retryable; a real outcome replaces failure, and neither state fabricates success.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: split the duplicated lifecycle source row by
  owner, completed the residual-sweep body audit, narrowed negative/over-pooled reference claims,
  and updated rail cleanup references from the retired residual-note path to `LandedCleanupNotice`.

- 2026-08-02T16:56+02:00 — 260731-EFA-L6 curator W1-B06: anchored 12 citation claims
  (4 Logic citations and 8 Repo-Internal reference rows); scoped result 0 findings.

- 2026-07-24T13:17:50Z — Added termination-time conversation disconnect ownership. Verification
  hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R5 (incl. fix round 1 findings 1 and 4):
  the lifecycle notice store (stop residuals that outlive tombstoned rows, dismissal that sticks
  via the swept-set), the refcounted focus-independent retire-residual sweep, and the detailed
  terminate/landed-cleanup flows keeping `controlStopDetail`, verbatim POST failures, and the
  route's own closed+skipped outcome. Retire is render-only from the cockpit (no actor seat) —
  the operator action is terminate. Verification metadata pinned to the leaf base until closeout
  stamps the L6 code commit.
