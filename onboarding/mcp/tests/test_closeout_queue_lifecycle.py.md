# mcp/tests/test_closeout_queue_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns queue binding, closeout claim/certification, integration claim, reversible release, and exact
lifecycle-operation identity.

## Code Commentary

### Logic

The suite distinguishes narrow never-governed legacy absence from damaged bound topology, then
drives idempotent claims and certification over reachable internal/external candidate records. It
also checks commit mismatch blockers and bounded operation/event identity.

### Invariants And Boundaries

- A durable queue binding fails closed if graph, parent, leaf, or contract identity later drifts.
- Certified external candidates carry exact code, memory-content, and ledger commits.
- Lifecycle transitions compare one-way owner fingerprints rather than exposing raw operation keys.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Binding damage cannot become legacy absence. | `test_live_parent_resolution_distinguishes_legacy_absence_from_bound_damage` | mcp/tests/test_closeout_queue_lifecycle.py:204-225 |
| Closeout certification binds all exact commits. | `test_certify_closeout_is_idempotent_and_binds_exact_commits` | mcp/tests/test_closeout_queue_lifecycle.py:254-299 |
| Exact integration commit blockers remain bounded scheduling facts. | `test_integration_commit_blockers_name_every_exact_mismatch` | mcp/tests/test_closeout_queue_lifecycle.py:317-346 |

## 260815-DAG Master Full-Gate Repair

Imports re-point to the restructured `models/queue/` and `worktrees/queue/` packages. The suite
gained three boundary proofs: a graph-less sprint with no stored binding resolves
`contract_queue_binding` to None, an integration entry without a queue binding falls through to
plain publication, and a blocked in-flight candidate refuses with
`closeout-candidate-integration-blocked`. The trailing `unittest.main()` block was removed.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_binding_parser_refuses_partial_malformed_and_non_leaf_contracts`, `test_unbound_legacy_absence_is_narrow`, `test_contract_binding_refuses_missing_graph_leaf_parent_and_binding_drift`, `test_queue_bound_task_publication_refuses_a_disappeared_master_parent`. This file now focuses on the residual binding/terminal guard surface after L2 removed much of the old lifecycle transition suite. Remaining queue lifecycle schema is transitional until L3.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_binding_parser_refuses_partial_malformed_and_non_leaf_contracts`, `test_unbound_legacy_absence_is_narrow`, `test_contract_binding_refuses_missing_graph_leaf_parent_and_binding_drift`, `test_queue_bound_task_publication_refuses_a_disappeared_master_parent`. | L65-L94; L96-L103; L105-L184; L186-L202 | `mcp/tests/test_closeout_queue_lifecycle.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: re-pointed queue imports and
  added the graph-less-no-binding, plain-publication, and blocked-candidate integration boundary
  proofs. Verified at code commit e5cb139f.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the public-revalidation case narrowed to
  `test_integration_revalidation_refuses_unclaimed_candidates` because the unused
  `require_queue_candidate_current` helper was removed; the integration-claim refusal remains
  forced. Verification remains closeout-owned.

- 2026-08-17T13:20+02:00 — No content impact: L5 repair: re-pointed stale mock targets and return tuples to match the L5 integration API (publish_queue_candidate_integration_result_under_authority, branch_commit, 4-tuple _prepare_integration_commits, durable-removal-intent idempotency). The documented test intent and coverage surface are unchanged.

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: added production-entry coverage for
  legacy absence, damaged bound topology, stale revalidation, unclaimed integration, exact
  completion ownership, and reversible closeout/integration release matrices.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  binding, claim, certification, and release assertions are identical.
- 2026-08-15T12:53+02:00 — Created for L3's focused lifecycle-transition coverage with only
  reachable durable candidate fixtures.
