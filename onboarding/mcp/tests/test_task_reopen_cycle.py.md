# mcp/tests/test_task_reopen_cycle.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pins the seven transitions MIK-R210@v2 legalises on one disposable world each, with no branch, ref,
archive or document written by hand: every step calls the entry point a registered tool calls.

## Code Commentary

### Logic

The archived-leaf cases start from a completed, landed, cleaned-up, archived leaf:
`test_a_completed_landed_cleaned_up_archived_leaf_reopens_and_its_seats_start` (:223) reopens it and
seats its roles, `test_worktree_start_with_the_arguments_task_reopen_names_succeeds` (:273) proves the
returned start arguments are the ones that work, `test_a_second_task_reopen_on_a_reopened_leaf_answers_reopened`
(:295) proves a repeated reopen answers `reopened` without changing anything, and
`test_three_complete_and_reopen_cycles_of_the_same_leaf_each_succeed` (:321) drives the same leaf
through three complete cycles under one id.

The master cases are the series half: `test_a_leaf_of_a_master_that_names_itself_as_parent_starts`
(:351) starts a leaf whose series contract records the master's own name as its parent,
`test_a_completed_master_reopens_from_the_sprint_line_and_its_leaf_follows` (:383) reopens a completed
master from its sprint's integration line and starts its leaf afterwards, and
`test_a_leaf_without_its_master_and_a_master_without_its_sprint_name_it` (:446) proves the refusal names
the file that is missing.

The cycle's completion is written the way the cleanup's archive records it (`worktree_cleanup` plus its
external archive), published and collected through `terminal_archive_required_result`, never by writing
archive bytes: what these cases pin is the reopen and the start, while closeout, integration and cleanup
have their own modules. That is a source-account limit, not a claim that a closeout ran here.

Two further cases pin the two reopen-path refusals ruling 7dc3b6d2 found in the D515 sandbox:
`test_a_master_whose_leaf_landed_again_proves_its_chain_without_a_task_file_edit` (:592) re-lands a leaf
that had already landed, reopens and lands it again, and proves the master's closeout chain accepts the
later position on its own line instead of demanding a contract-cell edit;
`test_a_completed_master_with_cleanup_pending_passes_the_cleanup_gate` (:632) completes a master whose
cleanup was never run and proves the reopen collects it rather than refusing. Both drive the same public
entry points as the cases above.

### Invariants And Boundaries

- A test declaration is evidence of its assertions, not an execution or acceptance receipt.
- This module owns no acceptance and no production behaviour; it drives the public entry points on a
  disposable world and records what they answered.

## Evidence

### Docs References

No external Domain Documentation source governs these repository-owned cases.

### Repo-Internal References

The module's own cases are the evidence; each class covers one arm of the reopen and start path.


- The archived-leaf class drives reopen, the named start arguments, a repeated reopen and three cycles. [1]



- The master class drives the self-named parent, the master reopen from its sprint line, and the refusal that names the missing file. [2]
