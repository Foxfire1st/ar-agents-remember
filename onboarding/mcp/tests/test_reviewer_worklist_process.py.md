# mcp/tests/test_reviewer_worklist_process.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Tests of the reviewer's isolated worklist computation with real child processes: that the child gives the
same answer as the computation in the calling process, that every transport failure is an explicit refusal
which is not kept, how requests share and queue for children, that children and their Git processes never
outlive their requests or the dashboard, that a build mismatch asks for a restart, that reviewer diffs do
not depend on the user's Git configuration, that tree reads have their own threads, and that creating a
comparison pin is idempotent. The module is in the `integration` lane.

## Code Commentary

### Helpers

- The module uses the fixture `world` of `test_review_git_trees`, the helpers `_ports`, `_live`, `_query`,
  `_body` and `_unconverted_base` of `test_review_read_latency`, and `_child_script`, `_fresh_memo` and
  `_observations` of `test_reviewer_worklist_reads`.
- `_child_script(script)` replaces only the launch of the child module with `python -P -c <script>`, so a
  test can run a faulty or held child through the real process owner. `_REPLY` is the imported `WORKLIST_REPLY` script prefix that
  builds a reply with the right identity and no document. `held_child_script` keeps that child in flight until admission is observed and the test releases it.
- `_ask(owner, payload, answers, errors)` calls `owner.compute` and collects the answer or the error.
  `_children`, `_all_children`, `_gone` and `_wait_gone` read `/proc` to follow process trees. Those observation helpers, the lifetime scripts and the controlled-clock/executor fixtures live in [reviewer_worklist_process_test_support.py](reviewer_worklist_process_test_support.py.md).

### Parity and failures

- `test_real_child_parity_source_reads_and_held_conversion_at_two_result_sizes` runs the view at 1 and at
  180 extra changed files over an unconverted base. At each size the child's document and its recorded
  reads equal those of `leaf_worklist` in the calling process, the response body equals the body computed
  without a child, the child's process ID differs from the test's, its interpreter is the running one and
  its module path lies in its own package root, every read of the child is in the caller's recording, and
  the request carries the comparison's candidate trees and held base tree. A repeated read starts no child. The larger reply is
  more than 65,536 bytes. A child in which `paired_memory_commit`, `_captured_code`, `directory_snapshot`
  and both `converted_base_files` raise still gives the same body, so the child does no second capture,
  pairing or conversion.
- `test_real_child_transport_failures_are_explicit_uncached_and_recoverable` runs fourteen faulty children:
  truncated JSON, exit status 7, another request digest, another source digest, another module path, six
  kinds of invalid read rows, a complete document without reads, a large error stream with invalid output,
  and a `NaN` in the document. Each gives a `refused` answer whose detail names the worklist, leaves the
  memo empty and leaves no child running. Through the real route, a number that overflows to infinity is
  refused with status 200 and no worklist in the body, while `1e308`, `-1e308` and `-1e-400` are served
  and kept. A launch that fails is a `candidate_unresolved` refusal, nothing is kept, and the next read
  succeeds.
- `test_build_mismatch_asks_for_a_dashboard_restart`: a child that exits with status 75 and a reply with
  another source digest both give a refusal whose action says to restart the dashboard.
- `test_overload_is_its_own_refusal_code_with_a_true_action`: a `WorklistOverloaded` from the collaborator
  becomes a refusal with the code `reviewer_busy` and the action "the reviewer is computing other
  worklists; retry".

### Sharing, queue and bound

- `test_identical_requests_share_one_child_and_others_wait_for_one_of_two_slots`: four identical and three
  different requests start four children, never more than two at once; the four identical ones get equal
  answers that are four distinct objects; the owner is empty afterwards.
- `test_twelve_identical_concurrent_reads_share_one_child_without_a_refusal`: twelve identical requests,
  one child, no error.
- `test_the_waiting_bound_counts_computations_not_the_requests_sharing_them`: twelve sharers of one
  request join one child; seven further distinct requests bring the controlled barrier to nineteen
  waiting requests over eight computations, and the ninth distinct computation (the twentieth request)
  raises `WorklistOverloaded`. Nineteen answers come from eight children. The case primes the serving
  build on the caller thread and proves the cold resolution happens exactly once, on that thread; it is
  a deterministic barrier proof, not the historical load qualification, which remains unrun.
- `test_overload_is_refused_only_past_the_waiting_bound_or_the_deadline_and_says_so`: with the bound set
  to 4, four admitted computations visibly occupy two children and two queue positions. The fifth refuses without joining the queue. Advancing only the injected owner clock past its deadline then expires both child holders and both queued computations with their distinct refusal kinds and no retained child.
- `test_a_cancelled_requester_leaves_the_shared_child_to_the_others_and_the_last_reaps_it`: one of two
  requesters cancels and the other still gets the answer from the one child; a sole requester that cancels
  returns only after its child has ended.
- `test_a_request_arriving_while_a_cancelled_flight_is_reaped_starts_its_own_computation`: while the
  reaping of a cancelled flight is held open, a new identical request is answered by a second child.
- `test_four_concurrent_first_reads_answer_alike_from_one_child`: four threads read a new comparison at the
  same moment; all four answer `trees` with one identical body, and one child replied.
- `test_three_changed_leaves_opened_in_quick_succession_all_answer`: three different comparisons are read
  one after the other while children are held. The third is observed queued behind two live children before release; all three answer, three children ran and at most two at once.
- `test_the_requests_deadline_runs_from_its_arrival_and_the_child_gets_what_is_left`: with a deadline of 2
  seconds, injected pre-child work advances the owner clock by 1.2 seconds. The child receives exactly the remaining 0.8-second budget; further injected advancement produces the deadline refusal and reaps the child.

### Lifetime

- `test_actual_disconnect_deadline_shutdown_and_queue_reap_children`: through the real route, a client
  disconnect and an owner shutdown each end a child that is blocked in `git cat-file --batch`, and its Git
  process; a child that sleeps past a deadline of 0.2 seconds raises a deadline error and leaves no active
  process; with two computations running and a third waiting, a shutdown ends all three requests and both
  children.
- `test_the_child_and_its_git_children_end_at_its_own_deadline` (Linux only): a child armed with a
  deadline of 0.8 seconds and blocked in Git is killed with its Git process.
- `test_a_killed_dashboard_takes_the_child_blocked_in_git_and_its_git_process_with_it` (Linux only): a
  parent process runs the real owner and a child blocked in Git; after the parent is killed with
  `SIGKILL`, the child and its Git process are observed gone under the shared hang guard.

### Git configuration, executor, pin

- `test_the_reviewers_diff_reads_do_not_depend_on_the_users_git_configuration`: the leaf-wide view and the
  review are read once under an empty global Git configuration and once under one that sets
  `diff.noprefix`, `diff.mnemonicPrefix`, `diff.srcPrefix`, `diff.dstPrefix`, `diff.external`,
  `diff.renames`, `diff.colorMoved`, `color.ui` and `core.quotePath`. Both bodies are identical, and every
  patch starts with `diff --git a/`.
- `test_every_parsed_diff_names_its_own_prefix_colour_and_driver`: the two argument tuples of the source
  inventory hold `PARSED_DIFF_OPTIONS`, and the worklist's blob diff holds the prefix options, `--no-color`
  and `--no-ext-diff`.
- `test_a_busy_default_executor_cannot_delay_a_tree_read`: while the event loop's default executor
  has both real workers held and a third job queued, a request to the route answers while every executor job is still unfinished. Release and draining happen afterwards.
- `test_a_pin_another_reader_made_or_is_making_is_the_answer_not_a_refusal`: when the creation of a pin
  fails because another reader created the same pin, `_pin` succeeds and the ref is kept; a ref that names
  another tree is refused and not moved; a held ref lock is released only after the actual `update-ref` lock refusal is observed, and the retry succeeds.

## Evidence

- The child's document, reads and body equal the in-process computation at two sizes. [1]
- Fourteen faulty children, the numeric cases through the route, and a failed launch. [2]
- Disconnect, deadline, shutdown and a queued computation. [3]
- One route request stopped by a disconnect or a shutdown. [4]
- Identical requests share one child and others wait for one of two slots. [5]
- Overload only past the bound or the deadline. [6]
- A cancelled requester leaves the shared child to the others. [7]
- A build mismatch asks for a restart. [8]
- The overload's code and action at the view. [9]
- Four concurrent first reads answer alike from one child. [10]
- Three changed leaves in quick succession all answer. [11]
- The child's own deadline ends it and its Git process. [12]
- A killed parent takes the child and its Git process with it. [13]
- The hostile Git configuration changes no answer. [14]
- The pinned argument lists. [15]
- A busy default executor does not delay a tree read. [16]
- A pin another reader made is success; another tree is refused; a held lock is waited out. [17]
- A request arriving during the reaping of a cancelled flight starts its own computation. [18]
- Twelve identical reads share one child. [19]
- The deadline runs from the request's arrival. [20]
- The bound counts computations, not requests. [21]
- The process owner under test. [22]

- Owner-local time proves the remaining child deadline without an elapsed-speed assertion. [23]
