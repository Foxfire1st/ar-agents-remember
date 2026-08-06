# mcp/src/agents_remember/benchmarks/runner_modules/roots.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/roots.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T02:26+02:00                     |
| lastVerifiedCommitHash | `a3e43cb0877c18b9d2b0e6ada4eb5719a01f251f`
| lastVerifiedCommitDate | 2026-08-06T05:49:07+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | "from agents_remember.benchmarks.runner_modules.roots import *" | mcp/src/agents_remember/benchmarks/runner.py:23-23 |
| The route-local overview summarizes how this module fits into the benchmark runner split. | `runner_modules` | onboarding/mcp/src/agents_remember/benchmarks/runner_modules/overview.md:13-18 |
| Benchmark behavior is covered through the existing worktree/tool test slices. | "from agents_remember.benchmarks import runner as benchmark_runner" | mcp/tests/test_worktree_support.py:23-23; mcp/tests/test_worktree_support.py:3217-3239 |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 3 citation rows: the facade star-import (benchmarks/runner.py L23), the route-local overview card (onboarding runner_modules/overview.md L13-L18), and the worktree test slices (test_worktree_support.py L22 + L3097-L3121). Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
