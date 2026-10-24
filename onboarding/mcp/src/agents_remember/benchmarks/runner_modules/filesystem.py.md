# mcp/src/agents_remember/benchmarks/runner_modules/filesystem.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Filesystem mutation helpers for benchmark workspace setup and runtime asset
exposure.

## Code Commentary

### Logic

`filesystem.py` owns safe path removal, copying packaged
runtime/provider assets, rendering root markers, creating benchmark-local
coordination scaffolding. Skills reach the workspace harness from the tool server's
package copy; no benchmark-local skill tree is written. Cross-platform long-path normalization (the Windows
`\\?\` prefix logic) is no longer inlined here; both `removable_path` and the
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

`sync_runtime_assets` writes the instruction targets and the provider assets only. `replace_tree`, `copy_workspace_skill_exposure` and `sync_workspace_skill_exposure` are removed, because a coordination-root or `.codex` skill folder would be a second distribution surface with no reader.

- The runtime-asset sync that writes no skill tree. [3]

- Current source account and its stated boundaries. [4]
