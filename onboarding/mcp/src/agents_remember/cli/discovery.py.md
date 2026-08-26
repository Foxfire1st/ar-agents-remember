# mcp/src/agents_remember/cli/discovery.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/cli/discovery.py`   |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-31T00:00+02:00                       |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`   |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The CLI consumer: `--config` optional, discovery fallback + `ConfigDiscoveryError` reporting. | "config_path = args.config or discover_config()", "except (ConfigDiscoveryError" | mcp/src/agents_remember/cli/dashboard.py:217-217; mcp/src/agents_remember/cli/dashboard.py:219-219 |
| The settings loader the discovered path feeds (`load_config`). | `load_config` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:149-157 |
| Unit tests: convention/registration hits, precedence, nearest-wins, malformed tolerance, template skip, miss error. | `DiscoverConfigTests`, "test_miss_raises_with_both_patterns_and_the_origin" | mcp/tests/test_cli_discovery.py:42-142 |

## Update History

- 2026-08-03T02:56:49+02:00 — W3-B04 curator: curated 2 table citations (2 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0911` armed with no
  exemptions): `_config_from_mcp_registration` was rebuilt on the new `_json_object`,
  `_nested_object` and `_config_argument` helpers, and `_is_usable_settings` now reuses
  `_json_object` — so both probes tolerate the same hostile input by construction. Discovery
  results and the `ConfigDiscoveryError` message are unchanged. Verification metadata pinned until
  closeout stamps the L2 commit.
- 2026-07-03T09:55+02:00 — Created for 260703 L1 (dashboard config auto-discovery): upward walk with
  convention-then-registration probing, nearest-wins, the `_is_usable_settings` semantic probe (the
  tracked placeholder template must never shadow real settings), and the both-patterns miss error.
  Verification metadata pinned until closeout stamps the code commit.
