# mcp/src/agents_remember/cli/leaf_set_seats.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

Determines which leaf seats a single `role_start_set` call starts and enforces that every caller-supplied seat override or replacement belongs to that leaf's seat set before any launch preparation begins.

## Code Commentary

`OPEN_AT_ONCE_SEATS` (`{"worker", "consolidator"}`) marks the executing seat that opens immediately on set start (other seats wait for their first message, except a Reviewer opened by `reviewer_message`), and `NAMEABLE_SEATS` lists every seat a set call can reference (`*ORDINARY_LEAF_SEATS, "consolidator"`). `set_seat_roles(coordination_root, call)` first rejects any unknown seat names in `call.replaces` with `_Refused("launch-refused", ...)`. It then resolves the leaf's seat tuple via `leaf_seat_roles_of(coordination_root, call.task_document_ref)` (defaulting to `ORDINARY_LEAF_SEATS` when `task_document_ref` is `None`). `_named_seats(call)` collects every seat with any override (`agent`, `model`, `effort`, or `feature_values`) or replacement entry; any seat outside the resolved set raises `_Refused("launch-refused", _foreign_detail(...), _foreign_remedy(...))`, stating whether the task document names a `consolidationList` and how to re-call.

## Relationships

Called by `mcp/src/agents_remember/cli/paseo_role_start.py` and `mcp/src/agents_remember/cli/role_launch_routes.py` (which also uses `OPEN_AT_ONCE_SEATS` to decide immediate launch vs. held seats). Depends on `tasks.consolidation_task` (`CONSOLIDATION_LEAF_SEATS`, `ORDINARY_LEAF_SEATS`, `leaf_seat_roles_of`), `models.role_agents.RoleStartSetCall`, and `cli.role_message_delivery._Refused`. Distinct from `cli/leaf_seat_handover.py` (sibling messaging payload) and `cli/seat_variant_rows.py` (per-seat settings overlay).

## Evidence

- `OPEN_AT_ONCE_SEATS` restricts immediate set opening to `worker` and `consolidator`, while `NAMEABLE_SEATS` defines the universe of seats a set call may override or replace. [1]
- `set_seat_roles` refuses unknown `replaces` entries, resolves the leaf's seat tuple from the task document (or `ORDINARY_LEAF_SEATS` without a ref), and refuses any foreign seat before preparation. [2]
- `_named_seats` gathers every seat for which the call supplies an `agent`, `model`, `effort`, `feature_values`, or `replaces` entry. [3]
- `_foreign_detail` distinguishes consolidation tasks (naming `consolidationList`) from ordinary tasks and enforces that a set never mixes Worker with Consolidator or Curator with Consolidator. [4]
