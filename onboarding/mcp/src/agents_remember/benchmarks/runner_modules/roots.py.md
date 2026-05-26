# mcp/src/agents_remember/benchmarks/runner_modules/roots.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/roots.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T02:26+02:00                     |
| lastVerifiedCommitHash | `a7e160cd4381245327da7c5a52e2272b3080ebf7` |
| lastVerifiedCommitDate | 2026-05-26T02:40:22+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Benchmark root resolution context manager.

## Code Commentary

### Logic

`roots.py` chooses an explicit benchmark root when supplied or opens the packaged source root and yields its bundled `benchmarks/` directory.

### Invariants And Boundaries

- Packaged benchmark fallback belongs here so CLI and MCP callers share one root-selection contract.

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
