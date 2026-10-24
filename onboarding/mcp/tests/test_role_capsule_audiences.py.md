# mcp/tests/test_role_capsule_audiences.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Stage-audience selection preserves role boundaries in compiled capsules: a compiler delivers the common part plus
the selected role's stage parts and nothing else, a declared step's detail bytes travel as separate frozen
references beside the handover file, and the Curator receives its ruled steps without the Manager's or another
role's material. The real operation audiences are checked against pinned bytes, and a repairing role stops after
three repairs of the same check or finding.

## Code Commentary

### Logic

`_compile_corpus_pair()` compiles a role against the corpus, `_delivered_curation_for_d301()` reads what the
Curator's capsule actually carries, `_expected_operation_stage()` and `_unmarked_pinned_operation()` give a case
the stage it expects and a control it can mutate. `R125_ADDRESSED_PARAGRAPHS`, `R125_OPERATION_SHA256` and
`R125_CLOSEOUT_SHA256` pin the delivered bytes; `MEMORY_REVIEW_PREDECESSOR`,
`MEMORY_REVIEW_RECORDED_LANE` and `CURATOR_SERVING_STAGE_BOUNDARY` name the lane and the producer boundary.

- **Audience selection.** `test_compiler_delivers_only_common_and_selected_role_stage_parts` keeps the compiler to
  the common part plus the selected stage.
- **Step details.** `test_compiler_carries_declared_step_detail_bytes_as_separate_references`,
  `test_handover_writes_immutable_source_details_beside_its_file`,
  `test_launch_composition_names_frozen_details_by_their_request_paths` and
  `test_step_details_are_named_for_reaching_their_step_not_intake` keep a step's detail a frozen file named by the
  request it belongs to.
- **Role boundaries.** `test_curator_receives_ruled_step_details_separately_and_keeps_writer_boundaries`,
  `test_manager_curation_does_not_receive_curators_card_or_writer_steps`,
  `test_curator_execution_support_is_an_unconditional_inline_output` and
  `test_leaf_role_texts_mark_only_their_own_completed_steps` keep each role's material with that role.
- **D301.** The `test_d301_*` cases keep the real capsules delivering named step files as frozen launch artifacts,
  the Curator's whole handover and step limits inside its capsule, external backing output inline, bootstrap
  reproducibility rather than reader execution, the delivered authoring resolving the actual routing, and the
  hand-off file read for the first review then reused for repairs.
- **Naming.** `test_curator_detail_names_use_only_curation_workflow_numbers_and_titles`,
  `test_nested_curator_file_names_use_the_same_operation_titles` and
  `test_every_curator_stage_keeps_the_serving_build_producer_boundary` keep detail names on the curation
  workflow's numbers and titles and the serving build's producer boundary.
- **Lanes.** `test_memory_review_instructions_select_the_independent_recorded_lane` selects the recorded memory
  review lane.
- **Pinned audiences.** `test_real_operation_audiences_preserve_pinned_common_and_only_addressed_paragraphs` and
  `test_operation_audience_markings_preserve_pinned_bytes_and_immutable_closeout` keep the pinned bytes and the
  immutable closeout text intact.
- **Repair limit.** `test_repairing_roles_stop_after_three_repairs_of_the_same_check_or_finding` stops a role
  after three repairs of the same subject.

### Conventions

A case compiles the real corpus and compares delivered bytes, so an extra paragraph that leaks into another
role's capsule fails rather than merely being unmentioned.

### Invariants And Boundaries

- A capsule carries the common part plus its own stage's parts, and nothing of another role's.
- A step's detail is an immutable frozen file, not a re-read of the source at send time.

## Evidence

- The compiler delivers only the common and selected role stage parts. [1]
- Declared step detail bytes travel as separate references. [2]
- The handover writes immutable source details beside its file. [3]
- The launch composition names frozen details by their request paths. [4]
- The Curator receives ruled step details separately and keeps the writer boundaries. [5]
- Manager curation receives neither the Curator's card nor the writer's steps. [6]
- The real D301 capsules deliver named step files as frozen launch artifacts. [7]
- The Curator's capsule keeps the whole handover and its step limits. [8]
- Step details are named for reaching their step, not for intake. [9]
- Curator execution support is an unconditional inline output. [10]
- External backing output stays inline. [11]
- Bootstrap requires reproducibility rather than reader execution. [12]
- Delivered authoring resolves the actual capsule routing. [13]
- The hand-off file is read for the first review and reused for repairs. [14]
- Curator detail names use only the curation workflow's numbers and titles. [15]
- Nested curator file names use the same operation titles. [16]
- Leaf role texts mark only their own completed steps. [17]
- Every Curator stage keeps the serving build's producer boundary. [18]
- Memory-review instructions select the independent recorded lane. [19]
- Real operation audiences preserve the pinned common part and only the addressed paragraphs. [20]
- Operation audience markings preserve the pinned bytes and the immutable closeout. [21]
- A repairing role stops after three repairs of the same check or finding. [22]
- The expected Reviewer-only paragraph includes the missing-entry return and the clean-sync no-round obligations. [23]
- The approved implementation and review body hashes are repinned in the existing corpus check. [24]
