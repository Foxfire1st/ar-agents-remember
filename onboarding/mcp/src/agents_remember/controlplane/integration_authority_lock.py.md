# mcp/src/agents_remember/controlplane/integration_authority_lock.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/integration_authority_lock.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T21:30+02:00 |
| lastVerifiedCommitHash | `de3a0fd9204f2e64755032274fb4e741bfddf6df` |
| lastVerifiedCommitDate | 2026-08-20T21:16:45+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Serializes task-derived protected-ref decisions and Git mutations for one configured repository across processes.

## Code Commentary

`integration_authority_lock_path` derives a stable lock file from the canonical coordination root and repository id. `integration_authority_lock` takes an exclusive advisory lock for the full caller-owned authority boundary, so task-topology publication, candidate declaration, start, closeout, integration, and terminal paths can share one ordering domain instead of using check-then-act branch guards.

Since 260815-DAG-L15 the context manager takes `create: bool = True` (L15-R8 F2): `create=False` is
the read-only dry-run preflight — when the lock file does not yet exist the check runs unlocked and
the dry-run never writes the lock file. The apply paths keep `create=True` and re-lock before any
mutation, so dry-run write-freedom never weakens the authority of an actual publication.

## Invariants And Boundaries

- The lock key is repository-scoped and derived from coordination authority, never a task-supplied arbitrary filesystem path.
- Callers must acquire sprint queue authority before this lock when both are needed.
- The lock protects the complete read-validate-mutate boundary; it is not a substitute for named-ref compare-and-swap.
- `create=False` is for previews only: it never writes the lock file, and any caller that mutates
  under it would run without the ordering domain — apply paths must keep `create=True`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The lock path is deterministic for a coordination root and repository id. | `integration_authority_lock_path` | mcp/src/agents_remember/controlplane/integration_authority_lock.py:12-16 |
| The context manager owns the exclusive flock lifetime and the `create=False` dry-run branch. | `integration_authority_lock` | mcp/src/agents_remember/controlplane/integration_authority_lock.py:19-43 |
| Graph authoring and sprint linkage dry-runs lock with `create=False`; apply paths re-lock. | `author_execution_graph`; `attach_master`; `detach_master` | mcp/src/agents_remember/application/task_execution_topology.py:193-261; mcp/src/agents_remember/application/task_sprint_linkage.py:197-241; mcp/src/agents_remember/application/task_sprint_linkage.py:244-293 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: `integration_authority_lock` gained the keyword-only
  `create` flag; the three dry-run paths (graph authoring + attach/detach) pass `create=False` so a
  preview never writes the lock file (playthrough F2), while apply paths keep `create=True`.
  Verified at code commit de3a0fd9.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created repository-wide integration authority lock onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
