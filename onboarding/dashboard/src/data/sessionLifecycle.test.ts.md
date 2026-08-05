# dashboard/src/data/sessionLifecycle.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionLifecycle.test.ts`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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
| The module under test. | `startRetireResidualSweep` | dashboard/src/data/sessionLifecycle.ts:136-154 |
| The centralized copy the honesty cases pin. | `terminateConfirmCopy` | dashboard/src/panels/session-cockpit/lifecycleCopy.ts:14-23 |
| The L6 fixtures driven through the real store. | `L6_CONTROLLED_WORKING` | dashboard/src/test/fixtures/catalogRows.ts:179-191 |
| The view-level companions (unfocused-residual render, rail End/error-row cases). | "renders the scope root + rail/stage/inspector with markers and zones (F-c: no statusline region)" | dashboard/src/panels/session-cockpit/SessionsView.test.tsx:164-206 |

## FEUI-L8 Reviewed Candidate Delta

Adds unavailable landed-cleanup authority coverage: exact intended `{id,label}` targets survive network loss, cleanup outcome remains absent, and copy names every retry target.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations after the file
  grew a header comment, a `beforeEach`/`afterEach` block, and the landed-cleanup
  authority-unavailable case. `terminateSessionDetailed` L34-L72 -> L40-L84 (the range now reaches
  the verbatim-failed-POST case it describes), `endSessionDetailed` L106-L128 -> L120-L144, and
  `endLandedDetailed` L130-L164 -> L146-L213 (both suites shifted down and the latter now holds
  two cases). Claims themselves re-verified and unchanged.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R5/R9 (incl. fix round 1 findings 1 and 4):
  residual kept from the terminate body, clean-terminate no-residual, verbatim failed-POST words,
  the focus-independent sweep (capture-once across beats, dismissal persistence, reload path),
  tombstone+notice flow, bulk-cleanup closed+skipped honesty, and the informational-copy rules
  (confirm names session · leaf · state; "fail" never appears). Verification metadata pinned to
  the leaf base until closeout stamps the L6 code commit.
