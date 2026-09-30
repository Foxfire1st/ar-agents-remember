# mcp/tests/test_knowledge_closeout_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_closeout_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:09:38+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R09@v2's evidence: the currentness rules, the packet's examples, the per-kind dispatch, and the gate at each
route (18 collected cases, 1,198 lines).** The fixture is a converted leaf on real Git repositories: two invariants of
one family (`INV-AAAAAA` with entries on `land` and `keep` in `pkg/a.py`, `INV-BBBBBB` with `sibling` in `pkg/b.py`),
the official `main` line in both repositories and the leaf's own `leaf` branches, so the parent line's memory tip and
the leaf's own memory commits are different commits. Registered in the `unit-regression` lane
(`test-evidence-lanes.toml:122`). The fixture world is module-local, by the dependency-ownership census's rule (a
separate support module was an unregistered evidence artifact on the worker's first integration run);
`test_knowledge_gate_routes.py` imports it.

## Code Commentary

### Logic

- **The fixture world (`Gated`, `build_gated`).** `contract_path` writes the leaf's series contract; helpers write
  history rows (`invariant_row`, `family_row`, `trace_rows`), re-anchor entries after a code edit (`reanchor`), and
  evaluate the gate (`gate()`, with or without an explicit tip). `_open` maps open-item findings by their head.
- **Cases:**
  1. `test_a_leaf_is_ready_only_once_current_rows_answer_every_item_and_a_new_edit_reopens_two`: the packet's
     conforming example, the non-conforming "covers one of two" (open, "does not cover RLZ-A00002"), and the first
     boundary: editing `land` again after the rows makes `RLZ-A00001` stale, and the count returns to 2 (the invariant
     row and the family row).
  2. `test_a_sibling_whose_meaning_changed_after_the_family_row_reopens_the_family`: the second boundary, "INV-BBBBBB
     (examined at 1, now 2)"; the partial cover reports "members without a current invariant row".
  3. `test_a_new_invariant_needs_no_row_and_admission_judges_it_new_against_the_parent_line`: no item for
     `INV-CCCCCC`, the family row must examine it, and a record committed on the leaf branch with a reference-only
     justification is refused `R27.2-new-record` (the L27 carry).
  4. `test_items_are_recomputed_from_the_new_base_after_a_sync`: a row at revision 1 against K_C revision 2 reopens.
  5. `test_an_incomplete_run_is_one_finding_naming_its_input_never_an_unhandled_error`: a `SubprocessError` at the
     outer recompute and inside the run (`tree_difference_observation`) names `git`; an unreadable `leaf.json` gives
     exactly one finding, `leaf task document` (the L03 and L11 carries).
  6. `test_every_registered_kind_is_decided_by_its_own_predicate_never_a_generic_lookup`: `set(GATE_PREDICATES) ==
     set(ITEM_KINDS)`; a counted onboarding change passes where `satisfying_row` finds nothing; unreadable sidecars;
     covered and uncovered unexplained items; planned items; reconsideration (D29); two item IDs with one subject; an
     unknown kind is open.
  7. `test_the_gate_runs_the_validator_and_its_history_row_rule`: a hand-edited `after` and a ghost subject are
     refused by `R09-history-rows` where rule 2 alone would pass, `R22.3-markers` too; the leaf's own file closed by
     hand is no waiver (review R1 F1; the assertion was flipped and the test renamed).
  8. `test_the_closeout_validator_refuses_until_the_gate_passes_and_never_runs_ungated`: through the real
     `require_current_curator_coherence`; `ports(gate=False)` refuses with `GATE_UNBOUND`.
  9. `test_the_closeout_memory_commit_closes_the_history_file_and_validates_its_exact_tree`: an R22.3 refusal before
     `begin_git_mutation`, then the commit with `closed: true` and the `Code-Commit` trailer.
  10. `test_direct_landing_gates_names_its_leaf_closes_its_history_and_restores_on_refusal`.
  11. `test_record_landing_checks_the_landed_memory_commit_is_closed_and_valid`: not closed, closed, no commit named,
      a marker violation, and an earlier leaf commit judged new.
  12. `test_a_master_or_checkpoint_landing_waits_until_no_entry_at_a_changed_path_is_stale`.
  13. `test_an_insertion_only_hunk_is_linked_only_by_a_candidate_range`: K_C drops `RLZ-A00001` and a line is inserted
      inside `land`; the hunk (0 old lines) is unlinked and raises `unexplained_hunk` (the L10 N3 carry).
  14. `test_an_unconverted_leaf_is_not_gated_at_any_route`: every route helper returns `None` with no services bound,
      including `_close_gated_leaf` (the memory repository's `count-objects` and `status` unchanged); a leaf that
      deletes the marker is still gated.
  15. `test_the_prepared_closeout_path_fails_closed_on_converted_memory`: both entry points refuse with
      `prepared-closeout-knowledge-history-unclosable` (gap 3).
  16. `test_the_gate_memo_reuses_a_verdict_only_for_the_identical_inputs` (gap 4).
  17. `test_a_kept_pass_is_recomputed_once_an_endpoint_s_approval_state_changes`, parametrised "v1 approved" and
      "manifest missing" (ruling 15:09:25).

### Conventions

- Real Git repositories under `tmp_path`, with a pinned environment (`git` helper); no network.
- The case budget: 18 collected cases; the file is at 1,198 lines, 2 under the 1,200 limit (review R1 note 14: the
  next case needs a split).

### Invariants And Boundaries

- The module pins MIK-R09 rules 1-8 and the carried obligations as the worker's obligation table lists them; the
  worker's mutation sets (26, 37 and 4, plus the reviewer's) are killed by it together with
  `test_knowledge_gate_routes.py`.

### Todos

- Split the module before the next case (1,198 of 1,200 lines).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries).

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: a converted leaf on real repositories. | "The fixture below is a converted leaf on real repositories" | mcp/tests/test_knowledge_closeout_gate.py:1-7 |
| The fixture world. | `Gated`; `build_gated` | mcp/tests/test_knowledge_closeout_gate.py:195-312; mcp/tests/test_knowledge_closeout_gate.py:331-374 |
| Rule 2 and the packet's examples. | `test_a_leaf_is_ready_only_once_current_rows_answer_every_item_and_a_new_edit_reopens_two`; `test_a_sibling_whose_meaning_changed_after_the_family_row_reopens_the_family` | mcp/tests/test_knowledge_closeout_gate.py:404-487 |
| New invariants, recompute after a sync, incomplete runs, the dispatch. | `test_a_new_invariant_needs_no_row_and_admission_judges_it_new_against_the_parent_line`; `test_every_registered_kind_is_decided_by_its_own_predicate_never_a_generic_lookup` | mcp/tests/test_knowledge_closeout_gate.py:490-667 |
| The validator's history-row rule at the gate. | `test_the_gate_runs_the_validator_and_its_history_row_rule` | mcp/tests/test_knowledge_closeout_gate.py:675-701 |
| The closeout validator and the closeout memory commit. | `test_the_closeout_validator_refuses_until_the_gate_passes_and_never_runs_ungated`; `test_the_closeout_memory_commit_closes_the_history_file_and_validates_its_exact_tree` | mcp/tests/test_knowledge_closeout_gate.py:731-845 |
| Direct, record, master and checkpoint landing. | `test_direct_landing_gates_names_its_leaf_closes_its_history_and_restores_on_refusal`; `test_a_master_or_checkpoint_landing_waits_until_no_entry_at_a_changed_path_is_stale` | mcp/tests/test_knowledge_closeout_gate.py:865-970 |
| The insertion-only symmetry, the unconverted leaf, the prepared path. | `test_an_insertion_only_hunk_is_linked_only_by_a_candidate_range`; `test_an_unconverted_leaf_is_not_gated_at_any_route`; `test_the_prepared_closeout_path_fails_closed_on_converted_memory` | mcp/tests/test_knowledge_closeout_gate.py:978-1046 |
| The memo and the approval state. | `test_the_gate_memo_reuses_a_verdict_only_for_the_identical_inputs`; `test_a_kept_pass_is_recomputed_once_an_endpoint_s_approval_state_changes` | mcp/tests/test_knowledge_closeout_gate.py:1049-1198 |
| The lane row. | "mcp/tests/test_knowledge_closeout_gate.py" | mcp/tests/test-evidence-lanes.toml:122-122 |

## Cross-Repo References

No meaningful cross-repo references found: the fixture builds its own repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:09:38+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): created this card for the new test module MIK-R09 adds, recording gaps 3 and 4 (14:38:47), the approval-state test (15:09:25), the F1 flip (16:07:55) and review R1 note 14 (split before the next case). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
