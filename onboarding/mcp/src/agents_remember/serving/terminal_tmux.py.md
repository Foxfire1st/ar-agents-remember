# mcp/src/agents_remember/serving/terminal_tmux.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/terminal_tmux.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Every command the dashboard runs against the ``tmux`` binary, and nothing else.

## Code Commentary

### Logic

Module-level surface:

- `TmuxProbeResult` (class, lines 62-66) — Evidence-bearing tmux session probe result.
- `tmux_client_environment` (function, lines 85-98) — Construct the environment for a dashboard-owned tmux client process.
- `_parse_tmux_version` (function, lines 101-109) — Extract ``(major, minor)`` from ``tmux -V`` output, or ``None`` when it is not a numeric release.
- `_tmux_version` (function, lines 113-135) — The local tmux release, probed once per process (``None`` when tmux is absent/unparseable).
- `_tmux_supports_client_capabilities` (function, lines 138-146) — Whether this tmux accepts ``-T`` (unknown versions answer ``False``).
- `tmux_probe_session` (function, lines 149-176) — Whether tmux knows ``name``, preserving why a negative probe happened.
- `_tmux_missing_session_stderr` (function, lines 179-181)
- `tmux_probe_result_from_bool` (function, lines 184-186)
- `tmux_kill_session` (function, lines 189-200) — Kill tmux session ``name``; no-op when tmux or the session is absent.
- `_env_flags` (function, lines 203-212) — Flatten ``env`` into tmux ``-e KEY=VALUE`` new-session flags (L2 knob injection).
- `tmux_create_detached` (function, lines 215-238) — Create tmux session ``name`` without attaching a local PTY client, seeding ``env`` at spawn.
- `tmux_enable_mouse` (function, lines 241-260) — Enable per-session mouse mode; no-op when tmux or the session is absent (idempotent).
- `tmux_cancel_copy_mode` (function, lines 263-281) — Leave copy-mode on session ``name``; harmless error when no mode is active.
- `pane_in_mode` (function, lines 284-306) — Read tmux's exact ``pane_in_mode`` flag without sending input.
- `ensure_terminal_input_ready` (function, lines 309-322) — Cancel copy mode when present and prove the exact pane left it before input.
- `tmux_session_name` (function, lines 325-332) — The deterministic tmux identity for an arbitrary session id.
- `build_tmux_command` (function, lines 335-370) — The persistent-session argv: ``tmux [-T sync] new-session -A -s <name> ...``.

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
| Defines the class `TmuxProbeResult` (lines 62-66) — Evidence-bearing tmux session probe result.. | `TmuxProbeResult` | mcp/src/agents_remember/serving/terminal_tmux.py:62-66 |
| Defines the function `tmux_client_environment` (lines 85-98) — Construct the environment for a dashboard-owned tmux client process.. | `tmux_client_environment` | mcp/src/agents_remember/serving/terminal_tmux.py:85-98 |
| Defines the function `_parse_tmux_version` (lines 101-109) — Extract ``(major, minor)`` from ``tmux -V`` output, or ``None`` when it is not a numeric release.. | `_parse_tmux_version` | mcp/src/agents_remember/serving/terminal_tmux.py:101-109 |
| Defines the function `_tmux_version` (lines 113-135) — The local tmux release, probed once per process (``None`` when tmux is absent/unparseable).. | `_tmux_version` | mcp/src/agents_remember/serving/terminal_tmux.py:113-135 |
| Defines the function `_tmux_supports_client_capabilities` (lines 138-146) — Whether this tmux accepts ``-T`` (unknown versions answer ``False``).. | `_tmux_supports_client_capabilities` | mcp/src/agents_remember/serving/terminal_tmux.py:138-146 |
| Defines the function `tmux_probe_session` (lines 149-176) — Whether tmux knows ``name``, preserving why a negative probe happened.. | `tmux_probe_session` | mcp/src/agents_remember/serving/terminal_tmux.py:149-176 |
| Defines the function `_tmux_missing_session_stderr` (lines 179-181). | `_tmux_missing_session_stderr` | mcp/src/agents_remember/serving/terminal_tmux.py:179-181 |
| Defines the function `tmux_probe_result_from_bool` (lines 184-186). | `tmux_probe_result_from_bool` | mcp/src/agents_remember/serving/terminal_tmux.py:184-186 |
| Defines the function `tmux_kill_session` (lines 189-200) — Kill tmux session ``name``; no-op when tmux or the session is absent.. | `tmux_kill_session` | mcp/src/agents_remember/serving/terminal_tmux.py:189-200 |
| Defines the function `_env_flags` (lines 203-212) — Flatten ``env`` into tmux ``-e KEY=VALUE`` new-session flags (L2 knob injection).. | `_env_flags` | mcp/src/agents_remember/serving/terminal_tmux.py:203-212 |
| Defines the function `tmux_create_detached` (lines 215-238) — Create tmux session ``name`` without attaching a local PTY client, seeding ``env`` at spawn.. | `tmux_create_detached` | mcp/src/agents_remember/serving/terminal_tmux.py:215-238 |
| Defines the function `tmux_enable_mouse` (lines 241-260) — Enable per-session mouse mode; no-op when tmux or the session is absent (idempotent).. | `tmux_enable_mouse` | mcp/src/agents_remember/serving/terminal_tmux.py:241-260 |
| Defines the function `tmux_cancel_copy_mode` (lines 263-281) — Leave copy-mode on session ``name``; harmless error when no mode is active.. | `tmux_cancel_copy_mode` | mcp/src/agents_remember/serving/terminal_tmux.py:263-281 |
| Defines the function `pane_in_mode` (lines 284-306) — Read tmux's exact ``pane_in_mode`` flag without sending input.. | `pane_in_mode` | mcp/src/agents_remember/serving/terminal_tmux.py:284-306 |
| Defines the function `ensure_terminal_input_ready` (lines 309-322) — Cancel copy mode when present and prove the exact pane left it before input.. | `ensure_terminal_input_ready` | mcp/src/agents_remember/serving/terminal_tmux.py:309-322 |
| Defines the function `tmux_session_name` (lines 325-332) — The deterministic tmux identity for an arbitrary session id.. | `tmux_session_name` | mcp/src/agents_remember/serving/terminal_tmux.py:325-332 |
| Defines the function `build_tmux_command` (lines 335-370) — The persistent-session argv: ``tmux [-T sync] new-session -A -s <name> ...``.. | `build_tmux_command` | mcp/src/agents_remember/serving/terminal_tmux.py:335-370 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
