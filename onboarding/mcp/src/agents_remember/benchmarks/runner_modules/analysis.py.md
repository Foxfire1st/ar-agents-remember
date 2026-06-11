# mcp/src/agents_remember/benchmarks/runner_modules/analysis.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/analysis.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
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

| Finding | Source Path |
| --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | [runner.py](agents-remember/mcp/src/agents_remember/benchmarks/runner.py) |
| The route-local overview summarizes how this module fits into the benchmark runner split. | [runner_modules overview](agents-remember/mcp/src/agents_remember/benchmarks/runner_modules/overview.md) |
| Benchmark behavior is covered through the existing worktree/tool test slices. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-05-31T12:30+02:00 — Rewrote Logic/Invariants for type-driven event parsing: per-turn `usage` summing via `USAGE_TOKEN_KEYS`, typed `command_execution`/`agent_message` items, fixed `TOKEN_KEYS`→`USAGE_TOKEN_KEYS` citation (1.0.0 review remediation).
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
