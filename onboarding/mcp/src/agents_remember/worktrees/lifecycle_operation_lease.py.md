# mcp/src/agents_remember/worktrees/lifecycle_operation_lease.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/lifecycle_operation_lease.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T23:38+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Prevents closeout, integration, cleanup, and abandon from concurrently owning the same contract.

## Code Commentary

The per-contract lease serializes lifecycle writers across operation kinds and inspects durable closeout/integrate records while held. A live or recovery-owned conflicting operation blocks the new mutation, closing last-writer races that per-kind operation stores cannot prevent.

## Invariants And Boundaries

- Lease identity is canonical contract identity.
- Running and irreversible recovery operations retain ownership.
- Terminal synchronous writers must acquire the same lease as detached operation launch.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Lease location is derived from the canonical contract. | `_lease_path` | mcp/src/agents_remember/worktrees/lifecycle_operation_lease.py:21-24 |
| Active operation census and the context manager own cross-kind exclusion. | `_active_operation_kinds`, `contract_lifecycle_lease` | mcp/src/agents_remember/worktrees/lifecycle_operation_lease.py:27-65 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created cross-operation lifecycle lease onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
