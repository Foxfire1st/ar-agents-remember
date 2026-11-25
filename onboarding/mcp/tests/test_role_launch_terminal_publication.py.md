# mcp/tests/test_role_launch_terminal_publication.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Integration test suite pinning that terminal `worktree_cleanup_tool` and concurrent role-launch preparation/publication arbitrate one enclosure generation so cleanup cannot be undone by a stale launch.

## Code Commentary

- Builds `_RoleStartFixture` over a landed leaf enclosure using `bound_worktree_services`, `_landed_leaf`, `_landed_leaf_config`, `_CatalogRuntime`, and `prepare_host`.
- `test_cleanup_cannot_be_undone_by_a_prepared_role_start` runs `cleanup_before_receipt()` immediately after `role_launch_routes.prepare_role_handover` returns and asserts `_role_launch_dispatch_endpoint` raises HTTP 409 mentioning `"enclosure"`, leaving the retired `worktree_group`, receipt file, and runtime agents absent.
- `test_cleanup_cannot_be_undone_during_role_preparation` runs `cleanup_before_receipt()` immediately after `role_launch_preparation._resolve_workspace` returns and asserts dispatch raises HTTP 409 without recreating the retired group, receipt, or host agent.

## Relationships

- Exercises `application/worktree_tools.py::worktree_cleanup_tool`, `cli/role_launch_routes.py`, `cli/role_launch_preparation.py`, `cli/role_launch_enclosure.py`, and `cli/role_launch_publication.py`.
- Registered in `mcp/tests/test-evidence-lanes.toml`.

## Evidence

- `_RoleStartFixture.cleanup_before_receipt` invokes `worktree_cleanup_tool` before any receipt exists and asserts the worktree group is removed. [1]
- Injecting terminal cleanup right after `prepare_role_handover` causes `_role_launch_dispatch_endpoint` to fail with HTTP 409 naming `"enclosure"` while keeping the retired group, receipt, and agents absent. [2]
- Injecting terminal cleanup right after `role_launch_preparation._resolve_workspace` causes dispatch to fail with HTTP 409 without recreating the retired group before receipt creation. [3]
