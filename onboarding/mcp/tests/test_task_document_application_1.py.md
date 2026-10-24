# mcp/tests/test_task_document_application_1.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds the first application group of the task-document tool: publication refuses a leaf with no master, a leaf
row is synced into its master, dry runs and replaces keep what they did not model, step edits name their parent
or refuse an ambiguous id, and the removed read operations refuse with the canonical file to read instead. It
also bounds what a write answers and sweeps the shipped texts for an instruction that still calls a removed read.

## Code Commentary

### Logic

`ApplicationTests1` drives `task_docs.task_doc_tools` against task documents read through `tasks.document` and
`tasks.leaf_doc`, with `worktrees.task_resolver` resolving a master.

- **Publication.** `test_every_task_doc_publication_refuses_a_leaf_without_a_master` refuses every publication
  operation on a masterless sub-task with the exact message and leaves the task root's file set and bytes alone.
- **Master linkage.** `test_leaf_create_syncs_parent_master_row`, `test_leaf_updates_preserve_manual_master_scope`,
  `test_leaf_sync_refuses_duplicate_or_mispointed_exact_parent_row_before_write`,
  `test_leaf_sync_demotes_completed_master_when_work_becomes_unresolved` and
  `test_explicit_cross_series_master_ref_is_refused_not_fallen_back` keep the parent row a leaf owes its master,
  while `test_an_unreadable_parent_master_refuses_the_leaf_edit_rather_than_dropping_the_row` refuses rather than
  dropping it.
- **Progress.** `test_done_child_counts_as_progress_without_changing_document_stage` and
  `test_five_major_eight_children_share_the_tool_progress_count` fix the counts without moving the stage.
- **Dry runs and replaces.** `test_dry_run_does_not_mutate_existing_files`,
  `test_dry_run_would_lose_flags_unmodeled_md_content`, `test_replace_rewrites_structural_fields_and_decisions`
  and `test_replace_rejects_document_path_change` keep a dry run read-only and a replace structural.
- **Steps.** `test_set_step_updates_only_and_names_the_parent_of_a_bare_substep_id`,
  `test_set_step_names_the_parent_for_a_dotted_child_id` and `test_set_step_refuses_an_ambiguous_id` keep a bare
  substep id from minting a top-level step; `test_add_step_creates_one_unit_and_refuses_an_existing_id`,
  `test_remove_step_requires_a_reason_and_records_the_removal` and
  `test_remove_step_deletes_a_done_step_and_repairs_a_completed_document` cover adding and removal, and
  `test_skip_step_is_exact_audited_and_does_not_cascade` keeps a skip exact and unaudited by cascade.
- **Notes.** `test_a_top_level_note_persists_instead_of_being_discarded` and
  `test_a_top_level_note_is_rendered_into_the_markdown` keep a note in both the JSON and the Markdown.
- **Removed reads.** `test_removed_read_operations_are_refused_with_file_names` and
  `test_removed_read_refusal_validates_against_the_model_the_tool_advertises` refuse with `operation-removed` and
  the canonical file to read, and the refusal survives its own declared response contract.
- **Answers.** `ApplicationWriteAnswers` bounds an ordinary write to 100 tokens, keeps a create naming only the
  rendered file, carries review state into `begin_review`, keeps a dry run's answer bounded, and requires a
  section body file to match the inline body and name its SHA-256.
- **Restamp.** `LeafDocMasterLinkBindingTests.test_binds_only_the_derived_fields_that_are_absent` binds only the
  absent derived fields on the unit population.
- **Removal sweep.** `TaskDocReadRemovalSweepTests.ROOTS` names the trees an instruction can still sit in — the
  product source, the packaged skill copy, the canonical skill tree and `docs` — because the harness skill mirrors
  are gone (MIK-R196 rule 7); `test_no_instruction_calls_task_doc_get`,
  `test_read_steps_survives_only_where_the_removal_is_named` and `test_deleted_read_helpers_stay_deleted` sweep
  them.

### Conventions

Cases hold the whole task-root file set and bytes before and after a read or a refusal, so a surprising write is
caught even when the answer is right.

### Invariants And Boundaries

- A write answers briefly and names the files it wrote, not their contents.
- A leaf that names a master owes it a row on every edit; an unreadable master refuses the edit.

## Evidence

- A leaf create syncs the parent master row. [1]
- Leaf updates preserve manual master scope. [2]
- An unreadable parent master refuses the leaf edit rather than dropping the row. [4]
- Dry runs keep unmodeled Markdown content and existing files. [10] [11]
- Replace rewrites structural fields and decisions, and rejects a document path change. [12] [13]
- Step edits name the parent or refuse an ambiguous id. [14] [15] [16]
- Adding and removing steps stay one unit, reasoned and recorded. [17] [18] [19]
- A top-level note persists and is rendered into the Markdown. [20] [21]
- The removed reads refuse with `operation-removed` and the canonical file guidance. [22]
- A skip is exact, audited and does not cascade. [23]
- The restamp decision table binds only the absent derived fields and overwrites a stale binding. [24]
- The class-local helpers author the pre-contract state and plan against it. [25]
- The removed-read refusal survives the declared response contract; an undeclared key still raises. [26] [27]

- The removal sweep covers the product source, the packaged skill copy, the canonical tree and `docs`, since the harness mirrors are gone. [28]


- Explicit cross-series master ref raises TaskDocError naming the reference, task-folder constraint and fix, while parent bytes/rows stay unchanged; no fallback — `test_explicit_cross_series_master_ref_is_refused_not_fallen_back` in mcp/tests/test_task_document_application_1.py. [5]
- Leaf sync refuses duplicate or mispointed exact parent row before write — mcp/tests/test_task_document_application_1.py:183-218. [6]
- Leaf sync demotes completed master when work becomes unresolved — mcp/tests/test_task_document_application_1.py:220-258. [7]
- Set status and set field — mcp/tests/test_task_document_application_1.py:260-266. [8]
- Set field cannot repoint plane owned contract identity — mcp/tests/test_task_document_application_1.py:268-279. [9]
- Real create tool plus saved JSON declares five-major/eight-child count assertions; source inspection is not a test run or acceptance — mcp/tests/test_task_document_application_1.py:111-136; mcp/tests/test_task_document.py:580-624. [29]
- All four public task_doc publication operations refuse the masterless subTask with the exact message and preserve the immediate task-root file set and bytes — mcp/tests/test_task_document_application_1.py:31-57. [30]
- Native create reports 0/1 major progress while both leaf and master row remain planning — `test_done_child_counts_as_progress_without_changing_document_stage` in mcp/tests/test_task_document_application_1.py. [31]
