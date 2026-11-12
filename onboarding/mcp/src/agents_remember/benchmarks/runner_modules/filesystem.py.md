# mcp/src/agents_remember/benchmarks/runner_modules/filesystem.py

## Governing Overview

[overview](overview.md)

## Purpose

Filesystem mutation helpers for benchmark workspace setup and runtime asset
exposure.

## Code Commentary

### Logic

`filesystem.py` owns safe path removal, copying packaged
provider assets, removing the retired coordinator startup files, rendering root markers, creating benchmark-local
coordination scaffolding. Skills reach the workspace harness from the tool server's
package copy; no benchmark-local skill tree is written. Cross-platform long-path normalization (the Windows
`\\?\` prefix logic) is not inlined here; both `removable_path` and the
copy helpers delegate to the shared `long_path` helper imported from
`agents_remember.install.assets`. The benchmark runtime scaffold creates central
`logs/mcp` and `logs/providers/...` directories alongside provider data and
runner roots.

### Invariants And Boundaries

- Copy/remove helpers are benchmark workspace mechanics, not general repository mutation policy.
- Benchmark workspaces should mirror the MCP runtime log layout with central
  `logs/` directories instead of legacy `providers/logs`.
- No skill tree is mirrored into a benchmark workspace: its harness reads the skills the tool server serves from the package copy.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
The [route overview](overview.md) describes the benchmark runner split; it is a discovery companion rather than a repository source target.

### Cross-Repo References

No configured sibling repository is required for this module.

## Runtime assets without a skill copy

`sync_runtime_assets` removes each retired coordinator startup file (`install.experiment.RETIRED_STARTUP_TARGETS`: `AGENTS.md`, `system/AGENTS.md`, `tasks/AGENTS.md`) from the coordination root, or prints the removal under `dry_run`, and then replaces the provider assets; it writes no instruction file. No helper copies a skill tree, because a coordination-root or `.codex` skill folder would be a second distribution surface with no reader.

- The runtime-asset sync that writes no skill tree. [3]

- The sync removes the retired coordinator startup files before replacing provider assets [5]


- The benchmark scaffold creates the central `logs/mcp` and `logs/providers/...` directories beside provider data and runner roots. [4]
