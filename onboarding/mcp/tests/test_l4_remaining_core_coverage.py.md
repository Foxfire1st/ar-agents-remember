# mcp/tests/test_l4_remaining_core_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l4_remaining_core_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces the remaining L4 integration-surface, queue publication, bootstrap journal, and integration
recovery decisions reported by the strict changed-line and changed-branch coverage gate.

## Code Commentary

The suite invokes production authority owners directly while patching only unrelated persistence or
Git effects. It covers topology-repair refusal, exact series identity, terminal queue publication,
conflict reset, bootstrap recovery, and completed-integration proof branches.

## Invariants And Boundaries

- Protected branch authority stays task-derived and repository-identity bound.
- Queue and bootstrap recovery tests preserve exact journal, candidate, and contract facts.
- Refusal-path forcing does not add fallback or compatibility behavior.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Repository-global topology and series authority branches are forced at the production census. | `IntegrationBranchAuthorityRemainderTests` | mcp/tests/test_l4_remaining_core_coverage.py:82-400 |
| Queue terminal and conflict-reset publication branches are forced without bypassing the queue owner. | `QueueLifecycleRemainderTests` | mcp/tests/test_l4_remaining_core_coverage.py:403-698 |
| Bootstrap WAL and integration recovery branches preserve exact authority and durable evidence. | `BootstrapRemainderTests`; `IntegrationRecoveryRemainderTests` | mcp/tests/test_l4_remaining_core_coverage.py:701-924; mcp/tests/test_l4_remaining_core_coverage.py:927-1066 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_publication_rethrows_unrelated_and_incomplete_repair_errors`, `test_surface_resolution_wraps_master_error_and_requires_super_branch`, `test_foreign_override_is_ignored`, `test_live_leaf_census_keeps_cleaned_atomic_and_refuses_sprint_reassignment`. The L2 additions force journal-owned claim transfer, exact protected-ref decisions, source-movement reconciliation, and organizational disposition/repair without queue-owned lifecycle evidence.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_publication_rethrows_unrelated_and_incomplete_repair_errors`, `test_surface_resolution_wraps_master_error_and_requires_super_branch`, `test_foreign_override_is_ignored`, `test_live_leaf_census_keeps_cleaned_atomic_and_refuses_sprint_reassignment`. | L83-L115; L117-L141; L143-L154; L156-L207 | `mcp/tests/test_l4_remaining_core_coverage.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 added `executionGraph` cells to sprint mocks so fixtures resolve as graph-mode; documented core coverage is unchanged. Verification remains closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T13:20+02:00 — No content impact: L5 repair: re-pointed stale mock targets and return tuples to match the L5 integration API (publish_queue_candidate_integration_result_under_authority, branch_commit, 4-tuple _prepare_integration_commits, durable-removal-intent idempotency). The documented test intent and coverage surface are unchanged.

- 2026-08-16T10:43+02:00 — Added the last Dagger-reported authority and conflict-reset decisions and regenerated the focused class ranges.
- 2026-08-16T10:10+02:00 — Created focused L4 core-authority forcing for the final targeted Dagger coverage gate.
