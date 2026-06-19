# mcp/src/agents_remember/benchmarks/runner_modules/workspace.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/workspace.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T02:26+02:00                     |
| lastVerifiedCommitHash | `4728fa846d20cffd3f25c34e072e41920b49461e` |
| lastVerifiedCommitDate | 2026-06-19T14:22:14+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Benchmark workspace and repository preparation orchestration.

## Code Commentary

### Logic

`workspace.py` derives source-only and with-memory workspace paths, prepares Git checkouts, renders benchmark AGENTS files, syncs runtime assets, writes MCP registration, prepares memory repos, and invokes configured provider setup. `prepare_case` calls `prepare_configured_providers` with no seed source: each benchmark stack indexes its own pinned fixture from scratch (hermetic-cold) rather than warm-starting from the live workspace.

### Invariants And Boundaries

- Workspace preparation is case setup, not Codex execution.
- Path derivation must stay manifest-validated and relative to the benchmark root.
- Benchmark provider setup is hermetic: `prepare_case` never passes a seed-source coordination root, so a benchmark run cannot start or clone the live workspace provider backends. Seeding from the live workspace previously cascaded a full re-embed across main and every worktree (task 260619).

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

- 2026-06-19T13:42: Benchmark provider setup is now hermetic — `prepare_case` passes no seed source, so each benchmark stack indexes its own pinned fixture from scratch and never starts/clones the live workspace provider backends (task 260619: that cross-stack disturbance had cascaded a full re-embed across main + every worktree).
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
