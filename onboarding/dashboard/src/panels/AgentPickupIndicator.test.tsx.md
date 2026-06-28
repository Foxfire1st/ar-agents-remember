# dashboard/src/panels/AgentPickupIndicator.test.tsx

| Field                  | Value                                                 |
| ---------------------- | ----------------------------------------------------- |
| repository             | agents-remember                                      |
| path                   | `dashboard/src/panels/AgentPickupIndicator.test.tsx` |
| doc_type               | `file-level-onboarding`                              |
| lastUpdated            | 2026-06-25T13:20+02:00                               |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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
without pretending the agent consumed the inbox entry.

## Invariants And Boundaries

- The component only reflects server projection state; tests do not synthesize local TTLs.
- Dismiss coverage asserts deletion of the pending inbox warning, not agent pickup.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Component under test. | [AgentPickupIndicator.tsx](AgentPickupIndicator.tsx) |
| Client helper mocked by the dismiss test. | [operatorInbox.ts](../data/operatorInbox.ts) |

## Update History

- 2026-06-25T13:20+02:00 — Created for task 23/24 coverage of waiting-for-agent and dismissible check-chat task-row feedback.
