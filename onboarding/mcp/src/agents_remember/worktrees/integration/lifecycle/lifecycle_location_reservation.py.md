# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_location_reservation.py

## Governing Overview

[Lifecycle operation integration overview](overview.md)

## Purpose

Exposes the shared exclusive lock context manager over an enclosure contract's lifecycle operation locator path so cross-module enclosure operations serialize on the same lock address as generation startup.

## Code Commentary

- `lifecycle_location_reservation(coordination_root, contract_path)` returns `exclusive_access(lifecycle_operation_locator_path(coordination_root, contract_path), _LOCATION_OWNERSHIP)`.
- Reuses `controlplane/durable_store.py::exclusive_access` and the path/ownership constants from `lifecycle_operation_location.py` rather than introducing a second lock file or policy.

## Relationships

- Shared coordination primitive consumed by `cli/role_launch_enclosure.py::publication_scope` (role-launch publication) and `worktrees/modules/terminal_retry.py::retry_terminal_group` (completed-generation folder removal retry), alongside generation reservation in `lifecycle_operation_location.py`.

## Evidence

- Imports `exclusive_access` and the canonical locator path/ownership definitions (`_LOCATION_OWNERSHIP`, `lifecycle_operation_locator_path`) to guarantee a single lock address across subsystems. [1]
- `lifecycle_location_reservation` returns an `exclusive_access` context manager bound to `lifecycle_operation_locator_path(coordination_root, contract_path)` with `_LOCATION_OWNERSHIP`. [2]
