# mcp/tests/test_worktree_status_running_operation.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Exercise the real status route with queued, running and finished lifecycle operations, distinguishing the compact answer from the saved whole result.

## Code Commentary

The fixture claims a closeout operation and calls the public status tool. The cases require a count and one kind/generation/state sentence for a queued or running operation, with no plural projection list in the answer. One operation stays below the answer bound without overflow or a cut hint. A second fixture retains both a queued closeout and a completed integration, then checks that the saved `lifecycleOperations` list equals every producer projection, including its nested fields. Phase status appears in the running sentence; finished operations contribute to the count without appearing as running.

## Evidence

- The public status answer carries a queued/running operation sentence and keeps the plural list out of that compact answer.
- The saved whole result retains the exact complete projection list.
- Phase text is preserved, and finished operations are not reported as running.

These are frozen-source assertion descriptions; this Curator ran no tests and supplies no execution receipt or review verdict.

- Source assertion: `test_the_saved_status_result_keeps_every_operation_projection`. [1]
- Source assertion: `test_a_status_answer_with_one_running_closeout_is_not_cut`. [2]
- Source assertion: `test_a_claimed_closeout_is_named_in_the_answer_the_guard_trims`. [3]
- Source assertion: `test_a_running_closeout_is_named_with_its_phase`. [4]
- Source assertion: `test_a_finished_closeout_is_not_named_as_running`. [5]
