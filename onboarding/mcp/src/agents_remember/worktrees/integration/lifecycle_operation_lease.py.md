# mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

Prevents closeout, integration, cleanup, and abandon from concurrently owning the same contract.

## Code Commentary

The per-contract lease serializes filesystem lifecycle writers across operation kinds. It is pure
serialization: it does not inspect durable operation records. Callers stabilize and validate their
candidate/input while holding the lease, then use `require_lifecycle_operation_compatible` to
decide same-kind or cross-kind conflict before journal or terminal mutation.

## Invariants And Boundaries

- Lease identity is canonical contract identity.
- Operation compatibility is a separate explicit decision made while the lease is held.
- Terminal synchronous writers must acquire the same lease as detached operation launch.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Lease location is derived from the canonical contract. | `_lease_path` | mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py:21-24 |
| The context manager owns only contract-scoped filesystem serialization. | `contract_lifecycle_lease` | mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py:38-51 |
| Record-aware same/cross-kind conflict is explicit and separate. | `require_lifecycle_operation_compatible` | mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py:54-74 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L1 Lease Scope Correction

`contract_lifecycle_lease` is now a pure per-contract filesystem serialization lease. It does **not** census active operation records or decide same/cross-kind compatibility. Callers acquire the lease, stabilize and validate candidate/input, then call `require_lifecycle_operation_compatible` before journaling or terminal mutation. This separation lets malformed input refuse without observing lifecycle state while preserving cross-writer serialization.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created cross-operation lifecycle lease onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
