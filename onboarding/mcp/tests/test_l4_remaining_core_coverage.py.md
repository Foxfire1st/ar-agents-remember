# mcp/tests/test_l4_remaining_core_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l4_remaining_core_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
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
| Repository-global topology and series authority branches are forced at the production census. | `IntegrationBranchAuthorityRemainderTests` | mcp/tests/test_l4_remaining_core_coverage.py:83-401 |
| Queue terminal and conflict-reset publication branches are forced without bypassing the queue owner. | `QueueLifecycleRemainderTests` | mcp/tests/test_l4_remaining_core_coverage.py:396-691 |
| Bootstrap WAL and integration recovery branches preserve exact authority and durable evidence. | `BootstrapRemainderTests`; `IntegrationRecoveryRemainderTests` | mcp/tests/test_l4_remaining_core_coverage.py:694-1184 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 added `executionGraph` cells to sprint mocks so fixtures resolve as graph-mode; documented core coverage is unchanged. Verification remains closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T13:20+02:00 — No content impact: L5 repair: re-pointed stale mock targets and return tuples to match the L5 integration API (publish_queue_candidate_integration_result_under_authority, branch_commit, 4-tuple _prepare_integration_commits, durable-removal-intent idempotency). The documented test intent and coverage surface are unchanged.

- 2026-08-16T10:43+02:00 — Added the last Dagger-reported authority and conflict-reset decisions and regenerated the focused class ranges.
- 2026-08-16T10:10+02:00 — Created focused L4 core-authority forcing for the final targeted Dagger coverage gate.
