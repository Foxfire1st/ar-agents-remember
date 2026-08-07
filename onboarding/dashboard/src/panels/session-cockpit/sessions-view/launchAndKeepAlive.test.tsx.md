# dashboard/src/panels/session-cockpit/sessions-view/launchAndKeepAlive.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/launchAndKeepAlive.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The launch-flow + keep-alive suite split from `SessionsView.test.tsx` by the
260731-EFA-L8 test split. Pins the L3 R5/R6 launch flow with the failed-launch
banner, and the B1 harness↔terminal contract that keeps the PTY stack alive through
focus handoffs.

## Code Commentary

### Logic

Seeds launch attempts and asserts the five-tier launch evidence and failed-launch
verbatim surfaces; then pins the keep-alive rule (the PTY layer stays mounted
through smart-focus handoff).

### Invariants And Boundaries

Assertions preserved from the monolithic suite; terminal ledgers come from
`test-utils.tsx`.

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
| The launch/keep-alive suite. | `describe` | dashboard/src/panels/session-cockpit/sessions-view/launchAndKeepAlive.test.tsx:40-200 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  launch/keep-alive suite split from `SessionsView.test.tsx`. Verification pinned to
  the leaf base until closeout stamps the code commit.
