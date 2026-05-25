# mcp/src/agents_remember/providers/lifecycle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:16+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`lifecycle.py` is the public provider lifecycle facade. It re-exports the
split implementation modules for GrepAI, CodeGraphContext, shared CLI/common
helpers, and aggregate watcher actions while keeping the executable lifecycle
entrypoint stable.

## Code Commentary

### Logic

The facade imports `ContextProviderError`, `stable_provider_id`, all CGC and
GrepAI lifecycle exports, shared common helpers, watcher operations, and the
CLI `main()` function. `__all__` is generated from the public global names so
tests and service callers can keep using the former monolithic public surface.

### Invariants And Boundaries

- Keep the facade import-only; implementation belongs in `lifecycle_modules/`.
- Keep `main()` sourced from `lifecycle_modules.cli`.
- Callers import this facade directly; there is no `provider_lifecycle.py`
  compatibility module.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The CLI parser, renderer, and dispatcher live in the lifecycle modules package. | [cli.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cli.py) |
| CGC exports are grouped behind the CGC package facade. | [cgc/__init__.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cgc/__init__.py) |
| GrepAI exports are grouped behind the Docker-owned GrepAI package facade. | [grepai/__init__.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/grepai/__init__.py) |

## Update History

- 2026-05-25T19:16+02:00: Updated after the `provider_lifecycle.py` compatibility shim was deleted and callers wired directly to this facade.
- 2026-05-25T19:09+02:00: Updated after CGC and GrepAI lifecycle exports moved into `cgc/` and `grepai/` subpackages.
- 2026-05-25T19:01+02:00: Created when provider lifecycle was split into modules and the public facade was renamed to `lifecycle.py`.
