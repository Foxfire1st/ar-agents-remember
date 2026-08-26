# mcp/tests/test_atomic_series_blocker_boundary_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_series_blocker_boundary_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:10+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused cross-boundary coverage proving that atomic selection, sync observation, terminal release,
and controlled refusals survive composition through structural dispatch and public worktree tools.

## Code Commentary

### Logic

Dispatch cases require a canonical owning master and derive standalone protected source explicitly.
Status cases preserve lifecycle-locator refusal while projecting any stable sync observation, and
translate terminal/configured-contract/caller failures through their declared public owners.

The remaining cases reject unknown sync contract kind, route completed abandon/cleanup replays
through exact selection release, surface finalization release failure as a typed block, and prove
attach/bootstrap stop on source-pair admission refusal. Public sync handles missing contracts,
mutation-owner reread changes, and series routing without bypassing the selected-series transaction.

### Invariants And Boundaries

- Structural worker dispatch has a canonical owning master; it cannot guess one from a leaf path.
- Sync status supplements lifecycle location evidence and never hides a stronger controlled refusal.
- Terminal abandon, cleanup, and finalization release only the exact selected series.
- Start/attach/bootstrap expose admission failure before process or implementation exposure.
- The public sync facade rereads under authority and delegates series work to the selected-series owner.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Status composition preserves sync observation and controlled contract/caller refusals. | `test_status_packet_preserves_locator_mismatch_with_sync_observation`; `test_status_tool_projects_sync_and_controlled_admission_refusals` | mcp/tests/test_atomic_series_blocker_boundary_edges.py:108-140; mcp/tests/test_atomic_series_blocker_boundary_edges.py:143-226 |
| Terminal replay and finalization use exact release and typed refusal. | `test_terminal_replays_release_exact_selection_for_abandon_and_cleanup`; `test_finalization_returns_a_typed_activation_release_refusal` | mcp/tests/test_atomic_series_blocker_boundary_edges.py:235-299; mcp/tests/test_atomic_series_blocker_boundary_edges.py:302-318 |
| Attach/bootstrap and public sync preserve admission/reread/series routing. | `test_attach_and_bootstrap_return_atomic_admission_refusals`; `test_sync_public_boundary_covers_missing_changed_and_series_routes` | mcp/tests/test_atomic_series_blocker_boundary_edges.py:321-357; mcp/tests/test_atomic_series_blocker_boundary_edges.py:360-389 |
| The public boundaries under test are structural dispatch, status/tools, start/bootstrap, sync, and terminal lifecycle composition. | `dispatch_agent_tool`; `worktree_status_tool`; `attach_result`; `ensure_master_series_contract`; `sync_result` | mcp/src/agents_remember/application/structural/agent_tools.py:377-442; mcp/src/agents_remember/application/worktree_tools.py:293-316; mcp/src/agents_remember/worktrees/modules/start.py:163-200; mcp/src/agents_remember/worktrees/modules/startup/start_contract.py:221-288; mcp/src/agents_remember/worktrees/modules/sync.py:29-68 |

## Cross-Repo References

No cross-repository implementation source governs this focused suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:10+02:00 — Created strict onboarding for the frozen public-boundary edge suite.
  Verification metadata remains empty until closeout can stamp a real code commit.