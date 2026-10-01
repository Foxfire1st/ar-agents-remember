# mcp/tests/test_task_document_application_1.py

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

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Leaf create syncs parent master row [1]
- Leaf updates preserve manual master scope [2]
- Done child cannot hide pending parent from progress or master sync [3]
- An unreadable parent master refuses the leaf edit rather than dropping the row [4]
- Explicit cross series master ref never falls back to local master [5]
- Leaf sync refuses duplicate or mispointed exact parent row before write [6]
- Leaf sync demotes completed master when work becomes unresolved [7]
- Set status and set field [8]
- Set field cannot repoint plane owned contract identity [9]
- Dry run does not mutate existing files [10]
- Dry run would lose flags unmodeled md content [11]
- Replace rewrites structural fields and decisions [12]
- Replace rejects document path change [13]
- Set step updates only and names the parent of a bare substep id [14]
- Set step names the parent for a dotted child id [15]
- Set step refuses an ambiguous id [16]
- Add step creates one unit and refuses an existing id [17]
- Remove step requires a reason and records the removal [18]
- Remove step deletes a done step and repairs a completed document [19]
- A top level note persists instead of being discarded [20]
- A top level note is rendered into the markdown [21]
- Read steps returns the checklist and changes nothing [22]
- Skip step is exact audited and does not cascade [23]
- The restamp decision table: both derived fields absent and only the series path absent both produce a candidate; a fresh lifecycle still overwrites a stale binding; the one exact no-op is everything bound and current. [24]
- The class-local helpers that author the pre-contract state directly and plan against it. [25]
- The focused read's payload survives the response model the tool advertises: the real handler's `steps` list validates through `finalize_tool_response`, and an undeclared key still fails. [26]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
