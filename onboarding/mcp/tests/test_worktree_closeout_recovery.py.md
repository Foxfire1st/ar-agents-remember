# mcp/tests/test_worktree_closeout_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_closeout_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
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
| Direct proof tests cover code/contract mismatch, memory-head mismatch, ledger identity, and reachability. | `test_recovery_rejects_code_and_contract_memory_mismatches`; `test_recovery_rejects_unproven_memory_commits` | mcp/tests/test_worktree_closeout_recovery.py:244-277; mcp/tests/test_worktree_closeout_recovery.py:279-318 |
| Production-shaped tests retain exact completion and unreachable-mapping refusal. | `test_completed_recovery_must_match_exactly`; `test_external_closeout_refuses_an_unreachable_existing_mapping` | mcp/tests/test_worktree_closeout_recovery.py:374-401; mcp/tests/test_worktree_closeout_recovery.py:403-426 |
| The stale contract memory cell is rejected in favor of the clean current post-claim memory HEAD. | `test_external_closeout_uses_clean_memory_head_when_no_mapping_exists` | mcp/tests/test_worktree_closeout_recovery.py:428-455 |
| Production recovery owns the finalization proof, typed outcome, code commit, and external tuple. | `prove_closeout_recovery_commits`; `MemoryCloseoutOutcome`; `accepted_code_commit`; `resume_external_commits` | mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:29-39; mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:42-57; mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:151-191; mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:194-235 |

## Cross-Repo References

The fixture models external memory within temporary repositories; it does not depend on another
product repository.

## R43 Recovery Success And Altitude Proof

Leaf recovery fixtures now state `kind="leaf"` explicitly. A new series case proves clean accepted
HEAD is reused without either commit primitive, and the external proof case now asserts the exact
successful `MemoryCloseoutOutcome` before exercising mismatch and ancestry refusals.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## Update History

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
