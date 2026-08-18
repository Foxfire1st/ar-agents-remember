# mcp/src/agents_remember/worktrees/lifecycle_operation_identity.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/lifecycle_operation_identity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-17T12:09+02:00 |
| lastVerifiedCommitHash | `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b` |
| lastVerifiedCommitDate | 2026-08-18T03:31:59+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Derives a stable fingerprint of the lifecycle cells that change only when a sequential operation advances, so repair can prove the exact accepted contract state.

## Code Commentary

### Logic

`operation_state_fingerprint` serializes the contract's base commits, closeout/integration status, candidate commits, integrated commits, and cleanup state into a sorted JSON payload and SHA-256 hashes it.

### Invariants And Boundaries

- Only lifecycle cells that advance monotonically with a sequential operation are hashed.
- The fingerprint is consumed by organizational completion repair to reject a contract that no longer matches its accepted operation state.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Stable fingerprint over advancing lifecycle cells. | `operation_state_fingerprint` | mcp/src/agents_remember/worktrees/lifecycle_operation_identity.py:11-28 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the lifecycle-operation state fingerprint.
