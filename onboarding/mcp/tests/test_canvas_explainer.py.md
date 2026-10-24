# mcp/tests/test_canvas_explainer.py

## Governing Overview

[Route overview](overview.md)

## Purpose

One leaf's explainer environment: a snapshot equal to the bound trees with the binding written last, an Update that links what it can, a Retire that ends the seat's processes and leaves a receipt, and confinement that holds planted links.

## Code Commentary

- A build writes every blob of both bound trees, counts them against git's own count, and ends with `bound` as its last step.
- An unchanged Update answers `current` and leaves the binding bytes untouched; a moved one links the unchanged files, writes the changed ones and removes the snapshot it replaced.
- Retire is judged by both process counts and by the receipt it leaves behind, and its preview touches nothing.
- A symlink planted in the workspace is held rather than followed, and a receipt id carrying a separator or a traversal is refused.
- Signalling matches exact markers and re-checks a process's start time before it is signalled.

## Evidence

- The case `test_a_build_writes_the_bound_trees_and_binds_last` protects the snapshot equalling the bound trees and the binding being the last write. [1]
- The case `test_an_unchanged_update_answers_current_and_writes_nothing` protects an unchanged Update answering current without touching the binding. [2]
- The case `test_a_moved_update_links_unchanged_files_and_removes_the_old_snapshot` protects a moved Update linking unchanged files and removing the snapshot it replaced. [3]
- The case `test_a_symlink_in_the_workspace_is_held_and_reported` protects a planted workspace symlink being held rather than followed. [5]

- The case `test_retire_ends_the_seats_processes_and_leaves_a_receipt` protects Retire ending the seat's processes by both counts and leaving a receipt. [4]
- The case `test_process_matching_and_signalling_use_exact_markers_and_start_time_identity` protects signalling only on exact markers and a matching start time. [6]
