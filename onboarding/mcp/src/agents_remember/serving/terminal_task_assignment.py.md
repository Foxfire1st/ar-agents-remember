# mcp/src/agents_remember/serving/terminal_task_assignment.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/terminal_task_assignment.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T23:19+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
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

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Conflict checks reselect after marking a dead preferred generation exited. | `task_binding_conflict_owner` | mcp/src/agents_remember/serving/terminal_task_assignment.py:55-78 |
| Assignment holds one catalog batch across validation, conflict checks, and publication. | `assign_terminal_session_to_task`; `_assign_terminal_session_to_task` | mcp/src/agents_remember/serving/terminal_task_assignment.py:107-132 |

## Cross-Repo References


## L23 Assignment Admission

Assigning an existing terminal to a structural task now proves task-derived
source lineage before catalog mutation or seat attachment. A stale/unavailable
projection returns the prior binding, requested role, detail, and evidence so
replacement-safe routing does not depend on agent-held ids.

## Update History

- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.
- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2: added dead-incumbent re-selection and one-batch
  assignment publication so a live staged heir is never mistaken for vacancy. Verification remains
  closeout-owned.

- 2026-08-12T20:10+02:00 — L23 curator: documented pre-mutation lineage refusal for terminal assignment; verification remains closeout-owned.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created; absorbs the behavior of removed `terminal_leaf_assignment.py` and `sprint_role_binding.py` under one generalized assignment contract.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: predecessor sprint-role binding card was created for immutable sprint provenance on named command seats.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: predecessor terminal-leaf assignment card was verified after the model-extraction/caller-rewrite wave.
- 2026-08-04T11:39+02:00 — 260731-EFA-L6 curator: predecessor card corrected role-aware `(leaf_key, seat_role)` binding semantics and citation evidence.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: predecessor assignment added explicit/defaulted seat role, `role-required`, live same-pair arbitration, and atomic leaf-plus-role moves.
- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator: predecessor assignment clarified that non-running rows cannot claim a new leaf.
- 2026-07-02T17:04+02:00 — Original terminal-leaf assignment card created for shared hosted-chat reassignment policy.
