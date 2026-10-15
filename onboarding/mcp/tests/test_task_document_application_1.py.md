# mcp/tests/test_task_document_application_1.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Source assertions for canonical task-document mutations, parent synchronization and bounded write/refusal answers. Dry-run preserves bytes; replace cannot repoint document/plane identity; exact step updates refuse mistaken bare/dotted/ambiguous IDs, audited remove and noncascading skip retain reasons, and notes persist/render. Major-only progress cannot hide unfinished parent/nested completion obligations. Native create/readback asserts five majors with eight children and (1,5) progress. Successful checklist read cases are retired; current get/read_steps calls refuse with canonical file guidance and unchanged bytes. These are declared cases, not newly executed results.

## Code Commentary

The instruction-removal sweep includes all eight shipped harness skill roots as well as canonical/package text. It detects unquoted operation=get, the old taskDocReadArgs tool-read sentence and obsolete blanket task_context instructions, while preserving documentary mentions of removal and the existing write/undeclared-key controls.

### Current Contract

Removed-read tests assert ok=false/operation-removed, canonical file guidance, unchanged JSON/Markdown, no steps and rejection of an undeclared model key. Ordinary write fixtures use their fixed 40-character coordination root; that measure is distinct from location-separated content measurement. ApplicationWriteAnswers and TaskDocReadRemovalSweepTests cover phrase answers, dry diffs without master/rendered dumps, by-file section bytes/SHA256 and conflict/nonregular input refusal, and removal of read instructions/helpers. Earlier successful checklist-read defects are historical. These source tests do not forbid best-effort identity parsing or certify a fresh registered session. Parent synchronization preserves manual scope. The renamed test_explicit_cross_series_master_ref_is_refused_not_fallen_back expects TaskDocError containing the invalid reference, folder constraint and remedy; it checks unchanged parent bytes and an empty subtask list, not an answered successful create. The pending-parent/done-child create case now reports `0/1` and keeps the parent row inProgress. The added five-major/eight-child case uses the real create tool and persisted JSON plus step_done/step_total to assert `1/5`; it is not just an object with fabricated summary counters.

### Logic

`test_set_step_updates_only_and_names_the_parent_of_a_bare_substep_id` records the L30/L31/L32 defect: the old upsert matched a bare id only at top level, so a call meant for the substep `S1.1` created a new top-level step titled `S1.1`, reported success and let `stepsDone` rise while the real substep stayed `pending`. The call now refuses, names the parent (`did you mean parent 'S1'?`), leaves the file bytes unchanged, and the parented call still updates the substep. `test_set_step_names_the_parent_for_a_dotted_child_id` covers a `<parent>.<child>` id whose child lives under that named parent; `test_set_step_refuses_an_ambiguous_id` covers a duplicated top-level id. `test_add_step_creates_one_unit_and_refuses_an_existing_id` separates creation from update: a new unit is appended, and a duplicate id, a missing title, an unknown parent and a duplicate substep have named refusal assertions; the loop checks that the top-level IDs remain unchanged, rather than comparing every file byte. `test_remove_step_requires_a_reason_and_records_the_removal` requires a nonblank reason and records the removal as a decision carrying the trimmed rationale. `test_remove_step_deletes_a_done_step_and_repairs_a_completed_document` records the developer ruling: a nonblank reason admits removing a `done` unit and operating on a `Completed` document, because the decision entry substitutes for the unresolved-work guard that otherwise refuses every other mutation — proven by two spurious units where removing the first leaves the second still blocking. `test_a_top_level_note_persists_instead_of_being_discarded` and `test_a_top_level_note_is_rendered_into_the_markdown` cover the top-level `note` field, which the key set had omitted, and its rendering onto the step's checkbox line even for a step with no outcome. Historically, `test_read_steps_returns_the_checklist_and_changes_nothing` asserted a returned checklist without the objective and byte-identical files. That successful read case is now removed, not retained or rerun; current `test_removed_read_operations_are_refused_with_file_names` asserts get/read_steps refusal and unchanged JSON/Markdown.

> **Retained historical source account — superseded by the current contract:**
> `test_read_steps_response_validates_against_the_model_the_tool_advertises` records the item-20 defect and its fix. `_read_steps` had always emitted a top-level `steps` list with nested `substeps` while `TaskDocResponse` declared only `stepsDone`/`stepsTotal`, so under `StrictResponseModel`'s `extra="forbid"` the envelope rejected the payload the handler had just produced — `steps: Extra inputs are not permitted` — and `read_steps` was unusable on every document, which is why every caller read the leaf JSON by hand instead. The response model now declares `steps: list[TaskDocStepRead] | None`; the case drives the real handler, validates its payload through `finalize_tool_response("task_doc", payload)`, asserts the returned `steps` list is exactly the authored top-level step with its nested substep, and keeps the fix from being a blanket widening of the envelope with a negative control: the same payload carrying an undeclared key still raises `ValidationError`.

Current source definitions below identify retained mutation, synchronization, skip/restamp, answer-bound and removed-read behavior. Historical successful checklist-read defects remain useful lessons but do not request restoration or claim those removed methods still run. Static inspection is neither collection nor an execution result.

**`test_create_writes_both_files` was REMOVED by 260913-LCA-L5, and it must not be restored as it
stood.** Its scenario authored a bare leaf through `task_doc` under a task root with no master
document, which the authoring plane now refuses by design (`_require_bindable_leaf_authoring`, see the
`application/task_docs/task_doc_tools.py` card): the leaf's derived `seriesContractPath` and
`enclosures[]` would have had nothing that could ever bind them. The file-write behavior it asserted is
not lost — it is covered by `test_leaf_create_syncs_parent_master_row` on a properly parented leaf, and
by the new end-to-end `test_leaf_doc_master_link_binding.py`.

The retained source contains the `LeafDocMasterLinkBindingTests` class, the focused decision table
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

## Native Major-Count Writer Witness

The native create call persists five major steps and eight nested children. Returned progress and the persisted document helpers both report (1,5). This source case complements, but does not execute or prove, the fabricated dashboard counter cases; it does not turn presentation counts into relaxed completion readiness.

- Real create tool plus saved JSON declares five-major/eight-child count assertions; source inspection is not a test run or acceptance. [29]

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Current source assertions are listed below. References 22 and 26 explicitly supersede the removed successful-read methods with the retained refusal/response-model cases. The older successful-read defect explanation above remains historical; no deleted method is restored.

- Leaf create syncs parent master row [1]

- Leaf updates preserve manual master scope [2]

- Pending-parent/done-child native create reports 0/1 major progress; master row remains inProgress. [3]

- An unreadable parent master refuses the leaf edit rather than dropping the row [4]

- Explicit cross-series master ref raises TaskDocError naming the reference, task-folder constraint and fix, while parent bytes/rows stay unchanged; no fallback [5]

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

- Current get/read_steps refuse with operation-removed and canonical file guidance, preserving JSON/Markdown; supersedes the removed successful checklist-read method. [22]

- Skip step is exact audited and does not cascade [23]

- The restamp decision table: both derived fields absent and only the series path absent both produce a candidate; a fresh lifecycle still overwrites a stale binding; the one exact no-op is everything bound and current. [24]

- The class-local helpers that author the pre-contract state directly and plan against it. [25]

- Current removed-read refusal survives finalize_tool_response with no steps; an undeclared key still raises ValidationError, rather than reintroducing successful reads. [26]

- Removed-read tests assert ok=false/operation-removed, canonical file guidance, unchanged JSON/Markdown, no steps and rejection of an undeclared model key. Ordinary write fixtures use their fixed 40-character coordination root; that measure is distinct from location-separated content measurement. ApplicationWriteAnswers and TaskDocReadRemovalSweepTests cover phrase answers, dry diffs without master/rendered dumps, by-file section bytes/SHA256 and conflict/nonregular input refusal, and removal of read instructions/helpers. Earlier successful checklist-read defects are historical. These source tests do not forbid best-effort identity parsing or certify a fresh registered session. [27]
### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.

- The removal sweep covers all eight shipped skill roots and obsolete tool-read/blanket-context instruction shapes. [28]
