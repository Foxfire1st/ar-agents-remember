# dashboard/src/data/sessionLifecycle.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionLifecycle.test.ts`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`       |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview      | `overview.md`                                   |

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

- **`terminateSessionDetailed`** (L34-L72): `controlStopDetail` kept from the response body
  (`L6_TERMINATE_RESPONSE_WITH_RESIDUAL`); a clean terminate carries no residual; a FAILED POST
  (502 + body) keeps the server's words verbatim — `{ok:false, error:"bridge host unavailable"}`
  (review finding 4 regression).
- **Retire-residual sweep (review F1, sev-3)** (L74-L104): hydrating an UNFOCUSED tombstoned row
  (`L6_RETIRED_WITH_STOP_ERROR`) captures the residual exactly once — repeated hydrates (the
  catalog serves the row every beat) never duplicate it, and a dismissal stays dismissed across
  later beats (the swept-set remembers). Rows already in the store when the sweep starts are
  captured too — the reload path (L98-L103).
- **`endSessionDetailed`** (L106-L128): tombstones the row out of the store AND records the stop
  residual as an informational notice.
- **`endLandedDetailed`** (L130-L164): records the route's own closed + skipped outcome — skips
  never vanish; `cleanupOutcomeCopy` renders `ended 1 · skipped 1 (landed-b: status:running)`.
- **Copy honesty** (L166-L185): the terminate confirm NAMES session · leaf · state (fixture
  label, `leaf 06_pty-stage-interactions-lifecycle`, `state working`); terminate AND retire
  residual copy contain "informational" + the verbatim detail, and `"fail"` never appears
  (case-insensitive).

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
| The module under test. | L21-L191 | [sessionLifecycle.ts](sessionLifecycle.ts) |
| The centralized copy the honesty cases pin. | L14-L47 | [../panels/session-cockpit/lifecycleCopy.ts](../panels/session-cockpit/lifecycleCopy.ts) |
| The L6 fixtures driven through the real store. | — | [../test/fixtures/catalogRows.ts](../test/fixtures/catalogRows.ts) |
| The view-level companions (unfocused-residual render, rail End/error-row cases). | — | [../panels/session-cockpit/SessionsView.test.tsx](../panels/session-cockpit/SessionsView.test.tsx) |

## FEUI-L8 Reviewed Candidate Delta

Adds unavailable landed-cleanup authority coverage: exact intended `{id,label}` targets survive network loss, cleanup outcome remains absent, and copy names every retry target.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R5/R9 (incl. fix round 1 findings 1 and 4):
  residual kept from the terminate body, clean-terminate no-residual, verbatim failed-POST words,
  the focus-independent sweep (capture-once across beats, dismissal persistence, reload path),
  tombstone+notice flow, bulk-cleanup closed+skipped honesty, and the informational-copy rules
  (confirm names session · leaf · state; "fail" never appears). Verification metadata pinned to
  the leaf base until closeout stamps the L6 code commit.
