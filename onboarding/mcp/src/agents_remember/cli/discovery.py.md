# mcp/src/agents_remember/cli/discovery.py

## Governing Overview

[overview.md](../../../../overview.md)

## Purpose

`cli/discovery.py` makes `--config` optional for the umbrella CLI: when the flag is omitted,
`discover_config()` finds the trusted MCP settings JSON by walking upward from the current
directory, so `agents-remember dashboard` runs flag-free from anywhere under the workspace.
It exists so the CLI and the harness always boot from the same settings file without the user
retyping an absolute path (260703 L1).

## Code Commentary

`discover_config(start=None)` resolves the origin (default `Path.cwd()`) and walks
`(origin, *origin.parents)`. At each level it probes, in order:

1. the settings convention `SETTINGS_CONVENTION` = `.claude/mcp/agents-remember-settings.json`,
2. an `.mcp.json` (`MCP_REGISTRATION`) whose `mcpServers`/`agents-remember` entry records a
   `--config` argument — `_config_from_mcp_registration` extracts the value following the first
   `--config` token in the entry's `args` list, reusing the harness's own registration verbatim.

The nearest directory wins and the first USABLE candidate ends the walk. Usability is the
semantic probe `_is_usable_settings`: the file must parse as a JSON object whose
`coordinationRoot` is a non-empty string naming an **existing absolute directory**. A miss raises
`ConfigDiscoveryError` with one message naming both probed patterns and the walk origin.

`_config_from_mcp_registration` is total over hostile input: missing file, unreadable bytes,
malformed JSON, non-dict shapes, foreign server entries, or a `--config` flag without a value all
return `None` (the walk continues) — discovery must never crash on someone else's `.mcp.json`.
Since 260731-EFA-L2 it is one line —
`_nested_object(_json_object(mcp_json), "mcpServers", _SERVER_NAME)` then `_config_argument(...)` —
over three named helpers that carry that totality explicitly:

- `_json_object(path)` — the file's top-level JSON object; `None` when absent, unreadable, or not
  an object. **Foreign and malformed files are someone else's**, so discovery skips them silently
  rather than crashing the walk. `_is_usable_settings` reuses it, which is why the two probes now
  tolerate exactly the same hostile input by construction.
- `_nested_object(container, *keys)` — follows `keys` down nested JSON objects, returning `None` at
  the first missing or non-object step.
- `_config_argument(arguments)` — the value following `--config` in a recorded argv list, if it
  carries one.

## Invariants And Boundaries

- **An explicit `--config` always bypasses discovery** — callers only invoke `discover_config()`
  when the flag is absent (see `cli/dashboard.py`).
- **The semantic probe is load-bearing, not cosmetic:** the repository ships a tracked placeholder
  template at the convention path (`.claude/mcp/agents-remember-settings.json` with
  `<PATH/TO/YOUR/...>` placeholders), so running from inside a source checkout must walk PAST it
  to the workspace's real settings. A purely syntactic "file exists" probe would shadow the real
  settings with the template.
- Per-level precedence is convention **before** `.mcp.json` registration; across levels,
  nearest-directory-wins beats both.
- The registration probe never validates the recorded path itself beyond usability — a registered
  `--config` pointing at a missing or template file is skipped silently and the walk continues.
- Discovery returns the settings **path**; validation/parsing into `McpRuntimeConfig` stays with
  `mcp.config.load_config` (no duplicate config semantics here).

## Evidence

### Repo-Internal References

- The CLI consumer: `--config` optional, discovery fallback + `ConfigDiscoveryError` reporting. [1]
- The CLI consumer: `--config` optional, discovery fallback + `ConfigDiscoveryError` reporting. [2]
- The settings loader the discovered path feeds (`load_config`). [3]
- Unit tests: convention/registration hits, precedence, nearest-wins, malformed tolerance, template skip, miss error. [4]
