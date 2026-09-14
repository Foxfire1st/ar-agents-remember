# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_door_control.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_door_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Worktree-integration overview](../overview.md)

## Purpose

Owns journal-retained closeout-door publication intent/proof and the resulting disposable-projection
refresh effects for lifecycle operations.

## Code Commentary

Only closeout and direct-landing records may carry door intent. An unfinished intent must settle
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

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

| Finding | Anchor | Source |
| --- | --- | --- |
| Door-intent control has no external authority. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Door intent is recorded on the journaled operation and its dependency declaration is rebound. | `record_door_intent` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_door_control.py:36-54 |
| The operation dependency vocabulary this seam uses. | `lifecycle_operation_dependencies` | mcp/src/agents_remember/models/lifecycles/operation.py:445-500 |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the door is journal-owned
  and the task-publication lock is gone, as the earlier entry records. Re-read the card:
  `record_door_intent` `:36-54` and `lifecycle_operation_dependencies` `operation.py:445-500` both
  still hold. No wording changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_door_control.py`
  changed since the recorded verification commit. Re-read the card against the frozen on-disk source
  and re-checked its claims and cited ranges: nothing this card asserts is falsified by the change,
  so no wording changed. Verification metadata remains closeout-owned; no verification stamp
  advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit — the door lives in the contract's own journal and
  `task_publication_lock` no longer exists. Corrected the publication sentence to the journal path
  and repointed `lifecycle_operation_dependencies` (428-484 → 445-500). Verification metadata
  remains closeout-owned.
- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the dependency rebinding in `record_door_intent`; prior journal-retention and projection-refresh prose preserved.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-door owner relocation to `integration.closeout.door`; journal-owned publication and projection refresh semantics are unchanged.
- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final journal-door control owner. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.