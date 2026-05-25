# mcp/src/agents_remember/providers/lifecycle_modules/cli.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle_modules/cli.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`cli.py` owns the provider lifecycle command-line surface: parser construction,
argument normalization, action dispatch, result rendering, and `main()`.

## Code Commentary

### Logic

The parser exposes `cgc`, `grepai`, and `watchers` subcommands with provider
action-specific arguments. Normalizers resolve paths and stable provider IDs
after parsing. Dispatch maps provider names to CGC, GrepAI, or watcher
implementation functions and renders either JSON, native bounded command
output, or a compact text summary.

### Invariants And Boundaries

- CLI dispatch is an operator interface; MCP service callers should use
  `lifecycle_service.py` and implementation functions directly.
- Argument normalization should stay shallow and avoid provider behavior.
- Captured native command output should remain streamable for bounded `run`
  actions.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public facade imports `main()` from this module. | [lifecycle.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle.py) |
| CGC and GrepAI implementations are dispatched from this CLI layer. | [cgc/__init__.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cgc/__init__.py); [grepai/__init__.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/grepai/__init__.py) |

## Update History

- 2026-05-25T19:09+02:00: Updated after CGC and GrepAI modules moved under package subfolders.
- 2026-05-25T19:01+02:00: Created from CLI/parser logic extracted out of provider lifecycle.
