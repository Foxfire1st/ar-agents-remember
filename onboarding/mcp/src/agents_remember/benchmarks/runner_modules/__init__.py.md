# mcp/src/agents_remember/benchmarks/runner_modules/__init__.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Package marker for the benchmark runner implementation modules.

## Code Commentary

### Logic

`__init__.py` intentionally contains only a package docstring so the public facade can import focused modules from a stable package path.

### Invariants And Boundaries

- Keep this package marker behavior-free; ownership belongs in named modules.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
- The route-local overview summarizes how this module fits into the benchmark runner split. [2]

### Cross-Repo References

No configured sibling repository is required for this module.
