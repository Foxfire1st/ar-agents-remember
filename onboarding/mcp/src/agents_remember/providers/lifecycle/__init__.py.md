# mcp/src/agents_remember/providers/lifecycle/__init__.py

## Governing Overview

[mcp/overview.md](overview.md)

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

## Evidence

### Repo-Internal References

- The CLI parser and dispatcher live in the lifecycle package. [1]
- CGC exports are grouped behind the CGC package facade. [2]
- GrepAI exports are grouped behind the Docker-owned GrepAI package facade. [3]
