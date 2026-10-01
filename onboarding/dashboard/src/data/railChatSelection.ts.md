# dashboard/src/data/railChatSelection.ts

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

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Role sets and creation boundaries are explicit by altitude. [1]
- Reviewer generations are parent-validated before seat selection. [2]
- The hook returns topology-specific seats and free-chat state. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
