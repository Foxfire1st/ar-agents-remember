# mcp/src/agents_remember/benchmarks/runner_modules/cli.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/cli.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T02:26+02:00                     |
| lastVerifiedCommitHash | `a7e160cd4381245327da7c5a52e2272b3080ebf7` |
| lastVerifiedCommitDate | 2026-05-26T02:40:22+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Argparse command wiring for benchmark list, prepare, run, and analyze commands.

## Code Commentary

### Logic

`cli.py` converts command-line arguments into `BenchmarkPrepareRequest` and `BenchmarkRunRequest` service calls, prints captured messages, and handles user-facing parser errors.

### Invariants And Boundaries

- CLI functions are adapters; benchmark behavior belongs in service, execution, workspace, or analysis modules.
- Keep command payload shape aligned with the MCP service functions.

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
