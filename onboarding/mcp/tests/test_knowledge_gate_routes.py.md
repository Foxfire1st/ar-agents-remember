# mcp/tests/test_knowledge_gate_routes.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R09 at every public route entry, and the fixes of the L09 reviews (28 test functions, 1,074 lines).** Review
R1 finding 5 found that deleting any route's gate call left the suites green, because the refusal tests called
private helpers. Each route test here enters through the route's own entry point, so removing the route's gate call
fails it: worktree closeout (`external_closeout_commits`), direct landing apply and preview (`direct_landing`), record
landing (`record_landing_result`), and the master and checkpoint landing (`_handover_or_apply_integration`). The
fixture world is `test_knowledge_closeout_gate.py`'s (`build_gated`, `_series`, …), imported. Registered in the
`unit-regression` lane (`test-evidence-lanes.toml:123`). The two sync-merge cases live in
`test_knowledge_validator_routes.py` instead, beside that module's `SyncFixture` cases: importing either into this
module would have added governed consumer rows to `evidence-lifecycle.toml`, whose bytes the dependency-ownership
census pins.

## Code Commentary

### Logic

- **Fixtures:** `world`, `ports` (the default validator and gate bound), `_answer` (current rows for every item),
  `_record` (a record-landing request), `_closeout` (the external closeout with only the journal hooks stubbed),
  `_configured`/`_land` (a configured, located series for `direct_landing(config, request, series)`), `_admitted`,
  `_receipts`, `_cancel`, `_commits`, `_history`, `_contradicting_row`, `_incomplete` and `_lost_line_range`.
- **Route entries (R1 F5):**
  - `test_the_worktree_closeout_refuses_restores_the_file_and_commits_it_closed_once_valid` (F2): a marker violation
    is refused, `begin_git_mutation` never runs, the file's open bytes are back; once repaired, the commit holds the
    file with `closed: true` and the same rows.
  - `test_record_landing_refuses_through_its_route_entry`;
    `test_the_master_and_checkpoint_landings_refuse_through_the_integration_route`;
    `test_direct_landing_preview_and_apply_refuse_through_their_route_entry` (including two open files, M20).
- **F1:** `test_a_hand_closed_leaf_file_is_refused_at_closeout_validation_and_record_landing` (a row whose `after`
  contradicts K_C, after R2-1 made the ghost subject refuse everywhere).
- **F3 and R2-2 (the direct landing's closing):** `test_an_input_conflict_or_a_failed_create_restores_the_closed_file`;
  `test_an_exact_retry_of_an_in_flight_generation_reaches_it_before_the_gate` (the retry resumes with
  `_close_gated_leaf` patched to fail if called); `test_cancelling_the_generation_restores_the_file_it_closed_but_never_a_later_edit`
  (N04); `test_another_generation_s_request_never_replaces_a_kept_closing` (N12, the reviewer's L96/L97 sequence);
  `test_a_closing_kept_by_a_call_that_ended_before_the_create_is_restored_at_the_next_apply` (N05);
  `test_an_unreadable_closing_receipt_is_a_named_refusal_at_apply_and_at_cancel` (R2-5; the worker is never
  terminated); `test_a_closing_the_memory_line_already_holds_is_never_restored`, parametrised over `sha1` and `sha256`
  memory repositories (R3-1; kills N16 and a hardcoded-SHA-1 mutation).
- **F4:** `test_a_timed_out_blob_read_or_an_unverifiable_entry_refuses_a_master_landing`.
- **R2-1 and the scoping:** `test_a_hand_committed_closed_history_file_with_a_ghost_subject_is_refused_at_master_landing`
  (N21); `test_a_sibling_s_file_closed_in_the_base_is_not_re_anchor_checked_at_a_leaf_route` (N01);
  `test_the_closeout_s_exact_tree_re_anchor_checks_the_file_it_has_just_closed` (N08) and
  `test_the_direct_landing_s_exact_tree_re_anchor_checks_the_file_it_has_just_closed` (N09).
- **R2-3 and R3-2:** `test_a_code_object_that_is_unavailable_is_named_and_keeps_the_item_findings` (an unavailable
  grammar, at the gate and at `net_stale_entries`); `test_a_recorded_blob_the_store_lacks_is_named_at_its_real_raise_site`
  (the worklist stays complete, the item open with "RLZ-A00003 is unverifiable (the blob eeee…)", no incomplete finding;
  kills N20); `test_a_git_failure_asking_for_a_recorded_blob_is_incomplete_and_never_kept` (`cat-file -e` exits 128:
  incomplete, naming Git's error; two evaluations, two `_evaluate` calls).
- **F6:** `test_the_routes_judge_a_leaf_s_earlier_record_new_against_the_parent_line`;
  `test_the_memo_key_holds_the_parent_tip`.
- **F7:** `test_record_landing_on_unconverted_memory_never_reads_the_landed_commit` (`would-record`).
- **F9 and notes:** `test_a_git_read_that_fails_inside_a_predicate_or_the_validator_is_never_a_verdict`;
  `test_a_marker_probe_git_cannot_answer_is_never_unconverted_memory` (an unreadable candidate tree, a missing official
  branch, a timed-out probe at `leaf_gate_refusal`); `test_every_file_read_is_in_the_read_set_and_a_conflicting_read_is_never_kept`.
- **L37: three gate guards pinned (the L09 review R4 carry, N23 to N25).**
  `test_a_git_failure_asking_for_a_recorded_blob_is_named_by_the_trees_and_the_lane`: `CodeTrees.has_blob` names
  a Git failure as its own input (N24), and the reviewer lane reads it `unavailable` with that reason, never
  raising (N23). `test_an_unwritable_closing_receipt_restores_the_file_and_admits_nothing`: direct landing
  restores the history file to its open bytes when the closing receipt cannot be written (N25). Each fails under
  its mutation.
- **L37: a hand-closed file landed later.** `test_a_hand_closed_leaf_file_is_refused_at_closeout_validation_and_record_landing`
  also lands the bad file one commit later, as an empty child and as a merge commit: both are refused with
  `R09-history-rows`. A parent that holds the file closed freezes nothing; only a closeout the contract records
  does.

### Conventions

- Mutation evidence: the worker's `fixr1-mutate.py` (26 killed), `r2-mutate.py` (37 killed) and `r3-mutate.py` (4
  killed), plus the reviewer's `mutate2.py`/`mutate3.py` (N01, N04, N05, N08, N09, N12, N16, N20 killed), all under
  `notes/reports/260928-MIK-L09-evidence/` of the task.

### Invariants And Boundaries

- Every public route that commits or lands memory has a refusal test entered through its own entry point (the carried
  L22 obligation: a refusal test at each route).

### Todos

- None.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries).

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: each route test enters through its own entry point. [1]

- F1 and the worktree closeout, record, master and checkpoint route entries. [2]

- Direct landing's route entries and its closing across calls. [3]
- Master landing refuses anything not current; ghost subjects; the scoping. [4]
- The exact trees re-anchor-check the file they just closed; an unavailable object. [5]
- The admission base, the memo key and record landing on unconverted memory. [6]
- Git failures, probes and the read set. [7]
- R3-1 and R3-2. [8]
- The lane row. [9]

- A Git failure asking for a recorded blob is named by the trees and the lane. [10]
- An unwritable closing receipt restores the file and admits nothing. [11]

- A hand-closed file is refused also one commit later and through a merge. [12]

### Cross-Repo References

No meaningful cross-repo references found: the fixture builds its own repositories.

No cross-repo boundary is crossed by this file.
