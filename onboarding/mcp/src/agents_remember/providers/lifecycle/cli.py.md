# mcp/src/agents_remember/providers/lifecycle/cli.py

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

## Evidence

### Repo-Internal References

- Public facade imports `main()` from this module. [1]
- CGC and GrepAI implementations are dispatched from this CLI layer. [2]
