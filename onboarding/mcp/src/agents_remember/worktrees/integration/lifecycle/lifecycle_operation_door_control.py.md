# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_door_control.py

## Governing Overview

[Worktree-integration overview](../overview.md)

## Purpose

Implements retained door-publication intent and evidence helpers. Current ordinary closeout runs synchronously without applying this journal route.

## Code Commentary

The retained record helper handles the door-intent fields of closeout and direct-landing shapes. A door-bearing direct record is historical and offers no current journal controls. An unfinished intent must settle
before another is accepted. Publication re-reads configured authority, then publishes the door
generation into the contract's own door journal (`<worktree_group>/reports/closeout-door.json`) before
downstream projections are refreshed.

Under CCR-R03@v1 `record_door_intent` rebinds the updated record's typed dependency declaration
(`lifecycle_operation_dependencies`) after the new door publication intent is attached, so the
journaled operation content-addresses the exact admitted door generation it now reads
cit:([`record_door_intent`], mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_door_control.py:36-54).

## Invariants And Boundaries

- Door intent/proof survives queue invalidation and enclosure-local retries.
- Projection refresh is downstream and may not weaken accepted canonical publication.
- No second evidence reader or successor-intent compatibility WAL is permitted.
- Every door-intent mutation recomputes the record's declared dependency set before persistence.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

Door-intent control has no external authority.

### Repo-Internal References

- Door intent is recorded on the journaled operation and its dependency declaration is rebound. [1]
- The operation dependency vocabulary this seam uses. [2]
