# mcp/tests/tool_answer_table_support.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The tool-answer table's rows, roster, validators and shared case helpers (MIK-R108 rules 3, 4, 6, 7 and 8): one table with a row for every registered tool and every operation of a tool that has operations, plus the authored roster and the gates every row must pass.

## Code Commentary

`build_tool_answer_table` returns the rule-6 table built only from the authored roster and the landed leaves' final rows, never synthesized from the registry: a tool without an authored entry has no row. `AUTHORED_INTERIM_OWNERS` names each interim row's leaf; the L109, L110 and L112 rows carry the shaped rows, their fields with caller-step uses, their authored bounds, and the ordinary and largest payloads the cases compare against. `ROW_CASE_FRAMEWORK_KEYS` lists what a case payload may hold outside a row's own fields. `check_tool_answer_roster` fails unless every registered tool has exactly one authored row; `validate_tool_answer_row`, `validate_row_case` and `_validate_shaped_row` are the gates, returning failure strings rather than raising so a case can assert every failure at once. `authored_row_owners`, `_big_blob`, `_server_info_case` and `_stub_config` are the remaining helpers, and `_L109_FIXTURES` points at the stored case directory.

## Invariants And Boundaries

Ownership is authored: a row without an owner would be a synthesized row, and a row whose owner has landed is a shaped row that must carry proven payloads. The bound is authored or taken from product data and validated against the measured largest case, not computed from it. This module holds no case of its own; the sibling case modules import it.

## Evidence

### Repo-Internal References

- The table is built from the authored roster and the landed final rows only, never synthesized from the registry. [1]

- The roster check requires exactly one authored row per registered tool, and the row gates return their failures rather than raising. [2]


- A shaped row's bound is authored or product-sourced and validated against its largest case, never computed from it, and its fields each carry a caller-step use. [3]

