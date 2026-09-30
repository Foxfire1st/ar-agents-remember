# mcp/tests/test_knowledge_gate_routes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_gate_routes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:09:38+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R09 at every public route entry, and the fixes of the L09 reviews (27 collected cases, 992 lines).** Review
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

### Conventions

- Mutation evidence: the worker's `fixr1-mutate.py` (26 killed), `r2-mutate.py` (37 killed) and `r3-mutate.py` (4
  killed), plus the reviewer's `mutate2.py`/`mutate3.py` (N01, N04, N05, N08, N09, N12, N16, N20 killed), all under
  `notes/reports/260928-MIK-L09-evidence/` of the task.

### Invariants And Boundaries

- Every public route that commits or lands memory has a refusal test entered through its own entry point (the carried
  L22 obligation: a refusal test at each route).

### Todos

- None.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries).

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: each route test enters through its own entry point. | "Each route test enters through the route's own entry point" | mcp/tests/test_knowledge_gate_routes.py:1-7 |
| F1 and the worktree closeout, record, master and checkpoint route entries. | `test_a_hand_closed_leaf_file_is_refused_at_closeout_validation_and_record_landing`; `test_the_worktree_closeout_refuses_restores_the_file_and_commits_it_closed_once_valid`; `test_the_master_and_checkpoint_landings_refuse_through_the_integration_route` | mcp/tests/test_knowledge_gate_routes.py:157-279 |
| Direct landing's route entries and its closing across calls. | `test_direct_landing_preview_and_apply_refuse_through_their_route_entry`; `test_another_generation_s_request_never_replaces_a_kept_closing`; `test_an_unreadable_closing_receipt_is_a_named_refusal_at_apply_and_at_cancel` | mcp/tests/test_knowledge_gate_routes.py:342-548 |
| Master landing refuses anything not current; ghost subjects; the scoping. | `test_a_timed_out_blob_read_or_an_unverifiable_entry_refuses_a_master_landing`; `test_a_hand_committed_closed_history_file_with_a_ghost_subject_is_refused_at_master_landing`; `test_a_sibling_s_file_closed_in_the_base_is_not_re_anchor_checked_at_a_leaf_route` | mcp/tests/test_knowledge_gate_routes.py:556-640 |
| The exact trees re-anchor-check the file they just closed; an unavailable object. | `test_the_closeout_s_exact_tree_re_anchor_checks_the_file_it_has_just_closed`; `test_a_code_object_that_is_unavailable_is_named_and_keeps_the_item_findings` | mcp/tests/test_knowledge_gate_routes.py:654-723 |
| The admission base, the memo key and record landing on unconverted memory. | `test_the_routes_judge_a_leaf_s_earlier_record_new_against_the_parent_line`; `test_the_memo_key_holds_the_parent_tip`; `test_record_landing_on_unconverted_memory_never_reads_the_landed_commit` | mcp/tests/test_knowledge_gate_routes.py:731-785 |
| Git failures, probes and the read set. | `test_a_git_read_that_fails_inside_a_predicate_or_the_validator_is_never_a_verdict`; `test_a_marker_probe_git_cannot_answer_is_never_unconverted_memory`; `test_every_file_read_is_in_the_read_set_and_a_conflicting_read_is_never_kept` | mcp/tests/test_knowledge_gate_routes.py:802-884 |
| R3-1 and R3-2. | `test_a_closing_the_memory_line_already_holds_is_never_restored`; `test_a_recorded_blob_the_store_lacks_is_named_at_its_real_raise_site`; `test_a_git_failure_asking_for_a_recorded_blob_is_incomplete_and_never_kept` | mcp/tests/test_knowledge_gate_routes.py:893-992 |
| The lane row. | "mcp/tests/test_knowledge_gate_routes.py" | mcp/tests/test-evidence-lanes.toml:123-123 |

## Cross-Repo References

No meaningful cross-repo references found: the fixture builds its own repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:09:38+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): created this card for the new test module of the review R1 fix round (F5: one refusal test per public route entry, ruling 16:07:55), which also pins F1-F4, F6, F7, F9, R2-1 to R2-5 (17:59:48) and R3-1/R3-2 (19:16:07). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
