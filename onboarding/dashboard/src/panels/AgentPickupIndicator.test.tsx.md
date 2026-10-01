# dashboard/src/panels/AgentPickupIndicator.test.tsx

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

## Evidence

### Repo-Internal References

- Component under test. [1]
- Client helper mocked by the dismiss test. [2]
