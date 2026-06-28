# dashboard/src/panels/AgentPickupIndicator.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/AgentPickupIndicator.tsx`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-25T13:10+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

Task-row feedback for pending dashboard responses that have not yet been consumed by an agent.

## Code Commentary

Renders a compact `waiting for agent` spinner for fresh `AgentPickupNode` records. When the backend
projects the node as `check-chat` after the 5-minute pickup TTL, it renders a compact warning with an
`x` button. The button calls `dismissOperatorInboxEntry(entryId)`, which physically deletes the pending
inbox entry through the dashboard serving endpoint; it does not mark the entry consumed by an agent.

## Invariants And Boundaries

- The component is driven by backend projection state, not local click memory.
- Dismiss means developer-cleared warning, not agent pickup.

## Update History

- 2026-06-25T13:10+02:00 — Created for task 23/24 waiting-for-agent/check-chat task-row feedback.
