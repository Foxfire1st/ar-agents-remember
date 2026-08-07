# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/measurements.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/measurements.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The measurement constants and persisted-measurement cache of the Conversation
Timeline, extracted from `ConversationTimeline.tsx` by the 260731-EFA-L8 split. Owns
`OPERATOR_SCROLL_KEYS`, the premeasure limits, the measurement cache read/write, and
the restore drive bound.

## Code Commentary

### Logic

`readStoredMeasurements` / `storeMeasurements` persist per-cache-id row measurements
under the `cockpit.chats.measurements.v1:` prefix. `OPERATOR_SCROLL_KEYS` deliberately
excludes ArrowDown because the conversation surface hijacks it into the agents line.

### Conventions

Pure storage helpers; no DOM.

### Invariants And Boundaries

The scroll-key set is exported for the keyboard-contract tests; adding ArrowDown back
would break the surface contract.

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
| The measurement cache and constants. | `readStoredMeasurements`; `storeMeasurements`; `OPERATOR_SCROLL_KEYS` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/measurements.ts:34-90 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  measurements module extracted from `ConversationTimeline.tsx`. Verification pinned
  to the leaf base until closeout stamps the code commit.
