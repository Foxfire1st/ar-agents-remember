# mcp/tests/test_migration_census.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_migration_census.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `3888cd8600e39a52c540d6038820759e3d4ffa7a`|
| lastVerifiedCommitDate |  2026-09-20T20:02:13+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

**The 48 `unit-regression` cases that pin `KS-R21@v1`'s truth-coverage census, staged migration and
cutover preparation as behaviour, in the nine section-comment families the module declares.** They are
the parser and its declared formats; the inventory taken over the *scope* rather than over the corpus;
the frozen baseline; the explicit-mapping registry with its single wildcard; the generation-9 census
record kinds; the shipped write path together with the four-cell accounting, its six measures and its
four slice axes; reference resolution's three states and the mechanical mismatch report; the cutover's
three artifacts, which execute nothing; and the closing AST sweep that refuses a corpus write anywhere
in the migration package. The docstring states the selection rule the whole file is written to — one
case per property, because a case that only restated another case's property would be a variant rather
than a protection — and it names the failures the requirement packet exists to prevent: an inventory
that cannot see a surface with no onboarding, an importer that interprets, a reference repaired by
resemblance, a mismatch reported as a verdict, a denominator taken from the corpus being measured, an
`N` whose cells do not close, and a cutover that executes itself. Six of the families never open the
candidate dataset at all — the parser, the inventory, the mappings, the baseline, the resolution
report and the cutover artifacts take strings, declared values and a temporary directory rather than
the harness — so only the accounting family, one record-kind case and the final sweep reach the
fixture's real dataset.

## Code Commentary

### Logic

**The module is three inline artifact literals, three local builders, and then the cases in the file's
own section order, each family introduced by a section comment that names the property it protects.**
`CARD_TEXT`, `OVERVIEW_TEXT` and `NO_TABLE_TEXT` are the parser's inputs written as literals, so the
five parser cases and the five inventory cases read text the module owns rather than a file outside
the temporary root a case makes. `_baseline` returns the fixture's frozen baseline through the one
factory that validates it; `_reference` derives a `census.ReferenceInventory` with an optional reviewer;
`_reference_for` builds one `Reference` at that baseline for the resolution cases. Those three builders
are the whole local vocabulary: every other case states its own values inline and names the shipped
constructor it is measuring.

**The parser family measures the metadata-table boundary and the declared-format registry.**
`test_the_metadata_table_ends_before_the_body_so_a_body_table_is_not_a_front_matter_key` asserts the
six keys in declaration order and that the card's own `Invariants And Boundaries` heading never became a
front-matter field.
`test_an_artifact_with_no_metadata_table_is_unsupported_and_reports_what_was_not_parsed` requires the
`unsupported` outcome with a `None` front matter and the unparsed content still carried, because a
silent skip would be an artifact with no row.
`test_a_route_overview_declares_its_scope_through_source_route_not_through_a_path` reads the route
overview as `route_local_overview`, finds `sourceRoute` equal to `mcp/` and asserts `path` is absent,
so a parser that only understood file cards would fail here.
`test_every_declared_format_carries_a_reason_and_the_unsupported_form_is_named` requires every entry of
`declared_formats()` to carry a non-blank reason and re-parses the generated artifact to confirm the
declared list did not silently widen. `test_citation_keys_are_read_as_references_with_their_location`
finds the card's declared citation key among the parsed citation keys, finds it again among the
reported references with the `cit:(` mark stripped, and reads its `field_or_section` as the heading it
was written under.

**The inventory family is the "scope, not the corpus" half of the requirement, and the baseline and
mapping families keep the census's inputs declared rather than inferred.**
`test_the_inventory_reports_an_in_scope_source_that_has_no_onboarding_card` builds a scope over two
sources with one card and finds the uncarded source in `rows_without_onboarding` with
`counts_by_state["absent"] == 1`.
`test_a_card_whose_declared_source_is_out_of_scope_still_gets_a_row` is the other direction of the
same omission: a card pointing at a source the scope does not name still produces a row, and every row
carries a non-empty parsing outcome.
`test_an_unreadable_artifact_becomes_a_row_with_its_outcome_rather_than_raising` writes non-UTF-8 bytes
and requires the `unreadable` outcome with the observed content instead of an exception.
`test_a_route_path_is_the_normalised_shipped_spelling_with_no_trailing_separator` asserts the resolved
entry's route is `mcp` and not `mcp/`, which is the spelling the shipped route writer admits.
`test_the_declared_doc_type_is_the_authority_for_an_artifacts_kind` plants a card whose declared form
disagrees with its filename and requires the declaration to win: `file-level-onboarding` observed and
`file_level_onboarding` as the kind.
`test_an_unfrozen_baseline_is_refused_rather_than_accepted_as_a_ref_name` hands `require_frozen_baseline`
the branch name `main` and reads back the `invalid_reference` refusal, then accepts the two object ids;
`test_two_baselines_are_two_observations_and_never_one_cohort` builds a second baseline and asserts the
two keys differ, because a census that merged them would report one cohort read at two trees.
`test_an_artifact_whose_declared_form_matches_no_entry_is_unmapped_and_not_best_fitted` asks
`mappings.select_mapping` for an undeclared format and gets `None`, then confirms the declared
catch-all still answers — so the unmapped state is reachable rather than absorbed — and requires
`mapping_identity(None)` to be `NO_MAPPING_ID`.
`test_the_disposition_mapping_is_the_registrys_only_wildcard_and_supplies_no_rationale` counts the
`"*"` entries and finds exactly one, without `rationale` among its supplied fields, and
`test_no_mapping_supplies_a_claim_kind_applicability_or_assessment` sweeps every entry against the
three curator-authored field names, because an importer that could fill one of them would be
classifying prose.

**The record-kind family measures the schema's own boundary, and the write-path cases measure what the
shipped batch operation will and will not do.** `test_the_census_records_carry_no_content_address_digest_or_fingerprint_column`
walks only the tables generation 9 appends — `GENERATION_9.tables[len(GENERATION_8.tables):]` — and
refuses any of the four identity columns, so a census row cannot become a second identity authority.
`test_the_census_record_kinds_join_a_registered_generation_that_appends_to_its_predecessor` asserts
generation 8's table tuple is a prefix of generation 9's and that every generation-8 table keeps its
columns and primary key, then pins `CURRENT_GENERATION is GENERATION_9`.
`test_a_raw_sql_update_of_a_census_row_is_aborted_by_the_schema` inserts one inventory row over the
fixture's real connection and then requires `apsw.Error` from an `UPDATE` on it, which is the trigger
pair generation 9 appends to every one of its six tables.
`test_the_seed_writes_every_census_record_kind_through_the_shipped_batch_operation` reads the seeded
dataset back and asserts four inventory rows, five claims, four dispositions, five evidence records and
one realization — the arithmetic of the fixture's own corpus, written through
`change_knowledge_candidate` and nothing beside it.
`test_re_running_the_same_records_at_the_same_baseline_refuses_rather_than_duplicating` applies one
identical inventory-row command twice: the first is `changed`, the second is `refused` with a refusal
present and `before` equal to `after`.
`test_a_resolution_target_state_is_stored_verbatim_and_never_repaired` stores a `corrected_by` link
whose target is not at this baseline and reads back `unresolved` and the untouched target ref, and
`test_a_disposition_split_link_records_which_records_a_claim_became` reads back a `split_into` link
naming the claim id the disposition produced.

**The accounting family is the requirement's arithmetic, and every case in it asserts a figure that a
wrong implementation could not produce.** `test_a_claim_with_no_assessment_is_pending_and_never_counted_as_supported`
finds the claim the fixture recorded without a verdict and requires its cell to be `P`, which is the
fabricated `T` the packet exists to prevent.
`test_the_accounting_closes_and_the_three_claim_states_are_separated` asserts
`total == supported + contradicted + unresolved + pending` and then the individual figures — one
supported, one contradicted, two pending, none unresolved, one historical outside the cohort.
`test_the_historical_piece_carries_a_disposition_and_stays_out_of_the_cohort` reads the disposition off
the claim payload and asserts `claim_enters_cohort` is false for it, and
`test_the_unique_and_occurrence_counts_are_both_reported_for_one_repeated_truth` asserts four
occurrences, three unique claims and a non-empty `repeats` for the text the fixture recorded twice.
`test_every_slice_axis_is_reported_and_each_slice_carries_the_four_way_separation` iterates the four
axes, requires each to be non-empty with the axis named in the message, and re-asserts the closing sum
per slice; `test_the_category_slice_is_keyed_by_the_curators_authored_claim_kind` reads the category
keys and finds the two authored kinds plus `unclassified`, so a key can only come from a recorded
association.
`test_the_correctness_measure_is_accompanied_by_its_unresolved_and_unassessed_counts` reads
`correctness_among_resolved_claims` as `0.5` and requires `U=0` and `P=2` in its own note;
`test_the_coverage_measures_are_unmeasured_without_an_independently_reviewed_inventory` requires
`not_measurable` with no value and an absent recorded reviewer;
`test_an_inventory_whose_reviewer_is_its_author_is_refused_and_publishes_no_coverage` makes the
reviewer the author and gets `coverage_is_publishable` false and a `ValueError` from
`require_independent_reviewer`; and
`test_the_report_renders_measures_together_and_never_as_one_composite_score` walks `MEASURE_NAMES`,
requires `not_measurable` to be visible in the rendering, and refuses the words `score`, `grade` and a
standalone `pass` anywhere in it.

**The resolution family makes "reported, never repaired" a measurement.** `test_reference_resolution_reports_resolved_unresolved_and_ambiguous_as_three_states`
resolves one exact spelling, one absent path, a differently-cased spelling, a truncated spelling and a
candidate set holding the same path twice, and reads back `resolved`, `unresolved`, `unresolved`,
`unresolved` and `ambiguous` — the ban on repair by resemblance stated as three comparisons plus one
count. `test_a_resolution_whose_candidates_contradict_its_state_is_refused_at_construction` builds an
`unresolved` resolution that carries a candidate and a `resolved` one that carries none, and requires
`ValueError` for both. `test_the_reference_counts_partition_totals_every_reference` asserts the three
counts sum to the two references read. `test_a_mechanical_mismatch_is_reported_as_a_fact_and_never_classified`
renders the `declared_source_absent` fact and then asserts none of the five disposition spellings
appears in the text, so the pipeline cannot choose one of the curator's four verdicts for itself.
`test_a_metadata_contradiction_is_reported_only_when_the_two_declared_paths_disagree` reads `None` for
two equal declared paths and the `metadata_contradicts_front_matter` kind for two that differ.
`test_two_records_claiming_one_anchor_are_reported_with_both_claimants` requires the duplicate tuple to
name the anchor and both claimants rather than which one is right.
`test_the_mismatch_report_renders_byte_identically_whatever_order_the_facts_arrived_in` renders two
facts in both orders and compares the two strings, and
`test_an_unresolved_reference_is_reported_as_a_mismatch_and_not_as_a_refusal` turns a resolution whose
kind has no candidates into one reported `declared_source_absent` mismatch instead of stopping the run.

**The cutover family is §8's prepared-and-not-executed boundary, and the last case is a syntactic proof
about the whole migration package.** `test_the_cutover_produces_three_artifacts_and_executes_none_of_them`
asserts the artifact mapping's three keys and reads `executes_cutover` false, `decision_state` `absent`
and no decision reference off the proposal. `test_the_escalation_quotes_the_governing_boundary_and_its_exact_item`
requires `design/storage-design.md:465` and the item `starts migration/cutover` verbatim, so the
proposal names the sentence the decision is reserved by.
`test_the_criteria_are_not_softened_and_an_unmet_one_is_reported_with_its_measure` deliberately fails
`CRIT-4-assessment-completion` and requires the verdict to begin `cutover is not yet justified` with
the criterion id and its observed measure inside it.
`test_an_evaluation_that_omits_a_declared_criterion_is_refused` and
`test_a_criterion_that_was_never_declared_cannot_be_measured` are the two ends of the same gate: an
evaluation missing a declared criterion raises, and a criterion id the registry never declared cannot
be measured at all. `test_the_plan_names_the_archival_step_the_point_of_no_return_and_the_rollback_story`
requires the point of no return to be one of the plan's own step orders, the archival text to state
that the archive is not on any reader's path, and the rollback story to speak of something reversible.
`test_the_plan_creates_no_trigger_no_flag_and_no_scheduled_activation` sweeps every step action for
`trigger`, `schedule` and `flag` and asserts the proposal carries no `approved` and no `activation`
attribute, which is requirement 8.4 read as an absence rather than a promise.
`test_the_census_declares_no_route_inference_and_no_corpus_write` parses every `*.py` under the
migration package with `ast` and asserts the offender list is empty, where an offender is a
`write_text`, `write_bytes` or `unlink` attribute call or a two-argument `open` — a mention inside a
docstring is not a write, and a write inside a comprehension is not missed.

### Conventions

- **Lane and marker.** `mcp/tests/test-evidence-lanes.toml:128` files this module under
  `unit-regression`, and the module declares no `pytestmark`: its cases are selected by the project
  default (`-m "not integration"`), not by a marker of their own.
- **One case per property, and no parametrisation.** Where a family has several spellings they are
  iterated inside one case with the failing value in the assertion — the four slice axes with `axis` in
  the message, the six `MEASURE_NAMES`, the five disposition spellings, and the three forbidden plan
  words — so a failure names which spelling failed rather than only that the case failed.
- **The fixture is the shared support module, imported by its bare module name.** The fourteen names
  it needs come in one `from migration_census_test_support import (...)` block; no case reaches a
  private name of the fixture, and the fixture's four artifact paths are the only paths the cases cite
  by value.
- **The real dataset is reached only through the harness.** Every case that writes or reads the
  candidate dataset takes `with census_harness() as harness:`, opens the store with `harness.store()` in
  a `try:` and closes it in the matching `finally:`; the parser, inventory, mapping, baseline,
  resolution and cutover cases take no store at all.
- **Nothing is mocked.** The inventory cases take pytest's `tmp_path` and write real files under it,
  the schema case executes real SQL over a real APSW connection and expects `apsw.Error`, and the final
  case reads real source files off disk — the only test doubles in the module are the three inline
  artifact literals, which are inputs rather than substitutes.
- **Assertions name the thing they are about.** The parser cases assert the whole key tuple rather
  than a count, the mismatch case reads the kind out of the rendered text, the slice cases put the axis
  in the failure message, and the accounting cases compare individual cells as well as the closing sum,
  so a discrepancy in any one of them is visible.

### Invariants And Boundaries

- **The metadata table ends before the body.** A body table is never a front-matter key, and an
  artifact that declares no metadata table is `unsupported` with the content that was not parsed rather
  than a silent skip.
- **The inventory is over the scope, not the corpus.** A source with no card gets a row, a card whose
  declared source is gone gets a row, and an unreadable artifact is a row carrying `unreadable` and its
  observed content instead of an exception.
- **The declared `doc_type` is the authority for an artifact's kind.** The filename is consulted only
  for an artifact that declares none, and a route overview declares its scope through `sourceRoute`.
- **A baseline is two exact object ids.** A ref name is refused with `invalid_reference`, and two
  baselines are two observations whose keys differ — they can never be merged into one cohort.
- **The mapping registry is data and has exactly one wildcard.** An undeclared format selects nothing
  rather than a nearest entry, and no mapping supplies a claim kind, an applicability, an assessment or
  a rationale.
- **The census record kinds append and carry no second identity authority.** Generation 9 preserves
  every generation-8 table, column and primary key, no census table declares a digest, fingerprint or
  content-address column, and a raw SQL update is aborted by the schema's own trigger.
- **Records are written only through the shipped batch operation.** There is no second write path and
  no bulk writer; a re-run at the same baseline refuses with `before` equal to `after` rather than
  appending duplicates.
- **A stored value is stored verbatim.** A link's target state is kept as `unresolved` with its target
  ref intact, never canonicalised into a match it never resolved to.
- **The accounting closes and absence is stated, never zero.** `N = T + F + U + P`; an unassessed claim
  is `P` and never `T`; a historical piece keeps its disposition and stays outside the cohort.
- **Both counts and all four slice axes are always reported.** Unique and occurrence counts travel
  together, and every slice carries the full four-way separation keyed by a recorded association.
- **No measure is a bare ratio and coverage has no corpus-derived denominator.** `T/(T+F)` carries its
  `U` and `P` in its own note, `C/K` is `not_measurable` until an independent reviewer is recorded, a
  self-reviewed inventory is refused, and the rendering carries no score, no grade and no standalone
  pass.
- **Resolution has three states and repairs nothing by resemblance.** The comparison is exact spelling
  equality, a state its own candidate set contradicts is refused at construction, and a dangling
  reference is a reported mismatch rather than a refusal.
- **The cutover is prepared and never executed.** Three artifacts with `executes_cutover` false and
  decision state `absent`; an omitted criterion and an undeclared criterion are both refused; no step
  action mentions a trigger, a schedule or a flag.
- **The migration package opens the corpus for reading only.** The closing sweep parses every `*.py` in
  the package and refuses any `write_text`, `write_bytes`, `unlink` or two-argument `open`, so a re-run
  cannot be made unmeasurable by an in-place rewrite.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The docstring fixes the operating policy — one case per property, because a case that restated another's property would be a variant rather than a protection — and names the seven consequential failures the requirement packet exists to prevent. | one case per property; "one case per property" | mcp/tests/test_migration_census.py:1-9 |
| Three inline artifact literals — a file card, a route overview and a generated artifact with no metadata table at all — are the text the parser and inventory cases read, so no case's input depends on a file outside the temporary root it makes. | `CARD_TEXT`; `OVERVIEW_TEXT`; `NO_TABLE_TEXT` | mcp/tests/test_migration_census.py:60-101 |
| Three local builders keep the frozen baseline, the reference inventory and one resolution input out of the shared support module: the baseline comes from the one factory that validates it, and the reference inventory is derived for an optional reviewer. | `_baseline`; `_reference`; `_reference_for` | mcp/tests/test_migration_census.py:104-129; mcp/tests/test_migration_census.py:660-667 |
| **The parser family's five cases:** the metadata table ends before the body so a body table is not a front-matter key; an artifact with no metadata table is `unsupported` and still carries what was not parsed; a route overview declares its scope through `sourceRoute` and carries no `path`; every declared format carries a non-blank reason; and a citation key is read as a reference with the section it came from. | `unsupported`; `sourceRoute`; `test_the_metadata_table_ends_before_the_body_so_a_body_table_is_not_a_front_matter_key`; `test_a_route_overview_declares_its_scope_through_source_route_not_through_a_path`; `test_every_declared_format_carries_a_reason_and_the_unsupported_form_is_named`; `test_citation_keys_are_read_as_references_with_their_location` | mcp/tests/test_migration_census.py:132-197; mcp/src/agents_remember/memory/migration/parse.py:256-282; mcp/src/agents_remember/memory/migration/parse.py:283-315 |
| **The inventory family's five cases:** an in-scope source with no card still gets a row and counts as `absent`; a card whose declared source is out of scope still gets a row with a parsing outcome; a non-UTF-8 artifact becomes a row with outcome `unreadable` instead of raising; a route path is the normalised shipped spelling with no trailing separator; and the declared `doc_type`, not the filename, decides the artifact kind. | `absent`; `unreadable`; `doc_type`; `test_the_inventory_reports_an_in_scope_source_that_has_no_onboarding_card`; `test_a_card_whose_declared_source_is_out_of_scope_still_gets_a_row`; `test_an_unreadable_artifact_becomes_a_row_with_its_outcome_rather_than_raising`; `test_a_route_path_is_the_normalised_shipped_spelling_with_no_trailing_separator`; `test_the_declared_doc_type_is_the_authority_for_an_artifacts_kind` | mcp/tests/test_migration_census.py:200-287; mcp/src/agents_remember/memory/migration/inventory.py:622-673; mcp/src/agents_remember/memory/migration/inventory.py:287-307; mcp/src/agents_remember/memory/migration/inventory.py:325-354 |
| **The baseline family's two cases:** a baseline named by a ref is refused with `invalid_reference` while two object ids are accepted as a `FrozenBaseline`, and two baselines are two observations whose keys differ so they can never be one cohort. | `invalid_reference`; `FrozenBaseline`; `test_an_unfrozen_baseline_is_refused_rather_than_accepted_as_a_ref_name`; `test_two_baselines_are_two_observations_and_never_one_cohort` | mcp/tests/test_migration_census.py:289-313; mcp/src/agents_remember/memory/migration/baseline.py:90-125; mcp/src/agents_remember/memory/migration/baseline.py:36-89 |
| **The mapping family's three cases:** a format the registry never declared selects nothing, so the unmapped state stays reachable rather than absorbed by the wildcard; the registry carries exactly one wildcard entry and it supplies no `rationale`; and no entry supplies a claim kind, an applicability or an assessment disposition. | `MAPPINGS`; `rationale`; `test_an_artifact_whose_declared_form_matches_no_entry_is_unmapped_and_not_best_fitted`; `test_no_mapping_supplies_a_field_only_a_curator_may_author` | mcp/tests/test_migration_census.py:315-347; mcp/src/agents_remember/memory/migration/mappings.py:51-51; mcp/src/agents_remember/memory/migration/mappings.py:80-160; mcp/src/agents_remember/memory/migration/mappings.py:161-197 |
| **The record-kind family's three cases:** no table generation 9 appends declares a content-address, logical-digest or fingerprint column, so a census record cannot become a second identity authority; generation 9 appends to generation 8 without retyping, reordering or dropping a table, column or primary key, and `CURRENT_GENERATION` is generation 9; and a raw SQL update of an inventory row is aborted by the schema's own trigger. | `content_digest`; `CURRENT_GENERATION`; `GENERATION_9`; `test_the_census_records_carry_no_content_address_digest_or_fingerprint_column`; `test_the_census_record_kinds_join_a_registered_generation_that_appends_to_its_predecessor`; `test_a_raw_sql_update_of_a_census_row_is_aborted_by_the_schema` | mcp/tests/test_migration_census.py:349-399; mcp/src/agents_remember/memory/knowledge/schema_generations.py:439-450; mcp/src/agents_remember/memory/knowledge/schema_generations.py:479-479; mcp/src/agents_remember/memory/knowledge/schema_v9.py:349-362 |
| **The write path is the shipped batch operation and it stores what it was given verbatim:** the seed's four inventory rows, five claims, four dispositions, five evidence records and one realization all arrive through `change_knowledge_candidate`; a re-run of the same records at the same baseline is `refused` with `before` equal to `after`; a link target is kept as `unresolved` with its ref intact; and a `split_into` link records which record a claim became. | `change_knowledge_candidate`; `refused`; `unresolved`; `split_into`; `CensusDispositionLink`; `test_the_seed_writes_every_census_record_kind_through_the_shipped_batch_operation`; `test_re_running_the_same_records_at_the_same_baseline_refuses_rather_than_duplicating`; `test_a_resolution_target_state_is_stored_verbatim_and_never_repaired`; `test_a_disposition_split_link_records_which_records_a_claim_became` | mcp/tests/test_migration_census.py:401-419; mcp/tests/test_migration_census.py:583-601; mcp/tests/test_migration_census.py:602-656; mcp/tests/migration_census_test_support.py:313-399; mcp/src/agents_remember/application/knowledge.py:318-341; mcp/src/agents_remember/models/knowledge/census.py:274-289; mcp/src/agents_remember/memory/knowledge/census_records.py:832-923 |
| **The accounting family closes the sum and separates every state:** an unassessed claim is cell `P` and never `T`, the separation refuses to exist unless `N = T + F + U + P`, the historical piece keeps its recorded disposition and stays outside the cohort, and one repeated truth is reported as both four occurrences and three unique claims. | `cell_of`; `claim_enters_cohort`; `Separation`; `UniqueOccurrenceCounts`; `test_a_claim_with_no_assessment_is_pending_and_never_counted_as_supported`; `test_the_accounting_closes_and_the_three_claim_states_are_separated`; `test_the_historical_piece_carries_a_disposition_and_stays_out_of_the_cohort`; `test_the_unique_and_occurrence_counts_are_both_reported_for_one_repeated_truth` | mcp/tests/test_migration_census.py:420-485; mcp/src/agents_remember/memory/migration/census_measures.py:81-116; mcp/src/agents_remember/memory/migration/census_measures.py:171-191; mcp/src/agents_remember/memory/migration/census_measures.py:265-279; mcp/src/agents_remember/memory/migration/census_measures.py:487-509 |
| Every slice axis is reported with the full separation and keyed by a recorded association: the four axes are iterated and each slice's own total is asserted to equal its four cells, and the category axis carries the two authored claim kinds plus the `unclassified` key. | `slice_axis`; `unclassified`; `test_every_slice_axis_is_reported_and_each_slice_carries_the_four_way_separation`; `test_the_category_slice_is_keyed_by_the_curators_authored_claim_kind` | mcp/tests/test_migration_census.py:487-523; mcp/src/agents_remember/memory/migration/census_measures.py:192-207; mcp/src/agents_remember/memory/migration/census_measures.py:228-232 |
| **A measure is never a bare ratio and coverage is never computed from the corpus being measured:** the correctness measure carries `U=0` and `P=2` in its own note, the coverage measures are `not_measurable` with no value while no reviewer is recorded, an inventory whose reviewer is its own author is refused, and the rendering holds no `score`, no `grade` and no standalone `pass`. | `not_measurable`; `require_independent_reviewer`; `score`; `grade`; `pass`; `test_the_correctness_measure_is_accompanied_by_its_unresolved_and_unassessed_counts`; `test_the_coverage_measures_are_unmeasured_without_an_independently_reviewed_inventory`; `test_an_inventory_whose_reviewer_is_its_author_is_refused_and_publishes_no_coverage`; `test_the_report_renders_measures_together_and_never_as_one_composite_score` | mcp/tests/test_migration_census.py:525-582; mcp/src/agents_remember/memory/migration/census.py:121-141; mcp/src/agents_remember/memory/migration/census.py:172-199; mcp/src/agents_remember/memory/migration/census_measures.py:117-147 |
| **Reference resolution has exactly three states and repairs nothing by resemblance:** an exact spelling resolves, a differently-cased or truncated spelling stays `unresolved`, a duplicated candidate set is `ambiguous`, a resolution whose candidates contradict its state is refused at construction, and the three counts partition every reference read. | `resolve_reference`; `Resolution`; `count_resolutions`; `test_reference_resolution_reports_resolved_unresolved_and_ambiguous_as_three_states`; `test_a_resolution_whose_candidates_contradict_its_state_is_refused_at_construction`; `test_the_reference_counts_partition_totals_every_reference` | mcp/tests/test_migration_census.py:670-711; mcp/src/agents_remember/memory/migration/resolution.py:59-101; mcp/src/agents_remember/memory/migration/resolution.py:141-160; mcp/src/agents_remember/memory/migration/resolution.py:169-178 |
| **A mismatch is a mechanical fact, never a verdict, and the report is order-independent:** the rendered fact names `declared_source_absent` and can hold none of the disposition spellings, a contradiction is reported only when two declared paths disagree, duplicate anchors are returned with both claimants, an unresolved reference becomes a mismatch rather than a refusal, and the report renders byte-identically in either arrival order. | `declared_source_absent`; `artifact_mismatches`; `metadata_contradiction`; `duplicate_anchor_claims`; `mismatches_from_resolutions`; `render_report`; `test_a_mechanical_mismatch_is_reported_as_a_fact_and_never_classified`; `test_a_metadata_contradiction_is_reported_only_when_the_two_declared_paths_disagree`; `test_two_records_claiming_one_anchor_are_reported_with_both_claimants`; `test_the_mismatch_report_renders_byte_identically_whatever_order_the_facts_arrived_in`; `test_an_unresolved_reference_is_reported_as_a_mismatch_and_not_as_a_refusal` | mcp/tests/test_migration_census.py:713-790; mcp/src/agents_remember/memory/migration/resolution.py:179-214; mcp/src/agents_remember/memory/migration/resolution.py:215-245; mcp/src/agents_remember/memory/migration/resolution.py:246-271; mcp/src/agents_remember/memory/migration/resolution.py:272-287; mcp/src/agents_remember/memory/migration/resolution.py:288-298 |
| **The cutover family's seven cases keep the switch prepared and unexecuted:** the three artifacts are `criteria`, `plan` and `proposal` with `executes_cutover` false and decision state `absent`; the proposal quotes `design/storage-design.md:465` and its exact item; an unmet criterion is reported with its own measure in a `cutover is not yet justified` verdict; an omitted criterion and an undeclared criterion are both refused; the plan names the archival step and a point of no return that is one of its own step orders; and no step action mentions a trigger, a schedule or a flag. | `cutover_artifacts`; `CUTOVER_PROPOSAL`; `CUTOVER_PLAN`; `evaluate_criteria`; `criteria_verdict`; `measure_criterion`; `design/storage-design.md:465`; `test_the_cutover_produces_three_artifacts_and_executes_none_of_them`; `test_the_escalation_quotes_the_governing_boundary_and_its_exact_item`; `test_the_criteria_are_not_softened_and_an_unmet_one_is_reported_with_its_measure`; `test_an_evaluation_that_omits_a_declared_criterion_is_refused`; `test_the_plan_names_the_archival_step_the_point_of_no_return_and_the_rollback_story`; `test_the_plan_creates_no_trigger_no_flag_and_no_scheduled_activation`; `test_a_criterion_that_was_never_declared_cannot_be_measured` | mcp/tests/test_migration_census.py:792-867; mcp/src/agents_remember/memory/migration/cutover.py:175-239; mcp/src/agents_remember/memory/migration/cutover.py:240-253; mcp/src/agents_remember/memory/migration/cutover.py:254-277; mcp/src/agents_remember/memory/migration/cutover.py:278-293; mcp/src/agents_remember/memory/migration/cutover.py:294-324; mcp/src/agents_remember/memory/migration/cutover.py:325-336 |
| The last case sweeps the whole migration package's syntax trees for corpus writes: the helper collects every `write_text`, `write_bytes` and `unlink` attribute call plus every two-argument `open`, so a mention inside a docstring is not a write and a write inside a comprehension is not missed, and the case asserts the offender list is empty. | `_writing_call_sites`; `write_text`; `write_bytes`; `unlink`; `ast`; `test_the_census_declares_no_route_inference_and_no_corpus_write` | mcp/tests/test_migration_census.py:869-903 |
| **The module is governed evidence rather than an unregistered case file:** it is the `evidence_node` of contract `migration-census-cases`, it is the sole consumer of the `shared-support` artifact `mcp/tests/migration_census_test_support.py`, and the lane manifest files it under `unit-regression`. | `evidence_node`; `migration-census-cases`; `shared-support`; `mcp/tests/test_migration_census.py`; `unit-regression` | mcp/tests/evidence-lifecycle.toml:74-77; mcp/tests/evidence-lifecycle.toml:1614-1630; mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/test-evidence-lanes.toml:128-128 |
| The 48 cases took the unit population six past its declared ceiling, so the ceiling was raised from 2200 to 2300 from the measurement rather than from the plan: the population is 2206 collected, an over-budget population executes zero tests because collection raises, and the integration ceiling was left unchanged. | `unit_case_budget`; `not integration`; `mcp/tests/test_migration_census.py` | pyproject.toml:278-278 |

## Cross-Repo References

No cross-repository behavior is exercised in this file. Its inputs are this repository's own declared
shapes, three inline Markdown literals and a temporary directory the case creates and owns; the frozen
baseline is a pair of object-id *strings* rather than any Git object this module opens, and the only
durable state it touches is the disposable candidate dataset the shared fixture initializes under its
own `TemporaryDirectory`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T00:58+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 7 enforced citation rows this card carried (citation_anchor_absent_from_range, citation_range_out_of_bounds). Every row was re-read against the source rather than trusted from the item's cited text. `_reference_for` was cited one line below its declaration (661-668 → 660-667); the write-path row's two case ranges started one line past their declarations (584-601 → 583-601, 603-656 → 602-656); the final sweep row's range ran one line past the end of the file (869-904 → 869-903); and two rows named cases that were merged upstream, so each was re-cited to the surviving case that carries the fact — `test_an_artifact_with_no_metadata_table_is_unsupported_and_reports_what_was_not_parsed` is now asserted inside `test_the_metadata_table_ends_before_the_body_so_a_body_table_is_not_a_front_matter_key` (132-197), and the wildcard/`rationale` and curator-authored-field pair inside `test_no_mapping_supplies_a_field_only_a_curator_may_author` (315-347). Five further rows on this card carried the same one-line-late range start outside the enforced bucket (the item's report-only "stale by a move" list) and were repointed to the declaration each claim names: 421-485 → 420-485, 488-523 → 487-523, 526-582 → 525-582, 671-711 → 670-711, 714-790 → 713-790. No claim wording was changed, every other range is untouched, and no verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 3 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `test_migration_census.py.md:285` (unit_case_budget) — re-read the claim against pyproject.toml, which now declares the pair 3000 / 600 at :263-264; wording corrected, anchor re-pointed at the literal the file declares; `test_migration_census.py.md:271` (test_the_metadata_table_ends_before_the_body_so_a_body_table_is_not_a_front_matter_key) — re-read the claim against the current module: the named case was renamed or consolidated, and the successor's own docstring names the consolidation; `test_migration_census.py.md:274` (test_no_mapping_supplies_a_field_only_a_curator_may_author) — re-read the claim against the current module: the named case was renamed or consolidated, and the successor's own docstring names the consolidation.
- 2026-09-19T22:38+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): **re-read each claim below against the construct its range now covers, corrected the wording where the construct had moved, re-derived every range from the construct's real extent in the file the claim cites, and only then left the card's stamp to closeout.** No `Generated citation repair` bullet is written: these are curator edits, not a mechanical projection. `test_migration_census.py.md:283` — re-read: the claim names the helper and the case; the cited range ran 1 line past the end of the file and pooled both constructs. Re-derived as the two constructs' own extents.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 3 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `test_migration_census.py.md:270` (`_baseline`, `_reference`, `_reference_for`); `test_migration_census.py.md:276` (`change_knowledge_candidate`, `refused`, `unresolved`, `split_into`, `CensusDispositionLink`, `test_the_seed_writes_every_census_record_kind_through_the_shipped_batch_operation`, `test_re_running_the_same_records_at_the_same_baseline_refuses_rather_than_duplicating`, `test_a_resolution_target_state_is_stored_verbatim_and_never_repaired`, `test_a_disposition_split_link_records_which_records_a_claim_became`); `test_migration_census.py.md:284` (`evidence_node`).
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for the `KS-R21@v1` census, staged-migration and cutover-preparation suite. It records the forty-eight cases in the file's own nine section-comment families: the five parser cases around the metadata-table boundary and the declared-format reasons, the five inventory cases that give a row to an uncarded source, an out-of-scope card, an unreadable artifact, the shipped route spelling and the declared `doc_type`, the frozen-baseline pair with its `invalid_reference` refusal, the three mapping cases with one wildcard and no curator-authored field, the three record-kind cases that keep generation 9 additive and refuse a raw SQL update, the shipped write path with its re-run refusal and verbatim link storage, the fourteen accounting cases that close `N = T + F + U + P`, report both counts, all four slice axes, the unmeasured coverage denominator and the composite-score refusal, the eight resolution cases with three states and an order-independent fact-only mismatch report, the seven cutover cases that execute none of their three artifacts and refuse both an omitted and an undeclared criterion, and the closing AST sweep that refuses a corpus write anywhere in the migration package. It also records the registry work this leaf carries — the `migration-census-cases` contract naming this module's seed case as its evidence node, the `shared-support` artifact naming this module as its only consumer, and the `unit-regression` lane member — and the measured consequence that the forty-eight cases took the unit population six past its ceiling and raised it to 2300. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
