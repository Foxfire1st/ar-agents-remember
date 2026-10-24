# mcp/tests/test_tool_answer_table.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the tool-answer table (MIK-R108 rules 3, 4, 6, 7 and 8): every registered tool has an authored row and no
row is an extra, a task-document row covers every operation, every row passes its gates without a bound above the
exception maximum, and no row is attributed to a leaf that no longer owns it. The three largest answers are
operation-produced and pinned rather than authored.

## Code Commentary

### Logic

The rows come from `tool_answer_table_support` and the shaped cases from `tool_answer_l109_cases`; the cases read
the table through `models.tools.tool_answer` and compare it with the live registration in
`models.tools.tool_registry`.

- **Coverage.** `test_every_registered_tool_has_an_authored_row_and_no_extras` and
  `test_missing_authored_row_fails` keep the table equal to the roster, and
  `test_task_doc_row_covers_every_operation` requires one task-document row to cover every operation.
- **Gates.** `test_every_row_passes_the_gates` runs each row through its checks, and
  `test_no_bound_above_the_exception_max` keeps every bound under the exception maximum;
  `test_exception_table_first_rows` and `test_interim_rows_hold_the_bound_and_name_a_leaf` cover the exception and
  interim rows, with an interim row naming the leaf that still owns it.
- **Shaping.** `test_curator_coherence_row_is_shaped` keeps the coherence row shaped, and
  `test_field_allowlist_mechanism` proves the field allowlist works as a mechanism rather than as a list.
- **Ownership.** `test_each_later_leaf_still_owns_rows`, `test_no_row_names_l112`,
  `test_no_built_row_names_the_landed_l110` and `test_no_row_names_l109` keep a row from claiming a leaf that has
  landed, and `test_l109_shaped_rows_are_the_table_rows` keeps the shaped rows the table's own rows.
- **Largest production.** `L109LargestProductionTests` requires the largest `read_ar_files`, `knowledge_read` and
  `knowledge_diff` answers to be produced by the operation and pinned, with `_pinned()` reading the pinned case.

### Conventions

A row is checked through the same gates the answer uses at delivery, so a row that would only look right in a
table is caught.

### Invariants And Boundaries

- The table and the registered roster are the same set.
- A bound is a token ceiling under the exception maximum, and the largest cases are produced, never authored.

## Evidence

- The table covers every registered tool with no extras and each task-document row covers every operation. [8]
- The three largest answers are operation-produced and pinned. [9]

- Table construction retains each row's fields, uses, cases, bound and interim ownership. [1]
- Cases are checked against missing uses, extra fields and bounds. [2]
- An explicitly over-long log path becomes its exact length and digest. [3]
- Produced install answers read the sandbox MCP authority, without an XDG user-settings precondition. [4]
- The delivery observer patches record_tool_completed and compares delivered tokens with returned and logged counts. [6]
- Ordinary and largest install fixtures pin copiedFiles=18 and createdDirs=44/43 as projection-equality fixtures under the existing answer bounds. [7]
