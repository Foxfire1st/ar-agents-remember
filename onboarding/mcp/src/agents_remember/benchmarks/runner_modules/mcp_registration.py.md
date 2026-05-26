# mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T02:26+02:00                     |
| lastVerifiedCommitHash | `a7e160cd4381245327da7c5a52e2272b3080ebf7` |
| lastVerifiedCommitDate | 2026-05-26T02:40:22+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Benchmark-local MCP/Codex registration and generated provider setup settings.

## Code Commentary

### Logic

`mcp_registration.py` writes `.codex/mcp` settings and `.codex/config.toml`, builds benchmark `McpRuntimeConfig`/lifecycle settings, names provider containers per case, and calls package-local provider setup with generated settings.

### Invariants And Boundaries

- Benchmark provider authority comes from generated MCP/provider settings, not coordinator `system/settings.json`.
- Temporary provider settings must be deleted after setup attempts.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | [runner.py](agents-remember-md/mcp/src/agents_remember/benchmarks/runner.py) |
| The route-local overview summarizes how this module fits into the benchmark runner split. | [runner_modules overview](agents-remember-md/mcp/src/agents_remember/benchmarks/runner_modules/overview.md) |
| Benchmark behavior is covered through the existing worktree/tool test slices. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
