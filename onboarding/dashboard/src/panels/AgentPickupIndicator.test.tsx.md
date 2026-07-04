# dashboard/src/panels/AgentPickupIndicator.test.tsx

| Field                  | Value                                                 |
| ---------------------- | ----------------------------------------------------- |
| repository             | agents-remember                                      |
| path                   | `dashboard/src/panels/AgentPickupIndicator.test.tsx` |
| doc_type               | `file-level-onboarding`                              |
| lastUpdated            | 2026-07-04T12:31+02:00                               |
| lastVerifiedCommitHash | `6b940141fc319f1d2d18b2c94fd9e9a213d43141`|
| lastVerifiedCommitDate | 2026-07-04T12:52:03+02:00|
| governingOverview      | `overview.md`                                        |

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest coverage for the task-row agent-pickup feedback component.

## Code Commentary

The tests render `AgentPickupIndicator` in both backend-projected states. The fresh
`waiting-for-agent` case proves the spinner/status renders without a dismissal
action. The stale `check-chat` case proves the warning renders an `x` control and
calls `dismissOperatorInboxEntry(entryId)` so the developer can remove the warning
without pretending the agent consumed the inbox entry. L3 fixture rows include
`messageKind` and `deliveryState` so the test shape stays aligned with the
backend projection.

## Invariants And Boundaries

- The component only reflects server projection state; tests do not synthesize local TTLs.
- Dismiss coverage asserts deletion of the pending inbox warning, not agent pickup.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Component under test. | [AgentPickupIndicator.tsx](AgentPickupIndicator.tsx) |
| Client helper mocked by the dismiss test. | [operatorInbox.ts](../data/operatorInbox.ts) |

## Update History

- 2026-07-04T12:31+02:00 - L3: updated pickup fixtures with message-kind and
  delivery-state fields from the expanded projection contract. Verification
  metadata pinned until closeout stamps the L3 commit.
- 2026-06-25T13:20+02:00 — Created for task 23/24 coverage of waiting-for-agent and dismissible check-chat task-row feedback.
