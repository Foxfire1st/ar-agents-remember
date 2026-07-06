# mcp/src/agents_remember/providers/lifecycle/cli.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/cli.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T22:34+02:00                     |
| lastVerifiedCommitHash | `9d58058e3ce4815b0356794fc21973ebe9c71345` |
| lastVerifiedCommitDate | 2026-07-06T11:47:10+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`cli.py` owns the provider lifecycle command-line surface: parser construction,
argument normalization, action dispatch, result rendering, and `main()`.

## Code Commentary

### Logic

The parser exposes `cgc`, `grepai`, and `watchers` subcommands with provider
action-specific arguments, including a `no_cache` flag (default `False`) on the
image-build paths that forces a from-scratch Docker rebuild. The
`--from-settings` help text (both providers) names the server-generated
provider lifecycle settings JSON and states there is no coordinator
`system/settings.json` fallback (260703-L13 — the implicit fallback was deleted
in `provider_settings.py`; settings-driven commands without the flag now refuse
with a `ContextProviderError`). Normalizers resolve
paths and stable provider IDs after parsing. Dispatch maps provider names to CGC, GrepAI, or watcher
implementation functions and renders either JSON, native bounded command
output, or a compact text summary. The CGC `patch` subcommand has been
removed: it is no longer parsed, no longer imported (`cgc_patch` is gone from
the `cgc.lifecycle` import), and no longer present in `cgc_cli_handlers()`.

### Invariants And Boundaries

- CLI dispatch is an operator interface; MCP service callers should use
`lifecycle_service.py` and implementation functions directly.
- Argument normalization should stay shallow and avoid provider behavior.
- CGC arguments do not carry a Python executable; Docker runner construction
  owns provider execution.
- Captured native command output should remain streamable for bounded `run`
  actions.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public facade imports `main()` from this module. | [lifecycle.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/__init__.py) |
| CGC and GrepAI implementations are dispatched from this CLI layer. | [cgc/__init__.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/__init__.py); [grepai/__init__.py](agents-remember/mcp/src/agents_remember/providers/grepai/lifecycle/__init__.py) |

## Update History

- 2026-07-06T22:34+02:00 — 260703-L13 ride-along: `--from-settings` help text rewritten for
  both providers — server-generated lifecycle settings JSON, no coordinator settings
  fallback. Parser shape unchanged. Verification metadata pinned until closeout stamps the
  L13 commit.

- 2026-05-31T12:50+02:00 — Removed the CGC `patch` subcommand: dropped the `cgc_patch` import, its `build_parser` action entry, and its `cgc_cli_handlers()` mapping; noted the removal in Logic (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented the `no_cache` argument added to the provider image-build subcommands (forwarded into the runner image builds for a from-scratch rebuild). Verified against `8927f03`.
- 2026-05-26T12:51+02:00: Updated after removing the CGC `--python`/host-venv install argument.
- 2026-05-25T19:09+02:00: Updated after CGC and GrepAI modules moved under package subfolders.
- 2026-05-25T19:01+02:00: Created from CLI/parser logic extracted out of provider lifecycle.
