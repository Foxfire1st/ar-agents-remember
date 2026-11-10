# mcp/tests/test_role_capsule_audiences.py

## Governing Overview

[overview](overview.md)

## Purpose

Stage-audience selection preserves role boundaries in compiled capsules: a compiler delivers the common part plus
the selected role's stage parts and nothing else, a declared step's detail bytes travel as separate frozen
references beside the handover file, and the Curator receives its ruled steps without the Manager's or another
role's material. The real operation audiences are checked against pinned bytes, and a repairing role stops after
three repairs of the same check or finding.

## Code Commentary

### Logic

`_compile_corpus_pair()` compiles a role against the corpus and `_delivered_curation_for_d301()` composes what the
Curator's capsule actually delivers at launch. `_assert_bound_action()` requires a read action to link to its detail
exactly once, and `_assert_detail_owner()` / `_assert_owner_clauses()` prove a clause lives in the detail or section
that owns it by failing on a mutant without it. The pins and named clauses come from the test-support modules
`capsule_audience_fixtures` (`D656_OPERATION_SHA256`, `D656_STAGE_SHA256`, `R125_OPERATION_ROLES`, the role and
operation pointer actions, `CURATOR_SERVING_STAGE_BOUNDARY`) and `capsule_audience_v13_fixtures` (the `V13_*` digest
tables with `inverse_v13_short_rules()` and `inverse_v13_paths()`).

- **Audience selection.** `test_compiler_delivers_only_common_and_selected_role_stage_parts` keeps the compiler to
  the common part plus the selected stage.
- **Step details.** `test_compiler_carries_declared_step_detail_bytes_as_separate_references`,
  `test_handover_writes_immutable_source_details_beside_its_file`,
  `test_launch_composition_names_frozen_details_by_their_request_paths` and
  `test_step_details_are_named_for_reaching_their_step_not_intake` keep a step's detail a frozen file named by the
  request it belongs to and bound to the one read action that needs it.
- **Role boundaries.** `test_curator_receives_ruled_step_details_separately_and_keeps_writer_boundaries`,
  `test_manager_curation_does_not_receive_curators_card_or_writer_steps`,
  `test_curator_execution_support_is_an_unconditional_inline_output` and
  `test_leaf_role_texts_mark_only_their_own_completed_steps` keep each role's material with that role.
- **D301.** The `test_d301_*` cases keep the real capsules delivering named step files as frozen launch artifacts,
  the Curator's inline boundaries with its family, change-routing, prose-history and memory-handover details each
  bound to the action that reads it, external backing output inline, bootstrap
  reproducibility rather than reader execution, the delivered authoring resolving the actual routing, and the
  hand-off file read for the first review then reused for repairs.
- **Naming.** `test_curator_detail_names_use_only_curation_workflow_numbers_and_titles`,
  `test_nested_curator_file_names_use_the_same_operation_titles` and
  `test_every_curator_stage_keeps_the_serving_build_producer_boundary` keep the Curator's delivered details equal to
  its declared pointer actions over a five-step curation workflow, nested details linked to their siblings by the
  actions that read them, and the serving build's producer boundary owned by Orientation: the orientation capsule
  carries it inline, curation and recovery carry a bound pointer to it, and the serving-build detail names
  Orientation as its owner.
- **Lanes.** `test_memory_review_instructions_select_the_independent_recorded_lane` selects the recorded memory
  review lane.
- **Pinned audiences.** `test_real_operation_audiences_preserve_pinned_common_and_only_addressed_paragraphs` and
  `test_operation_audience_markings_preserve_pinned_bytes_and_immutable_closeout` pin the current bytes with the
  `V13_*` tables, require that undoing only the admitted short-rule edits and the pinned reference-path moves
  reproduces the `D656_*` digests, and keep the immutable closeout text intact.
- **Repair limit.** `test_repairing_roles_stop_after_three_repairs_of_the_same_check_or_finding` stops a role
  after three repairs of the same subject.

### Conventions

A case compiles the real corpus and compares delivered bytes, so an extra paragraph that leaks into another
role's capsule fails rather than merely being unmentioned.

### Invariants And Boundaries

- A capsule carries the common part plus its own stage's parts, and nothing of another role's.
- A step's detail is an immutable frozen file, not a re-read of the source at send time.


The pinned Architect planning paragraph includes the single developer question “go, or review first?”, disclosure that the upfront review has a planned comparison with no task workspace, first-Explain environment creation, and the `intentReview` answer. The Manager paragraphs pin that `intent-review-open` waits for the Architect's go and is not retried. Their planning/coordination seals move with those exact admitted sentences.

Complete V13 operation and per-recipient stage digest literals pin the current audience projections, including closeout bytes, and the inverse transforms tie them back to the D656 digests. Detail checks cover all declared role/operation pairs and require every declared read action to bind to exactly one link to its emitted detail. Writer syntax and report semantics live in the serving-build and publication-report details, separate from the serving-build authority that Orientation owns. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
- The compiler delivers only the common and selected role stage parts. [1]
- Declared step detail bytes travel as separate references. [2]
- The handover writes immutable source details beside its file. [3]
- The launch composition names frozen details by their request paths. [4]

- The Curator receives ruled step details separately and keeps the writer boundaries. [5]

- Manager curation receives neither the Curator's card nor the writer's steps. [6]

- The real D301 capsules deliver named step files as frozen launch artifacts. [7]

- The Curator's capsule keeps the whole handover and its step limits. [8]

- Curator execution support is an unconditional inline output. [10]

- External backing output stays inline. [11]

- Bootstrap requires reproducibility rather than reader execution. [12]

- Delivered authoring resolves the actual capsule routing. [13]

- The hand-off file is read for the first review and reused for repairs. [14]

- Leaf role texts mark only their own completed steps. [17]

- Every Curator stage keeps the serving build's producer boundary. [18]

- Memory-review instructions select the independent recorded lane. [19]

- A repairing role stops after three repairs of the same check or finding. [22]

- For every declared role/operation pair the delivered detail records equal the role's and operation's pointer actions; each read action binds to exactly one link to the detail's emitted file, each emitted detail round-trips its revision, size and read-only mode, and intake-wording, missing-target, duplicated-paragraph and empty-step mutations must fail; the census covers every declared pair and every declared detail. [9]


- The Curator's delivered curation workflow is numbered one to five with the checks, fact-check and repair headings; its delivered details equal its role and curation pointer actions, each bound to its read action, and its role section carries no numbered workflow. [15]


- Nested Curator details are read through their launch artifacts: the prose-and-history detail binds card history to the card-formats detail, the knowledge-ingest detail binds a deciding or writing command-line run to the serving-build detail, and the serving-build detail binds such a run to `server_info.servingBuild` and names Orientation as the authority owner. [16]


- For every manifest-declared role/operation pair, the real-operation audience test compiles the addressed capsule, rejects leaked audience markers and compares that operation block's content hash with its `V13_STAGE_SHA256` entry; undoing the admitted short-rule edits must match `V13_PRE_SHORT_STAGE_SHA256` and then undoing the pinned path moves must match `D656_STAGE_SHA256`; its final census must cover every declared pair. [20]


- The operation-source test compares raw source bytes against `V13_OPERATION_SHA256`, the short-rule-restored bytes against `V13_PRE_SHORT_OPERATION_SHA256` and the path-restored bytes against `D656_OPERATION_SHA256`. authorized-closeout must keep audience=all and operations/closeout.md; every other operation must use sections and begin with the common audience marker. [21]

- The current Reviewer-addressed review paragraph says a clean sync opens no new freeze or round, sends shared-path/test-failure repairs for one look, and returns a freeze whose finding entries are missing without counting a round. The real-operation audience test binds each addressed review block to its stored stage seal. [23]


- `V13_OPERATION_SHA256` records the current implementation and review source seals alongside the other operations, and the operation-source test compares actual source bytes with those recorded values. This describes stored assertions, not a new approval or repinning event. [24]

- The current planning text asks the developer once "go, or review first?", discloses planned comparison without a task workspace and explainer-workspace creation on first Explain, and records the intentReview answer. Current coordination says intent-review-open waits for Architect go and is not retried. The audience tests retain separate source and addressed-stage seal tables for those operation texts. [25]


- Complete V13 operation and per-recipient stage digest literals pin the current audience projections, including closeout bytes, and the inverse transforms tie them back to the D656 digests. Detail checks cover all declared role/operation pairs and require every declared read action to bind to exactly one link to its emitted detail. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [27]
