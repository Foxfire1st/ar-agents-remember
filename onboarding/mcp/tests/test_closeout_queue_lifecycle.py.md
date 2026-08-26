# mcp/tests/test_closeout_queue_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Forces closeout-door source transitions and retry convergence independently from the disposable
scheduling projection and enclosure-external operation journal.

## Code Commentary

### Logic

The suite checks the exact same-generation and successor-generation transition maps, immutable
operation ownership after claim, claimed-door successor construction, idempotent declaration, and
idempotent defer/resume/withdraw behavior. Its series-status case proves that status reads do not
invent a candidate assertion.

### Invariants And Boundaries

- Same-generation transitions are narrow and a claimed generation cannot change operation owner.
- A successor of a claimed generation is a new waiting generation with cleared operation cells.
- Repeating the same declaration intent converges on one generation.
- Door control is contract-owned; post-claim lifecycle evidence does not return to the queue.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-generation transition and claimed-owner immutability are explicit. | `test_same_generation_transition_map_is_narrow`; `test_claimed_same_generation_cannot_rewrite_operation_owner` | mcp/tests/test_closeout_queue_lifecycle.py:22-60 |
| Successor generation rules clear operation ownership. | `test_cross_generation_map_is_exact`; `test_claimed_successor_has_new_generation_and_no_operation_cells` | mcp/tests/test_closeout_queue_lifecycle.py:62-113 |
| Repeated declaration and door controls converge. | `test_same_intent_declare_retry_converges_on_one_generation`; `test_defer_resume_withdraw_are_idempotent_for_exact_generation` | mcp/tests/test_closeout_queue_lifecycle.py:125-143 |

## 260815-DAG Master Full-Gate Repair

Imports re-point to the restructured `models/queue/` and `worktrees/queue/` packages. The suite
gained three boundary proofs: a graph-less sprint with no stored binding resolves
`contract_queue_binding` to None, an integration entry without a queue binding falls through to
plain publication, and a blocked in-flight candidate refuses with
`closeout-candidate-integration-blocked`. The trailing `unittest.main()` block was removed.

## 260821-CLIVE-L2 Historical Regression Contract

Before the final L3 cutover this file covered residual queue binding and terminal guards. Those tests
and their lifecycle-shaped queue owner were removed; the names below are retained only as migration
history and are not the current test contract.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `test_binding_parser_refuses_partial_malformed_and_non_leaf_contracts`, `test_unbound_legacy_absence_is_narrow`, `test_contract_binding_refuses_missing_graph_leaf_parent_and_binding_drift`, `test_queue_bound_task_publication_refuses_a_disappeared_master_parent`. | `test_cross_generation_map_is_exact` | mcp/tests/test_closeout_queue_lifecycle.py:62-99 |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces closeout-door declaration, defer, resume, withdraw, claim, and retry semantics as contract-owned source transitions.

### Current Invariants

- Door retries converge on the same immutable generation.
- Post-claim lifecycle outcomes remain journal facts and do not mutate a queue lifecycle row.

## Update History

- 2026-08-26T10:44:52+02:00 — Fixture authority clarified: the queue fixture explicitly enables direct execution before exercising public door transitions; the documented door-source and retry contract is unchanged.

- 2026-08-24T16:00+02:00 — Final closeout audit: removed obsolete queue
  claim/certification ownership from the live card and reconciled it to the exact current door-source
  retry and transition suite. Timestamp records the bounded architect correction wave.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

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
