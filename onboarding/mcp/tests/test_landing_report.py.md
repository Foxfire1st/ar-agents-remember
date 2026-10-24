# mcp/tests/test_landing_report.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Shows what a landing cuts from a card and what it adds (MIK-R120@v1): a card over the measure reports both
numbers, a cut counts removed against added, an under-measure card is not reported, and only a source card
proven deleted is exempt. Additions carry their own sizes and a sum, and the answer keeps whole counts with
bounded first rows inside the token limit.

## Code Commentary

### Logic

The cases drive `memory_quality.converted_check`, the curator checklist, the answer projection and the worktree
contract, with the role texts read through `leaf_instruction_wording` and the capsules compiled from the
capsule manifest.

- **Measure.** `test_card_over_measure_reports_both_numbers`, `test_card_cut_counts_removed_against_added` and
  `test_card_under_measure_not_reported` pin the threshold and the pair of counts.
- **Exemptions.** `test_only_proven_deleted_source_card_not_reported` keeps known absence on both sides from
  counting as a source deletion, and `test_leaf_run_proves_deletion_with_both_code_trees` exempts only the
  actually deleted source.
- **Moves.** `test_renamed_card_compared_across_move` and `test_named_rename_cut_reported_across_move` compare a
  moved card through the R-name the code change records; `test_duplicate_blob_copies_name_no_rename` keeps
  unchanged duplicate-blob files copies rather than renames.
- **Additions.** `test_added_file_reported_with_size_and_sum` reports each path's size and the total while the
  knowledge roots stay excluded; `test_symlinks_reported_without_following_targets` reports dangling and live
  links at their own `lstat` size; `test_linked_worktree_pointer_is_not_an_addition` keeps a clean linked
  worktree's pointer out.
- **Surfaces.** `test_checklist_renders_landing_rows_without_refusing` and
  `test_converted_check_carries_landing_counts` put the counts on the checklist and the converted check;
  `test_answer_carries_two_counts_first_rows_within_bound` keeps whole counts with slim first rows in a
  200-row answer.
- **Wording.** `test_role_texts_hold_landing_sentences_everywhere` and
  `test_reviewer_landing_sentences_are_delivered_before_memory_review` keep the protected sentences on their
  delivered step-8 surface.
- **Base.** `test_leaf_base_reports_committed_and_keeps_older_base_out`,
  `test_leaf_base_update_excludes_older_base_files`, `test_removed_cards_answer_the_same_measure` and
  `test_leaf_base_request_reads_contract_and_none_without_base` keep the admitted base binding the measure.
- **Cost.** `test_line_delta_work_is_linear_in_card_size` compares repeated-line hash work at two sizes.

### Conventions

The measure is asserted at its consumers (checklist, converted check, answer) rather than in the measuring
function alone.

### Invariants And Boundaries

- An under-measure card is not reported, and a card proven deleted on both code sides is not a cut.
- A copy is never reported as a rename, and a worktree pointer is never an addition.

## Evidence

- A measured card reports its exact removed and added numbers with no refusing finding. [1]
- Known absence on both code sides is not a source deletion; an actually deleted source is exempt. [2]
- Added paths carry individual sizes and a total while the knowledge roots are excluded. [3]
- Two hundred cut rows keep whole counts and bounded slim first rows within the answer token limit. [4]

- Curator sources and canonical capsule retain the three protected clauses; each discovered Reviewer root delivers both protected landing sentences in the named step-8 memory file. [5]

- The admitted memory base retains cuts and additions across a mid-leaf commit. [6]
- Repeated-line hash work is compared at two sizes. [9]

- The current role-text cases accept the scoped Curator equivalent, exercise deletion controls on both surviving source roots and compile canonical Curator/curation. Both Reviewer landing sentences are checked in the exact delivered step-8 file with per-sentence deletion controls. [10]


- Real knowledge-gate evaluation is complete and non-refusing with the populations aboard in the disposable fixture. [7]
- The closeout-quality fixture reports landed and clean counts with unchanged zero refusing findings. [8]
