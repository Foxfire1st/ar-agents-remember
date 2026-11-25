# mcp/src/agents_remember/cli/role_launch_enclosure.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Arbitrates role-launch filesystem writes and folder preparation against a worktree enclosure's active lifecycle generation so prepared role starts cannot write into or recreate a retired or terminal task folder.

## Code Commentary

- `publication_scope` yields immediately when `workspace` carries no `contractPath`; otherwise it holds `lifecycle_location_reservation(coordination_root, contract_path)`, reloads the contract from disk, and verifies `coordination_root`, `lifecycle_id`, `worktree_group`, and `leaf_workspace_allows_creation`.
- Any generation mismatch or terminal contract raises `EnclosurePublicationRefusal` (an HTTP `409` exception) naming `repo_id` and `contract_path` and advising `worktree_status`.
- `prepare_role_folders` derives `taskReportAccessRoot`, `taskReportRoot`, and `scratchRoot` separately for `LEAF_ROLES` (`<root>/role-reports/<role>/<req>` and `<root>/scratch/<role>/<req>`) versus non-leaf roles (`<root>/.agents-remember/role-executions/<req>/...`), rejecting symlinks or paths resolving outside `root` before directory creation.

## Relationships

- Consumed by `cli/role_launch_preparation.py`, `cli/role_launch_publication.py`, `cli/role_launch_routes.py`, and `cli/role_launch_workspace.py`.
- Shares the exclusive locator reservation lock with `worktrees/integration/lifecycle/lifecycle_location_reservation.py` and `worktrees/modules/terminal_retry.py`.

## Evidence

- `EnclosurePublicationRefusal` returns HTTP 409 with `worktree_status` guidance when a handover targets an inactive enclosure generation. [1]
- `publication_scope` serializes on `lifecycle_location_reservation`, reloads the contract, and verifies coordination root, lifecycle ID, worktree group, and creation eligibility before admitting writes. [2]
- `prepare_role_folders` assigns leaf and non-leaf report/scratch paths, rejects symlinks or escapes outside the workspace root, and creates the local directories. [3]
