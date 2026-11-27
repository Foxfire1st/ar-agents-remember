# mcp/src/agents_remember/application/knowledge_writer/row_tests.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Validates hand-off row test-evidence fields (`testsRun`, `testsNotRun`, `noProofRecorded`), enforces the consolidation-task requirement that every rule row record how it was checked, and records reached `consolidationSubjects` onto consolidation history documents.

## Code Commentary

`read_row_tests(raw)` picks any present `TEST_KEYS` from a raw hand-off row and validates them through `ConsolidationEvidence.model_validate`, returning `(named_dict, [])` or `({}, formatted_refusals)`. `misplaced_tests_refusal(row, tests)` refuses test keys on any row whose subject resolves (via `row_kind_for_subject`) to a kind other than `invariant` or `family`. `missing_rule_tests_refusal(row, consolidating)` refuses a rule row in a consolidation task (`consolidating=True`) unless at least one of `testsRun`, `testsNotRun`, or `noProofRecorded` is truthy. `consolidation_subjects_of(items)` extracts the sorted unique subjects of `CONSOLIDATION_KIND` persisted worklist items, and `with_consolidation_subjects(document, subjects)` writes `document["consolidationSubjects"]` when non-empty.

## Relationships

Called by `knowledge_writer/handoff.py` (`TEST_KEYS`, `read_row_tests`) and `knowledge_writer/authoring_rows.py` (`consolidation_subjects_of`, `misplaced_tests_refusal`, `missing_rule_tests_refusal`, `with_consolidation_subjects`). Depends on `knowledge_worklist.consolidation.CONSOLIDATION_KIND`, `models.knowledge_files.history.row_kind_for_subject`, and `models.knowledge_files.history_consolidation.ConsolidationEvidence`.

## Evidence

- `read_row_tests` extracts `TEST_KEYS` from raw row input and validates their shape through `ConsolidationEvidence.model_validate`. [1]
- `misplaced_tests_refusal` rejects test-evidence keys on rows whose subject is neither an `invariant` nor a `family`. [2]
- `missing_rule_tests_refusal` refuses rule rows in a consolidation task that omit all of `testsRun`, `testsNotRun`, and `noProofRecorded`. [3]
- `consolidation_subjects_of` collects the sorted distinct subjects of `CONSOLIDATION_KIND` worklist items for persistence on the history file. [4]
