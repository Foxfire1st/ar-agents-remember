# mcp/src/agents_remember/application/seat_retirement_scope.py

## Governing Overview

[Application overview](overview.md)

## Purpose

Decides which bound role callers may retire or replace a recorded role seat based on caller scope and current task-document topology rather than original-starter identity.

## Code Commentary

- `retirement_scope_refusal(config, caller, agent_id, selection)` returns `None` when the bound caller is authorized and a refusal message naming caller scope, recorded target selection, and `"Nothing was archived."` otherwise.
- Self-retirement and self-replacement are always refused (`caller.agent_id == agent_id`).
- Caller scope by canonical role (`canonical_role(caller.role)`):
  - `architect`: may retire or replace any other role seat.
  - `manager`: may retire or replace seats whose current master matches `caller.master_ref` (seats on that master or any leaf of that master).
  - `orchestrator`: may retire or replace seats whose current sprint matches `caller.sprint_ref` (seats on that sprint, any master currently commanded by that sprint, or any leaf of such a master).
  - All other roles (`worker`, `reviewer`, `curator`, `investigator`, `bootstrap`): may retire or replace no seats.
- `_within_document_scope` resolves current parent links through `TaskDocumentTopology(config.coordination_root)` from the most specific recorded task reference (`task_document_ref` -> master -> sprint), so a master attached to a sprint after a seat started counts as inside that sprint. `TaskDocumentRefError` refuses cleanly without archiving.

## Relationships

- Consumed by `cli/role_retire.py` (`_retire_seat`) for `retire_child` authorization and `cli/role_launch_liveness.py` (`_replacement_caller`) for non-step-up leaf and non-leaf replacement authorization.
- Uses `application/role_launch_context.py` (`selection_binding`), `models/role_identity.py` (`canonical_role`), and `tasks/document_refs.py` (`TaskDocumentTopology`).

## Evidence

- `retirement_scope_refusal` enforces self-refusal, Architect universal scope, Manager/Orchestrator topology scope, non-coordinator refusal, and scope-naming refusal text. [1]
- `_within_document_scope` resolves live master and sprint membership from current canonical task documents via `TaskDocumentTopology`. [2]
- `_scope_of` formats the caller's scope description for refusal details. [3]
