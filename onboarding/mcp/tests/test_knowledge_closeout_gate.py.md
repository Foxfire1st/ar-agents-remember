# mcp/tests/test_knowledge_closeout_gate.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R09@v2's evidence: the currentness rules, the packet's examples, the per-kind dispatch, and the gate at each
route (17 top-level test definitions and 1,334 physical source lines by static inspection, not fresh pytest collection).** The fixture is a converted leaf on real Git repositories: two invariants of
one family (`INV-AAAAAA` with entries on `land` and `keep` in `pkg/a.py`, `INV-BBBBBB` with `sibling` in `pkg/b.py`),
the official `main` line in both repositories and the leaf's own `leaf` branches, so the parent line's memory tip and
the leaf's own memory commits are different commits. Registered in the `unit-regression` lane
(`test-evidence-lanes.toml:122`). The fixture world is module-local, by the dependency-ownership census's rule (a
separate support module was an unregistered evidence artifact on the worker's first integration run);
`test_knowledge_gate_routes.py` imports it.

## Code Commentary

### Logic

- **The fixture world (`Gated`, `build_gated`).** `contract_path` writes the leaf's series contract; helpers write
  history rows (`invariant_row`, `family_row`, `trace_rows(world, ...)`), re-anchor entries after a code edit
  (`reanchor`), and evaluate `gate()` with or without a tip. `trace_rows` recomputes the worklist and
  fills `sources` from each trace item's `sourceBlobs`; `_open` maps findings by their head.
- **Cases:**
  1. `test_a_leaf_is_ready_only_once_current_rows_answer_every_item_and_a_new_edit_reopens_two`: the packet's
     conforming example, the non-conforming "covers one of two" (open, "does not cover RLZ-A00002"), and the first
     boundary: editing `land` again makes `RLZ-A00001` stale and reopens four items: invariant, family,
     file trace and route trace. The unchanged `reopens_two` test name is not its current count; the
     source also asserts the file trace's "changed after" reason.
  2. `test_a_sibling_whose_meaning_changed_after_the_family_row_reopens_the_family`: the second boundary, "INV-BBBBBB
     (examined at 1, now 2)" and the touched sibling item, followed by readiness after current complete invariant/family rows. It does not assert a separate partial-cover stage.
  3. `test_a_new_invariant_needs_no_row_and_admission_judges_it_new_against_the_parent_line`: no item for
     `INV-CCCCCC`, the family row must examine it, and a record committed on the leaf branch with a reference-only
     justification is refused `R27.2-new-record` (the L27 carry).
  4. `test_items_are_recomputed_from_the_new_base_after_a_sync`: a row at revision 1 against K_C revision 2 reopens.
  5. `test_an_incomplete_run_is_one_finding_naming_its_input_never_an_unhandled_error`: a `SubprocessError` at the
     outer recompute and inside the run (`tree_difference_observation`) names `git`; an unreadable `leaf.json` gives
     exactly one finding, `leaf task document` (the L03 and L11 carries).
  6. `test_every_registered_kind_is_decided_by_its_own_predicate_never_a_generic_lookup`: registry/predicate
     parity; planned, reconsideration and family-route dispatch; repeated item IDs and unknown-kind refusal.
     `test_r53_kinds_are_decided_by_their_own_predicates` separately asserts counted-card edits alone
     leave onboarding open, current/stale source-bound rows and uncovered-trace binding, unreadable
     sidecars, membership candidate-revision currency and changed record-row revision/disposition.
  7. `test_the_gate_runs_the_validator_and_its_history_row_rule`: a hand-edited `after` and a ghost subject are
     refused by `R09-history-rows` where rule 2 alone would pass, `R22.3-markers` too; the leaf's own file closed by
     hand is no waiver (review R1 F1; the assertion was flipped and the test renamed).
  8. `test_the_closeout_validator_refuses_until_the_gate_passes_and_never_runs_ungated`: through the real
     `require_current_curator_coherence`; `ports(gate=False)` refuses with `GATE_UNBOUND`.
  9. `test_the_closeout_memory_commit_closes_the_history_file_and_validates_its_exact_tree`: an R22.3 refusal before
     `begin_git_mutation`, restoration of the open history bytes on refusal, then a controlled `RuntimeError("reached the commit")` at the mutation seam. The case checks history closure/restore and reaching that seam, not a successful product memory commit or committed trailer.
  10. `test_direct_landing_gates_names_its_leaf_closes_its_history_and_restores_on_refusal`.
  11. `test_record_landing_checks_the_landed_memory_commit_is_closed_and_valid`: not closed, closed, no commit named,
      a marker violation, and an earlier leaf commit judged new.
  12. `test_a_master_or_checkpoint_landing_waits_until_no_entry_at_a_changed_path_is_stale`.
  13. `test_an_insertion_only_hunk_is_linked_only_by_a_candidate_range`: K_C drops `RLZ-A00001` and a line is inserted
      inside `land`; the hunk (0 old lines) is unlinked and raises `unexplained_hunk` (the L10 N3 carry).
  14. `test_an_unconverted_leaf_is_refused_at_every_route_before_anything_moves`: leaf, landing and record guards return the central `legacy-format` refusal without bound gate services; `_close_gated_leaf` raises before capture, with memory objects and status unchanged. `leaf_worklist` remains `None`.
  15. `test_the_gate_memo_reuses_a_verdict_only_for_the_identical_inputs` (gap 4).
  16. `test_a_kept_pass_is_recomputed_once_an_endpoint_s_approval_state_changes`, parametrised "v1 approved" and
      "manifest missing" (ruling 15:09:25).
- **L37.** The closeout's memory commit now runs the gate too, so
  `test_the_closeout_memory_commit_closes_the_history_file_and_validates_its_exact_tree` commits its code edit first
  and answers the items that edit opens (`_answered`) before it closes the file. The memo test builds its key with
  the leaf's memory `HEAD` beside the parent line's tip.

### Conventions

- Real Git repositories under `tmp_path`, with a pinned environment (`git` helper); no network.
- Static source population: 17 top-level test definitions and 1,334 physical lines. Earlier 17-definition/18-case/1,206-line figures are historical; no pytest collection, execution or limit enforcement was performed here.

### Invariants And Boundaries

- Historical worker/reviewer mutation evidence (sets of 26, 37 and 4, plus the reviewer's) belongs
  to the named MIK-R09-era runs with `test_knowledge_gate_routes.py`; it is not fresh mutation
  proof for the added R53 predicate cases.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries).

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: a converted leaf on real repositories. [1]

- The fixture world. [2]


- The validator's history-row rule at the gate. [5]



- The closeout validator and the closeout memory commit. [6]



- Direct, record, master and checkpoint landing. [7]


- Insertion-only hunks link only by candidate ranges; ordinary unconverted leaf/landing/record and direct-closeout guards refuse before movement. [8]



- The memo and the approval state. [9]


- The lane row. [10]


- The memo key names the parent tip and the leaf's memory HEAD. [12]


### Cross-Repo References

No meaningful cross-repo references found: the fixture builds its own repositories.

No cross-repo boundary is crossed by this file.

- Rule 2 examples: a new edit reopens four items, including source-bound file/route traces. [3]
- New invariants, recompute, incomplete runs and registry dispatch; added R53 predicate assertions cover source/membership/record currency. [4]
- The closeout test answers the code commit's items with recomputed source-bound trace rows, then checks closure/restore and reaching the mutation seam, not a successful product memory commit. [11]
- Current source delta inspected statically: Align renamed-but-unchanged test identifiers with four-item reopening and R53 source-bound predicates; replace stale population figures with actual static source counts, preserving the narrow closeout mutation-seam limit. [13]
