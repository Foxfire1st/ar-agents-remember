# mcp/tests/test_explainer_planned.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The planned-mode page a planning leaf shows before any change: declared effects become planned rows, scope paths resolve at the code tip or are listed as text, and the page offers nothing that could start anything.

## Code Commentary

- Every declared effect appears as a `planned · <effect>` row, an existing subject showing its current statement and a new subject its hand-off label.
- A scope path resolves at the code tip; one that two tip files answer, or one whose packet text was not read, is listed as text instead of being guessed.
- The top line reads `planned · no changes`, only deterministic sorts are offered, and the payload counts no model turns and no agent starts.
- The module is pure: it imports no host, service or bridge.

## Evidence

- The case `test_the_document_is_a_real_task_document_and_its_effects_become_planned_rows` protects each declared effect becoming a planned row. [1]
- The case `test_an_existing_subject_shows_its_current_statement_and_a_new_subject_its_label` protects a current statement and a hand-off label being told apart. [2]
- The case `test_a_scope_path_two_tip_files_answer_is_listed_as_text` protects an ambiguous scope path being listed as text rather than resolved. [3]
- The case `test_only_deterministic_sorts_are_offered` protects the sorts being deterministic and free of judgment ordering. [4]
- The case `test_the_page_has_no_action_that_could_start_anything` protects the page carrying no action, no model turn and no agent start. [5]
- The case `test_the_module_imports_no_host_service_or_bridge` protects the planned payload staying a pure read. [6]
