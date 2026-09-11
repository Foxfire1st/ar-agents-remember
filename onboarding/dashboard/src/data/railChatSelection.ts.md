# dashboard/src/data/railChatSelection.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/railChatSelection.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T07:35+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Owns role ordering, topology-aware seat validation, and live session selection for the Chats rail.

## Code Commentary

### Logic

`useRailChatSessions` resolves the selected task altitude, filters live sessions by exact task
identity, rejects reviewer generations with the wrong structural parent, and returns the relevant
leaf, master, or sprint seat set. Free chats remain selected by runtime session role.

### Conventions

Role order is explicit per altitude. Reviewer validity is delegated to `reviewerContext.ts` so rail
placement and display share one parent contract.

### Invariants And Boundaries

- Leaf, master, and sprint seats never share one reviewer-parent rule.
- Sprint reviewer is visible but not created through the generic missing-role starter.
- A working leaf role wins before stable role and session-id tie breaks.
- Unbound free chats remain outside task topology.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Role sets and creation boundaries are explicit by altitude. | `SPRINT_ROLE_ORDER`; `CREATABLE_SPRINT_ROLES`; `MASTER_ROLE_ORDER` | dashboard/src/data/railChatSelection.ts:15-25 |
| Reviewer generations are parent-validated before seat selection. | `reviewerIsValid`; `roleSeats` | dashboard/src/data/railChatSelection.ts:60-117 |
| The hook returns topology-specific seats and free-chat state. | `useRailChatSessions` | dashboard/src/data/railChatSelection.ts:119-169 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-31T07:35+02:00 — Created for 260821-ARSPAWN-L5 independent-review repair. Verification remains closeout-owned.
