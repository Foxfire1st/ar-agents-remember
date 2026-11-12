# mcp/src/agents_remember/cli/discovery.py

## Governing Overview

[overview](../../../../overview.md)

## Purpose

`cli/discovery.py` makes `--config` optional for the umbrella CLI: when the flag is omitted,
`discover_config()` selects the user's one MCP authority settings file,
`<XDG_CONFIG_HOME or ~/.config>/agents-remember/agents-remember-settings.json`, so a command runs
flag-free from any directory and never reads a workspace registration.

## Code Commentary

`discover_config()` takes no starting directory and never inspects the current directory. It asks
`mcp_settings_path()` (`kernel/primitives/mcp_settings_location.py`) for the file beside the user's
role settings; a relative `XDG_CONFIG_HOME` raises `UserSettingsLocationError`, which discovery turns
into `ConfigDiscoveryError`.

Usability is the semantic probe `_settings_coordination_root`: the file must parse as a JSON object
whose `coordinationRoot` is a non-empty string naming an **existing absolute directory**. A miss
raises `ConfigDiscoveryError` naming the expected file and the remedy (create it, or pass
`--config` with an explicit settings path).

On success discovery prints one provenance line to stderr, built by
`cli/settings_provenance.discovered_settings_line`: `settings discovered: <path>`, extended when the
dashboard daemon of the same coordination root runs with another settings file. Standard output
stays the command's own.

## Invariants And Boundaries

- **An explicit `--config` always bypasses discovery** — callers only invoke `discover_config()`
  when the flag is absent (see `cli/dashboard.py`).
- **No workspace file selects the authority:** `.mcp.json` registrations and harness-folder
  settings such as `.claude/mcp/agents-remember-settings.json` are never consulted, whatever the
  current directory.
- Discovery returns the settings **path**; validation/parsing into `McpRuntimeConfig` stays with
  `kernel/primitives/runtime_config.load_config` (no duplicate config semantics here).
- Discovery writes nothing: the provenance line reads the daemon state and the answering
  dashboard's process and changes neither settings file.

## Evidence

### Repo-Internal References

- The CLI consumer: `--config` optional, discovery fallback + `ConfigDiscoveryError` reporting. [1]
- The CLI consumer: `--config` optional, discovery fallback + `ConfigDiscoveryError` reporting. [2]
- The settings loader the discovered path feeds (`load_config`). [3]

- Unit tests: the user config wins over workspace registrations, the current directory is never inspected, malformed and foreign registrations have no effect, and a miss names the user config and the `--config` remedy. [4]

- Discovery selects the user's settings file, refuses an unusable one with the remedy, and prints the provenance line to stderr. [5]
- The probe accepts only a JSON object naming an existing absolute coordination directory. [6]
- The authority file sits beside the user's role settings. [7]
