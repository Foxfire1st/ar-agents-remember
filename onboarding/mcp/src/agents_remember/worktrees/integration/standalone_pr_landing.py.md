# mcp/src/agents_remember/worktrees/integration/standalone_pr_landing.py

## Governing Overview

[integration overview](overview.md)

## Purpose

Defines the shared contract eligibility predicate, finalize/cleanup readiness blockers, and abandoned-contract landing-record refusal for pull-request-landed standalone masters. Centralizing these checks keeps `finalize`, `worktree_cleanup`, and `worktree_record_landing` aligned on the exact same contract boundary.

## Code Commentary

- `PR_STRATEGY` (`"pr"`) names the `integration.strategy` value recorded for pull-request landings; `CONTRACT_ABANDONED_CODE` (`"contract-abandoned"`) names the refusal code returned when recording a landing on an abandoned contract or task document.
- `is_pr_landed_standalone_candidate(contract)` matches only series contracts (`kind == "series"`) with `integration_strategy == "pr"`, `integration_status == "completed"`, and `closeout_status != "completed"`. Callers still verify `sprint_ref is None` through `integration_branch_authority` so sprint-commanded masters, leaves, checkpoints, and already closed-out series stay on their existing routes.
- `pr_landed_standalone_blockers(contract, *, master_status)` computes readiness blockers without requiring `closeout_status == "completed"` or `code_commit`:
  - `master-abandoned` when `master_status == "abandoned"` or `contract.cleanup == "abandoned"`;
  - `landed-commit-missing` when `integrated_code_commit` is empty, or when `memory_mode == "external"` and `_external_memory_landed(contract)` is false (missing `integrated_memory_content_commit`, missing memory repo/source branch, or memory commit not an ancestor of `memory_source_branch`);
  - `not-landed-on-target-branch` when `integrated_code_commit` is present but not an ancestor of `code_source_branch`;
  - `memory-carryover-incomplete` when `guidance.carryover_done(contract)` is false.
- `abandoned_contract_reason(contract)` returns an operator-facing refusal sentence with `task_reopen` guidance when `contract.cleanup == "abandoned"` or when `_contract_task_status(contract)` reads `"abandoned"`. `_read_task_status` returns `None` when the task document is missing or unreadable (`OSError` or `ValueError`), so missing/unreadable documents fall through to the caller's existing checks rather than being misclassified as abandoned.

## Relationships

- Imported by `mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py` (`_require_series_task_terminal` `worktree_cleanup` branch), `mcp/src/agents_remember/worktrees/modules/finalize.py` (`_readiness`), and `mcp/src/agents_remember/worktrees/modules/record_landing.py` (`record_landing_result`, `PR_STRATEGY`, `CONTRACT_ABANDONED_CODE`).
- Reads Git ancestry via `worktrees/modules/git.py::is_ancestor`, carryover state via `worktrees/modules/guidance.py::carryover_done`, and task-document status via `tasks/store.py::read_task_doc` and `tasks/leaf_doc.py::find_leaf_doc`.
- Exercised by `mcp/tests/test_standalone_master_pr_finalize.py`.

## Evidence

- `PR_STRATEGY` and `CONTRACT_ABANDONED_CODE` define the shared PR strategy label and abandoned-contract refusal code. [1]
- `is_pr_landed_standalone_candidate` matches only non-closed-out series contracts with `integration_strategy == "pr"` and `integration_status == "completed"`. [2]
- `pr_landed_standalone_blockers` and `_external_memory_landed` compute `master-abandoned`, `landed-commit-missing`, `not-landed-on-target-branch`, and `memory-carryover-incomplete` without requiring `closeout_status == "completed"` or `code_commit`. [3]
- `abandoned_contract_reason`, `_read_task_status`, and `_contract_task_status` refuse abandoned contracts and task documents while leaving missing or unreadable documents to existing checks. [4]
