# mcp/src/agents_remember/benchmarks/runner_modules/cli.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/cli.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T02:26+02:00                     |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a`
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | "from agents_remember.benchmarks.runner_modules.cli import *" | mcp/src/agents_remember/benchmarks/runner.py:12-13 |
| The route-local overview summarizes how this module fits into the benchmark runner split. | `# mcp/src/agents_remember/benchmarks/runner_modules Overview` | onboarding/mcp/src/agents_remember/benchmarks/runner_modules/overview.md:1-137 |
| Benchmark behavior is covered through the existing worktree/tool test slices. | `WorktreeSupportTests`, "test_benchmark_provider_ids_follow_selected_variants" | mcp/tests/test_worktree_support.py:767-842; mcp/tests/test_worktree_support_benchmark.py:114-114 |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-08-04T18:26+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the three malformed rows —
  facade re-export bound to the verbatim `from agents_remember.benchmarks.runner_modules.cli
  import *` literal (runner.py:12-13), the route overview cited as the memory card with its `#`
  heading anchor, and the test-slice row given the corrected `WorktreeSupportTests` /
  benchmark-provider-ids ranges (same correction as the analysis card). Spurious `agents-remember/`
  path prefixes dropped; claim wording unchanged.
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
