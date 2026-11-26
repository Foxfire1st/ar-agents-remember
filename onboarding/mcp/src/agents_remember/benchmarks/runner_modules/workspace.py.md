# mcp/src/agents_remember/benchmarks/runner_modules/workspace.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Benchmark workspace and repository preparation orchestration.

## Code Commentary

### 260731-EFA-L2 Preparation And Workspace Objects

`prepare_case(preparation, case)` takes a `BenchmarkPreparation` carrying `benchmarks_root`, `dry_run`, and `force_clone` (`skill_exposure_mode`, `provider_timeout`, `allowed_provider_ids`, `filter_benchmark_provider_ids`, and `prepare_configured_providers` are removed). Once the roots are laid down, `prepare_case` builds one **`BenchmarkWorkspace`** (case, with-memory root, coordination root, source repo root, memory repo) and hands it to `write_benchmark_mcp_registration(workspace, dry_run=dry_run)`.

### Logic

`workspace.py` derives source-only and with-memory workspace paths, prepares Git checkouts, renders benchmark AGENTS files, syncs runtime assets, writes MCP registration, and prepares memory repos.


### Invariants And Boundaries

- Workspace preparation is case setup, not Codex execution.
- Path derivation must stay manifest-validated and relative to the benchmark root.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
The [route overview](overview.md) describes the benchmark runner split; it is a discovery companion rather than a repository source target.

### Cross-Repo References

No configured sibling repository is required for this module.

## Preparation writes no skill exposure

`prepare_case` syncs the runtime assets and no longer calls `sync_workspace_skill_exposure`, and no preparation object carries a skill-exposure mode: the workspace's harness reads the skills the tool server serves from its package copy, through the benchmark-local MCP registration this workspace writes.

- The case preparation that lays down assets and no skill exposure. [3]

- Current source account and its stated boundaries. [4]
