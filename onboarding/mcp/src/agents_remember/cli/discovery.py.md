# mcp/src/agents_remember/cli/discovery.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/cli/discovery.py`   |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-03T09:55+02:00                       |
| lastVerifiedCommitHash | `08307e134bbdcff9b67e38232e513ebea21d3abf`   |
| lastVerifiedCommitDate | 2026-07-03T11:19:21+02:00|
| governingOverview      | `../../../../overview.md`                     |

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The CLI consumer: `--config` optional, discovery fallback + `ConfigDiscoveryError` reporting. | [dashboard.py](agents-remember/mcp/src/agents_remember/cli/dashboard.py) |
| The settings loader the discovered path feeds (`load_config`). | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| Unit tests: convention/registration hits, precedence, nearest-wins, malformed tolerance, template skip, miss error. | [test_cli_discovery.py](agents-remember/mcp/tests/test_cli_discovery.py) |

## Update History

- 2026-07-03T09:55+02:00 — Created for 260703 L1 (dashboard config auto-discovery): upward walk with
  convention-then-registration probing, nearest-wins, the `_is_usable_settings` semantic probe (the
  tracked placeholder template must never shadow real settings), and the both-patterns miss error.
  Verification metadata pinned until closeout stamps the code commit.
