# mcp/src/agents_remember/serving/codex_app_server_turns.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_turns.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `StartedTurn` (lines 28-39) — What ``turn/start`` answered: which turn began, in what state, for which operation.. | `StartedTurn` | mcp/src/agents_remember/serving/codex_app_server_turns.py:28-39 |
| Defines the function `verified_asset_path` (lines 42-52) — Re-verify the staged file at construction before the native process sees its path.. | `verified_asset_path` | mcp/src/agents_remember/serving/codex_app_server_turns.py:42-52 |
| Defines the function `turn_input` (lines 55-61) — Build the turn input blocks; verified local images ride as native paths.. | `turn_input` | mcp/src/agents_remember/serving/codex_app_server_turns.py:55-61 |
| Defines the function `turn_start_params` (lines 64-92) — The ``turn/start`` params for one submission, carrying only the policies that are set.. | `turn_start_params` | mcp/src/agents_remember/serving/codex_app_server_turns.py:64-92 |
| Defines the function `rejected_turn_receipt` (lines 95-111) — The receipt for a turn ``turn/start`` itself reported terminal.. | `rejected_turn_receipt` | mcp/src/agents_remember/serving/codex_app_server_turns.py:95-111 |
| Defines the function `accepted_turn_receipt` (lines 114-137) — The receipt for a turn that started, recording whether it also finished inside the call.. | `accepted_turn_receipt` | mcp/src/agents_remember/serving/codex_app_server_turns.py:114-137 |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
