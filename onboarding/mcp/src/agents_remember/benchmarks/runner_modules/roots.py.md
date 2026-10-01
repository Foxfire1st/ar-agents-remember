# mcp/src/agents_remember/benchmarks/runner_modules/roots.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Benchmark root resolution context manager.

## Code Commentary

### Logic

`roots.py` chooses an explicit benchmark root when supplied or opens the packaged source root and yields its bundled `benchmarks/` directory.

### Invariants And Boundaries

- Packaged benchmark fallback belongs here so CLI and MCP callers share one root-selection contract.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
- The route-local overview summarizes how this module fits into the benchmark runner split. [2]

### Cross-Repo References

No configured sibling repository is required for this module.
