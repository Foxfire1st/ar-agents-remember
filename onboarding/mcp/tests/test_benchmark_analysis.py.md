# mcp/tests/test_benchmark_analysis.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_benchmark_analysis.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                         |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_benchmark_analysis.py` pins the Codex event semantics that benchmark
JSONL metric extraction depends on (F9/F13). It guards `analyze_jsonl` against
drift in how a Codex run log maps onto the summary metrics so the benchmark
runner reports correct token, command, and final-answer figures.

## Code Commentary

### Logic

The tests import `analyze_jsonl` from
`agents_remember.benchmarks.runner_modules.analysis`. A local `_write_jsonl`
helper serializes a list of event dicts to newline-delimited JSON in a temporary
file, which `analyze_jsonl` then parses back into a metrics dict.

Three cases assert the Codex schema contract:

- The end-to-end case feeds a thread/turn lifecycle with two
  `command_execution` items, two `agent_message` items, and a single
  `turn.completed` carrying a `usage` object. It checks that token fields
  (`input_tokens`, `cached_input_tokens`, `output_tokens`,
  `reasoning_output_tokens`) come from `turn.completed.usage`, that
  `command_event_count` counts `command_execution` items, that `final_answer`
  is the text of the last `agent_message`, and that `event_count` counts every
  raw event.
- The multi-turn case proves token usage is summed across multiple
  `turn.completed` events rather than overwritten.
- The item-filtering case proves only `item.completed` `command_execution`
  items are counted: an `agent_message` and an `item.started` command are both
  excluded, leaving a single counted command.

### Conventions

Plain `unittest.TestCase` with `assertEqual`, run via `unittest.main()` under
`__main__`. Fixtures are built inline as Python dicts mirroring real Codex event
shapes and written to a `tempfile.TemporaryDirectory`, so no on-disk sample logs
are needed. Test names describe the contract they pin rather than the function
name.

### Invariants And Boundaries

- Tokens are sourced exclusively from `turn.completed.usage` and accumulate
  across turns.
- `command_event_count` counts only completed `command_execution` items;
  `item.started` events and non-command items do not contribute.
- `final_answer` is the last `agent_message` text seen, so ordering of
  `agent_message` events matters.
- The tests exercise metric extraction only; they do not cover run-root
  aggregation, grouping, or summary-markdown rendering in the same module.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `analyze_jsonl` and the per-event metric extraction under test live in the benchmark analysis module. | `analyze_jsonl` | mcp/src/agents_remember/benchmarks/runner_modules/analysis.py:96-100 |
| The token-key set summed from `turn.completed.usage` is defined in benchmark runner constants. | `USAGE_TOKEN_KEYS` | mcp/src/agents_remember/benchmarks/runner_modules/constants.py:19-24 |

## Update History

- 2026-08-03T03:09:46+02:00 — W3-B04 curator: curated 1 table citation (1 total), supplying the exact anchor and path; the scoped fixer generated the final extent.
- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
