# mcp/tests/test_closeout_queue_candidate_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_candidate_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns exact route-review, source-lineage, ledger, tree, lifecycle-owner, and atomic-master landing
evidence for closeout candidates.

## Code Commentary

### Logic

The suite mutates full review records and evidence bytes, source tips, ledger rows, commit trees,
and each atomic finalization predicate. Public atomic release is proven both on the all-true path
and with each independently false prerequisite.

### Invariants And Boundaries

- Same summary/count route reviews still invalidate when their exact rows or files change.
- Atomic landing requires code and memory ancestry, exact finalized commits, approved human review,
  ledger agreement, and content movement beyond the base.
- Evidence paths remain task-confined and readable.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Full route-review identity and drift are forced. | `test_route_review_blockers_translate_invalid_and_detect_drift` | mcp/tests/test_closeout_queue_candidate_evidence.py:128-144 |
| Atomic predicates require an exact finalized series landing. | `test_atomic_contract_predicates_require_exact_final_series_landing` | mcp/tests/test_closeout_queue_candidate_evidence.py:141-217 |
| Public proof covers success and each false predicate. | `test_public_atomic_landing_proof_translates_invalid_and_false_predicates` | mcp/tests/test_closeout_queue_candidate_evidence.py:528-560 |

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260815-DAG Master Full-Gate Repair

Imports re-point to the restructured `worktrees/queue/` and `worktrees/integration/` packages
(`closeout_queue_candidate_evidence`, `closeout_queue`, `closeout_queue_errors`, and
`integration.lifecycle_operation_store`). The suite gained
`test_atomic_landing_proof_translates_landed_probe_failures`, which proves a raising
`_atomic_code_landed` probe inside `require_atomic_master_landed` translates to
`CloseoutQueueError("no valid exact landing")`; the trailing `unittest.main()` block was removed.

## Update History

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the test only repoints `LifecycleOperationStore` to its moved integration lifecycle package. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: re-pointed imports to the
  worktrees/queue and worktrees/integration packages and added the landed-probe failure
  translation proof for `require_atomic_master_landed`. Verified at code commit e5cb139f.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  route, lineage, ledger, tree, and atomic evidence assertions are identical.
- 2026-08-15T12:53+02:00 — Created for the split L3 candidate-evidence suite and the bounded atomic
  predicate refactor required by the CRAP gate.
