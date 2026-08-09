# dashboard/src/panels/session-cockpit/sessions-view/stopResiduals.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/stopResiduals.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-09T20:25+02:00                                      |
| lastVerifiedCommitHash | `fb0296562ceb29929a3675a1b0195700d23bc56a`                  |
| lastVerifiedCommitDate | 2026-08-09T20:35:49+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The stop-residual suite split from `SessionsView.test.tsx` by the 260731-EFA-L8 test
split. Pins the L6 stage InteractionBar and stop-residual behavior (informational
stop residuals outlive tombstoned rows).

## Code Commentary

### Logic

Seeds terminal sessions and covers two independent boundaries: a focused lifecycle-free pending
answer posts once to the exact session interaction-response route without using `/submit`, while a
stopped seat retains its informational residual after the row is tombstoned.

### Invariants And Boundaries

Assertions preserved from the monolithic suite.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused composer proves lifecycle-free exact-session routing and duplicate-send locking. | "routes the focused lifecycle-free composer answer once by exact session" | dashboard/src/panels/session-cockpit/sessions-view/stopResiduals.test.tsx:72-136 |
| The stop-residual suite. | "L6: stage surface — InteractionBar and stop residuals" | dashboard/src/panels/session-cockpit/sessions-view/stopResiduals.test.tsx:49-183 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-09T20:25+02:00 — 260713-TES-L5F2: replaced the obsolete lifecycle-gate answer fixture
  with lifecycle-free exact-session response routing while preserving the stop-residual assertions.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  stop-residual suite split from `SessionsView.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
