# mcp/src/agents_remember/install/mcp_settings.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Copies the workspace's old MCP settings file (`.claude/mcp/agents-remember-settings.json`) once into the user's MCP settings file beside the user role settings, as one step of `runtime_install`.

## Code Commentary

`copy_mcp_settings(workspace_root, dry_run=...)` returns a small report with `sourcePath`, `userPath` and a `state`; `install/runtime.py::install_runtime_from_config` puts it in the install result as `mcpSettings`. The destination is `kernel/primitives/mcp_settings_location.py::mcp_settings_path()`, `agents-remember-settings.json` in the same directory as the user settings file (`$XDG_CONFIG_HOME/agents-remember/` or `~/.config/agents-remember/`).

- An existing destination is never touched: `already-present`. A missing source: `no-source`. A dry run reports `would-copy` and writes nothing.
- The real copy creates the destination exclusively (`O_EXCL`, mode 0600 at creation), copies the bytes, then copies the source's metadata with `shutil.copystat`; a copy that does not complete removes the partial destination. A completed copy reports `copied`. The source is never removed or changed, and no permission is closed here.
- An `OSError` becomes a report, not a raised error: `permission` for a `PermissionError`, otherwise `refused`, each with the error text and a remedy that asks the developer to resolve it and rerun `runtime_install`.
- The copy runs inside `observe_install_effect`, so the changed entry is reported like other install effects.

## Evidence

- The old settings convention path the copy reads. [1]
- Already-present, no-source and dry-run states return before any write. [2]
- Exclusive creation, byte and metadata copy, and removal of an incomplete destination. [3]
- Errors become permission or refused reports with a remedy. [4]
- The user MCP settings file sits beside the user role settings. [5]
- The install result carries the copy report. [6]
