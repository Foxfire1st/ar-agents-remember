# dashboard/src/data/sessionLifecycle.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The unit suite for the **cockpit lifecycle flows** (260715-FEUI-L6 R5): terminate keeps the stop
residual, bulk cleanup keeps the route's honest outcome, the retire-residual sweep captures
focus-independently, and residual copy is INFORMATIONAL — the word "fail" never appears. Runs
against the real `sessionStore` (hydrated from the L6 fixtures) with fetch stubbed per case;
`lifecycleNoticeStore` reset in `beforeEach`.

## Code Commentary

### Logic

- **`terminateSessionDetailed`** cit:(["keeps controlStopDetail from the terminate response instead of discarding the body"], dashboard/src/data/sessionLifecycle.test.ts:41-54): `controlStopDetail` kept from the response body
  (`L6_TERMINATE_RESPONSE_WITH_RESIDUAL`); a clean terminate carries no residual; a FAILED POST
  (502 + body) keeps the server's words verbatim — `{ok:false, error:"bridge host unavailable"}`
  (review finding 4 regression).
- **Retire-residual sweep (review F1, sev-3)** cit:(["captures retireControlStopError for an UNFOCUSED tombstoned row"], dashboard/src/data/sessionLifecycle.test.ts:87-108): hydrating an UNFOCUSED tombstoned row
  (`L6_RETIRED_WITH_STOP_ERROR`) captures the residual exactly once — repeated hydrates (the
  catalog serves the row every beat) never duplicate it, and a dismissal stays dismissed across
  later beats (the swept-set remembers). Rows already in the store when the sweep starts are
  captured too — the reload path cit:(["rows already in the store when the sweep starts are captured too (reload path)"], dashboard/src/data/sessionLifecycle.test.ts:110-117).
- **`endSessionDetailed`** cit:(["tombstones the row and records the stop residual as an informational notice"], dashboard/src/data/sessionLifecycle.test.ts:121-143): tombstones the row out of the store AND records the stop
  residual as an informational notice.
- **`endLandedDetailed`** cit:(["bulk cleanup honesty"], dashboard/src/data/sessionLifecycle.test.ts:146-213): records the route's own closed + skipped outcome — skips
  never vanish; `cleanupOutcomeCopy` renders `ended 1 · skipped 1 (landed-b: status:running)`.
- **Copy honesty** cit:(["lifecycleCopy honesty rules"], dashboard/src/data/sessionLifecycle.test.ts:215-234): the terminate confirm NAMES session · leaf · state (fixture
  label, `leaf 06_pty-stage-interactions-lifecycle`, `state working`); terminate AND retire
  residual copy contain "informational" + the verbatim detail, and `"fail"` never appears
  (case-insensitive).

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The module under test. [1]
- The centralized copy the honesty cases pin. [2]
- The L6 fixtures driven through the real store. [3]
- The view-level companions (unfocused-residual render, rail End/error-row cases). [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

Adds unavailable landed-cleanup authority coverage: exact intended `{id,label}` targets survive network loss, cleanup outcome remains absent, and copy names every retry target.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
