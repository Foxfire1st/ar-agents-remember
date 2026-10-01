# scripts/harness/shared/agents-remember-settings.json

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

The canonical placeholder MCP settings template shipped in every harness starter package
as `mcp/agents-remember-settings.json`. `scripts/sync-harness.py` copies it **verbatim**
into all eight starter packages, and additionally to `.vscode/mcp/` for the VS Code
starter (which spans two folders). It replaces eight byte-identical copies.

## Code Commentary

### Logic

A `version: 1` settings object with the keys a fresh workspace needs, all values written
as placeholders that `render-starter.py` substitutes at render time:

- `coordinationRoot`, `workspaceRoot`, `transcriptRoot` — all built from
  `<PATH/TO/YOUR/PROJECTS_FOLDER>`, with the coordination root at
  `<workspace>/ar-coordination` and MCP transcripts under its `logs/mcp`.
- `repositories` — one entry keyed `<YOUR_REPOSITORY_FOLDER_NAME>`.
- `providers` — `codegraphcontext-code` and `grepai-memory`, declared empty so the
  opt-in Docker providers are visible without being configured.
- `timeoutCaps` — `toolSeconds: 60`, `providerSetupSeconds: 1800`.

### Invariants And Boundaries

- This is a **template**, not live settings. The placeholder strings are the contract:
  `render-starter.py`'s `render_settings` replaces `<PATH/TO/YOUR/PROJECTS_FOLDER>` and
  `<YOUR_REPOSITORY_FOLDER_NAME>` in the rendered copy, so changing a placeholder's
  spelling here without changing `PLACEHOLDER_VALUES` in `sync-harness.py` breaks
  rendering.
- The tracked placeholder shape is deliberately recognisable as a template: the dashboard
  CLI's settings discovery uses a semantic usability probe so this file cannot shadow a
  user's real settings.
- Editing a generated copy is caught by `sync-harness.py --check` in both hook tiers and
  by `mcp/tests/test_sync_harness.py`.

## Evidence

### Repo-Internal References

- The generator that fans this file out verbatim, including to `.vscode/mcp/`. [1]
- `render_settings` performs the placeholder substitution in a rendered workspace. [2]
- The settings schema this template instantiates. [3]
