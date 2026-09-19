# mcp/tests/test_knowledge_detection_signals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_detection_signals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The declared field-set review plus the required set and the closed vocabularies' agreement with their tuples.** | "test_the_signal_field_set_is_required_and_carries_no_conclusion_bearing_field" | mcp/tests/test_knowledge_detection_signals.py:185-222 |
| **The nine-parameter construction table: every required field, dropped one at a time.** | "test_a_signal_missing_a_required_field_fails_construction" | mcp/tests/test_knowledge_detection_signals.py:223-246 |
| **A conclusion refused as an extra field, and a verdict refused inside the prose field.** | "test_a_payload_supplying_a_conclusion_bearing_field_is_refused_naming_it"; "test_a_verdict_written_into_the_detail_string_is_refused_as_the_same_defect" | mcp/tests/test_knowledge_detection_signals.py:247-284 |
| The closed, versioned condition vocabulary and the refusal that quotes its version. | "test_a_condition_outside_the_declared_vocabulary_is_refused_with_the_vocabulary_version" | mcp/tests/test_knowledge_detection_signals.py:289-303 |
| **The granularity refusal: a whole-file locator cannot support a span observation.** | "test_a_whole_file_observation_recorded_as_a_body_change_is_refused" | mcp/tests/test_knowledge_detection_signals.py:304-341 |
| **The three declared input sets, each member's own discriminator, and the three refusals that keep them distinct.** | "test_the_declared_input_set_vocabulary_is_exactly_three_members_each_with_its_own_discriminator"; "test_a_both_sides_declared_signal_recording_one_side_is_refused_naming_both_halves"; "test_a_union_declaration_with_no_recorded_probe_outcome_is_refused_naming_the_missing_fact" | mcp/tests/test_knowledge_detection_signals.py:346-397 |
| **One side as a complete fact rather than a degraded two-sided one, and the over-claim about the unread side refused.** | "test_a_trigger_side_only_signal_records_one_side_and_no_probe_and_is_not_degraded"; "test_a_trigger_side_only_signal_asserting_a_fact_about_the_unread_side_is_refused" | mcp/tests/test_knowledge_detection_signals.py:398-451 |
| The omission and its limitation refused in both directions. | "test_a_signal_declaring_an_omission_without_the_limitation_and_the_reverse_are_both_refused" | mcp/tests/test_knowledge_detection_signals.py:452-490 |
| The unconditional no-assessment statement, and the advertised truncation and unmapped-path gaps. | "test_every_signal_states_that_no_semantic_assessment_was_performed"; "test_an_incomplete_scan_must_declare_its_truncation_and_an_unmapped_path_its_gap" | mcp/tests/test_knowledge_detection_signals.py:491-522 |
| **Retention refused at a destination that cannot retain, and the unresolved reference that names what would resolve it.** | "test_a_manifest_may_not_be_reported_retained_at_a_destination_that_cannot_retain_it"; "test_a_manifest_reference_that_cannot_be_resolved_names_what_would_resolve_it" | mcp/tests/test_knowledge_detection_signals.py:527-587 |
| **A stale run keeps its recorded versions on the run and on every signal — currentness marks, it never relabels.** | "test_currentness_follows_from_the_version_comparison_and_never_relabels_a_signal" | mcp/tests/test_knowledge_detection_signals.py:592-665 |
| The policy identity and the extractor version as named constants rather than paths. | "test_the_policy_identity_and_the_extractor_version_are_named_constants_not_paths" | mcp/tests/test_knowledge_detection_signals.py:670-690 |
| **A dataset predating the detection table refused with both generation numbers as facts and no migration.** | "test_a_dataset_predating_the_detection_table_refuses_a_detection_write" | mcp/tests/test_knowledge_detection_signals.py:695-723 |
| **Generation 4's additive rule as a prefix equality, with the appended table, its key tuple and its two triggers.** | "test_generation_4_appends_only_and_the_first_twenty_names_are_generation_3_s" | mcp/tests/test_knowledge_detection_signals.py:724-751 |
| The one valid signal the cases vary, and the helper set that builds the sides and the recorded input set. | `signal`; `recorded_input_set`; `input_side`; `both_sides`; `snapshot` | mcp/tests/test_knowledge_detection_signals.py:134-183; mcp/tests/test_knowledge_detection_signals.py:110-132; mcp/tests/test_knowledge_detection_signals.py:83-96; mcp/tests/test_knowledge_detection_signals.py:77-81 |
| The manifest helper whose retention answer the manifest cases assert — re-cited at its own extent. | `manifest` | mcp/tests/test_knowledge_detection_signals.py:98-108 |
| The production record whose construction boundary these cases measure. | `DetectionSignalPayload`; `DetectionScopeManifest`; `conclusion_bearing_fields` | mcp/src/agents_remember/models/knowledge/detection.py:635-753; mcp/src/agents_remember/models/knowledge/detection.py:417-458; mcp/src/agents_remember/models/knowledge/detection.py:268-283 |
| **The generation this module's rule is about: it pins generation 4 by name, which is now one generation behind the newest the registry supports.** | `REQUIRED_DETECTION_GENERATION` | mcp/src/agents_remember/memory/knowledge/detection.py:86-86 |
| The generation builder this module measures against. | `create_schema_statements` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:196-202 |
| **The registry that now holds eight generations, so "the newest supported generation" is generation 8 and generation 4 is the detection rule's own pinned generation rather than the tip.** | `GENERATIONS` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:456-466 |
| **The generation this module's rule is about, and the generation builder/registry it is measured against.** | `REQUIRED_DETECTION_GENERATION`; `create_schema_statements`; `GENERATIONS` | mcp/src/agents_remember/memory/knowledge/detection.py:86-86; mcp/src/agents_remember/memory/knowledge/schema_generations.py:186-186; mcp/src/agents_remember/memory/knowledge/schema_generations.py:425-434; mcp/src/agents_remember/memory/knowledge/schema_generations.py:196-196; mcp/src/agents_remember/memory/knowledge/schema_generations.py:456-469 |
| The lane row this module is registered under. | "unit-regression = [" | mcp/tests/test-evidence-lanes.toml:5-5 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T19:54:18+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the one enforced `citation_anchor_absent_from_range` row in this document.** The registry row cited `schema_generations.py:456-456`, the comment line above the registry, for `GENERATIONS`; the tuple itself is declared at `459`, so the range was widened to `456-469` (the full `GENERATIONS: tuple[SchemaGeneration, ...] = ( … )` declaration). The claim, the anchors and the other four ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `create_schema_statements` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:196-202. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `GENERATIONS` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:456-466. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `create_schema_statements` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:186-192. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand while resolving the memory sync** — `create_schema_statements`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T06:30:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 1 generated projection bullet(s) by hand** — `GENERATIONS`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): **re-read the registry claim against the construct as it now stands.** `KS-R18@v1` appends generation 5, so the registry this case measures holds **five** members rather than four, and the row now says so and names why the case measures the sequence structurally (contiguous `1..N` with `ar-knowledge-sqlite/vN` names in register order) rather than as a hand-written list — a literal list would have gone stale exactly here. Each anchor now resolves to its own extent: the builder's declaration and the registry's own lines are cited separately instead of one range being repeated for both. No other row of this card was changed. Verification metadata advances to the leaf's base commit `e963a01c` because the claim was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T03:15:00+00:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): created this one-to-one card for the new unit-regression suite over the detection *signal*. It records the one-valid-record helper that makes every case name the field it varied, the nine-parameter construction table, the two halves of "a conclusion must not be representable" (an extra field and a verdict written into the prose field), the closed and versioned condition vocabulary, the granularity refusal that makes a whole-file change unable to stand for a span change, the three declared input sets with their three distinct refusals, one side as a complete fact with the unread-side over-claim refused, the declaration/omission agreement checked in both directions, the retention answer that refuses a destination that cannot retain and names what would resolve an unresolved reference, currentness that marks stale without relabelling, the named-constant policy identities, the predating-dataset refusal with both generation numbers as facts, and generation 4's additive rule asserted as a prefix equality. Verification metadata is the leaf's base commit `4264dcc9`: the code commit does not exist yet and closeout owns that stamp.
