# mcp/tests/test_memory_verdict_ref.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Pytest regression suite (13 test functions) verifying memory-review `verdictRef` file validation, collected `notes/reports/<rel>` mapping across closeout and direct landing, single-definition `COLLECTED_REPORT_DIRECTORY` usage across report collection, launch `taskReportRoot` producers, and archived-task state conversion (`memory/conversion/state_owners.py`), unmapped legacy reference reporting, and post-cleanup readability.

## Code Commentary

- Validates `role_reports.collected_report_ref` and `is_collected_report_ref` on valid relative paths, empty/traversal rejections, and non-collected inputs.
- Exercises `task_doc record_review` for memory rounds: accepts `notes/reports/<rel>` before the canonical copy exists when `<group>/role-reports/<rel>` exists, preserves omitted `verdictRef` and code-round rules, refuses fallback to a series contract when no leaf enclosure exists, and refuses bare, missing, escaping, and blank references on both ordinary and record-only paths while leaving the task JSON unchanged.
- Exercises closeout and direct landing across absolute `role-reports/`, relative `role-reports/`, relative `notes/reports/`, absolute `notes/reports/`, and legacy `task-reports/` alias forms to confirm history records store `notes/reports/<rel>`, foreign worktree groups never match, and unmappable pre-existing bare references stay as recorded and are named by both closeout/landing summaries and `committed_review_note`.
- Asserts `collect_group_reports` and `collected_report_ref` share `COLLECTED_REPORT_DIRECTORY`, runs both a static AST scan over all `taskReportRoot` producers in `mcp/src/agents_remember/` (`role_launch_enclosure.py`, `role_launch_workspace.py`) and runtime monkeypatch overrides proving enclosed-leaf, direct-leaf, and non-leaf `prepare_role_folders` follow `COLLECTED_REPORT_DIRECTORY` without creating `notes/reports`, and runs an AST/runtime check (`test_state_conversion_uses_shared_collected_report_ref_without_duplicate_literals`) proving `memory/conversion/state_owners.py::_durable_verdict_ref` shares `COLLECTED_REPORT_PARTS`, `ROLE_REPORT_DIRECTORY`, and `collected_report_ref` with zero hardcoded literals outside docstrings.
- Runs an end-to-end closeout, integration, and cleanup cycle recording an absolute worktree `verdictRef` and verifying the committed history record names `notes/reports/<rel>` and opens after worktree removal.
- Registered in `mcp/tests/test-evidence-lanes.toml` (`unit-regression`) and 9 consumer lists in `mcp/tests/evidence-lifecycle.toml`. Descriptions here summarize source assertions and catalog membership, not a live test run receipt.

## Relationships

- Exercises `worktrees/memory_verdict_ref.py`, `worktrees/role_reports.py`, `worktrees/review_fact_source.py`, `worktrees/modules/closeout_external.py`, `worktrees/review_note.py`, `application/task_docs/task_doc_route_review.py`, `cli/role_launch_enclosure.py`, `cli/role_launch_workspace.py`, and `memory/conversion/state_owners.py`.
- Listed in `mcp/tests/test-evidence-lanes.toml` and `mcp/tests/evidence-lifecycle.toml`.

## Evidence

- Tests `collected_report_ref`, `is_collected_report_ref`, `collect_group_reports`, static/runtime `COLLECTED_REPORT_DIRECTORY` sharing across every `taskReportRoot` producer, and `memory/conversion/state_owners.py` sharing with zero duplicate literals. [1]
- Tests memory `record_review` acceptance of pre-copy `notes/reports/<rel>`, bound-leaf-only resolution, and refusal of bare/missing/escaping references on ordinary and record-only paths. [2]
- Tests closeout and direct-landing mapping of valid and legacy-alias `verdictRef` forms to `notes/reports/<rel>` and rejection of foreign worktree groups. [3]
- Tests unmapped pre-existing reference preservation and closeout/direct-landing notes plus end-to-end closeout, integrate, and cleanup readability. [4]
