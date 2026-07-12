# dashboard/src/panels/AgentPickupIndicator.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/AgentPickupIndicator.tsx`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-12T17:50 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`|
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

Task-row feedback for pending dashboard responses that have not yet been consumed by an agent.

## Governing Overview

[panels overview](overview.md)

## Code Commentary

Renders static inbox delivery/acknowledgment state for an `AgentPickupNode`. Fresh pending rows show a
bordered delivery marker and `brief unacknowledged` for dispatch briefs or `message unacknowledged` for
other messages. The exact `deliveryState` remains in the title; overdue `check-chat` rows keep the
dismiss action. There is no model-busy spinner, Motion dependency, generation inference, or second
poller. Dismiss calls `dismissOperatorInboxEntry(entryId)` and means developer-cleared warning, not
agent pickup.

## Invariants And Boundaries

- The component is driven by backend projection state, not local click memory.
- Dismiss means developer-cleared warning, not agent pickup.
- Inbox acknowledgment is independent from live hosted-chat `turnState`; an idle chat may sit beside a pending or overdue inbox row.

## Update History

- 2026-07-12T17:50 — 260712-TRH-L6: replaced the false generation spinner with static inbox delivery/acknowledgment wording and recorded the independent chat-activity axis. Reviewer F3 notes that queued/no-hosted-session rows are technically undelivered rather than unacknowledged; this remains a follow-up wording residual.
- 2026-06-25T13:10+02:00 — Created for task 23/24 waiting-for-agent/check-chat task-row feedback.
