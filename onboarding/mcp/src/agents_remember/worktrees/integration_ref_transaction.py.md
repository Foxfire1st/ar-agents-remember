# mcp/src/agents_remember/worktrees/integration_ref_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration_ref_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T23:38+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Moves exact code and external-memory integration refs with journal-bound compare-and-swap, torn-pair recovery, ledger proof, and checkout refresh.

## Code Commentary

`prepare_integration_ref_move` snapshots exact canonical refs only after plane authority. `merge_integrated_commits` consumes that prepared capability, advances the named refs with expected-old CAS, verifies the external-memory ledger/content ancestry, and records enough state for recovery. Checkout refresh accepts clean old or already-new state, refuses untracked/concurrent changes, and never uses ambient HEAD as the target authority.

## Invariants And Boundaries

- The lowest ref writer requires an unforgeable prepared/recovery capability.
- Every ref update names `refs/heads/<canonical>` and includes the expected old object id.
- External code and memory movement is one recoverable pair; rollback never clobbers a concurrently advanced ref.
- The mapped memory-content commit must descend from the prior memory tip and be reachable from the ledger commit.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Preparation binds current sources, exact targets, and journal authority. | `prepare_integration_ref_move` | mcp/src/agents_remember/worktrees/integration_ref_transaction.py:78-140 |
| The integration transaction owns ordered CAS and pair recovery facts. | `merge_integrated_commits` | mcp/src/agents_remember/worktrees/integration_ref_transaction.py:143-208 |
| Ledger mapping and ancestry are re-proved at the irreversible owner. | `require_integrated_ledger_mapping` | mcp/src/agents_remember/worktrees/integration_ref_transaction.py:211-226 |
| Recovery and checkout refresh are exact and idempotent. | `recover_integration_ref`, `refresh_owned_checkout`, `refresh_recovered_checkout` | mcp/src/agents_remember/worktrees/integration_ref_transaction.py:229-344 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created named-ref integration transaction onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
