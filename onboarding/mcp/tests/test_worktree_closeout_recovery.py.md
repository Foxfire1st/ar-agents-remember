# mcp/tests/test_worktree_closeout_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_closeout_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-14T05:26Z |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038` |
| lastVerifiedCommitDate |  2026-08-14T08:23:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Prove closeout restart reconciliation around every irreversible code, memory, ledger, and contract
boundary, including the crash after a new memory content commit but before its journal cell is
published.

## Code Commentary

### Logic

The suite exercises the extracted recovery journal directly and the production closeout helpers
through temporary external-memory repositories. It covers exact code-HEAD and candidate-tree
proof, clean post-claim adoption without recommit, conflicting or unreachable memory mappings,
internal/external contract mismatches, exact completed recovery, and the stale-contract-memory
window where clean current memory HEAD must win.

### Conventions

Git topology cases use the shared real-repository fixture; narrow failure branches patch only the
adjacent Git or ledger primitive and assert exact refusal text and journal cells.

### Invariants And Boundaries

- Recovery may reuse only commits proved by Git and the durable ledger.
- A completed contract must match the journal exactly.
- Post-claim clean HEAD is recovery evidence; stale pre-attempt contract cells are not.
- The suite runs only inside the Dagger-attested Python acceptance environment.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-internal test boundary.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Direct journal tests cover accepted code and external memory/ledger reconciliation. | `CloseoutRecoveryTests`; `test_code_commit_recovery_proves_head_and_candidate_tree`; `test_external_resume_rejects_conflict_missing_head_and_unreachable_content` | mcp/tests/test_worktree_closeout_recovery.py:54-178 |
| Production-shaped tests cover contract proof, exact finalization, and unreachable mappings. | `test_recovery_rejects_code_and_contract_memory_mismatches`; `test_completed_recovery_must_match_exactly`; `test_external_closeout_refuses_an_unreachable_existing_mapping` | mcp/tests/test_worktree_closeout_recovery.py:180-299 |
| The stale contract memory cell is rejected in favor of the clean current post-claim memory HEAD. | `test_external_closeout_uses_clean_memory_head_when_no_mapping_exists` | mcp/tests/test_worktree_closeout_recovery.py:301-328 |
| Production recovery helpers journal code and the complete external tuple. | `accepted_code_commit`; `resume_external_commits` | mcp/src/agents_remember/worktrees/closeout_recovery.py:23-102 |

## Cross-Repo References

The fixture models external memory within temporary repositories; it does not depend on another
product repository.

## Update History

- 2026-08-14T05:26Z — Created for the L23 final recovery suite and its exact post-memory-commit
  crash-window proof. Verification remains closeout-owned.
