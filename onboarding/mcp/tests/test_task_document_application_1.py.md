# mcp/tests/test_task_document_application_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_task_document_application_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-14T07:05+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted change set; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises canonical task-document mutations and their parent synchronization. Dry-run preserves bytes and reports unmodeled Markdown loss; replace updates intended structural fields but cannot repoint the document or plane-owned contract; the step plane updates a unit only in place, names the parent of a bare substep id instead of minting a top-level step, refuses an ambiguous id, creates one unit at a time, requires and records a nonblank removal reason, admits a reasoned removal of done work on a Completed document, persists and renders top-level notes, and reads the checklist without changing it; skip is exact, audited and non-cascading. Completion remains blocked by unfinished obligations.

## Code Commentary

### Logic

`test_set_step_updates_only_and_names_the_parent_of_a_bare_substep_id` records the L30/L31/L32 defect: the old upsert matched a bare id only at top level, so a call meant for the substep `S1.1` created a new top-level step titled `S1.1`, reported success and let `stepsDone` rise while the real substep stayed `pending`. The call now refuses, names the parent (`did you mean parent 'S1'?`), leaves the file bytes unchanged, and the parented call still updates the substep. `test_set_step_names_the_parent_for_a_dotted_child_id` covers a `<parent>.<child>` id whose child lives under that named parent; `test_set_step_refuses_an_ambiguous_id` covers a duplicated top-level id. `test_add_step_creates_one_unit_and_refuses_an_existing_id` separates creation from update: a new unit is appended, and a duplicate id, a missing title, an unknown parent and a duplicate substep each refuse without changing the document. `test_remove_step_requires_a_reason_and_records_the_removal` requires a nonblank reason and records the removal as a decision carrying the trimmed rationale. `test_remove_step_deletes_a_done_step_and_repairs_a_completed_document` records the developer ruling: a nonblank reason admits removing a `done` unit and operating on a `Completed` document, because the decision entry substitutes for the unresolved-work guard that otherwise refuses every other mutation — proven by two spurious units where removing the first leaves the second still blocking. `test_a_top_level_note_persists_instead_of_being_discarded` and `test_a_top_level_note_is_rendered_into_the_markdown` cover the top-level `note` field, which the key set had omitted, and its rendering onto the step's checkbox line even for a step with no outcome. `test_read_steps_returns_the_checklist_and_changes_nothing` returns the checklist with substeps and notes, omits the objective, and leaves both the JSON and the rendered Markdown byte-identical.

`test_read_steps_response_validates_against_the_model_the_tool_advertises` records the item-20 defect and its fix. `_read_steps` had always emitted a top-level `steps` list with nested `substeps` while `TaskDocResponse` declared only `stepsDone`/`stepsTotal`, so under `StrictResponseModel`'s `extra="forbid"` the envelope rejected the payload the handler had just produced — `steps: Extra inputs are not permitted` — and `read_steps` was unusable on every document, which is why every caller read the leaf JSON by hand instead. The response model now declares `steps: list[TaskDocStepRead] | None`; the case drives the real handler, validates its payload through `finalize_tool_response("task_doc", payload)`, asserts the returned `steps` list is exactly the authored top-level step with its nested substep, and keeps the fix from being a blanket widening of the envelope with a negative control: the same payload carrying an undeclared key still raises `ValidationError`.

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in history describe prior populations and must not be used to recreate removed tests or claim they still run. The retained behavior and its fixture limits, described above, govern this card.

**`test_create_writes_both_files` was REMOVED by 260913-LCA-L5, and it must not be restored as it
stood.** Its scenario authored a bare leaf through `task_doc` under a task root with no master
document, which the authoring plane now refuses by design (`_require_bindable_leaf_authoring`, see the
`application/task_docs/task_doc_tools.py` card): the leaf's derived `seriesContractPath` and
`enclosures[]` would have had nothing that could ever bind them. The file-write behavior it asserted is
not lost — it is covered by `test_leaf_create_syncs_parent_master_row` on a properly parented leaf, and
by the new end-to-end `test_leaf_doc_master_link_binding.py`.

The same change added the `LeafDocMasterLinkBindingTests` class (`:577-663`), the focused decision table
for the restamp half of the start binding: both reachable pre-contract states (both derived fields
absent, and only the series contract path absent) must produce a candidate, `enclosures[]` alone is not
a reachable case because the identity lookup finds a leaf through its own `enclosures[]` refs, a fresh
lifecycle still overwrites a stale binding, and the one exact no-op is everything bound and current.

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
| Leaf create syncs parent master row | `test_leaf_create_syncs_parent_master_row` | mcp/tests/test_task_document_application_1.py:20-33 |
| Leaf updates preserve manual master scope | `test_leaf_updates_preserve_manual_master_scope` | mcp/tests/test_task_document_application_1.py:35-52 |
| Done child cannot hide pending parent from progress or master sync | `test_done_child_cannot_hide_pending_parent_from_progress_or_master_sync` | mcp/tests/test_task_document_application_1.py:54-69 |
| An unreadable parent master refuses the leaf edit rather than dropping the row | `test_an_unreadable_parent_master_refuses_the_leaf_edit_rather_than_dropping_the_row` | mcp/tests/test_task_document_application_1.py:71-96 |
| Explicit cross series master ref never falls back to local master | `test_explicit_cross_series_master_ref_never_falls_back_to_local_master` | mcp/tests/test_task_document_application_1.py:98-107 |
| Leaf sync refuses duplicate or mispointed exact parent row before write | `test_leaf_sync_refuses_duplicate_or_mispointed_exact_parent_row_before_write` | mcp/tests/test_task_document_application_1.py:109-142 |
| Leaf sync demotes completed master when work becomes unresolved | `test_leaf_sync_demotes_completed_master_when_work_becomes_unresolved` | mcp/tests/test_task_document_application_1.py:144-168 |
| Set status and set field | `test_set_status_and_set_field` | mcp/tests/test_task_document_application_1.py:184-190 |
| Set field cannot repoint plane owned contract identity | `test_set_field_cannot_repoint_plane_owned_contract_identity` | mcp/tests/test_task_document_application_1.py:192-203 |
| Dry run does not mutate existing files | `test_dry_run_does_not_mutate_existing_files` | mcp/tests/test_task_document_application_1.py:191-207 |
| Dry run would lose flags unmodeled md content | `test_dry_run_would_lose_flags_unmodeled_md_content` | mcp/tests/test_task_document_application_1.py:209-235 |
| Replace rewrites structural fields and decisions | `test_replace_rewrites_structural_fields_and_decisions` | mcp/tests/test_task_document_application_1.py:237-280 |
| Replace rejects document path change | `test_replace_rejects_document_path_change` | mcp/tests/test_task_document_application_1.py:298-312 |
| Set step updates only and names the parent of a bare substep id | `test_set_step_updates_only_and_names_the_parent_of_a_bare_substep_id` | mcp/tests/test_task_document_application_1.py:298-332 |
| Set step names the parent for a dotted child id | `test_set_step_names_the_parent_for_a_dotted_child_id` | mcp/tests/test_task_document_application_1.py:334-350 |
| Set step refuses an ambiguous id | `test_set_step_refuses_an_ambiguous_id` | mcp/tests/test_task_document_application_1.py:366-376 |
| Add step creates one unit and refuses an existing id | `test_add_step_creates_one_unit_and_refuses_an_existing_id` | mcp/tests/test_task_document_application_1.py:364-390 |
| Remove step requires a reason and records the removal | `test_remove_step_requires_a_reason_and_records_the_removal` | mcp/tests/test_task_document_application_1.py:392-411 |
| Remove step deletes a done step and repairs a completed document | `test_remove_step_deletes_a_done_step_and_repairs_a_completed_document` | mcp/tests/test_task_document_application_1.py:413-457 |
| A top level note persists instead of being discarded | `test_a_top_level_note_persists_instead_of_being_discarded` | mcp/tests/test_task_document_application_1.py:473-484 |
| A top level note is rendered into the markdown | `test_a_top_level_note_is_rendered_into_the_markdown` | mcp/tests/test_task_document_application_1.py:472-490 |
| Read steps returns the checklist and changes nothing | `test_read_steps_returns_the_checklist_and_changes_nothing` | mcp/tests/test_task_document_application_1.py:492-529 |
| Skip step is exact audited and does not cascade | `test_skip_step_is_exact_audited_and_does_not_cascade` | mcp/tests/test_task_document_application_1.py:595-638 |
| The restamp decision table: both derived fields absent and only the series path absent both produce a candidate; a fresh lifecycle still overwrites a stale binding; the one exact no-op is everything bound and current. | `LeafDocMasterLinkBindingTests`; `test_binds_only_the_derived_fields_that_are_absent` | mcp/tests/test_task_document_application_1.py:577-663; mcp/tests/test_task_document_application_1.py:602-666 |
| The class-local helpers that author the pre-contract state directly and plan against it. | `_leaf_doc_path`; `_rewrite_leaf_doc`; `_plan` | mcp/tests/test_task_document_application_1.py:653-654; mcp/tests/test_task_document_application_1.py:656-660; mcp/tests/test_task_document_application_1.py:662-664 |
| The focused read's payload survives the response model the tool advertises: the real handler's `steps` list validates through `finalize_tool_response`, and an undeclared key still fails. | `test_read_steps_response_validates_against_the_model_the_tool_advertises` | mcp/tests/test_task_document_application_1.py:547-593 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History
- 2026-09-18T19:54:57+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the four enforced `citation_anchor_absent_from_range` rows in this document** (two table rows). (a) The class-local-helpers row described `_leaf_doc_path`, `_rewrite_leaf_doc` and `_plan` with six fragment ranges inside `589-614`. Those fragments were the three helpers' own bodies in their pre-move layout; this leaf's changes moved the whole block down, and the three helpers now sit at `653-654`, `656-660` and `662-664`. The six stale fragments were replaced by those three ranges: the same three anchors, each inside the range that holds it, with no anchor and no claim removed. (b) The restamp-table row cited `602-663`, which stops three lines above the `def test_binds_only_the_derived_fields_that_are_absent` it names at `666`; that range was widened to `602-666`. The claims, every anchor and the other ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `test_replace_rejects_document_path_change` repointed to mcp/tests/test_task_document_application_1.py:298-312. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `test_skip_step_is_exact_audited_and_does_not_cascade` repointed to mcp/tests/test_task_document_application_1.py:595-638. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:28+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded the item-20 fix and the case that carries it. `read_steps` emitted a top-level `steps` list with nested `substeps` that the declared `TaskDocResponse` forbade under `extra="forbid"`, so the operation was unusable on every document and callers read the leaf JSON by hand instead; the model now declares `steps: list[TaskDocStepRead] | None`, and `test_read_steps_response_validates_against_the_model_the_tool_advertises` drives the real handler, validates its payload through `finalize_tool_response` and keeps the declaration from becoming a blanket widening with a negative control (an undeclared key on the same payload still raises `ValidationError`). One paragraph in `### Logic` and one reference row record it; the existing `read_steps` claims were re-read against the source and remain true. Verification metadata is not advanced — the change is uncommitted and closeout owns the stamp — and the metadata block gains a `reviewedWorkingCandidate` row naming this leaf's candidate as what was read.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_set_status_and_set_field` repointed to mcp/tests/test_task_document_application_1.py:184-190. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_set_field_cannot_repoint_plane_owned_contract_identity` repointed to mcp/tests/test_task_document_application_1.py:192-203. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_set_step_refuses_an_ambiguous_id` repointed to mcp/tests/test_task_document_application_1.py:366-376. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_a_top_level_note_persists_instead_of_being_discarded` repointed to mcp/tests/test_task_document_application_1.py:473-484. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-14T07:05+02:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): recorded that `test_create_writes_both_files` was **removed**, and why it must not be
  restored as it stood — its scenario authored a leaf under a task root with no master document, which the
  authoring plane now refuses by design, so the leaf's derived master link had nothing that could bind it;
  the file-write behavior it asserted survives in `test_leaf_create_syncs_parent_master_row` and in the
  new end-to-end module. Added the new `LeafDocMasterLinkBindingTests` class with its decision table and
  three helper rows, and replaced the removed test's row. Re-derived every row in the reference table
  against the current source with AST (the removal at the top and the 84-line addition at the bottom moved
  all but the first ranges; the old `Create writes both files` row is gone and the `ApplicationTests1`
  class now starts at `:19`). Verification metadata remains closeout-owned; no execution or acceptance
  claim.

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
