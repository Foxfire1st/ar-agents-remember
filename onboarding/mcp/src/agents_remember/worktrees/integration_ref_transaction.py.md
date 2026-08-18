# mcp/src/agents_remember/worktrees/integration_ref_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration_ref_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T23:38+02:00 |
| lastVerifiedCommitHash | `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b` |
| lastVerifiedCommitDate | 2026-08-18T03:31:59+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Moves exact code and external-memory integration refs with journal-bound compare-and-swap, torn-pair recovery, ledger proof, and checkout refresh.

## Code Commentary

`IntegrationSources` is now a frozen dataclass with a `replay_required` property; `require_integrated_ledger_mapping` accepts the memory source commit plus an expected series ledger prefix.

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
| Ledger mapping and ancestry are re-proved at the irreversible owner. | `require_integrated_ledger_mapping` | mcp/src/agents_remember/worktrees/integration_ref_transaction.py:229-278 |
| Recovery and checkout refresh are exact and idempotent. | `recover_integration_ref`, `refresh_owned_checkout`, `refresh_recovered_checkout` | mcp/src/agents_remember/worktrees/integration_ref_transaction.py:305-341; mcp/src/agents_remember/worktrees/integration_ref_transaction.py:358-386; mcp/src/agents_remember/worktrees/integration_ref_transaction.py:389-420 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-17T16:55+02:00 — 260815-DAG-L5 repair: `require_integrated_ledger_mapping` now short-circuits a no-change leaf (whose landed code commit is already in the source ledger) before the preserved-history and ancestor checks, since such a leaf has no new code or memory content to verify. Verification remains closeout-owned.

- 2026-08-17T12:35+02:00 — 260815-DAG-L5: `IntegrationSources` became a frozen dataclass and the ledger proof now takes the memory source commit plus an expected series prefix. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created named-ref integration transaction onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
