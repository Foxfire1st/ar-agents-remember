# mcp/src/agents_remember/benchmarks/runner_modules/manifest.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Benchmark manifest loading, validation, provider selection, and prompt/variant filtering.

## Code Commentary

### Logic

`manifest.py` validates relative manifest paths, loads case JSON, filters cases/prompts/variants, normalizes provider ids, and computes selected provider requirements.

### Invariants And Boundaries

- Manifest paths must stay relative and cannot escape with absolute paths or `..`.
- Provider ids are allowlisted benchmark ids, not arbitrary MCP provider names.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
- The route-local overview summarizes how this module fits into the benchmark runner split. [2]

### Cross-Repo References

No configured sibling repository is required for this module.
