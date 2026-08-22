# mcp/tests/test_worktree_closeout_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_closeout_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Prove closeout restart reconciliation around every irreversible code, memory, ledger, and contract
boundary, including the crash after a new memory content commit but before its journal cell is
published.

## Code Commentary

### Logic

The suite exercises the extracted recovery journal and finalization proof directly, plus the production closeout helpers
through temporary external-memory repositories. It covers exact code-HEAD and candidate-tree
proof, clean post-claim adoption without recommit, conflicting or unreachable memory mappings,
internal/external contract mismatches, exact completed recovery, and the stale-contract-memory
window where clean current memory HEAD must win. Candidate 11 also forces missing ledger/worktree
authority and threads a real normalized message authority through external refresh and resume.

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
| Direct journal tests cover accepted code and external memory/ledger reconciliation. | `CloseoutRecoveryTests`; `test_code_commit_recovery_proves_head_and_candidate_tree`; `test_external_resume_rejects_conflict_missing_head_and_unreachable_content` | mcp/tests/test_worktree_closeout_recovery.py:95-312 |
| Direct proof tests cover code/contract mismatch, memory-head mismatch, ledger identity, and reachability. | `test_recovery_rejects_code_and_contract_memory_mismatches`; `test_recovery_rejects_unproven_memory_commits` | mcp/tests/test_worktree_closeout_recovery.py:314-347; mcp/tests/test_worktree_closeout_recovery.py:349-388 |
| Production-shaped tests retain exact completion, unreachable-mapping, and missing external-authority refusals. | `test_completed_recovery_must_match_exactly`; `test_external_closeout_refuses_an_unreachable_existing_mapping`; `test_external_closeout_requires_ledger_and_memory_worktree` | mcp/tests/test_worktree_closeout_recovery.py:444-522 |
| The stale contract memory cell is rejected in favor of the clean current post-claim memory HEAD. | `test_external_closeout_uses_clean_memory_head_when_no_mapping_exists` | mcp/tests/test_worktree_closeout_recovery.py:524-560 |
| Production recovery owns the finalization proof, typed outcome, code commit, and external tuple. | `prove_closeout_recovery_commits`; `MemoryCloseoutOutcome`; `accepted_code_commit`; `resume_external_commits` | mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:36-45; mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:48-63; mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:157-213; mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:216-276 |

## Cross-Repo References

The fixture models external memory within temporary repositories; it does not depend on another
product repository.

## R43 Recovery Success And Altitude Proof

Leaf recovery fixtures now state `kind="leaf"` explicitly. A new series case proves clean accepted
HEAD is reused without either commit primitive, and the external proof case now asserts the exact
successful `MemoryCloseoutOutcome` before exercising mismatch and ancestry refusals.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260821-CLIVE-L1 Recovery Migration

Recovery fixtures now patch the extracted `closeout_external` owner, publish canonical contracts, and construct normalized accepted input. Existing clean-head, ancestry, mapping, and finalization cases now additionally align with mutation evidence and the exact finalized-contract hash rather than treating recovery cells as standalone authority.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-17T12:30+02:00 — No content impact: L5 coverage-pragma alignment only; the documented recovery behavior is unchanged.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-14T12:13:26+02:00 — R43 curator: recorded explicit leaf altitude, clean series reuse
  without commit, and the positive recovered-outcome assertion. Verification remains closeout-owned.

- 2026-08-14T11:48:55+02:00 — R42 curator: repointed recovery-proof expectations from the
  closeout coordinator to `closeout_recovery.py` and refreshed the shifted direct-test ranges.
  Verification remains closeout-owned.

- 2026-08-14T05:26Z — Created for the L23 final recovery suite and its exact post-memory-commit
  crash-window proof. Verification remains closeout-owned.
