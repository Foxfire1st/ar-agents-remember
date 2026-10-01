# mcp/src/agents_remember/serving/codex_app_server_turns.py

## Governing Overview

[overview](overview.md)

## Purpose

The ``turn/start`` request shape and the receipts one Codex submission produces.

## Code Commentary

### Logic

Module-level surface:

- `StartedTurn` (class, lines 28-39) — What ``turn/start`` answered: which turn began, in what state, for which operation.
- `verified_asset_path` (function, lines 42-52) — Re-verify the staged file at construction before the native process sees its path.
- `turn_input` (function, lines 55-61) — Build the turn input blocks; verified local images ride as native paths.
- `turn_start_params` (function, lines 64-92) — The ``turn/start`` params for one submission, carrying only the policies that are set.
- `rejected_turn_receipt` (function, lines 95-111) — The receipt for a turn ``turn/start`` itself reported terminal.
- `accepted_turn_receipt` (function, lines 114-137) — The receipt for a turn that started, recording whether it also finished inside the call.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `StartedTurn` (lines 28-39) — What ``turn/start`` answered: which turn began, in what state, for which operation.. [1]
- Defines the function `verified_asset_path` (lines 42-52) — Re-verify the staged file at construction before the native process sees its path.. [2]
- Defines the function `turn_input` (lines 55-61) — Build the turn input blocks; verified local images ride as native paths.. [3]
- Defines the function `turn_start_params` (lines 64-92) — The ``turn/start`` params for one submission, carrying only the policies that are set.. [4]
- Defines the function `rejected_turn_receipt` (lines 95-111) — The receipt for a turn ``turn/start`` itself reported terminal.. [5]
- Defines the function `accepted_turn_receipt` (lines 114-137) — The receipt for a turn that started, recording whether it also finished inside the call.. [6]
