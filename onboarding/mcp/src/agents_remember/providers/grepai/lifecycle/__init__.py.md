# mcp/src/agents_remember/providers/grepai/lifecycle/__init__.py

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`__init__.py` is the Docker-owned GrepAI lifecycle export facade. It groups the
split GrepAI implementation modules behind one import surface for
`providers.lifecycle`.

## Code Commentary

### Logic

The lazy GrepAI lifecycle facade searches core, compose, backend, embedder, runner,
and actions in that order and keeps the provider Docker-owned.

### Invariants And Boundaries

- Keep this module import-only.
- GrepAI remains Docker-or-bust; implementation modules must not add host binary
  or host Ollama fallbacks.

## Evidence

### Repo-Internal References

- The parent lifecycle facade lists the GrepAI lifecycle package among its lazy exports. [1]
- The lazy GrepAI facade searches core, compose, backend, embedder, runner, and actions in order, imports a matching module, caches the symbol, and raises if none exists. [2]
