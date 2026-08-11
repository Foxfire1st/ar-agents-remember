# mcp/src/agents_remember/serving/terminal_task_assignment.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/terminal_task_assignment.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T06:47+02:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Assigns an existing hosted terminal to a canonical task document and role while enforcing singular
seat occupancy. It replaces leaf-only terminal assignment and sprint-role binding with one
level-neutral operation.

## Code Commentary

### Logic

Conflict helpers identify the current or replacement occupant of a document+role seat.
`assign_terminal_session_to_task` validates task altitude and uniqueness, then persists the binding
and emits the updated catalog result. Relationship authorization belongs at the structural
application boundary, before this assignment primitive is called.

### Conventions

Assignment accepts a real `TaskDocumentRef`; caller-specific parsing belongs at the API/tool edge.

### Invariants And Boundaries

- One live occupant per singular structural seat.
- Assignment never invents sprint/master anchor leaves.
- A conflict reports structural ownership and does not silently evict another seat.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Conflict checks use document+role occupancy. | `task_binding_conflict_owner` | mcp/src/agents_remember/serving/terminal_task_assignment.py:49-94 |
| Assignment validates and persists the structural binding. | `assign_terminal_session_to_task` | mcp/src/agents_remember/serving/terminal_task_assignment.py:96-170 |

## Cross-Repo References


## Update History

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created; absorbs the behavior of removed `terminal_leaf_assignment.py` and `sprint_role_binding.py` under one generalized assignment contract.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: predecessor sprint-role binding card was created for immutable sprint provenance on named command seats.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: predecessor terminal-leaf assignment card was verified after the model-extraction/caller-rewrite wave.
- 2026-08-04T11:39+02:00 — 260731-EFA-L6 curator: predecessor card corrected role-aware `(leaf_key, seat_role)` binding semantics and citation evidence.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: predecessor assignment added explicit/defaulted seat role, `role-required`, live same-pair arbitration, and atomic leaf-plus-role moves.
- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator: predecessor assignment clarified that non-running rows cannot claim a new leaf.
- 2026-07-02T17:04+02:00 — Original terminal-leaf assignment card created for shared hosted-chat reassignment policy.
