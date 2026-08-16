# mcp/src/agents_remember/controlplane/integration_authority_lock.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/integration_authority_lock.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T23:38+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Serializes task-derived protected-ref decisions and Git mutations for one configured repository across processes.

## Code Commentary

`integration_authority_lock_path` derives a stable lock file from the canonical coordination root and repository id. `integration_authority_lock` takes an exclusive advisory lock for the full caller-owned authority boundary, so task-topology publication, candidate declaration, start, closeout, integration, and terminal paths can share one ordering domain instead of using check-then-act branch guards.

## Invariants And Boundaries

- The lock key is repository-scoped and derived from coordination authority, never a task-supplied arbitrary filesystem path.
- Callers must acquire sprint queue authority before this lock when both are needed.
- The lock protects the complete read-validate-mutate boundary; it is not a substitute for named-ref compare-and-swap.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The lock path is deterministic for a coordination root and repository id. | `integration_authority_lock_path` | mcp/src/agents_remember/controlplane/integration_authority_lock.py:12-17 |
| The context manager owns the exclusive flock lifetime. | `integration_authority_lock` | mcp/src/agents_remember/controlplane/integration_authority_lock.py:19-33 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created repository-wide integration authority lock onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
