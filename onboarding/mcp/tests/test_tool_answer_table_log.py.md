# mcp/tests/test_tool_answer_table_log.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The tool-call log cases: records and their fields, raised and refused calls, the terminating routes, the length and secret rules, pruning and the settings.

## Code Commentary

The records half requires a success line to hold the rule-3 fields, refused and raised calls to be logged, a refusal to carry its code and a SHA-256 `resultDigest` even when the returned answer preserves `ok: true`, a long argument to be replaced by its length and a digest, and credential fields and credential-like environment values to be masked. The cases include embedded, short, slash-bearing and path-looking credential values. Ordinary environment values stay in the logged arguments, and home-folder paths follow the ordinary length rule. Pruning touches only old tool logs, respects the day change and the keep-days setting, and leaves an enclosure's logs alone. A failing log write does not fail the call, no coordination root means no log and no failure, a custom absolute transcript root holds the line, detail and location, and the append is one whole line. Raised calls log through the production entry and still raise, including an unknown tool and a strict-argument refusal. The terminating routes (cleanup, abandon and finalize) log to the root and never into an enclosure, while an ordinary tool uses the live enclosure; a removed group falls back to the root. The settings cases pin the defaults, the parsing and bad-value refusals, and the stats command collects rows over a day span with its exit codes.

## Invariants And Boundaries

The log is evidence about a call and never a reason for one to fail: a write error answers a log error and keeps the call's result. A secret is omitted rather than shortened, and the length rule applies to ordinary path text without mistaking a home path for a secret. A terminating route must not write inside an enclosure it is about to remove.

## Evidence

### Repo-Internal References

- Refused and raised calls are logged, and a long argument becomes its length and digest rather than its text. [1]

- The logger masks credential fields and credential-like environment values. Ordinary environment values are retained, and ordinary home paths follow the length rule. [2]

- Cleanup, abandon and finalize log to the coordination root and never into an enclosure. [3]

- The log classifies refusal and retains the result digest even when the answer has ok true. [4]
