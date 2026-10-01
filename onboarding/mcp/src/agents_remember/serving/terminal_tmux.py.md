# mcp/src/agents_remember/serving/terminal_tmux.py

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

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `TmuxProbeResult` (lines 62-66) — Evidence-bearing tmux session probe result.. [1]
- Defines the function `tmux_client_environment` (lines 85-98) — Construct the environment for a dashboard-owned tmux client process.. [2]
- Defines the function `_parse_tmux_version` (lines 101-109) — Extract ``(major, minor)`` from ``tmux -V`` output, or ``None`` when it is not a numeric release.. [3]
- Defines the function `_tmux_version` (lines 113-135) — The local tmux release, probed once per process (``None`` when tmux is absent/unparseable).. [4]
- Defines the function `_tmux_supports_client_capabilities` (lines 138-146) — Whether this tmux accepts ``-T`` (unknown versions answer ``False``).. [5]
- Defines the function `tmux_probe_session` (lines 149-176) — Whether tmux knows ``name``, preserving why a negative probe happened.. [6]
- Defines the function `_tmux_missing_session_stderr` (lines 179-181). [7]
- Defines the function `tmux_probe_result_from_bool` (lines 184-186). [8]
- Defines the function `tmux_kill_session` (lines 189-200) — Kill tmux session ``name``; no-op when tmux or the session is absent.. [9]
- Defines the function `_env_flags` (lines 203-212) — Flatten ``env`` into tmux ``-e KEY=VALUE`` new-session flags (L2 knob injection).. [10]
- Defines the function `tmux_create_detached` (lines 215-238) — Create tmux session ``name`` without attaching a local PTY client, seeding ``env`` at spawn.. [11]
- Defines the function `tmux_enable_mouse` (lines 241-260) — Enable per-session mouse mode; no-op when tmux or the session is absent (idempotent).. [12]
- Defines the function `tmux_cancel_copy_mode` (lines 263-281) — Leave copy-mode on session ``name``; harmless error when no mode is active.. [13]
- Defines the function `pane_in_mode` (lines 284-306) — Read tmux's exact ``pane_in_mode`` flag without sending input.. [14]
- Defines the function `ensure_terminal_input_ready` (lines 309-322) — Cancel copy mode when present and prove the exact pane left it before input.. [15]
- Defines the function `tmux_session_name` (lines 325-332) — The deterministic tmux identity for an arbitrary session id.. [16]
- Defines the function `build_tmux_command` (lines 335-370) — The persistent-session argv: ``tmux [-T sync] new-session -A -s <name> ...``.. [17]
