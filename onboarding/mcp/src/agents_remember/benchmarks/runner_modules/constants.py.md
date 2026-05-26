# mcp/src/agents_remember/benchmarks/runner_modules/constants.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/constants.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T02:26+02:00                     |
| lastVerifiedCommitHash | `a7e160cd4381245327da7c5a52e2272b3080ebf7` |
| lastVerifiedCommitDate | 2026-05-26T02:40:22+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Shared benchmark constants for paths, provider ids, token aliases, Codex policy, and MCP registration names.

## Code Commentary

### Logic

`constants.py` centralizes values that multiple benchmark modules need, including supported benchmark providers, `.codex` paths, sandbox modes, and benchmark MCP names.

### Invariants And Boundaries

- Constants should stay declarative. Add behavior to a named owner module instead of expanding this file into a utility grab bag.

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
