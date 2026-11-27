# mcp/src/agents_remember/mcp/registration/seat_retirement.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Registers the native `retire_child` tool for scope-authorized retirement of any role agent by agent ID. It is not the removed structural session-retirement plane.

## Code Commentary

The `retire_child` signature stays strict while the payload loads lazily on invocation.

### Logic

The public signature receives required `agent_id: str` and `role: LauncherRole`, plus keyword-only `reason: str = "delegated seat retired"`, `interrupt_turn: bool = False`, and optional `sprint_document_ref`, `master_document_ref`, and `task_document_ref` (taskless seats need none). It constructs `RetireChildRequest` and delegates to `tools.retire_child_payload`. Registration owns wire shape and description (282 chars, within the 500-char docstring cap); receipt ownership, scope enforcement, open-child checking, and host retirement belong to `cli/role_retire.py` and `application/seat_retirement_scope.py`.

### Invariants And Boundaries

Scope uses the caller binding and the selection recorded for `agent_id`. Open child seats block retirement, active turns or running provider subagents require `interrupt_turn=true`, and repeated authorized retirement is idempotent under the delegate's contract. This module does not stage or land code.

## Evidence

No Domain Documentation source is configured for this repository-specific boundary.

- `register_seat_retirement_tools` registers scope-based `retire_child` with required `agent_id` and `role`, optional task references, `reason`, and `interrupt_turn`. [1]

- The `retire_child` signature stays strict while `tools.retire_child_payload` loads only when retirement is invoked. [2]
