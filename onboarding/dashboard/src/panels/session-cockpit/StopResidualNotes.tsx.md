# dashboard/src/panels/session-cockpit/StopResidualNotes.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/StopResidualNotes.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **stop-residual rendering** (260715-FEUI-L6 R5): `controlStopDetail` (kept from a terminate
response) and `retireControlStopError` (swept off retired catalog rows) are INFORMATIONAL facts
about sessions that terminated/retired SUCCESSFULLY — e.g. "control command queue is stopped"
from a startup-failed bridge whose graceful stop had nothing to talk to. They render on the STAGE
as dismissable `role="status"` lines (the terminated row itself is a tombstone the rail no longer
shows, so the residual must outlive the row), never as a "termination failed" state, never
silently discarded.

## Code Commentary

### Logic

- **Store-fed** (L41-L44): reads `residuals` from `useLifecycleNotices`
  (`data/sessionLifecycle`'s dedicated notice store — deliberately NOT `perSession`: the
  residual outlives the tombstoned row); renders nothing at zero residuals.
- **Note anatomy** (L45-L70): one bordered `role="status"` line per residual, keyed
  `sessionId-at`; copy comes from the centralized module (`terminateResidualCopy` /
  `retireResidualCopy` by `residual.kind` — both carry "(informational)"); the ✕ dismiss calls
  `dismissResidual(sessionId, at)` — a dismissal sticks across poll beats (the sweep's dedup
  set), and only a reload deliberately resurfaces it (the catalog row carries the fact forever).

### Invariants And Boundaries

- Presentation-only: no store writes beyond dismiss, no fetches; capture lives in the data layer
  (the focus-independent retire sweep — review finding 1 — and the terminate flow).
- The word "fail" must never appear in residual copy (test-asserted across the suites); failure
  states have their OWN surface (the rail's end-failure alert).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The store read, note anatomy, dismiss wiring. | L41-L72 | [StopResidualNotes.tsx](StopResidualNotes.tsx) |
| The notice store + capture paths (terminate detail, retire sweep, dedup). | L21-L118 | [../../data/sessionLifecycle.ts](../../data/sessionLifecycle.ts) |
| The centralized informational copy. | L20-L32 | [lifecycleCopy.ts](lifecycleCopy.ts) |
| The view mounting the notes at the top of the stage body. | L628 | [SessionsView.tsx](SessionsView.tsx) |
| The inspector's sibling rendering for a retired row's stop note. | L105-L111 | [SeatInspector.tsx](SeatInspector.tsx) |
| View-level residual cases (role="status", "informational", no "fail"). | — | [SessionsView.test.tsx](SessionsView.test.tsx) |

## Update History

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R5: the dismissable informational
  `role="status"` residual lines on the stage — terminate `controlStopDetail` and swept
  `retireControlStopError` rendered from the dedicated lifecycle notice store (residuals outlive
  tombstoned rows), copy centralized and never styled as failure, dismissals durable across poll
  beats. Verification metadata pinned to the leaf base until closeout stamps the L6 code commit.
