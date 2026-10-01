# mcp/src/agents_remember/providers/lifecycle/__main__.py

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`__main__.py` keeps `python -m agents_remember.providers.lifecycle` working
after `providers.lifecycle` changed from a module file into a package facade.

## Code Commentary

### Logic

The entrypoint imports `main` from the lifecycle package facade and exits with
that command's return code.

### Invariants And Boundaries

- CLI argument parsing stays in `cli.py`.
- This file is only the package execution adapter.

## Evidence

### Repo-Internal References

- The lifecycle CLI parser and main function live in `cli.py`. [1]
