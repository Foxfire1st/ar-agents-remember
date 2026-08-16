# mcp/src/agents_remember/benchmarks/runner_modules/analysis.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/analysis.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a`
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

JSONL and run-output analysis helpers for benchmark results.

## Code Commentary

### Logic

`analysis.py` parses Codex JSONL event payloads by event type: it sums per-turn token usage from `turn.completed` events' `usage` object, counts `command_execution` items and captures the latest `agent_message` text as the final answer from `item.completed` events, still scans payloads for error/stderr strings, loads per-run metadata, groups rows by prompt/variant, and renders `summary.md` tables.

### Invariants And Boundaries

- This module parses benchmark output only; it must not run Codex or mutate benchmark workspaces.
- The set of usage token keys (`USAGE_TOKEN_KEYS`) lives in `constants.py` so event parsing stays data-driven.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | "from agents_remember.benchmarks.runner_modules.analysis import *" | mcp/src/agents_remember/benchmarks/runner.py:11-11 |
| The route-local overview summarizes how this module fits into the benchmark runner split. | `# mcp/src/agents_remember/benchmarks/runner_modules Overview` | onboarding/mcp/src/agents_remember/benchmarks/runner_modules/overview.md:1-137 |
| Benchmark behavior is covered through the existing worktree/tool test slices. | `WorktreeSupportTests`, "test_benchmark_provider_ids_follow_selected_variants" | mcp/tests/test_worktree_support.py:767-842; mcp/tests/test_worktree_support_benchmark.py:114-114 |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-08-04T18:25+02:00 — 260731-EFA-L6 S18-B17 curator: corrected the test-slice ranges — the
  `WorktreeSupportTests` class extent had overshot into the next class (573-3049 → 573-3093) and
  the benchmark-provider-ids test citation pointed past its method (3125-3125 → 3167-3226, inside
  `BenchmarkRunnerPortabilityTests`). Claim wording unchanged.
- 2026-08-03T02:55:58+02:00 — W3-B04 curator: curated 3 table citations (3 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-05-31T12:30+02:00 — Rewrote Logic/Invariants for type-driven event parsing: per-turn `usage` summing via `USAGE_TOKEN_KEYS`, typed `command_execution`/`agent_message` items, fixed `TOKEN_KEYS`→`USAGE_TOKEN_KEYS` citation (1.0.0 review remediation).
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
