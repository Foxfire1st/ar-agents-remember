# mcp/src/agents_remember/providers/lifecycle/cli.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/cli.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `2e2117a194ab1576c860dbca39b6acff0d1c20fa` |
| lastVerifiedCommitDate | 2026-05-26T14:55:50+02:00|
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
- CGC arguments do not carry a Python executable; Docker runner construction
  owns provider execution.
- Captured native command output should remain streamable for bounded `run`
  actions.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public facade imports `main()` from this module. | [lifecycle.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/__init__.py) |
| CGC and GrepAI implementations are dispatched from this CLI layer. | [cgc/__init__.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/__init__.py); [grepai/__init__.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/__init__.py) |

## Update History

- 2026-05-26T12:51+02:00: Updated after removing the CGC `--python`/host-venv install argument.
- 2026-05-25T19:09+02:00: Updated after CGC and GrepAI modules moved under package subfolders.
- 2026-05-25T19:01+02:00: Created from CLI/parser logic extracted out of provider lifecycle.
