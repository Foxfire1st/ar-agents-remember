# mcp/tests/test_task_intent_review.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The intent review between a new leaf and its first start: while the record reads pending or review-first, every start and the stage move itself are refused before anything is created, and a leaf without the field is an older leaf that is admitted.

## Code Commentary

- A replace that omits the field keeps it and a call that would drop it is refused, so no route can silently clear the review; only the architect among hosted seats may write it.
- Every gate refuses: the stage move to in progress, `worktree_start` before the enclosure exists, `worktree_attach`, and every leaf role's workspace resolution.
- A start that found a live enclosure makes the move as its last act, so the first seat's copies already read in progress, while a refused start moves nothing.
- The native go resolves to the exact retained revision's manifest and digest; a tampered manifest resolves unverified, and a symlink on the way is refused.
- A pending leaf is left out of ready and the master order shows it.

## Evidence

- The case `test_replace_keeps_the_field_it_omits_and_refuses_a_call_that_would_drop_it` protects the review field surviving a replace that omits it and refusing one that would drop it. [1]
- The case `test_a_move_to_in_progress_is_refused_while_the_review_is_open` protects the stage move being refused while the review is open. [2]
- The case `test_a_start_is_refused_before_the_enclosure_is_created` protects a start being refused before any enclosure is created. [3]
- The case `test_every_leaf_role_is_refused_before_any_enclosure_is_made` protects every leaf role's resolution refusing before an enclosure is made. [4]
- The case `test_a_found_live_enclosure_moves_the_leaf_and_its_master_row` protects a found live enclosure making the move as the resolution's last act. [5]
- The case `test_the_native_go_resolves_to_the_exact_retained_revision_manifest_and_digest` protects the go resolving to the exact retained revision and its sealed manifest digest. [6]
