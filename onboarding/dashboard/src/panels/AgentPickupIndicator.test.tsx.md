# dashboard/src/panels/AgentPickupIndicator.test.tsx

| Field                  | Value                                                 |
| ---------------------- | ----------------------------------------------------- |
| repository             | agents-remember                                      |
| path                   | `dashboard/src/panels/AgentPickupIndicator.test.tsx` |
| doc_type               | `file-level-onboarding`                              |
| lastUpdated            | 2026-07-12T17:50 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                        |

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest coverage for the task-row agent-pickup feedback component.

## Code Commentary

The tests render `AgentPickupIndicator` in pending and overdue backend-projected states. They prove delivery/acknowledgment wording is static, no inline generation animation remains, and overdue `check-chat` still calls `dismissOperatorInboxEntry(entryId)` without pretending the agent consumed the inbox entry. Fixture rows include `messageKind` and `deliveryState` so the test shape stays aligned with the backend projection.

## Invariants And Boundaries

- The component only reflects server projection state; tests do not synthesize local TTLs.
- Dismiss coverage asserts deletion of the pending inbox warning, not agent pickup.
- Pickup acknowledgment is tested independently from the chat activity indicator.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Component under test. | `AgentPickupIndicator` | dashboard/src/panels/AgentPickupIndicator.tsx:42-83 |
| Client helper mocked by the dismiss test. | `dismissOperatorInboxEntry` | dashboard/src/data/operatorInbox.ts:34-48 |

## Update History

- 2026-08-03T02:36+02:00 — W3-B01 curator: curated 2 Repo-Internal table citations with exact component and dismissal-helper anchors. Verification metadata remains unchanged for closeout.

- 2026-07-12T17:50 — 260712-TRH-L6: refreshed coverage for static delivery/acknowledgment wording and the no-spinner contract; metadata is pinned to the current code HEAD until closeout.
- 2026-07-04T12:31+02:00 - L3: updated pickup fixtures with message-kind and
  delivery-state fields from the expanded projection contract. Verification
  metadata pinned until closeout stamps the L3 commit.
- 2026-06-25T13:20+02:00 — Created for task 23/24 coverage of waiting-for-agent and dismissible check-chat task-row feedback.
