# mcp/src/agents_remember/controlplane/integration_authority_lock.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/integration_authority_lock.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
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
| Graph authoring (`task_doc.author_execution_graph`) dry-runs lock with `create=False`; its apply path re-locks before publication. | `author_execution_graph` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:193-261 |
| Sprint-linkage attach (`task_doc.attach_master`) dry-runs lock with `create=False`; its apply path re-locks before publication. | `attach_master` | mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:197-241 |
| Sprint-linkage detach (`task_doc.detach_master`) dry-runs lock with `create=False`; its apply path re-locks before publication. | `detach_master` | mcp/src/agents_remember/application/task_docs/task_sprint_linkage.py:244-293 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR provenance-debt repair: split the multi-anchor `author_execution_graph`; `attach_master`; `detach_master` evidence row into three rows, one per distinct definition, each citing its own exact source range (task_execution_topology.py:193-261, task_sprint_linkage.py:197-241, task_sprint_linkage.py:244-293) with operation-specific wording. `author_execution_graph` previously resolved 4 times at verification because the row also cited task_sprint_linkage.py, where the name occurs three further times (docstring line 4, error strings at lines 485 and 599); each claim now maps to exactly one unambiguous definition, so verification is unique.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: re-verified after the authoring sources moved to `application/task_docs/` — the dry-run `create=False` contract and the apply-path `create=True` re-lock are unchanged. Verified at code commit e5cb139f.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15: `integration_authority_lock` gained the keyword-only
  `create` flag; the three dry-run paths (graph authoring + attach/detach) pass `create=False` so a
  preview never writes the lock file (playthrough F2), while apply paths keep `create=True`.
  Verified at code commit de3a0fd9.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created repository-wide integration authority lock onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
