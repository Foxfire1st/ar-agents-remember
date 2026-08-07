# dashboard/src/panels/session-cockpit/sessions-view/lifecycle.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/lifecycle.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The lifecycle/session suite split from `SessionsView.test.tsx` by the
260731-EFA-L8 test split. Pins the S5 legacy-duty parity, smart-default focus +
handoff + session cycling (L2 R9/F17), and authoritative landed cleanup through rail
and palette callers (F5-S5-2).

## Code Commentary

### Logic

Seeds legacy/ready sessions via `test-utils.tsx` and asserts duty parity, focus
handoff, cycling, and the cleanup callers' authority.

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
| The lifecycle suite. | `describe` | dashboard/src/panels/session-cockpit/sessions-view/lifecycle.test.tsx:34-280 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  lifecycle suite split from `SessionsView.test.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
