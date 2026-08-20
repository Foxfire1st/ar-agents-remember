# mcp/tests/test_direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T09:35+02:00 |
| lastVerifiedCommitHash | `a9d50e08b830c4a34c14e495706c19fe697f47ab` |
| lastVerifiedCommitDate | 2026-08-20T09:26:15+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Behavioral test suite for the L16 direct-execution machinery (L16-R6/R7/R8/R9): the direct
landing operation (`worktrees/direct_landing.py`) and the branch-addressed route-review binding
(`application/task_doc_route_review.py`). Drives real scratch git repos, series contracts, and a
real external-memory checkout + ledger.

## Code Commentary

### Logic

`_scratch_config` builds a policy-enabled `McpRuntimeConfig`; `_series_fixture` creates a code
repo + series contract (+ memory repo) fixture. `DirectLandingTests` prove the policy gate, leaf
contract refusal, code-commit-verification-then-ledger landing, the moved-candidate pre-commit
refusal, and the intent-note requirement. `DirectLandingBranchTests` covers the branch-addressed
refusal branches: blank code commit, contract changed under the lock (TOCTOU), unresolvable commit
tree, preview with internal memory (reports mode), preview refusing external memory without
authority paths, invalid ledger, apply with internal memory, missing memory paths, memory branch
mismatch, idempotent re-land with a matching memory commit, conflicting ledger mapping refusal, and
unreachable ledger commit refusal. `BranchAddressedRouteReviewTests` prove the branch-addressed
`record_route_review` stamp equals the series branch HEAD tree, its policy gate, the missing
binding recovery dialect, the blank-leaf-id naming, `branch_addressed` only for
`record_route_review`, the bound-form success, and the closeout declare refusal naming the direct
landing alternative.

### Conventions

Uses the same scratch-repo harness as `test_seat_independent_execution.py` and the worktree test
family; assertions target the exact typed statuses, not message substrings.

### Invariants And Boundaries

- Every refusal path is asserted by its typed `status`; idempotent re-land and the ledger-conflict
  branch are covered (no coverage note remains open for this suite).
- Tests never mutate a real coordination root.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The direct landing policy gate and leaf refusal. | `test_direct_landing_is_policy_gated`; `test_direct_landing_refuses_leaf_contracts` | mcp/tests/test_direct_landing.py:138-165 |
| Code-commit verification then ledger/memory commit. | `test_direct_landing_verifies_code_commit_then_ledger` | mcp/tests/test_direct_landing.py:166-220 |
| Pre-commit gate refuses a moved candidate tree. | `test_direct_landing_precommit_gate_refuses_moved_candidate` | mcp/tests/test_direct_landing.py:221-243 |
| Idempotent re-land and conflicting-mapping refusal. | `test_reland_with_matching_memory_commit_is_idempotent`; `test_reland_with_conflicting_ledger_mapping_is_refused` | mcp/tests/test_direct_landing.py:490-547 |
| Branch-addressed route-review stamp equals branch HEAD tree. | `test_record_route_review_branch_addressed_stamps_branch_head` | mcp/tests/test_direct_landing.py:603-642 |
| The operation under test. | `direct_landing` | mcp/src/agents_remember/worktrees/direct_landing.py:74-126 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the direct landing operation and
  branch-addressed route-review binding (L16-R6/R7/R8/R9); covers the policy gate, commit
  verification, pre-commit candidate-tree gate, idempotent re-land, ledger conflict, and the
  recovery-naming refusal dialect. Verified at code commit a9d50e08.
