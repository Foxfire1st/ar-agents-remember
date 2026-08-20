# mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

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
| Lease location is derived from the canonical contract. | `_lease_path` | mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py:21-24 |
| Active operation census and the context manager own cross-kind exclusion. | `_active_operation_kinds`, `contract_lifecycle_lease` | mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py:27-35; mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py:38-65 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created cross-operation lifecycle lease onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.