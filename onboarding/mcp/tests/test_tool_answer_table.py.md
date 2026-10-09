# mcp/tests/test_tool_answer_table.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The rule-6 contract table population for MIK-R108: one row per registered tool and per `task_doc` operation (fields with caller uses, ordinary/largest cases, bounds, interim ownership), the short-form guard behavior, the daily-line/redaction/append transaction, and the row gate itself.

## Code Commentary

### Logic

- `ToolAnswerRow` carries a row's fields, uses, cases, bound and interim leaf; `validate_row_case` fails missing rows, extra fields, unused fields, over-bound cases and bounds over twice the largest case.
- Guard classes pin the measured short form (fixed part, location fit, error cut, late-failure re-guard, envelope strip, recursive list cap through retained items).
- Log classes pin one whole line per call, concurrent non-interleaving appends, counted stalls, raised-call logging with terminating-operation destinations, and credential redaction (keys, short credential-variable values, ordinary values, home paths).
- Row-gate classes pin shaped-row acceptance, empty-use failure, invalid-code rejection and guard-hit failure.

### Invariants And Boundaries

- The table is the contract L109–L112 build their per-tool answers against; a registered tool without a row fails.
- Interim rows (bound 4000, no fields) name exactly one of L109–L112; a leaf does not land while a row names it.

## Evidence

- Each row carries fields, uses, cases, bound and interim ownership. [1]
- Rows are validated against missing uses, extra fields and over-bound cases. [2]
