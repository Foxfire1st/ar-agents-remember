# mcp/tests/test_tool_answer_table.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The rule-6 contract table population for MIK-R108: one row per registered tool and per `task_doc` operation (fields with caller uses, ordinary/largest cases, bounds, interim ownership), and the row gate. The frozen source still includes `ToolAnswerGuardTests` and `ToolAnswerLogTests`; separate guard/log modules coexist with these table-local classes rather than replacing them.

## Code Commentary

### Logic

- `ToolAnswerRow` carries a row's fields, uses, cases, bound and interim leaf; `validate_row_case` fails missing rows, extra fields, unused fields, over-bound cases and bounds over twice the largest case.
- L110 memory/coherence rows are imported from `tool_answer_l110_rows`; they are authored final rows,
  not interim L110 allowances. Shared runtime witnesses derive ordinary/largest cases from real
  results; the common table validates field/use and bound contracts.
- Row-gate classes pin shaped-row acceptance, empty-use failure, invalid-code rejection and guard-hit failure. Table-local `ToolAnswerGuardTests` and `ToolAnswerLogTests` retain their own assertion populations alongside the separate guard/log modules; no source extraction or fresh execution is implied.

### Invariants And Boundaries

- The table is the contract L109–L112 build their per-tool answers against; a registered tool without a row fails.
- `AUTHORED_INTERIM_OWNERS` explicitly includes `retire_child` and `role_start_set`
  under L100, matching the product's interim owner declarations. The builder creates
  only declared rows; the roster gate still rejects any registered tool without one.
  Native `retire_child` is no longer asserted to be a removed tool.
- Interim rows (bound4000, no fields) name their explicit current owner; L100 joins
  the retained L109/L111 interim populations. L110's ten retained tools and L112's
  retained tools keep their final rows. A leaf does not land while a row names it.

## Grant answer row scope

The added direct_execution_grant row belongs to the interim answer contract; its map/roster assertions are structural evidence, not L94 completion or full-final answer acceptance. Retained final-row exceptions and historical counts remain attributed.

## Evidence

- Each row carries fields, uses, cases, bound and interim ownership. [1]
- Rows are validated against missing uses, extra fields and over-bound cases. [2]
