# mcp/tests/test_l4_integration_authority_gap_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l4_integration_authority_gap_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces task-derived integration target, ordinary-worktree, series-terminal, and repository-checkout
authority refusals that are deliberately rare in positive lifecycle suites.

## Code Commentary

The cases pin standalone/default landing restrictions, shared code-memory identity refusal, checked
out branch/repository identity, exact atomic spelling and parent protection, parent-series shape,
and contract-independent carryover checkout authority.

## Invariants And Boundaries

- Every negative case calls the real authority owner.
- No compatibility alias or default-branch fallback is introduced for tests.
- Series and leaf authority remain distinct surfaces.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite owns focused branch gaps in task-derived integration authority. | `IntegrationTargetGapCoverageTests`; `OrdinaryAndTerminalAuthorityGapCoverageTests`; `RepositoryCheckoutGapCoverageTests` | mcp/tests/test_l4_integration_authority_gap_coverage.py:42-131; mcp/tests/test_l4_integration_authority_gap_coverage.py:134-317; mcp/tests/test_l4_integration_authority_gap_coverage.py:320-350 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-16T08:12+02:00 — Created focused L4 task-derived authority forcing during targeted Dagger coverage repair.
