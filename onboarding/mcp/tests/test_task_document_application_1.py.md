# mcp/tests/test_task_document_application_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_task_document_application_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `723fd2f1becc130d85d7a6b285b93115be0df852` |
| lastVerifiedCommitDate | 2026-09-13T02:07:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises canonical task-document mutations and their parent synchronization. Dry-run preserves bytes and reports unmodeled Markdown loss; replace updates intended structural fields but cannot repoint the document or plane-owned contract; the step plane updates a unit only in place, names the parent of a bare substep id instead of minting a top-level step, refuses an ambiguous id, creates one unit at a time, requires and records a nonblank removal reason, admits a reasoned removal of done work on a Completed document, persists and renders top-level notes, and reads the checklist without changing it; skip is exact, audited and non-cascading. Completion remains blocked by unfinished obligations.

## Code Commentary

### Logic

`test_set_step_updates_only_and_names_the_parent_of_a_bare_substep_id` records the L30/L31/L32 defect: the old upsert matched a bare id only at top level, so a call meant for the substep `S1.1` created a new top-level step titled `S1.1`, reported success and let `stepsDone` rise while the real substep stayed `pending`. The call now refuses, names the parent (`did you mean parent 'S1'?`), leaves the file bytes unchanged, and the parented call still updates the substep. `test_set_step_names_the_parent_for_a_dotted_child_id` covers a `<parent>.<child>` id whose child lives under that named parent; `test_set_step_refuses_an_ambiguous_id` covers a duplicated top-level id. `test_add_step_creates_one_unit_and_refuses_an_existing_id` separates creation from update: a new unit is appended, and a duplicate id, a missing title, an unknown parent and a duplicate substep each refuse without changing the document. `test_remove_step_requires_a_reason_and_records_the_removal` requires a nonblank reason and records the removal as a decision carrying the trimmed rationale. `test_remove_step_deletes_a_done_step_and_repairs_a_completed_document` records the developer ruling: a nonblank reason admits removing a `done` unit and operating on a `Completed` document, because the decision entry substitutes for the unresolved-work guard that otherwise refuses every other mutation — proven by two spurious units where removing the first leaves the second still blocking. `test_a_top_level_note_persists_instead_of_being_discarded` and `test_a_top_level_note_is_rendered_into_the_markdown` cover the top-level `note` field, which the key set had omitted, and its rendering onto the step's checkbox line even for a step with no outcome. `test_read_steps_returns_the_checklist_and_changes_nothing` returns the checklist with substeps and notes, omits the objective, and leaves both the JSON and the rendered Markdown byte-identical.

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in history describe prior populations and must not be used to recreate removed tests or claim they still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Create writes both files | `test_create_writes_both_files` | mcp/tests/test_task_document_application_1.py:18-24 |
| Leaf create syncs parent master row | `test_leaf_create_syncs_parent_master_row` | mcp/tests/test_task_document_application_1.py:26-39 |
| Leaf updates preserve manual master scope | `test_leaf_updates_preserve_manual_master_scope` | mcp/tests/test_task_document_application_1.py:41-58 |
| Done child cannot hide pending parent from progress or master sync | `test_done_child_cannot_hide_pending_parent_from_progress_or_master_sync` | mcp/tests/test_task_document_application_1.py:60-75 |
| An unreadable parent master refuses the leaf edit rather than dropping the row | `test_an_unreadable_parent_master_refuses_the_leaf_edit_rather_than_dropping_the_row` | mcp/tests/test_task_document_application_1.py:77-102 |
| Explicit cross series master ref never falls back to local master | `test_explicit_cross_series_master_ref_never_falls_back_to_local_master` | mcp/tests/test_task_document_application_1.py:104-113 |
| Leaf sync refuses duplicate or mispointed exact parent row before write | `test_leaf_sync_refuses_duplicate_or_mispointed_exact_parent_row_before_write` | mcp/tests/test_task_document_application_1.py:115-148 |
| Leaf sync demotes completed master when work becomes unresolved | `test_leaf_sync_demotes_completed_master_when_work_becomes_unresolved` | mcp/tests/test_task_document_application_1.py:150-174 |
| Set status and set field | `test_set_status_and_set_field` | mcp/tests/test_task_document_application_1.py:176-182 |
| Set field cannot repoint plane owned contract identity | `test_set_field_cannot_repoint_plane_owned_contract_identity` | mcp/tests/test_task_document_application_1.py:184-195 |
| Dry run does not mutate existing files | `test_dry_run_does_not_mutate_existing_files` | mcp/tests/test_task_document_application_1.py:197-213 |
| Dry run would lose flags unmodeled md content | `test_dry_run_would_lose_flags_unmodeled_md_content` | mcp/tests/test_task_document_application_1.py:215-241 |
| Replace rewrites structural fields and decisions | `test_replace_rewrites_structural_fields_and_decisions` | mcp/tests/test_task_document_application_1.py:243-286 |
| Replace rejects document path change | `test_replace_rejects_document_path_change` | mcp/tests/test_task_document_application_1.py:288-302 |
| Set step updates only and names the parent of a bare substep id | `test_set_step_updates_only_and_names_the_parent_of_a_bare_substep_id` | mcp/tests/test_task_document_application_1.py:304-338 |
| Set step names the parent for a dotted child id | `test_set_step_names_the_parent_for_a_dotted_child_id` | mcp/tests/test_task_document_application_1.py:340-356 |
| Set step refuses an ambiguous id | `test_set_step_refuses_an_ambiguous_id` | mcp/tests/test_task_document_application_1.py:358-368 |
| Add step creates one unit and refuses an existing id | `test_add_step_creates_one_unit_and_refuses_an_existing_id` | mcp/tests/test_task_document_application_1.py:370-396 |
| Remove step requires a reason and records the removal | `test_remove_step_requires_a_reason_and_records_the_removal` | mcp/tests/test_task_document_application_1.py:398-417 |
| Remove step deletes a done step and repairs a completed document | `test_remove_step_deletes_a_done_step_and_repairs_a_completed_document` | mcp/tests/test_task_document_application_1.py:419-463 |
| A top level note persists instead of being discarded | `test_a_top_level_note_persists_instead_of_being_discarded` | mcp/tests/test_task_document_application_1.py:465-476 |
| A top level note is rendered into the markdown | `test_a_top_level_note_is_rendered_into_the_markdown` | mcp/tests/test_task_document_application_1.py:478-496 |
| Read steps returns the checklist and changes nothing | `test_read_steps_returns_the_checklist_and_changes_nothing` | mcp/tests/test_task_document_application_1.py:498-535 |
| Skip step is exact audited and does not cascade | `test_skip_step_is_exact_audited_and_does_not_cascade` | mcp/tests/test_task_document_application_1.py:537-580 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: replaced the removed `test_set_step_inserts_then_updates_without_duplicating` row with the current step-plane population and recorded its behavior — a bare substep id is refused with its parent named instead of minting a top-level step (the L30/L31/L32 defect), an ambiguous id refuses, `add_step` creates one unit and refuses duplicates or a missing title, `remove_step` requires a nonblank reason, records the removal as a decision, and by the developer ruling admits removing a `done` unit from a `Completed` document, top-level notes persist and render, and `read_steps` returns the checklist without writing. Corrected the skip-step range to the measured source. Verification metadata remains closeout-owned.

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (task_doc_tool takes
  `call: TaskDocCall`); suite purpose unchanged. Verified at code commit a9d50e08.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the legacy-master orchestration regression became
  `test_set_field_orchestration_fields_require_exact_commanded_masters` — a graph-less sprint is
  the legal atomic-sequential default, so refusal now requires inexact declared facts (undeclared
  super branch or unresolvable commanded alias); the sprint-only `integrationBranch` refusal is
  unchanged. Verification remains closeout-owned.
- 2026-08-15T03:33:21+02:00 — 260815-DAG-L1 second targeted-Dagger repair: the exact artifact
  showed the adjacent legacy `integrationBranch` success expectation also contradicted the closed
  sprint schema. The regression now proves both partial orchestration edits refuse and leave the
  master unchanged.
- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: replaced the obsolete
  implicit-orchestration success expectation with the explicit topology-migration refusal required
  by the new contract, while retaining the adjacent integration-branch assertions.
- 2026-08-14T06:40+02:00 — L23 final candidate review: application tests preserve strict
  task-addressed mutation and manager-lineage preflight without accepting runtime identifiers.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
