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

- **One resolution.** A subject read matches a direct `read_knowledge_review` answer and has a judgment, resolves once and captures each worktree once; the unchanged resolve-time baseline stands for the remembered trees during the publication recheck. The recheck still refuses a candidate that moved while the review was composed.
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
  timings: before both lookups, between them, and absent-then-present. Only the between-lookups timing
  patches the parent's `leaf_expected_effects`, and the worklist computation runs in the child's own
  interpreter, so that callback cannot restore bytes inside the child's lookups. The injected race repeats
  on every computation, so the view is computed twice and the answer is the refusal `inputs_changing` with
  the document as offending input and an action that says to retry. Nothing is kept, and the next read equals a fresh read of the original inputs.
- **Memo bounds.** The view memo holds at most `CAPACITY` entries at two population sizes, serves nothing
  older than `MAX_AGE_SECONDS`, never answers another key, and has no key for a recorded comparison or for
  a leaf whose memory head or parent tip cannot be read.
- **Retired knowledge-diff subjects:** the aggregate three-Git-question/per-file-parity and literal two-size patch-selection cases were removed from this module. Its thirteen current top-level test definitions retain resolution/capture counts, exact supplied candidate/base operands, no leaf memory-tree diff, observed task-read refusal/recovery, bounded memo reuse and freshness; no current literal aggregate patch proof is claimed. The recorded leaf-view case reads a bound complete stored worklist as `persisted`, with the child's exact CRLF-byte identity imported into the parent. A missing worklist has source `absent`, no state or items, and an imported `ABSENT` identity; both readable outcomes retain code facts. Malformed JSON and a directory at the worklist path refuse with the observed byte or unreadable identity. None of these recorded reads enters `LEAF_VIEW_MEMO`.
- **Freshness.** A read after an edit shows the new content, also for a same-size rewrite in the second of
  the index write, and nothing composed is kept on the server.

The same-size, same-second Git rewrite scenario imports the single `rewrite_in_the_second_of_the_index_write` owner from [knowledge_index_test_support.py](knowledge_index_test_support.py.md). Its real clock alignment is the scenario's subject; the 120-second alignment guard does not assert scheduler speed. The original captured-tree/currentness assertions remain at this file's test owner.

## Evidence

- Historical removed aggregate three-Git-question/per-file-reference test, not current evidence.
- Historical removed literal-filename two-size patch test, not current evidence.

- The shared owner establishes a same-size rewrite in the index-write second. [19]

- The module docstring: the port every case enters through and the machine-independent counts. [6]

- The four review ports as the routes call them. [7]

- The recheck refuses a moved candidate. [9]
- A held converted base tree is not written again. [10]

- The leaf-wide view passes the captured trees and base commits and is computed once. [11]



- An incomplete worklist recomputes and is not kept; the next complete worklist may be memoized, while changed/conflicting external-input observations cause misses. No memory-patch failure/recovery is asserted. [12]


- An unreadable or absent task input is observed and nothing is kept. [13]
- An edit restored during the computation is computed twice and answered as inputs_changing. [14]
- The memo's bounds and keys. 

- A read after an edit shows the new content.  Anchor: `test_a_read_after_an_edit_shows_the_new_content_and_nothing_composed_is_kept` [18]



- The subject read matches direct read_knowledge_review composition, carries judgment, resolves once and captures each worktree once. [8]

- The live leaf view computes once for an unchanged exact comparison, with subsequent edits changing the computation key. [20]
- An explicit negative assertion forbids a diff invocation containing both comparison memory trees. [21]
- The worklist receives the comparison's candidate trees and base commits; it performs no directory snapshot or code capture of its own. [22]
- the recorded leaf-view declaration distinguishes persisted and absent worklists while retaining code facts, refuses malformed and unreadable inputs, checks read identities and leaves LEAF_VIEW_MEMO empty. [23]

## Comparison-aware live-read adapters

`Ports.entries` takes the optional comparison number; the existing warm/measured entry read passes `None`, and `_ports` supplies `None` before the summary observer. The measured capture, resolution, index and body assertions remain the same. These live-read adapter changes do not extend the budget assertion to two distinct numbered summary or entry comparisons.


## Recorded-answer reuse and object loss

Three further retained declarations cover recorded answers: identical closed-tree inputs reuse the composed tree-view body, a new comparison-directory input set composes again, and loss of a recorded root tree or descendant object invalidates the kept answer in favour of the matching cold result. The descendant parameter table exercises removal, unreadability and a truncated compressed blob whose header remains readable. These assertions already exist in the base; the optional comparison-argument adaptation did not add them.

- Entry and summary adapters provide the optional comparison argument. [24]
- The measured live entry read passes None and retains one-resolution/capture and index assertions.

- Retired at the fifth freeze d59c3493: mcp/tests/test_review_read_latency.py:229-274 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 9547923129aa0b49d6b4f93a758f4fce70233745; mcp/tests/test_review_read_latency.py::test_the_view_memo_is_bounded_by_count_and_by_age_and_never_answers_another_key - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 9547923129aa0b49d6b4f93a758f4fce70233745. Retired means the anchor no longer stands, not that the cited subject was deleted.
