# mcp/src/agents_remember/worktrees/memory_verdict_ref.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Validates supplied memory-review `verdictRef` paths against existing files at recording time and maps qualifying references to task-relative `notes/reports/<rel>` for history closeout and direct landing.

## Code Commentary

- `memory_verdict_contract` returns the bound leaf `WorktreeContract` (preferring an explicit leaf contract or resolving `leaf_enclosure_path(task_root, doc_id)` for a `subTask`), never substituting a series contract.
- `require_bound_memory_verdict_ref` and `require_memory_verdict_ref` accept an omitted (`None`) `verdictRef` as before and otherwise require a usable path string naming an existing file in one of three accepted forms:
  1. an absolute path to an existing regular file;
  2. `role-reports/<rel>` confined inside `<worktree_group>/role-reports/`;
  3. `notes/reports/<rel>` confined inside `<task_root>/notes/reports/` or `<worktree_group>/role-reports/` (accepted before the copy exists because collection occurs at send or cleanup).
  Invalid, missing, or escaping paths raise `ReviewHistoryError(MEMORY_VERDICT_REF_INVALID, ...)` listing the accepted forms. Code rounds and route reviews are not checked here.
- `collected_verdict_ref` maps a usable `verdictRef` to `notes/reports/<rel>` via `role_reports.collected_report_ref` when the reference is already in collected form, uses relative `role-reports/<rel>` or legacy `task-reports/<rel>`, or is an exact relative path (`_exact_relative_to`, without folder-name substring search and never matching another worktree group) under `<worktree_group>/role-reports`, `<worktree_group>/task-reports`, or `<task_root>/notes/reports`. Pre-existing references that cannot be mapped return unchanged.
- `unmapped_verdict_ref_note(reference)` formats the closeout and landing sentence naming an unmapped pre-existing `verdictRef`.

## Relationships

- Called by `application/task_docs/task_doc_route_review.py::_record_task_review_bound` on every memory `record_review` transition (ordinary and record-only).
- Called by `worktrees/review_fact_source.py::_review_fact` (serving both `modules/closeout_external.py` and `direct_history_closing.py`) and by `modules/closeout_external.py::_review_note` and `worktrees/review_note.py::_history_review_note` for unmapped-reference reporting.
- Imports the single collected-form definition (`COLLECTED_REPORT_DIRECTORY`, `COLLECTED_REPORT_PARTS`, `ROLE_REPORT_DIRECTORY`, `LEGACY_ROLE_REPORT_ALIAS`, `collected_report_ref`, `is_collected_report_ref`) from `worktrees/role_reports.py`.

## Evidence

- `memory_verdict_contract` resolves only a bound leaf worktree contract and never returns a series contract. [1]
- `require_bound_memory_verdict_ref` and `require_memory_verdict_ref` enforce the three accepted file-existing forms for supplied memory `verdictRef` values and raise `review-verdict-ref-invalid` listing accepted forms. [2]
- `collected_verdict_ref` maps exact relative paths under the bound contract's `role-reports/`, legacy `task-reports`, or task `notes/reports/` to `notes/reports/<rel>` via `collected_report_ref` and returns unmappable references unchanged. [3]
- `unmapped_verdict_ref_note` produces the closeout and landing sentence naming a recorded `verdictRef` that could not map to `notes/reports/<rel>`. [4]
