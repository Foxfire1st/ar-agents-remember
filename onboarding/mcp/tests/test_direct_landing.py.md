# mcp/tests/test_direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T11:29+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
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
tree, preview with internal memory (omitted messages become typed not-applicable), preview refusing external memory without
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
- Internal-memory preview omits memory/ledger messages and exposes both legs as typed
  not-applicable. Non-preview direct landing then refuses the currently unsupported internal-memory
  mutation before memory/ledger Git; it does not synthesize messages.
- Tests never mutate a real coordination root.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The direct landing policy gate and leaf refusal. | `test_direct_landing_is_policy_gated`; `test_direct_landing_refuses_leaf_contracts` | mcp/tests/test_direct_landing.py:138-153; mcp/tests/test_direct_landing.py:155-168 |
| Code-commit verification then ledger/memory commit. | `test_direct_landing_verifies_code_commit_then_ledger` | mcp/tests/test_direct_landing.py:170-232 |
| Pre-commit gate refuses a moved candidate tree. | `test_direct_landing_precommit_gate_refuses_moved_candidate` | mcp/tests/test_direct_landing.py:234-257 |
| Internal-memory preview accepts omitted N/A messages; apply refuses the unsupported mutation boundary. | `test_preview_with_internal_memory_reports_mode`; `test_apply_with_internal_memory_is_refused` | mcp/tests/test_direct_landing.py:392-413; mcp/tests/test_direct_landing.py:463-482 |
| Idempotent re-land and conflicting-mapping refusal. | `test_reland_with_matching_memory_commit_is_idempotent`; `test_reland_with_conflicting_ledger_mapping_is_refused` | mcp/tests/test_direct_landing.py:526-559; mcp/tests/test_direct_landing.py:561-590 |
| Branch-addressed route-review stamp equals branch HEAD tree. | `test_record_route_review_branch_addressed_stamps_branch_head` | mcp/tests/test_direct_landing.py:649-687 |
| The operation under test. | `direct_landing` | mcp/src/agents_remember/worktrees/direct_landing.py:82-152 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L1 Direct-Landing Migration

External-memory landing calls that reach enabled message validation provide explicit memory and
ledger messages required by the shared direct-landing input contract. Internal-memory preview/apply cases omit those
messages because both legs are typed not-applicable; preview returns that plan, while apply refuses
the unsupported mutation boundary before Git. The suite's route-review and landing behavior
remains, but any former “atomic” characterization is retired: the lock serializes the two
sequential external-memory commits and does not supply rollback or crash recovery.

## Update History

- 2026-08-22T11:29+02:00 — 260821-CLIVE-L1 candidate12 rebind: corrected the
  overbroad explicit-message claim and recorded internal-memory omission as typed not-applicable,
  followed by the existing mutation-time `direct-landing-memory-required` refusal. Bound to reviewed
  candidate tree `8f03b256fe24aa77262da805f1538ee39ccb4dd6`, full diff SHA
  `ccb36a898b455cd67ca00c378e5ba0f18851be01faf3d26eced3b9af062f429e`, same-reviewer PASS;
  verification metadata remains pinned until governed closeout.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the direct landing operation and
  branch-addressed route-review binding (L16-R6/R7/R8/R9); covers the policy gate, commit
  verification, pre-commit candidate-tree gate, idempotent re-land, ledger conflict, and the
  recovery-naming refusal dialect. Verified at code commit a9d50e08.
