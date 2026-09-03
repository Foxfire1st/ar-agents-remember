# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_door_control.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_door_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Worktree-integration overview](../overview.md)

## Purpose

Owns journal-retained closeout-door publication intent/proof and the resulting disposable-projection
refresh effects for lifecycle operations.

## Code Commentary

Only closeout and direct-landing records may carry door intent. An unfinished intent must settle
before another is accepted. Publication re-reads configured authority under the task-publication
lock; the journal retains the accepted proof before downstream projections are refreshed.

Under CCR-R03@v1 `record_door_intent` rebinds the updated record's typed dependency declaration
(`lifecycle_operation_dependencies`) after the new door publication intent is attached, so the
journaled operation content-addresses the exact admitted door generation it now reads
cit:([`record_door_intent`], mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_door_control.py:44-54).

## Invariants And Boundaries

- Door intent/proof survives queue invalidation and enclosure-local retries.
- Projection refresh is downstream and may not weaken accepted canonical publication.
- No second evidence reader or successor-intent compatibility WAL is permitted.
- Every door-intent mutation recomputes the record's declared dependency set before persistence.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

| Finding | Anchor | Source |
| --- | --- | --- |
| Door-intent control has no external authority. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Door intent is recorded on the journaled operation and its dependency declaration is rebound. | `record_door_intent` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_door_control.py:44-54 |
| The operation dependency vocabulary this seam uses. | `lifecycle_operation_dependencies` | mcp/src/agents_remember/models/lifecycles/operation.py:428-484 |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the dependency rebinding in `record_door_intent`; prior journal-retention and projection-refresh prose preserved.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-door owner relocation to `integration.closeout.door`; journal-owned publication and projection refresh semantics are unchanged.
- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final journal-door control owner. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.