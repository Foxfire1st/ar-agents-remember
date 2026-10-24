# mcp/tests/test_explainer_server.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The seat's own server judged at its mounted boundary: the kept authoring tools, the reads over the bound snapshot, the grade tools under the leaf's lock, and the report to the architect.

## Code Commentary

- The kept authoring tools still answer over this environment, and the packet is re-read at call time so an Update needs no restart.
- Every read names the snapshot and the binding it was read at, and a traversal, an absolute path, an unserved surface or a symlink is refused by name.
- The git reads answer exact ids, sizes and history, and refuse an option, a range, a worktree path or a foreign repository.
- A grade at a binding the environment has left is refused; a writer waits on the leaf's lock so neither writer loses keys.
- A report copies the developer's words byte for byte and delivers once; a delivery that holds or times out settles as its own terminal state.

## Evidence

- The case `test_the_kept_authoring_tools_answer_over_this_environment` protects the kept authoring tools answering over this environment. [1]
- The case `test_a_path_outside_the_admitted_surfaces_is_refused_by_name` protects a traversal, an absolute path, an unserved surface and a symlink being held. [2]
- The case `test_git_refuses_an_option_a_range_a_worktree_path_and_a_foreign_repository` protects the git reads refusing another program, a range, a worktree path and another repository. [3]
- The case `test_a_grade_at_a_binding_the_environment_left_is_refused` protects a grade at a binding the environment left being refused. [4]
- The case `test_render_publishes_ready_revision_with_derived_part_map_and_rereads_binding_under_frames_lock` protects a render publishing a ready revision with its derived part map and a lock-time binding re-read. [5]
- The case `test_production_report_delivery_routes_per_master_holds_limits_and_settles_transitions` protects report delivery routing per master and settling holds, limits and timeouts. [6]
