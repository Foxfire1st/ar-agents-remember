# mcp/tests/test_canvas_explainer.py

## Governing Overview

[Route overview](overview.md)

## Purpose

One leaf's explainer environment: exact detached worktrees with the binding written last, an Update that reuses those worktrees, a Retire that ends the seat's processes and leaves a receipt, and path confinement that holds planted links.

## Code Commentary

- A build checks out both bound trees as registered detached worktrees. It checks the bound contents, creates inputs and stages, and ends with `bound`.
- An unchanged Update answers `current` and leaves the binding bytes untouched; a moved one reuses both registered worktrees at the new exact trees and leaves no snapshot directories.
- Retire is judged by both process counts and by the receipt it leaves behind, and its preview touches nothing.
- A symlink planted in the workspace is held rather than followed, and a receipt id carrying a separator or a traversal is refused.
- Signalling matches exact markers and re-checks a process's start time before it is signalled.

The Build test checks the copied task’s leaf ID, the exact requirement text, and the manifest’s selected report paths and SHA-256 values. The moved Update test checks that missing input and stage folders are recreated, the task copy is present, the new packet replaces the old one, and the stage file retains its text.

## Evidence

- The case `test_a_build_checks_out_both_bound_trees_and_binds_last` checks exact registered detached worktrees and the binding being the last write.
- The case `test_an_unchanged_update_answers_current_and_writes_nothing` protects an unchanged Update answering current without touching the binding. [2]
- The case `test_a_moved_update_reuses_both_registered_worktrees` checks that a moved Update retains both worktree registrations, checks out the new trees and leaves no snapshot directories.
- The case `test_a_symlink_in_the_workspace_is_held_and_reported` protects a planted workspace symlink being held rather than followed. [5]

- The case `test_retire_ends_the_seats_processes_and_leaves_a_receipt` protects Retire ending the seat's processes by both counts and leaving a receipt.
- The case `test_process_matching_and_signalling_use_exact_markers_and_start_time_identity` protects signalling only on exact markers and a matching start time.

- Retired at the fifth freeze d59c3493: mcp/tests/test_canvas_explainer.py:192-231 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/tests/test_canvas_explainer.py:442-489 - the region it cited is not in the file at the candidate and no re-point was possible; mcp/tests/test_canvas_explainer.py::test_a_build_writes_the_bound_trees_and_binds_last - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/tests/test_canvas_explainer.py::test_a_moved_update_links_unchanged_files_and_removes_the_old_snapshot - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.

- Build checks out registered detached worktrees and creates the standard workspace directories. [6]
- Update reuses the registered worktrees and moves them to the new tree identities. [7]
- The selected-leaf manifest includes the exact active, archived and closed reports and cited measurements. [8]

- Moved Update checks task-copy presence, replacement of the old packet, recreation of missing folders and preservation of the existing stage file content. [9]
