# mcp/src/agents_remember/application/log_capture.py

## Governing Overview

[MCP Application Layer Overview](overview.md)

## Purpose

Trims verbose subprocess command output and redacts inline credentials from nested tool-response payloads before they cross the MCP transport boundary.

## Code Commentary

`summarize_command_logs` recursively walks nested dictionaries and lists in place and returns the same root payload object. Each dictionary node is treated as successful when `node.get("ok") is True` or `node.get("returncode") == 0`.

On every visited dictionary node, `_drop_verbose_plumbing` unconditionally removes the redundant `"json"` mirror (`_DROP_ALWAYS`). When the node succeeded, `_shrink_logs` replaces non-empty string `"stdout"` and `"stderr"` values with `""` (preserving the response schema keys) and `_drop_verbose_plumbing` strips debug-only plumbing keys (`"command"`, `"commands"`, `"compose"`, `"migration"` in `_DROP_ON_SUCCESS`). When the node did not succeed, `_shrink_logs` caps non-empty `"stdout"` and `"stderr"` strings through `tail_lines` to the last `failure_tail` lines (default `DEFAULT_FAILURE_TAIL = 30`, prefixing `... [<omitted> earlier line(s) omitted] ...` when lines are dropped), while `_drop_verbose_plumbing` keeps the debugging keys and passes `"command"` and `"commands"` through `_redact_commands`.

`_redact_commands` walks dictionary values recursively and transforms flat list elements via `_redact_token`, which masks any string token containing `"PASSWORD="` to `<prefix>=***` using `partition("=")` so inline secrets (such as `PGPASSWORD=...`) do not surface in failed-command diagnostics. Non-string or empty log values are left untouched, and recursion mutates the terminal response tree in place rather than copying it.

## Relationships

- Sole internal caller: `mcp/src/agents_remember/application/worktree_tools.py` (`summarized_worktree_start_tool`), which wraps `worktree_start_tool` before transport in `mcp/src/agents_remember/mcp/tools/worktree.py`.
- Uses only standard-library typing (`typing.Any`). It owns response-payload trimming and secret redaction at the application boundary and does not execute subprocesses or alter domain status outcomes.

## Evidence

- `tail_lines` keeps at most the final `max_lines` lines and prepends an omitted-line count marker when input exceeds the limit. [1]
- `summarize_command_logs` classifies each dict node as successful on `ok is True` or `returncode == 0` and recursively trims and redacts nested dicts and lists in place. [2]
- `_shrink_logs` empties non-empty string `stdout`/`stderr` on success while keeping keys present, and caps them with `tail_lines` on failure. [3]
- `_drop_verbose_plumbing` always removes `json`, drops `command`/`commands`/`compose`/`migration` on success, and retains redacted `command`/`commands` on failure. [4]
- `_redact_commands` and `_redact_token` mask string tokens containing `PASSWORD=` to `<prefix>=***` across command lists and dicts. [5]
- `summarized_worktree_start_tool` applies `summarize_command_logs` to the `worktree_start_tool` response before transport. [6]
