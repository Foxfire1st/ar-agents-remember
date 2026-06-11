# mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-30T21:51+02:00                     |
| lastVerifiedCommitHash | `825a172bdf0d4ee3489ae25dbcc19c4e9c7b9493` |
| lastVerifiedCommitDate | 2026-05-30T17:31:45+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Benchmark-local MCP/Codex registration and generated provider setup settings.

## Code Commentary

### Logic

`mcp_registration.py` writes `.codex/mcp` settings and `.codex/config.toml`,
builds benchmark `McpRuntimeConfig`/lifecycle settings, names provider
containers per case, derives benchmark transcript roots under `logs/mcp`,
derives provider log roots under `logs/providers/<provider>/<instance>`, and
calls package-local provider setup with generated settings. Generated
`timeoutCaps` use the current `providerSetupSeconds` key (renamed from
`providerSeconds`).

### Invariants And Boundaries

- Benchmark provider authority comes from generated MCP/provider settings, not coordinator `system/settings.json`.
- Benchmark provider instances should use the same central `logs/` layout as
  workspace and worktree provider instances.
- Temporary provider settings must be deleted after setup attempts.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | [runner.py](agents-remember/mcp/src/agents_remember/benchmarks/runner.py) |
| The route-local overview summarizes how this module fits into the benchmark runner split. | [runner_modules overview](agents-remember/mcp/src/agents_remember/benchmarks/runner_modules/overview.md) |
| Benchmark behavior is covered through the existing worktree/tool test slices. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-05-30T21:51+02:00: Documented that benchmark-generated `timeoutCaps` now use the renamed `providerSetupSeconds` key (was `providerSeconds`). Verified against `825a172`.
- 2026-05-28T12:32+02:00: Updated after benchmark-generated MCP/provider settings moved logs under `logs/mcp` and `logs/providers/`.
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
