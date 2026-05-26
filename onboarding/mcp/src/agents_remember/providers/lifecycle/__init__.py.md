# mcp/src/agents_remember/providers/lifecycle/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`providers.lifecycle` is the public provider lifecycle package facade. It
re-exports provider-owned CGC and GrepAI lifecycle modules, shared lifecycle
helper modules, CLI functions, and aggregate watcher actions.

## Code Commentary

### Logic

The facade imports `ContextProviderError`, `stable_provider_id`, all CGC and
GrepAI lifecycle exports, shared helper modules by responsibility, watcher
operations, and the CLI `main()` function. `__all__` is generated from the
public global names so tests and service callers can keep using the former
monolithic public surface.

### Invariants And Boundaries

- Keep the facade import-only; provider-specific implementation belongs in
  provider-owned lifecycle packages.
- Keep `main()` sourced from `lifecycle.cli`.
- Callers import this facade directly; there is no `provider_lifecycle.py`
  compatibility module.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The CLI parser and dispatcher live in the lifecycle package. | [cli.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/cli.py) |
| CGC exports are grouped behind the CGC package facade. | [cgc/__init__.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/__init__.py) |
| GrepAI exports are grouped behind the Docker-owned GrepAI package facade. | [grepai/__init__.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/__init__.py) |

## Update History

- 2026-05-25T21:14+02:00: Updated after `providers.lifecycle` became a package facade and shared lifecycle helpers were split by responsibility.
- 2026-05-25T19:16+02:00: Updated after the `provider_lifecycle.py` compatibility shim was deleted and callers wired directly to this facade.
- 2026-05-25T19:09+02:00: Updated after CGC and GrepAI lifecycle exports moved into `cgc/` and `grepai/` subpackages.
- 2026-05-25T19:01+02:00: Created when provider lifecycle was split into modules and the public facade was renamed to `lifecycle.py`.
