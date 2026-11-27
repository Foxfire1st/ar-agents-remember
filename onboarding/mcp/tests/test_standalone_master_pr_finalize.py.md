# mcp/tests/test_standalone_master_pr_finalize.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Integration tests for finalizing and cleaning up a pull-request-landed standalone master after `worktree_record_landing`, plus the `contract-abandoned` refusal in `worktree_record_landing`. Registered in the `integration` lane of `mcp/tests/test-evidence-lanes.toml`.

## Code Commentary

- `StandalonePrWorld` builds temporary Git code and converted external-memory repositories with atomic series masters starting from `cleanup: pending` and non-`Completed` (`inProgress`) status, optional PR merge + `worktree_sync_tool`, optional sprint attachment (`attach_sprint`), and optional child leaves (`make_leaf`).
- `test_pr_landed_standalone_master_end_to_end_records_finalizes_and_retires` runs `worktree_record_landing_tool` (dry run and apply), `lifecycle_finalize_task_tool` (dry run and apply), and `task_doc_tool(operation="retire_master")` (dry run and apply), asserting cleanup completion, branch deletion, `Completed` status with `completedAt`, vacant atomic-series activation, skipped finalize archive (`master-archived-only-by-retire`), and final archival into `0_archive/`.
- `test_pr_landed_standalone_master_is_directly_cleanable_before_completed` verifies direct `worktree_cleanup_tool` succeeds before `Completed` and leaves subsequent `lifecycle_finalize_task_tool` able to mark the master `Completed`.
- `test_finalize_cleanup_failure_leaves_master_document_unchanged` verifies an unmerged commit on the series work branch yields `cleanup-blocked` with `"Cleanup did not complete; task documents were not changed."` and leaves the master document `inProgress`.
- `test_finalize_refusals_for_missing_unlanded_and_abandoned_standalone_master` verifies finalize blockers for empty `integrated_code_commit` (`landed-commit-missing`), empty or unreachable external `integrated_memory_content_commit` (`landed-commit-missing`), unlanded code commit (`not-landed-on-target-branch`), `cleanup == "abandoned"` (`master-abandoned`), and abandoned master task document (`master-abandoned` on finalize, `master-not-completed` on direct cleanup).
- `test_checkpoint_sprint_master_and_pr_leaf_keep_todays_refusals` verifies checkpoints (`integration-not-complete`), sprint-attached masters (`closeout-not-complete`, `code-commit-missing`, `master-not-completed`), and PR-landed leaves without closeout (`closeout-not-complete`, `code-commit-missing`) keep their existing refusals.
- `test_record_landing_refuses_abandoned_contract_and_preserves_missing_doc` verifies `CONTRACT_ABANDONED_CODE` registration in `RECORD_LANDING_REFUSAL_CODES`, `contract-abandoned` refusal in dry run and apply without overwriting `cleanup: abandoned` (for both `not-started` and `completed` integration states, abandoned master documents, and abandoned leaf documents), and that a missing task document falls through to `commit-missing`.

## Relationships

- Exercises `standalone_pr_landing.py`, `integration_branch_authority.py`, `finalize.py`, `record_landing.py`, and `tool_answer_l111_test_support.py`.
- Registered in `mcp/tests/test-evidence-lanes.toml` (`integration`) and as an exact consumer of `_user_settings_guard.py`, `fixtures/repository_profiles/node/package-lock.json`, and `tool_answer_l111_test_support.py` in `mcp/tests/evidence-lifecycle.toml`. Membership declares test selection and dependency reachability, not execution.

## Evidence

- `StandalonePrWorld` creates series contracts starting from `cleanup: pending` and non-`Completed` master status, with helpers for sprint attachment and child leaves. [1]
- End-to-end test exercises `worktree_record_landing_tool`, `lifecycle_finalize_task_tool`, and `task_doc_tool` (`retire_master`) into `0_archive/`. [2]
- Direct cleanup before `Completed` and cleanup-before-task-documents failure ordering are each asserted. [3]
- Finalize refusals for missing/unlanded commits, abandoned state, checkpoints, sprint-attached masters, and PR-landed leaves are asserted. [4]
- Abandoned-contract refusal in `worktree_record_landing` and missing-document fallthrough are asserted alongside `RECORD_LANDING_REFUSAL_CODES`. [5]
