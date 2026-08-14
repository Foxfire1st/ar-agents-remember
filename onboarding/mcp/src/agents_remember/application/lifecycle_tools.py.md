# mcp/src/agents_remember/application/lifecycle_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the function `_result` (lines 21-23) — Return the raw use-case result for the MCP adapter to finalize.. | `_result` | mcp/src/agents_remember/application/lifecycle_tools.py:21-23 |
| Defines the function `_state_fields` (lines 26-27). | `_state_fields` | mcp/src/agents_remember/application/lifecycle_tools.py:26-27 |
| Defines the function `lifecycle_start_tool` (lines 30-43). | `lifecycle_start_tool` | mcp/src/agents_remember/application/lifecycle_tools.py:30-43 |
| Defines the function `lifecycle_block_tool` (lines 46-62) — Lower-level compatibility builder; public agent gates use ``lifecycle_gate``.. | `lifecycle_block_tool` | mcp/src/agents_remember/application/lifecycle_tools.py:46-62 |
| Defines the function `lifecycle_resume_tool` (lines 65-70). | `lifecycle_resume_tool` | mcp/src/agents_remember/application/lifecycle_tools.py:65-70 |
| Defines the function `lifecycle_turn_end_notification_tool` (lines 73-91) — NOTIFY-AND-CONTINUE turn end (leaf-28): declare the turn complete and stop.. | `lifecycle_turn_end_notification_tool` | mcp/src/agents_remember/application/lifecycle_tools.py:73-91 |
| Defines the function `lifecycle_end_tool` (lines 94-99). | `lifecycle_end_tool` | mcp/src/agents_remember/application/lifecycle_tools.py:94-99 |
| Defines the function `lifecycle_phase_tool` (lines 102-107). | `lifecycle_phase_tool` | mcp/src/agents_remember/application/lifecycle_tools.py:102-107 |
| Defines the function `switch_lifecycle_tool` (lines 110-129) — Leave the current lifecycle and adopt a fresh one (no target).. | `switch_lifecycle_tool` | mcp/src/agents_remember/application/lifecycle_tools.py:110-129 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
