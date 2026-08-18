# mcp/tests/test_orchestration_portfolio.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/tests/test_orchestration_portfolio.py`              |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-08-18T00:00+02:00                                   |
| lastVerifiedCommitHash | `e460d4c000983d96a3ef6d105a1aeecbb73d5dc5`               |
| lastVerifiedCommitDate | 2026-08-18T13:41:53+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Covers the orchestrator portfolio loop (`orchestration_portfolio.py`): reshape classification,
deterministic frontier choice, dependency-safe frontier recomputation, and the per-master manager
slice. It reuses the `QueueFixture` from `test_closeout_queue.py` so the graph, grades, and
declaration flow are real rather than test-only.

## Code Commentary

### Logic

`PortfolioClassifyTests` proves the four substantial reshape signals versus the ordinary default.
`PortfolioChooseTests` proves priority-then-node-order selection and the empty-frontier refusal.
`PortfolioFrontierTests` builds a real `QueueFixture` (with and without a dependency edge, and with an
atomic master), declares candidates, and asserts that the frontier excludes downstream and
ungraded/atomic-blocker-held candidates while `manager_slice` scopes each manager to their own
master.

### Invariants And Boundaries

- A downstream candidate behind an incomplete predecessor is never in the frontier.
- An atomic master without an active blocker is never in the frontier.
- Choice is priority rank, then node order, then task key.
- The manager slice only reports the owning master's candidates.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Reshape classification covers substantial signals and the ordinary default. | `test_reshape_classification` | mcp/tests/test_orchestration_portfolio.py:28-34 |
| Choice prefers priority then node order and refuses an empty frontier. | `test_choose_prefers_priority_then_node_order` | mcp/tests/test_orchestration_portfolio.py:48-55 |
| Frontier recomputation excludes downstream and ungraded candidates. | `test_recompute_frontier_excludes_downstream_and_ungraded` | mcp/tests/test_orchestration_portfolio.py:76-83 |
| Manager slice scopes to the owning master. | `test_manager_slice_scopes_to_owning_master` | mcp/tests/test_orchestration_portfolio.py:100-114 |

## Update History

- 2026-08-18T00:00+02:00 — 260815-DAG-L7: created the orchestrator portfolio loop test suite.
  Verification metadata pinned until closeout stamps the L7 commit.
