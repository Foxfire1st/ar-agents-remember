# mcp/src/agents_remember/benchmarks/runner_modules/execution.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/execution.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T02:26+02:00                     |
| lastVerifiedCommitHash | `4728fa846d20cffd3f25c34e072e41920b49461e` |
| lastVerifiedCommitDate | 2026-06-19T14:22:14+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Codex benchmark execution policy, command construction, per-run metadata, and run orchestration.

## Code Commentary

### Logic

`execution.py` resolves `codex` from PATH, validates the allowlisted sandbox modes, writes per-run metadata, runs prompt variants, builds batches, executes them concurrently, writes summaries, and reports subprocess failures. `benchmark_mcp_config_overrides(cwd)` reads the benchmark workspace's `.codex/config.toml` `mcp_servers` table and emits `-c mcp_servers.<name>.<key>=<literal>` overrides (scalars, `env`, and `env_vars`), which `codex_command` appends so the benchmarked Codex talks to the benchmark's **own** isolated MCP server rather than inheriting the host workspace's MCP configuration.

### Invariants And Boundaries

- Codex execution remains benchmark-only host execution and must not accept arbitrary executable paths or shell snippets.
- `run_case()` is an orchestration wrapper; batching, dry-run replay, and failure collection live in focused helpers.
- The benchmarked Codex must be pointed at the benchmark's own MCP server via the generated `.codex/config.toml` overrides, so a benchmark run never drives the live workspace MCP/providers.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | [runner.py](agents-remember/mcp/src/agents_remember/benchmarks/runner.py) |
| The benchmark MCP registration writes the `.codex/config.toml` whose `mcp_servers` table these overrides read. | [mcp_registration.py](agents-remember/mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py) |
| Benchmark behavior is covered through the existing worktree/tool test slices. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-06-19T13:42: Added `benchmark_mcp_config_overrides()` and wired it into `codex_command`: it reads the benchmark workspace `.codex/config.toml` `mcp_servers` table and emits `-c mcp_servers.<name>.<key>=<literal>` overrides so the benchmarked Codex uses the benchmark's own isolated MCP server, not the host workspace's.
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
