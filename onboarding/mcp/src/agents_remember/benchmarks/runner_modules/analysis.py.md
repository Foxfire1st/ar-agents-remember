# mcp/src/agents_remember/benchmarks/runner_modules/analysis.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

JSONL and run-output analysis helpers for benchmark results.

## Code Commentary

`range_text` filters numeric int/float observations, returns `n/a` for no numeric data, emits a single value when bounds coincide, otherwise formats `low - high`. It only formats the selected metric column. cit:([`range_text`], mcp/src/agents_remember/benchmarks/runner_modules/analysis.py:131-139).

### Logic

`analysis.py` parses Codex JSONL event payloads by event type: it sums per-turn token usage from `turn.completed` events' `usage` object, counts `command_execution` items and captures the latest `agent_message` text as the final answer from `item.completed` events, still scans payloads for error/stderr strings, loads per-run metadata, groups rows by prompt/variant, and renders `summary.md` tables.

### Invariants And Boundaries

- This module parses benchmark output only; it must not run Codex or mutate benchmark workspaces.
- The set of usage token keys (`USAGE_TOKEN_KEYS`) lives in `constants.py` so event parsing stays data-driven.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
- The route-local overview summarizes how this module fits into the benchmark runner split. [2]

### Cross-Repo References

No configured sibling repository is required for this module.
