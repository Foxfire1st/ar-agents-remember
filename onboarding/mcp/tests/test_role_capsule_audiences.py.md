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

**Historical source account, superseded by the current clause below:** `_compile_corpus_pair()` compiles a role against the corpus, `_delivered_curation_for_d301()` reads what the
Curator's capsule actually carries, `_expected_operation_stage()` and `_unmarked_pinned_operation()` give a case
the stage it expects and a control it can mutate. `R125_ADDRESSED_PARAGRAPHS`, `R125_OPERATION_SHA256` and
`R125_CLOSEOUT_SHA256` pin the delivered bytes; `MEMORY_REVIEW_PREDECESSOR`,
`MEMORY_REVIEW_RECORDED_LANE` and `CURATOR_SERVING_STAGE_BOUNDARY` name the lane and the producer boundary. [Historical source custody: `mcp/tests/test_role_capsule_audiences.py` blob `ee20e82cebeed3333d4831fe27894c9806cfb48c` at code base `59b01fb8f72a38d2d27f9c37b8b9ca2513fd3fa0`; this is no current implementation claim.]

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
  workflow's numbers and titles for ordinary details, the conditional triggers for writer-command and refused-write details, and the serving build's producer boundary.
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


The pinned Architect planning paragraph includes the single developer question “go, or review first?”, disclosure that the upfront review has a planned comparison with no task workspace, first-Explain environment creation, and the `intentReview` answer. The Manager paragraphs pin that `intent-review-open` waits for the Architect's go and is not retried. Their planning/coordination seals move with those exact admitted sentences.

Complete D656 operation and per-recipient stage digest literals pin the reviewed audience projections, including closeout bytes. Detail checks cover all declared role/operation pairs and distinguish standing, knowledge-use and conditional writer/refusal triggers. Writer syntax/report semantics remain separate from inline serving-build authority. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
- The compiler delivers only the common and selected role stage parts. [1]
- Declared step detail bytes travel as separate references. [2]
- The handover writes immutable source details beside its file. [3]
- The launch composition names frozen details by their request paths. [4]

- The Curator receives ruled step details separately and keeps the writer boundaries. Anchor: `test_curator_receives_ruled_step_details_separately_and_keeps_writer_boundaries` [5]

- Manager curation receives neither the Curator's card nor the writer's steps. [6]
- The real D301 capsules deliver named step files as frozen launch artifacts. [7]
- The Curator's capsule keeps the whole handover and its step limits. [8]
- Ordinary step details are named for reaching their step, not intake; writer-command and refused-write details instead retain their expressly checked before-CLI and correct-refusal triggers. [Past-epoch source caption, detached from live reference 9. Recorded citation custody: mcp/tests/test_role_capsule_audiences.py blob c1306dc9442d617691906ff7e59f1648bba45c0d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: Every declared role/operation’s delivered details are checked for an exact reach-step trigger and not-before wording. Knowledge-use details have role-specific reach triggers; writer-command and refused-write details keep their explicit conditional triggers. An intake-wording mutation must fail and the seen-source census must equal all declared details.
- Curator execution support is an unconditional inline output. [10]
- External backing output stays inline. [11]
- Bootstrap requires reproducibility rather than reader execution. [12]
- Delivered authoring resolves the actual capsule routing. [13]
- The hand-off file is read for the first review and reused for repairs. [14]
- Ordinary Curator detail names match the curation workflow numbers and titles; writer-command and refused-write details instead use their explicitly checked conditional triggers. [Past-epoch source caption, detached from live reference 15. Recorded citation custody: mcp/tests/test_role_capsule_audiences.py blob c1306dc9442d617691906ff7e59f1648bba45c0d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The ordinary Curator detail labels are checked against curation workflow numbers and titles. Standing details retain when-you-reach/not-before labels; writer-command and correct-write-refusal details instead use their explicitly declared conditional triggers.

- Nested curator file names use the same operation titles. [Past-epoch source caption, detached from live reference 16. Recorded citation custody: mcp/tests/test_role_capsule_audiences.py blob c1306dc9442d617691906ff7e59f1648bba45c0d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: Nested Curator detail checks keep card and writer record-format references at Curation workflow2 Before ingest, while separately retaining the serving-build command read before a CLI deciding run or write.
- Leaf role texts mark only their own completed steps. [17]
- Every Curator stage keeps the serving build's producer boundary. [18]
- Memory-review instructions select the independent recorded lane. [19]
- Real operation audiences preserve the pinned common part and only the addressed paragraphs. [Past-epoch source caption, detached from live reference 20. Recorded citation custody: mcp/tests/test_role_capsule_audiences.py blob c1306dc9442d617691906ff7e59f1648bba45c0d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: For every manifest-declared role/operation pair, the real-operation audience test compiles the addressed capsule, rejects leaked audience markers and compares that operation block’s content hash with its D656_STAGE_SHA256 entry; its final census must cover every declared pair.
- Operation audience markings preserve the pinned bytes and the immutable closeout. [Past-epoch source caption, detached from live reference 21. Recorded citation custody: mcp/tests/test_role_capsule_audiences.py blob c1306dc9442d617691906ff7e59f1648bba45c0d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The operation-source test compares raw source bytes against D656_OPERATION_SHA256. authorized-closeout must keep audience=all and operations/closeout.md; every other operation must use sections and begin with the common audience marker.
- A repairing role stops after three repairs of the same check or finding. [22]
- The expected Reviewer-only paragraph includes the missing-entry return and the clean-sync no-round obligations. [Past-epoch source caption, detached from live reference 23. Recorded citation custody: mcp/tests/test_role_capsule_audiences.py blob c1306dc9442d617691906ff7e59f1648bba45c0d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The current Reviewer-addressed review paragraph says a clean sync opens no new freeze or round, sends shared-path/test-failure repairs for one look, and returns a freeze whose finding entries are missing without counting a round. The real-operation audience test binds each addressed review block to its stored stage seal.

Past-epoch account (original reference and targets retained):

- The approved implementation and review body hashes are repinned in the existing corpus check. [Past-epoch source caption, detached from live reference 24. Recorded citation custody: mcp/tests/test_role_capsule_audiences.py blob c1306dc9442d617691906ff7e59f1648bba45c0d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The expected-operation table records current implementation and review SHA-256 seals alongside the other operations, and the operation-source test compares actual source bytes with those recorded values. This describes stored assertions, not a new approval or repinning event.

- The expected operation corpus pins the implementation and review body hashes alongside the other admitted operation seals; this assertion describes retained pins, not a fresh approval or repinning event. [Past-epoch source caption, detached from live reference 26. Recorded citation custody: mcp/tests/test_role_capsule_audiences.py blob c1306dc9442d617691906ff7e59f1648bba45c0d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The expected operation corpus retains implementation and review source hashes among the D656_OPERATION_SHA256 entries; the existing byte-comparison test checks each admitted operation source against its entry. This asserts retained pins rather than a fresh approval or repinning event.

- The pinned Architect planning paragraph includes the single developer question “go, or review first?”, disclosure that the upfront review has a planned comparison with no task workspace, first-Explain environment creation, and the `intentReview` answer. The Manager paragraphs pin that `intent-review-open` waits for the Architect's go and is not retried. Their planning/coordination seals move with those exact admitted sentences. Anchor: `test_real_operation_audiences_preserve_pinned_common_and_only_addressed_paragraphs` [Past-epoch source caption, detached from live reference 25. Recorded citation custody: mcp/tests/test_role_capsule_audiences.py blob c1306dc9442d617691906ff7e59f1648bba45c0d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The current planning text asks the developer once “go, or review first?”, discloses planned comparison without a task workspace and explainer-workspace creation on first Explain, and records the intentReview answer. Current coordination says intent-review-open waits for Architect go and is not retried. The audience tests retain separate source and addressed-stage seal tables for those operation texts.

- Every declared role/operation’s delivered details are checked for an exact reach-step trigger and not-before wording. Knowledge-use details have role-specific reach triggers; writer-command and refused-write details keep their explicit conditional triggers. An intake-wording mutation must fail and the seen-source census must equal all declared details. [9]
- The ordinary Curator detail labels are checked against curation workflow numbers and titles. Standing details retain when-you-reach/not-before labels; writer-command and correct-write-refusal details instead use their explicitly declared conditional triggers. [15]
- Nested Curator detail checks keep card and writer record-format references at Curation workflow2 Before ingest, while separately retaining the serving-build command read before a CLI deciding run or write. [16]
- For every manifest-declared role/operation pair, the real-operation audience test compiles the addressed capsule, rejects leaked audience markers and compares that operation block’s content hash with its D656_STAGE_SHA256 entry; its final census must cover every declared pair. [20]
- The operation-source test compares raw source bytes against D656_OPERATION_SHA256. authorized-closeout must keep audience=all and operations/closeout.md; every other operation must use sections and begin with the common audience marker. [21]
- The current Reviewer-addressed review paragraph says a clean sync opens no new freeze or round, sends shared-path/test-failure repairs for one look, and returns a freeze whose finding entries are missing without counting a round. The real-operation audience test binds each addressed review block to its stored stage seal. [23]
- The expected-operation table records current implementation and review SHA-256 seals alongside the other operations, and the operation-source test compares actual source bytes with those recorded values. This describes stored assertions, not a new approval or repinning event. [24]
- The current planning text asks the developer once “go, or review first?”, discloses planned comparison without a task workspace and explainer-workspace creation on first Explain, and records the intentReview answer. Current coordination says intent-review-open waits for Architect go and is not retried. The audience tests retain separate source and addressed-stage seal tables for those operation texts. [25]
- The expected operation corpus retains implementation and review source hashes among the D656_OPERATION_SHA256 entries; the existing byte-comparison test checks each admitted operation source against its entry. This asserts retained pins rather than a fresh approval or repinning event. [26]

- Complete D656 operation and per-recipient stage digest literals pin the reviewed audience projections, including closeout bytes. Detail checks cover all declared role/operation pairs and distinguish standing, knowledge-use and conditional writer/refusal triggers. Writer syntax/report semantics remain separate from inline serving-build authority. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [27]
