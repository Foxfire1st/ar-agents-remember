# mcp/src/agents_remember/cli/leaf_seat_handover.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

Builds the `leafSeats` block injected into a leaf seat's launch hand-over so sibling seats on the same leaf can address each other directly by role and task reference rather than by agent ID.

## Code Commentary

`leaf_seats(role, task, seat_selection)` reads the leaf's seat roster from `task.document` via `tasks.consolidation_task.leaf_seat_roles`—yielding `("worker", "reviewer", "curator")` for an ordinary leaf and `("consolidator", "reviewer")` for a consolidation task—and returns `{"roles": [...], "roleMessageArguments": {...}}`. `roleMessageArguments` includes an entry for every sibling except the recipient seat itself, containing `role`, `master_document_ref`, `task_document_ref` (JSON-dumped from `task.ref`), and `sprint_document_ref` only when `seat_selection.get("sprintDocumentRef")` is not `None` (omitted for leaves under a standalone master). No sibling agent ID is emitted; role-plus-task addressing resolves to whichever agent holds that seat at delivery time.

## Relationships

Called by `mcp/src/agents_remember/cli/role_launch_preparation.py` when assembling a leaf seat's hand-over, and projected by `mcp/src/agents_remember/cli/role_handover_projection.py` (`_project_leaf_seats`). Delegates seat-set derivation to `agents_remember.tasks.consolidation_task.leaf_seat_roles` and consumes `ResolvedTaskDocument` from `agents_remember.tasks.document_refs`. Covered directly by `mcp/tests/test_consolidator_role.py`. Distinct from `serving/explainer_watcher.py`'s same-named `leaf_seats` helper (which discovers active watcher seats) and from `cli/leaf_set_seats.py` (which validates `role_start_set` calls).

## Evidence

- `leaf_seats` derives the leaf's role roster from `task.document` via `leaf_seat_roles` and builds `roleMessageArguments` for every sibling except the current `role` without naming agent IDs. [1]
- `sprint_document_ref` is included in sibling `role_message` arguments only when `seat_selection["sprintDocumentRef"]` is present, supporting standalone-master leaves without a sprint. [2]
