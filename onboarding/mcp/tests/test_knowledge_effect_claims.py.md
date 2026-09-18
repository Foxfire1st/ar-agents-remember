# mcp/tests/test_knowledge_effect_claims.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_effect_claims.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:20+02:00 |
| lastVerifiedCommitHash |  `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate |  2026-09-18T13:43:14+02:00 |
| reviewedWorkingCandidate | `ar/260915-ks-l13` uncommitted staged source; base `b5a74aee6cdf671c9963f3aba4df6d44b856f697` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](../overview.md)

## Purpose

`InvariantEffectClaim`: the authored effect, its closed vocabulary and its one code. **33 cases**, in the
order the requirement states its clauses, all in the `unit-regression` lane.

## Code Commentary

### Logic

Every case protects one clause group: which payload shape the kind admits, the closed nine-label
vocabulary, the one cardinality rule and its one refusal code, which references resolve, the author and the
lifecycle as stored envelope data, the batch union and the kind registry, and the derived read beside the
mechanical comparison's documented semantic silence.

Two properties are load-bearing enough that the module's own probe tuples exist to make them checkable:

- **There is no truth verdict field and no derived label.** `VERDICT_FIELD_NAMES` probes for a field that
  would make a stored claim a verdict rather than a claim, and each probe is asserted refused as the
  shipped `invalid_payload` — asserted, so the case cannot pass by there being nothing to probe.
  `IDENTITY_FIELD_NAMES` probes for a content address, a logical digest, a fingerprint or a generated
  summary. And an authored effect that the comparison contradicts is stored **exactly as authored**: an
  author records `weaken` on a revision whose statement grew, the record is served with that label and
  `unresolved_references == ()`, and nothing reports the growth or flags the disagreement. A store that
  quietly disagreed with its author is the failure the whole requirement exists to prevent.
- **The comparison keeps its semantic silence.** No field of `KnowledgeDiffItem`,
  `KnowledgeDiffSourceChange` or `KnowledgeDiffResult` carries an effect, a preservation, a severity or a
  verdict word, and the shipped field-name vocabulary carries none either, so the record group adds a
  record *beside* the comparison and never a field on it.

**The vocabulary is closed and pinned, not unioned.** The nine labels are asserted as the literal tuple in
the document's own order, and the literal type the payload validates against *is* that tuple, so a synonym,
a compound label, a free-text label and a locally added tenth member all fail. `DIVISION_EFFECT_LABELS` is
asserted as exactly the frozenset of `split` and `merge` — the set the module's own
`NON_DIVISION_LABELS` is derived from by subtraction rather than restated, so the seven-label tuple cannot
drift from the vocabulary. Near-miss spellings are measured against a real dataset and refused as
`invalid_payload` with the observed label named and nothing written; the same synonym is refused at
construction, so a widening that only the write path enforced would fail here.

**The cardinality rule is one reading, and it is not just a count.** One predicate is asserted over the
four readings Example 6 names, and the cases prove the rule also rejects a claim naming one revision on
*both* sides under an otherwise-admitted combination. Every non-division label admits any counts as long as
the two sides differ, including no references at all. A contradiction is refused as `invalid_payload` and
never as `invalid_reference`, which is the exact instability the blocking finding `CR13-2` was about.

**The lifecycle is the shipped vocabulary and the author is the admission.** Every stored row is served as
`proposed` and no code path sets `accepted`; a payload carrying its own `actor_ref` is refused, while the
command that *can* declare accepted origin data is refused as `promotion_not_supported` — that is what
makes the opposite property checkable. The stored revision and its record row are sealed: the envelope
triggers refuse an update of the payload and a delete of the revision, and the record row cannot be rebound
to another kind.

**The write path is one path.** The batch union carries exactly the four authored-effect commands and their
four kinds; each effect kind resolves to exactly one frozen model in the envelope registry and the effect
kind set does not overlap the requirement kinds; the record group's own operation vocabulary declares the
read and no write operation. Duplicates are keyed on the identical *declaration*, not on the label: an
identical second claim is `duplicate_identity`, while two claims with the same label and different
references, and two differently labelled claims for one comparison, are both stored — an authored
disagreement is not a conflict and is not resolved.

**The read is derived and the generation is refused as a fact.** Two reads over unchanged rows reproduce
the scope byte-for-byte and `READ_OPERATION == "read_effect_scope"`; against a genuine generation-4 dataset
the read refuses as `unsupported_schema` with both numbers, the observed one read from the dataset and the
required one read from the record group's own constant rather than a literal, and nothing is migrated,
repaired or written through.

**What the cases deliberately do NOT assert.** No case asserts that a claim is correct, verified,
consistent with the comparison, or accepted; none asserts a resolved assessment reference; and the
`record_revision.content_digest` column is deliberately **not** counted as a forbidden column — the
exception is the requirement's own, because the sealed revision's content digest belongs to the shipped
envelope and what the packet forbids is these records carrying an identity *of their own*, which the
payload cases assert directly.

### Conventions

Cases are hermetic: temporary directories, in-process APSW databases built through
`mcp/tests/candidate_batch_test_support.py`, a genuine earlier-generation dataset through
`mcp/tests/generation_test_support.py`, and the shared knowledge fixture. The lane row is
`mcp/tests/test-evidence-lanes.toml:164`, and the module is inside the unit population registered in
`mcp/tests/evidence-lifecycle.toml`. The cases drive direct assertions and subtests rather than
parametrization, with every assertion naming the probe, label or kind it is about.

### Invariants And Boundaries

- **No case was removed to make room.** The module is new; it adds 33 cases to the unit population and
  changes no shipped case.
- **The forbidden field sets are asserted as an absence at both planes**: the payload model refuses an
  undeclared field through its ordinary `extra="forbid"` rule — there is no named denylist to relax — and
  no column of any registered generation carries one of the names. A case that asserted only the validator
  half would leave the schema free to hold the value later.
- **A refusal is asserted with its facts**, not merely with a code: the out-of-vocabulary refusal names the
  observed label beside all nine admitted values, the cardinality refusal carries the label and the
  observed counts, and each is paired with `wrote_nothing()`.
- **The change-set half of this record group lives in its sibling module**, `test_knowledge_change_sets.py`,
  and the division of labour is stated in both docstrings.
- **Nothing in this module writes outside a temporary root**, and the record group resolves no requirement
  reference: a stored requirement revision is written by the requirement module's own operation and read
  back unchanged, with this record group's change-set list still empty.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring stating what these cases protect, the failures each case catches, and why the forbidden field sets are asserted as an absence at both planes. | "The forbidden field sets are asserted as an **absence** at both planes" | mcp/tests/test_knowledge_effect_claims.py:1-22 |
| The seven labels that claim neither division nor union, derived by subtraction from the admitted set so the tuple cannot drift. | `NON_DIVISION_LABELS` | mcp/tests/test_knowledge_effect_claims.py:85-87 |
| The probe names that would make a stored claim a verdict rather than a claim. | `VERDICT_FIELD_NAMES` | mcp/tests/test_knowledge_effect_claims.py:91-100 |
| The probe names that would make this record group its own identity authority, or its own narrative. | `IDENTITY_FIELD_NAMES` | mcp/tests/test_knowledge_effect_claims.py:105-114 |
| The case that asserts the effect set is closed, spelled once, in the document's own order, and that the literal type is the declared tuple. | `test_the_closed_vocabulary_is_exactly_the_nine_labels_doc13_names` | mcp/tests/test_knowledge_effect_claims.py:228-248 |
| The case that asserts an out-of-vocabulary label is refused as invalid payload naming the observed label beside all nine admitted values, with nothing written. | `test_an_out_of_vocabulary_label_names_the_observed_label_and_all_nine_admitted_values` | mcp/tests/test_knowledge_effect_claims.py:251-270 |
| The case that asserts near-miss spellings are refused rather than corrected, each asserted and each named in its failure. | `test_every_near_miss_spelling_is_refused_rather_than_corrected` | mcp/tests/test_knowledge_effect_claims.py:273-289 |
| The case that asserts the shape check holds at construction as well as at the storage boundary. | `test_the_payload_model_refuses_a_synonym_at_construction` | mcp/tests/test_knowledge_effect_claims.py:292-302 |
| The case that asserts one cardinality reading predicts exactly the four cases Example 6 names. | `test_the_one_cardinality_rule_admits_exactly_the_four_readings_example_six_names` | mcp/tests/test_knowledge_effect_claims.py:309-319 |
| The case that asserts a split with one output and a merge with one input are refused under the same code, naming label and counts. | `test_a_split_with_one_output_is_refused_as_invalid_payload_naming_label_and_counts` | mcp/tests/test_knowledge_effect_claims.py:322-355 |
| The case that asserts one revision on both sides is refused even though its counts are inside the admitted combination. | `test_one_revision_on_both_sides_is_refused_and_the_shared_reference_is_named` | mcp/tests/test_knowledge_effect_claims.py:358-386 |
| The case that asserts a cardinality contradiction is never reported as an invalid reference. | `test_a_cardinality_contradiction_is_never_reported_as_invalid_reference` | mcp/tests/test_knowledge_effect_claims.py:389-411 |
| The case that asserts every non-division label admits any counts when the two sides differ, and that "any counts" includes none. | `test_every_non_division_label_admits_any_counts_when_the_two_sides_differ` | mcp/tests/test_knowledge_effect_claims.py:414-443 |
| The case that asserts a claim naming no revision on either side is admissible and stored. | `test_an_admissible_claim_with_no_references_at_all_is_stored` | mcp/tests/test_knowledge_effect_claims.py:446-457 |
| The case that asserts the author is the shipped envelope stamped from the admission, and that a payload cannot supply one. | `test_the_author_is_the_admitted_envelope_and_a_payload_cannot_supply_one` | mcp/tests/test_knowledge_effect_claims.py:464-491 |
| The case that asserts a rationale that says nothing is refused at both planes. | `test_a_rationale_that_says_nothing_is_refused_at_both_planes` | mcp/tests/test_knowledge_effect_claims.py:494-506 |
| The case that asserts an unresolvable input or output is refused as an invalid reference naming the identity, with nothing written. | `test_an_input_that_resolves_to_no_stored_revision_is_refused_as_invalid_reference` | mcp/tests/test_knowledge_effect_claims.py:509-535 |
| The case that asserts a claim naming a change set that is not stored is a dangling reference rather than a claim outside every change set. | `test_a_claim_naming_a_change_set_that_is_not_stored_is_refused_as_invalid_reference` | mcp/tests/test_knowledge_effect_claims.py:538-551 |
| The case that asserts the batch applies commands in order, so a citation arriving before its change set is refused by name with its remedy. | `test_a_claim_authored_before_its_change_set_in_one_batch_is_refused_with_its_remedy` | mcp/tests/test_knowledge_effect_claims.py:554-575 |
| The case that asserts the batch union carries exactly the four authored-effect commands and no member accepting a computed label or free-form text. | `test_the_candidate_batch_union_carries_the_four_authored_effect_commands_and_nothing_else` | mcp/tests/test_knowledge_effect_claims.py:582-601 |
| The case that asserts every effect kind resolves to exactly one frozen model and that the effect kind set does not overlap the requirement kinds. | `test_the_envelope_registry_resolves_every_effect_kind_to_its_own_frozen_model` | mcp/tests/test_knowledge_effect_claims.py:604-630 |
| The case that asserts no field can hold a truth verdict about the label, probing the payload through the envelope registry and naming the admitted probe in its failure. | `def test_no_field_can_hold_a_truth_verdict_about_the_label()`; `validate_record_payload` | mcp/tests/test_knowledge_effect_claims.py:633-648; mcp/tests/test_knowledge_effect_claims.py:642-642 |
| The case that asserts no field can hold an identity of this record group's own, or a generated summary or narrative. | `test_no_field_can_hold_an_identity_of_this_record_groups_own` | mcp/tests/test_knowledge_effect_claims.py:651-666 |
| The case that asserts no registered generation carries a verdict, severity or summary column on any table of this record group, and that the appended table carries no identity column either. | `test_no_registered_generation_carries_a_verdict_identity_or_summary_column`; ""content_digest" in GENERATION_4.columns["record_revision"]" | mcp/tests/test_knowledge_effect_claims.py:669-702; mcp/tests/test_knowledge_effect_claims.py:702-702 |
| The case that asserts an incorrect authored effect is stored exactly as authored, with nothing reporting the disagreement. | `test_an_incorrect_authored_effect_is_stored_exactly_as_authored` | mcp/tests/test_knowledge_effect_claims.py:705-729 |
| The case that asserts every stored row is served as proposed and no path sets accepted. | `test_the_stored_lifecycle_is_the_shipped_vocabulary_and_never_a_third_state` | mcp/tests/test_knowledge_effect_claims.py:732-746 |
| The case that asserts a command declaring accepted origin data is refused as promotion not supported. | `test_a_command_declaring_accepted_origin_data_is_refused_as_promotion_not_supported` | mcp/tests/test_knowledge_effect_claims.py:749-769 |
| The case that asserts a stored claim revision cannot be rewritten or deleted and its record row cannot be rebound. | `test_a_stored_claim_revision_cannot_be_rewritten_or_deleted` | mcp/tests/test_knowledge_effect_claims.py:772-804 |
| The case that asserts an unresolved assessment reference is a stored state reported verbatim with its holder, never a refusal. | `test_an_assessment_reference_that_resolves_to_nothing_is_stored_and_reported_unresolved` | mcp/tests/test_knowledge_effect_claims.py:811-837 |
| The case that asserts an identical second claim is refused as duplicate identity with the dataset unchanged. | `test_a_duplicate_identical_claim_is_refused_as_duplicate_identity` | mcp/tests/test_knowledge_effect_claims.py:840-856 |
| The case that asserts two differently labelled claims for one comparison are both stored and neither is promoted. | `test_two_differently_labelled_claims_for_one_comparison_are_both_stored` | mcp/tests/test_knowledge_effect_claims.py:859-876 |
| The case that asserts the duplicate rule is keyed on the declaration, not on the label alone. | `test_a_second_claim_with_the_same_label_but_other_references_is_not_a_duplicate` | mcp/tests/test_knowledge_effect_claims.py:879-893 |
| The case that asserts the read serves a derived scope that reproduces byte-for-byte and that the read is the record group's one operation. | `test_the_authored_effect_read_serves_a_derived_scope_and_reproduces_byte_for_byte` | mcp/tests/test_knowledge_effect_claims.py:900-919 |
| The case that asserts a generation-4 dataset is refused as unsupported schema with both numbers as facts and nothing migrated. | `test_the_record_group_is_registered_by_generation_eight_and_refuses_an_earlier_dataset` | mcp/tests/test_knowledge_effect_claims.py:922-951 |
| The case that asserts no field of the mechanical comparison can hold an authored meaning. | `test_no_field_of_the_mechanical_comparison_can_hold_an_authored_meaning` | mcp/tests/test_knowledge_effect_claims.py:954-968 |
| The case that asserts the record group's own operation vocabulary declares the read and no write path beside the batch. | `test_the_record_groups_own_operation_vocabulary_declares_the_read_and_nothing_else` | mcp/tests/test_knowledge_effect_claims.py:971-981 |
| The case that asserts a stored requirement revision is written by the requirement module's own operation and left untouched, with this record group's change-set list empty. | `test_a_stored_requirement_revision_is_untouched_by_this_record_group` | mcp/tests/test_knowledge_effect_claims.py:984-1004 |
| The lane row placing this module in the unit population. | "mcp/tests/test_knowledge_effect_claims.py" | mcp/tests/test-evidence-lanes.toml:164-164; mcp/tests/test-evidence-lanes.toml:177-184 |
| The registration listing this module among the exact consumers of the shared candidate-batch case harness. | "candidate-batch-case-harness"; `"mcp/tests/test_knowledge_effect_claims.py"` | mcp/tests/evidence-lifecycle.toml:1093-1098; mcp/tests/evidence-lifecycle.toml:1116-1116; mcp/tests/evidence-lifecycle.toml:28-35 |
| The registration listing this module among the exact consumers of the shared earlier-generation case support. | "knowledge-generation-cases"; `"mcp/tests/test_knowledge_effect_claims.py"` | mcp/tests/evidence-lifecycle.toml:1170-1175; mcp/tests/evidence-lifecycle.toml:1203-1203; mcp/tests/evidence-lifecycle.toml:43-50 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The cases exercise one in-process knowledge store
under a temporary root and construct no process, publication or Git object.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:20+02:00 — 260915-KS-L13 curator (uncommitted change set on `ar/260915-ks-l13`, base `b5a74aee`): created this one-to-one card for the effect-claim record group's 33 cases. It records the two load-bearing absences probed rather than trusted (no truth-verdict field, no derived label, with an incorrect authored effect stored exactly as authored), the closed and pinned nine-label vocabulary with its subtraction-derived seven-label complement, the one cardinality rule that is not merely a count, the lifecycle and author as envelope data with `promotion_not_supported` making the opposite property checkable, the duplicate rule keyed on the declaration, the derived read beside the mechanical comparison's documented silence, and the generation-4 refusal that names both numbers as facts. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
