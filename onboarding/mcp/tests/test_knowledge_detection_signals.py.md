# mcp/tests/test_knowledge_detection_signals.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

**`DetectionSignal`: the required facts, the closed vocabularies and the construction refusals — 20 case
definitions, one of them a nine-parameter construction table, for 28 collected cases.**

These cases protect the facts-only record and its declared-input-set contract. They occupy the
`unit-regression` lane (registered in `mcp/tests/test-evidence-lanes.toml`) because what they measure is a
typed record's own construction boundary — which fields are required, which vocabulary a value must come
from, and which shape is refused — and not a process, a publication or a Git object.

Every case is named for the property its own assertions measure, and each names the failure it catches: a
signal missing a required field, a condition outside the policy's declared vocabulary, a declaration
disagreeing with the discriminator it recorded, an observed change recorded at a granularity nothing
observed, a rendered judgment written into a prose field, and a manifest reported retained at a
destination that cannot retain it.

The module's helpers build **one valid signal** and let each case vary exactly one thing through
`signal(**overrides)`, so an assertion names the field it overrode rather than restating the whole record;
the `detail` default is the rendered basis, computed from the values the case supplied, so a case that
does not override it is exercising the rendering rule rather than bypassing it.

## Code Commentary

### Logic

- **The field-set review and the required set, in one case.**
  `test_the_signal_field_set_is_required_and_carries_no_conclusion_bearing_field` reviews the *declared*
  field names through `conclusion_bearing_fields`, asserts the required set is present, and asserts the
  closed vocabularies' members are exactly their tuples — including that the `Literal` and the tuple
  agree.
- **A nine-parameter construction table.** `test_a_signal_missing_a_required_field_fails_construction` is
  parametrized over nine field names (namespace, route, condition, input set, extractor version, policy
  version, manifest, scope status, limitations), so "requirement 1.1's field set is all-required" is
  measured field by field rather than asserted once.
- **A conclusion is refused as an extra field and as prose.**
  `test_a_payload_supplying_a_conclusion_bearing_field_is_refused_naming_it` supplies a conclusion-named
  field and asserts the shipped base refuses it; `test_a_verdict_written_into_the_detail_string_is_refused_as_the_same_defect`
  writes a verdict into `detail` and asserts the refusal names the field and the record — the two halves
  of requirement 5.2.
- **The vocabulary is closed and versioned.**
  `test_a_condition_outside_the_declared_vocabulary_is_refused_with_the_vocabulary_version` asserts an
  undeclared condition is refused with the vocabulary's own version rather than recorded as prose.
- **The granularity is part of the fact.**
  `test_a_whole_file_observation_recorded_as_a_body_change_is_refused` records
  `attributed_span_changed` against a `file` locator and asserts the refusal names the locator and the
  granularity the observation supports.
- **The three declared input sets, each with its own discriminator.**
  `test_the_declared_input_set_vocabulary_is_exactly_three_members_each_with_its_own_discriminator`
  asserts the closed set and the three derived discriminator strings;
  `test_a_both_sides_declared_signal_recording_one_side_is_refused_naming_both_halves` is the
  silent-widening shape;
  `test_a_union_declaration_with_no_recorded_probe_outcome_is_refused_naming_the_missing_fact` is union
  semantics the signal cannot show it applied;
  `test_a_trigger_side_only_signal_records_one_side_and_no_probe_and_is_not_degraded` asserts one side is
  a *complete* fact rather than an incomplete two-sided one, and
  `test_a_trigger_side_only_signal_asserting_a_fact_about_the_unread_side_is_refused` is the opposite
  over-claim — the signal may not claim the other side was unchanged.
- **A declaration and an omission cannot disagree in either direction.**
  `test_a_signal_declaring_an_omission_without_the_limitation_and_the_reverse_are_both_refused` drives
  both halves on the shipped idiom.
- **The unconditional statement and the advertised gaps.**
  `test_every_signal_states_that_no_semantic_assessment_was_performed` and
  `test_an_incomplete_scan_must_declare_its_truncation_and_an_unmapped_path_its_gap`.
- **Retention is a report about a verified destination.**
  `test_a_manifest_may_not_be_reported_retained_at_a_destination_that_cannot_retain_it` asserts an
  enclosure-local home cannot satisfy retention, and
  `test_a_manifest_reference_that_cannot_be_resolved_names_what_would_resolve_it` asserts the unresolved
  answer names what would resolve it and is never an empty manifest.
- **Currentness never relabels.**
  `test_currentness_follows_from_the_version_comparison_and_never_relabels_a_signal` marks a run stale and
  asserts the recorded versions survive on the run and on every signal.
- **The published identities are constants, not paths.**
  `test_the_policy_identity_and_the_extractor_version_are_named_constants_not_paths`.
- **The generation rules the record depends on.**
  `test_a_dataset_predating_the_detection_table_refuses_a_detection_write` builds a genuine version-3
  dataset and refuses the write with the observed and required versions as facts, migrating nothing; and
  `test_generation_4_appends_only_and_the_first_twenty_names_are_generation_3_s` asserts the additive rule
  as the prefix equality it is, the appended table, the key tuple, the two triggers and the absence of any
  `ALTER TABLE` in every generation's statements.

### Conventions

- **One valid record, varied by keyword.** Every case builds its signal through `signal(**overrides)`; the
  helper computes the correct `detail` for whatever the case supplied, so overriding a limitation without
  re-rendering is not a way to pass.
- **Refusals are asserted by their text as well as their occurrence**, so a case that expects a
  *specific* refusal cannot pass on an unrelated one.
- **The module is hermetic.** Temporary directories, in-process APSW databases opened through the
  production `open_database`/`create_schema_statements` seam, fixed identities in module constants, and no
  network, clock or Git dependency.
- **The generation cases build up, never down**: a version-3 dataset is created from generation 3's own
  recorded DDL and its own `user_version`, never by downgrading a generation-4 file.

### Invariants And Boundaries

- **The case population is the leaf's own 28 and no integration case.** The unit population is 1315
  against the declared budget; this module's contribution is stated in the leaf's worker report rather
  than raised here.
- **A case that measures the additive rule asserts a prefix equality, not a table count**, so a later
  generation appending its own table does not falsify it.
- **Boundary.** The module protects the *record's* construction contract. The walk, the write path and the
  round trip are `mcp/tests/test_knowledge_detection_runs.py`; nothing here opens a detection store to
  write a run.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The declared field-set review plus the required set and the closed vocabularies' agreement with their tuples.** [1]
- **The nine-parameter construction table: every required field, dropped one at a time.** [2]
- **A conclusion refused as an extra field, and a verdict refused inside the prose field.** [3]
- The closed, versioned condition vocabulary and the refusal that quotes its version. [4]
- **The granularity refusal: a whole-file locator cannot support a span observation.** [5]
- **The three declared input sets, each member's own discriminator, and the three refusals that keep them distinct.** [6]
- **One side as a complete fact rather than a degraded two-sided one, and the over-claim about the unread side refused.** [7]
- The omission and its limitation refused in both directions. [8]
- The unconditional no-assessment statement, and the advertised truncation and unmapped-path gaps. [9]
- **Retention refused at a destination that cannot retain, and the unresolved reference that names what would resolve it.** [10]
- **A stale run keeps its recorded versions on the run and on every signal — currentness marks, it never relabels.** [11]
- The policy identity and the extractor version as named constants rather than paths. [12]
- **A dataset predating the detection table refused with both generation numbers as facts and no migration.** [13]
- **Generation 4's additive rule as a prefix equality, with the appended table, its key tuple and its two triggers.** [14]
- The one valid signal the cases vary, and the helper set that builds the sides and the recorded input set. [15]
- The manifest helper whose retention answer the manifest cases assert — re-cited at its own extent. [16]
- The production record whose construction boundary these cases measure. [17]
- **The generation this module's rule is about: it pins generation 4 by name, which is now one generation behind the newest the registry supports.** [18]
- The generation builder this module measures against. [19]
- **The registry that now holds eight generations, so "the newest supported generation" is generation 8 and generation 4 is the detection rule's own pinned generation rather than the tip.** [20]
- **The generation this module's rule is about, and the generation builder/registry it is measured against.** [21]
- The lane row this module is registered under. [22]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
