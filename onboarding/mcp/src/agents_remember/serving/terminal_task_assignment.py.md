# mcp/src/agents_remember/serving/terminal_task_assignment.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Assigns an existing hosted terminal to a canonical task document and role while enforcing singular
seat occupancy. It replaces leaf-only terminal assignment and sprint-role binding with one
level-neutral operation.

## Code Commentary

### Logic

Conflict helpers identify the current or replacement occupant of a document+role seat.
`task_binding_conflict_owner` re-evaluates after publishing a dead preferred generation as exited,
so a live staged heir becomes the conflict instead of the seat being misreported vacant.
`assign_terminal_session_to_task` holds one catalog batch across lookup, role/topology/lineage
validation, incumbent and staged-replacement conflict checks, and binding publication. Relationship
authorization belongs at the structural application boundary, before this assignment primitive is
called.

### Conventions

Assignment accepts a real `TaskDocumentRef`; caller-specific parsing belongs at the API/tool edge.

### Invariants And Boundaries

- One live occupant per singular structural seat.
- Assignment never invents sprint/master anchor leaves.
- A conflict reports structural ownership and does not silently evict another seat.
- Dead-incumbent cleanup is followed by fresh canonical-seat selection before vacancy is returned.
- Conflict re-evaluation and binding publication share one catalog transaction.

### Todos

None.

## Evidence

### Docs References


### Repo-Internal References

- Conflict checks reselect after marking a dead preferred generation exited. [1]
- Assignment holds one catalog batch across validation, conflict checks, and publication. [2]

### Cross-Repo References


## L23 Assignment Admission

Assigning an existing terminal to a structural task now proves task-derived
source lineage before catalog mutation or seat attachment. A stale/unavailable
projection returns the prior binding, requested role, detail, and evidence so
replacement-safe routing does not depend on agent-held ids.
