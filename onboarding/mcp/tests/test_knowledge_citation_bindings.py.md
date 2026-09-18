# mcp/tests/test_knowledge_citation_bindings.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_citation_bindings.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `a7076008db4772554123794392f84b51143004ec` |
| lastVerifiedCommitDate | 2026-09-18T16:14:01+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l18` uncommitted source; base `e963a01c` |
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](../overview.md)

## Purpose

The citation-binding vocabulary's 25 collected unit cases: the generation-5 append, the closed state
vocabulary and its shipped-literal identity, the counts partition and key-form coverage, the projection
rule, and the closure's refusal and honesty properties. Every case runs against real Pydantic models
and the real registry — no store, no subprocess, no fixture invented for the occasion.

## Code Commentary

### Logic

The generation cases measure the append by **the generation it descends from**: `GENERATION_5`'s
tables begin with `GENERATION_4`'s twenty-one names and each inherited name keeps generation 4's
columns, and `test_the_generation_1_pin_still_recomputes_after_this_leaf_appends_a_generation` proves
the pinned generation-1 fingerprint is unaffected. `test_the_binding_table_has_no_content_address_digest_or_fingerprint_column`
scans the declared column set for identity-valued names — the case would fail if a digest column were
ever added. `test_the_locator_check_names_exactly_the_shipped_source_locator_union` and
`test_the_key_form_check_names_exactly_the_declared_key_forms` read the declared `CHECK` constraints as
text, so a fourth, binding-local spelling cannot be introduced silently.

`test_every_shared_fact_reports_the_identical_shipped_literal` is parametrized over the four shared
states and asserts membership of the shipped `ANCHOR_RESOLUTIONS`;
`test_the_binding_vocabulary_extends_the_shipped_one_only_in_one_direction` asserts the reverse
direction too, so the shipped vocabulary cannot acquire a citation fact. The counts cases drive
`CitationBindingCounts` from both directions (a report that dropped a declared state, and one whose
per-state counts do not partition the set), and the coverage cases refuse a record that leaves an
uncovered form uncounted.

The projection cases assert the three consequences directly, including `hasattr` checks on
`AssessmentDisplay` for a field that must not exist. The closure cases assert a genuine
`selection_incomplete` refusal with the bound reached and **no items and no counts**, that the result
has no semantic-completeness attribute, and that the enumeration returns every recorded binding with
exactly one state.

### Invariants And Boundaries

- Every case here is hermetic: in-process models, the real registry, temporary directories. There is
  no store open, no Git subprocess and no integration marker, which is why the module is registered in
  the unit lane.
- The cases assert **structure**, not literals where a literal would go stale: the generation sequence
  is checked as contiguous `1..N` with `ar-knowledge-sqlite/vN` names rather than as a hand-written
  list, so a renumber cannot leave a green case behind.
- The module-local helpers (`_projection_case`, the small model builders) are module-local test
  source. They are deliberately **not** registered in the governed test-input inventory, and must not
  be.

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
| **The append measured by the generation it descends from, by name, and the generation-1 pin recomputed after the append.** | `test_generation_5_appends_to_generation_4_without_touching_its_twenty_one_tables`; `test_the_generation_1_pin_still_recomputes_after_this_leaf_appends_a_generation` | mcp/tests/test_knowledge_citation_bindings.py:119-145; mcp/tests/test_knowledge_citation_bindings.py:148-151 |
| **The case that scans the declared column set for an identity-valued name, which is how "no second identity authority" is enforced rather than promised.** | `test_the_binding_table_has_no_content_address_digest_or_fingerprint_column` | mcp/tests/test_knowledge_citation_bindings.py:142-160 |
| The two cases that read the declared `CHECK` constraints as text, so a binding-local locator or key-form spelling cannot appear. | `test_the_locator_check_names_exactly_the_shipped_source_locator_union`; `test_the_key_form_check_names_exactly_the_declared_key_forms` | mcp/tests/test_knowledge_citation_bindings.py:173-187; mcp/tests/test_knowledge_citation_bindings.py:190-195 |
| **The shipped-literal identity, asserted per shared fact in both directions.** | `test_every_shared_fact_reports_the_identical_shipped_literal`; `test_the_binding_vocabulary_extends_the_shipped_one_only_in_one_direction` | mcp/tests/test_knowledge_citation_bindings.py:201-236 |
| The closed vocabulary agreeing with its facts in both directions. | `test_the_closed_vocabulary_and_its_facts_agree_in_both_directions` | mcp/tests/test_knowledge_citation_bindings.py:250-255 |
| **The counts partition refused in both directions, and the coverage that refuses to leave an uncovered form uncounted.** | `test_a_count_report_refuses_an_aggregate_that_dropped_a_key_from_the_denominator`; `test_a_key_form_coverage_refuses_to_leave_an_uncovered_form_uncounted` | mcp/tests/test_knowledge_citation_bindings.py:299-332; mcp/tests/test_knowledge_citation_bindings.py:335-345 |
| The uncovered-form state distinct from an absent key, and the write-boundary refusal of a key without the declared mark. | `test_an_uncovered_key_form_is_a_counted_state_distinct_from_an_absent_key`; `test_a_prose_key_that_does_not_carry_the_declared_mark_is_refused` | mcp/tests/test_knowledge_citation_bindings.py:269-299; mcp/tests/test_knowledge_citation_bindings.py:336-347; mcp/tests/test_knowledge_citation_bindings.py:348-356 |
| **The three projection consequences measured directly.** | `test_a_projection_display_refuses_a_conclusion_without_its_basis`; `test_a_projection_row_renders_a_missing_assessment_as_missing`; `test_a_stale_assessment_is_measured_from_its_examined_inputs_and_never_upgraded` | mcp/tests/test_knowledge_citation_bindings.py:377-431 |
| **The bound refusal with no items and no counts, and the absent completeness field beside the declared coverage.** | `test_a_bound_closure_refuses_with_selection_incomplete_and_the_bound_reached`; `test_the_closure_states_no_semantic_completeness_and_reports_its_declared_coverage` | mcp/tests/test_knowledge_citation_bindings.py:433-522 |
| The enumeration returning every recorded binding with exactly one state, and an unresolvable key keeping its recorded key and attribution. | `test_the_enumeration_returns_every_recorded_binding_with_exactly_one_state`; `test_an_unresolvable_key_keeps_its_recorded_key_and_its_attribution` | mcp/tests/test_knowledge_citation_bindings.py:524-679 |
| **The lane row this module occupies, and the lane it sits in — the unit lane, because every case here is hermetic.** | "mcp/tests/test_knowledge_citation_bindings.py" | mcp/tests/test-evidence-lanes.toml:85-85 |

## Cross-Repo References

No cross-repository behavior is exercised in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_citation_bindings.py" repointed to mcp/tests/test-evidence-lanes.toml:85-85. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_citation_bindings.py" repointed to mcp/tests/test-evidence-lanes.toml:84-84. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T09:30+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read the generation-append claim and retired the generated projection bullet that had rewritten its range mechanically.** The generated repair of 2026-09-18T06:06:32+00:00 repointed the two case names to `mcp/tests/test_knowledge_citation_bindings.py:119-145` and `mcp/tests/test_knowledge_citation_bindings.py:148-151` by anchor-range projection rather than by reading; both ranges were checked against the declarations and both hold — `test_generation_5_appends_to_generation_4_without_touching_its_twenty_one_tables` opens at `:119` and `test_the_generation_1_pin_still_recomputes_after_this_leaf_appends_a_generation` at `:148` — so the range is kept and the claim's wording is unchanged. The projection bullet is retired because a mechanically projected range is unverified evidence even when it happens to land correctly; the row is now backed by a reading. Verification metadata advances to the merged base commit `15fe8678`.
- 2026-09-18T06:06:32+00:00: Generated citation repair: `test_the_locator_check_names_exactly_the_shipped_source_locator_union`; `test_the_key_form_check_names_exactly_the_declared_key_forms` repointed to mcp/tests/test_knowledge_citation_bindings.py:173-187; mcp/tests/test_knowledge_citation_bindings.py:190-195. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:06:32+00:00: Generated citation repair: `test_the_closed_vocabulary_and_its_facts_agree_in_both_directions` repointed to mcp/tests/test_knowledge_citation_bindings.py:250-255. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:06:32+00:00: Generated citation repair: `test_a_count_report_refuses_an_aggregate_that_dropped_a_key_from_the_denominator`; `test_a_key_form_coverage_refuses_to_leave_an_uncovered_form_uncounted` repointed to mcp/tests/test_knowledge_citation_bindings.py:299-332; mcp/tests/test_knowledge_citation_bindings.py:335-345. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): created this one-to-one card for the leaf's unit case module (25 collected cases). It records what each group of cases protects, because the protection is not obvious from the names: the generation append is measured **by the generation it descends from, by name**, so a renumber changes two names and not a column list; the identity-column case scans the **declared column set** for an identity-valued name, which is how "no second identity authority on the binding" is enforced rather than promised; the two `CHECK` cases read the constraint text, so a fourth binding-local spelling cannot be introduced silently; and the shipped-literal identity is asserted in **both** directions, so the shipped vocabulary cannot acquire a citation member. The card also records that the cases assert structure rather than literals where a literal would go stale — the registry sequence is checked as contiguous `1..N` with `ar-knowledge-sqlite/vN` names — and that the module-local helpers are deliberately unregistered test source. Verification metadata advances to the leaf's base commit `e963a01c` because every cited construct was re-read against the working tree; the code commit does not exist yet and closeout owns that stamp.
