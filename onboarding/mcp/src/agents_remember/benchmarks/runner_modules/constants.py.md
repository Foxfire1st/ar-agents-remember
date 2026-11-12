# mcp/src/agents_remember/benchmarks/runner_modules/constants.py

## Governing Overview

[overview](overview.md)

## Purpose

Shared benchmark constants for paths, provider ids, Codex usage token fields, Codex policy, and MCP registration names.

## Code Commentary

### Logic

`constants.py` centralizes values that multiple benchmark modules need, including supported benchmark providers, `.codex` paths, sandbox modes, and benchmark MCP names.

### Invariants And Boundaries

- Constants should stay declarative. Add behavior to a named owner module instead of expanding this file into a utility grab bag.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
- The route-local overview summarizes how this module fits into the benchmark runner split. 

### Cross-Repo References

No configured sibling repository is required for this module.

## No skill-exposure constants

The module holds no skill-exposure constants and no coordinator instruction-file targets: nothing mirrors a skill tree into a benchmark workspace, and the coordinator startup files a benchmark workspace must not keep are named by `install.experiment.RETIRED_STARTUP_TARGETS`, which `filesystem.py` imports for `sync_runtime_assets`. The workspace `AGENTS.md` templates (`WORKSPACE_AGENTS_TEMPLATE`, `SOURCE_ONLY_AGENTS_TEMPLATE`) remain here.

- Workspace instruction templates remain declared constants [4]
- The retired coordinator startup files are declared by the install experiment module [5]
