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
coordination scaffolding, and exposing skills into the benchmark
`.codex/skills` tree. Cross-platform long-path normalization (the Windows
`\\?\` prefix logic) is no longer inlined here; both `removable_path` and the
copy helpers delegate to the shared `long_path` helper imported from
`agents_remember.install.assets`. The benchmark runtime scaffold creates central
`logs/mcp` and `logs/providers/...` directories alongside provider data and
runner roots.

### Invariants And Boundaries

- Copy/remove helpers are benchmark workspace mechanics, not general repository mutation policy.
- Benchmark workspaces should mirror the MCP runtime log layout with central
  `logs/` directories instead of legacy `providers/logs`.
- Skill exposure remains copy-only or disabled; no shell/symlink installer fallback belongs here.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
- The route-local overview summarizes how this module fits into the benchmark runner split. [2]

### Cross-Repo References

No configured sibling repository is required for this module.
