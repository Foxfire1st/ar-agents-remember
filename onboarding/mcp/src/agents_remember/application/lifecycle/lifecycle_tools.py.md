# mcp/src/agents_remember/application/lifecycle/lifecycle_tools.py

## Governing Overview

[overview](../overview.md)

## Purpose

Application operations for the ``lifecycle_*`` signals.

## Code Commentary

### Logic

Module-level surface:

- `_result` (function, lines 21-23) — Return the raw use-case result for the MCP adapter to finalize.
- `_state_fields` (function, lines 26-27)
- `lifecycle_start_tool` (function, lines 30-43)
- `lifecycle_block_tool` (function, lines 46-62) — Lower-level compatibility builder; public agent gates use ``lifecycle_gate``.
- `lifecycle_resume_tool` (function, lines 65-70)
- `lifecycle_turn_end_notification_tool` (function, lines 73-91) — NOTIFY-AND-CONTINUE turn end (leaf-28): declare the turn complete and stop.
- `lifecycle_end_tool` (function, lines 94-99)
- `lifecycle_phase_tool` (function, lines 102-107)
- `switch_lifecycle_tool` (function, lines 110-129) — Leave the current lifecycle and adopt a fresh one (no target).

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the function `_result` (lines 21-23) — Return the raw use-case result for the MCP adapter to finalize.. [1]
- Defines the function `_state_fields` (lines 26-27). [2]
- Defines the function `lifecycle_start_tool` (lines 30-43). [3]
- Defines the function `lifecycle_block_tool` (lines 46-62) — Lower-level compatibility builder; public agent gates use ``lifecycle_gate``.. [4]
- Defines the function `lifecycle_resume_tool` (lines 65-70). [5]
- Defines the function `lifecycle_turn_end_notification_tool` (lines 73-91) — NOTIFY-AND-CONTINUE turn end (leaf-28): declare the turn complete and stop.. [6]
- Defines the function `lifecycle_end_tool` (lines 94-99). [7]
- Defines the function `lifecycle_phase_tool` (lines 102-107). [8]
- Defines the function `switch_lifecycle_tool` (lines 110-129) — Leave the current lifecycle and adopt a fresh one (no target).. [9]
