# mcp/tests/tool_answer_l111_test_support.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Share the answer-table row type, deterministic task/landing/role illustration rows, and independent answer-versus-detail measurement helpers. This is support, not an executable acceptance verdict.

## Code Commentary

`ToolAnswerRow` distinguishes interim/unshaped rows from field-and-use-bearing shaped rows; the defaulted `production_paths` field lets owners identify live proof paths separately from illustrations. `_apply_l111_shaped_rows` builds operation-specific task-document rows, ordinary and waited message rows, and the remaining owned tools from their declared field sets and product bounds, with no L111 interim owner. Fixed synthetic cases demonstrate shape/scale; their labels are not a universal largest-input proof.

The location splitter recursively removes absolute-path string values from mappings, including mappings inside lists; a bare list string remains content. The target helper separately asserts location-free content tokens, at most two distinct location values, and the entire delivered answer against its unchanged bound. Paths are measured, not normalized into shorter roots.

The delegating spy captures post-validation wholes at `finalize_tool_response` before projection, without replacing product behavior. Detail readback compares the complete parsed mapping to that independent whole and enforces the existing detail-file byte budget; it does not assert raw JSON formatting equality or impose a delivered-token ceiling on the file. Deleting a dropped field or changing a retained value is tested by the consuming discriminator tests, not by executing this support file itself.

The task-document illustration now includes `put_open_question` in `_L111_TASK_DOC_UPDATED`, with the synthetic text `put_open_question applied`. This is an operation-specific updated-answer example, not proof of task ownership, concurrent keyed publication or a live operation result.

## Evidence

- Shared table rows distinguish authored illustrations and live proof paths. [1]
- Mapping values are split recursively; bare list strings remain content. [2]
- Content target, distinct locations and whole delivered bound are three independent measures. [3]
- The spy captures independent validated wholes at the real finalizer seam. [4]

- Detail identity is complete parsed-mapping equality under the file's byte budget. [5]


- Owned tool/operation rows retain fields, uses and product bounds without an L111 interim entry. [6]


- The updated-answer illustration supplies the put_open_question operation text; it is not a live task-document publication result. [7]
