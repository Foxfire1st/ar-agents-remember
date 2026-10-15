# mcp/tests/test_review_read_latency.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Tests that a reviewer read does work in proportion to what changed and still answers what it answered
before. Every case enters through the ports the dashboard composes
(`cli.dashboard.serving_collaborators`) on the fixture world of `test_review_git_trees`: a live leaf with
an uncommitted code edit and an uncommitted knowledge edit. The asserted counts of resolutions, captures
and Git children do not depend on the machine. The module also exports the helpers `_ports`, `_live`,
`_query`, `_body` and `_unconverted_base` that the reviewer worklist test modules import.

## Code Commentary

- **One resolution.** A subject read resolves once and captures each worktree once; the unchanged resolve-time baseline stands for the remembered trees during the publication recheck. The recheck still refuses a candidate that moved while the review was composed.
- **Converted base.** A converted base tree that Git holds is not written again; each mismatched input
  and an absent tree are written again.
- **Leaf-wide view.** `test_the_leaf_wide_view_captures_nothing_itself_and_is_computed_once_per_comparison`
  wraps the collaborator `isolated_leaf_worklist`. The view passes the comparison's candidate trees as
  `candidate` and its base commits as `base`, takes no directory snapshot and no code capture of its own,
  and is computed once per comparison.
- **Never kept after a failure:** the current test recomputes each incomplete worklist and leaves its memo empty; a recovered complete worklist may then be kept. A changed or inconsistently read external input makes the remembered view unavailable. No memory-patch failure/recovery is asserted.
- **Unreadable task input.** `test_an_unreadable_task_input_is_observed_and_never_memoized_even_when_the_worklist_completes`
  makes one task JSON unreadable or absent. Because the computation runs in a child process, the test
  replays the same failure identity into the child's reply (`_reply` is wrapped). The complete answer is
  returned each time and no view is kept.
- **Edit during the computation.** `test_a_task_edit_restored_during_computation_refuses_and_the_next_read_uses_original_inputs`
  changes the leaf's task document while the worklist is computed and restores it afterwards, at three
  points of the lookup. The injected race repeats on every computation, so the view is computed twice and
  the answer is the refusal `inputs_changing` with the document as offending input and an action that says
  to retry. Nothing is kept, and the next read equals a fresh read of the original inputs.
- **Memo bounds.** The view memo holds at most `CAPACITY` entries at two population sizes, serves nothing
  older than `MAX_AGE_SECONDS`, never answers another key, and has no key for a recorded comparison or for
  a leaf whose memory head or parent tip cannot be read.
- **Retired knowledge-diff subjects:** the aggregate three-Git-question/per-file-parity and literal two-size patch-selection cases were removed from this module. Its nine current top-level test definitions retain resolution/capture counts, exact supplied candidate/base operands, no leaf memory-tree diff, observed task-read refusal/recovery, bounded memo reuse and freshness; no current literal aggregate patch proof is claimed.
- **Freshness.** A read after an edit shows the new content, also for a same-size rewrite in the second of
  the index write, and nothing composed is kept on the server.

The same-size, same-second Git rewrite scenario imports the single `rewrite_in_the_second_of_the_index_write` owner from [knowledge_index_test_support.py](knowledge_index_test_support.py.md). Its real clock alignment is the scenario's subject; the 120-second alignment guard does not assert scheduler speed. The original captured-tree/currentness assertions remain at this file's test owner.

## Evidence

- Historical removed aggregate three-Git-question/per-file-reference test, not current evidence.
- Historical removed literal-filename two-size patch test, not current evidence.

- The shared owner establishes a same-size rewrite in the index-write second. [19]

- The module docstring: the port every case enters through and the machine-independent counts. [6]
- The four review ports as the routes call them. [7]
- One resolution and the captures of one subject read. [8]
- The recheck refuses a moved candidate. [9]
- A held converted base tree is not written again. [10]
- The leaf-wide view passes the captured trees and base commits and is computed once. [11]

- An incomplete worklist recomputes and is not kept; the next complete worklist may be memoized, while changed/conflicting external-input observations cause misses. No memory-patch failure/recovery is asserted. [12]

- An unreadable or absent task input is observed and nothing is kept. [13]
- An edit restored during the computation is computed twice and answered as inputs_changing. [14]
- The memo's bounds and keys. [15]
- A read after an edit shows the new content.  Anchor: `test_a_read_after_an_edit_shows_the_new_content_and_nothing_composed_is_kept` [18]
- The leaf view is computed once per exact comparison [20]
- No diff invocation spans the two memory trees  Anchor: `memory_base` [21]
- The worklist gets the comparison's own candidate trees  Anchor: `isolated_leaf_worklist` [22]
