# mcp/tests/test_role_capsule_compiler.py

## Governing Overview

[tests overview](overview.md)

## Purpose

Focused behavioral checks for the deterministic role-capsule compiler. The compiler's contract is
a set of **observable properties**, and each case here pins one of them: identical admitted facts
and source bytes compile to identical ordered content and digest; ephemeral diagnostics do not move
that digest while a real change to an applicable block does; an unrelated role's source never
reaches a worker capsule; requested tools are narrowed while skill references are merely carried;
every documented refusal happens for its own reason and advertises its remedy; composition needs
neither model nor network; and an unknown role or operation is refused instead of falling back.

**49 test functions → 50 collected cases** (one parametrized).

## Code Commentary

### Logic

The fixture is a small **in-memory corpus built to the canonical manifest schema**, so a case
varies exactly one fact. That is deliberate: *a fixture that mirrors the whole shipped corpus could
only be mutated by editing the things under test, which is how a vacuous assertion gets written.*
Since this leaf's review repairs, the fixture also carries a declared **skill reference**, so the
carried channel is exercised in the same one-fact style as everything else.

Fixture helpers: `fixture_manifest_document` (136-186), `manifest_bytes` (187-192),
`source_text` (193-196), **`skill_source` (197-216)**, `make_source` (217-234),
`manifest_source` (235-247), `all_sources` (248-271), `selection_for` (272-292),
`worker_binding` (293-316), `launcher_binding` (317-329), `compile_worker` (330-347),
`failure` (348-353), `replaced` (354-376).

The cases group by property:

| Group | Cases |
| --- | --- |
| determinism and identity | `test_identical_input_compiles_to_identical_ordered_content_and_digest` (377-388) · `test_instruction_order_is_shared_core_then_role_then_operation` (389-399) · `test_reordering_the_composed_blocks_changes_the_semantic_digest` (422-446) · `test_a_real_binding_change_does_move_the_semantic_digest` (447-460) |
| diagnostics are not identity | `test_a_declared_but_unselected_specialization_changes_diagnostics_not_identity` (400-421) |
| selection scope | `test_changing_an_unrelated_role_leaves_the_worker_capsule_untouched` (461-471) · `test_changing_an_applicable_operation_block_changes_that_capsule` (472-483) · `test_a_shared_core_change_reaches_the_capsule_that_composes_it` (484-499) · `test_an_admitted_specialization_is_composed_after_the_operation` (592-607) |
| role / operation refusals | `test_unknown_role_is_refused_and_never_acquires_a_capsule` (500-518) · `test_unknown_operation_is_refused_instead_of_falling_back` (519-526) · `test_operation_the_role_cannot_run_is_refused_instead_of_substituted` (527-534) |
| launcher seat | `test_launcher_seat_composes_its_own_core_and_is_not_a_tenth_role` (535-543) · `test_launcher_is_refused_an_operation_no_role_inherits_to_it` (544-556) |
| missing / undeclared material | `test_missing_mandatory_material_is_refused_rather_than_omitted` (557-566) · `test_a_source_the_manifest_does_not_declare_is_refused` (567-573) · `test_a_source_read_from_the_wrong_composition_root_is_refused` (574-583) · `test_repository_specialization_must_be_admitted_on_the_binding` (584-591) |
| duplicates and overrides | `test_duplicate_identity_with_byte_identical_content_collapses_to_one_block` (608-629) · `test_duplicate_identity_with_a_different_body_stops_compilation` (630-650) · `test_an_explicit_override_records_its_provenance_and_selects_the_winner` (651-684) · `test_an_override_that_supersedes_an_unselected_identity_is_refused` (685-703) · `test_an_override_that_pulls_an_earlier_tier_over_a_role_is_refused` (704-724) · `test_an_override_may_replace_a_block_from_a_later_tier` (725-747) · `test_two_overrides_for_one_identity_are_refused_as_unorderable` (748-776) |
| **the two capability channels** | `test_a_tool_request_inside_the_policy_is_carried_but_not_granted` (777-788) · `test_a_tool_request_outside_the_admitted_policy_is_refused` (789-803) · **`test_the_worker_fixture_carries_the_skill_reference_it_declares` (1095-1131)** · **`test_a_skill_reference_without_its_admitted_root_file_is_refused` (1063-1094)** |
| tools and task context | `test_a_supplied_task_projection_is_carried_in_its_own_channel` (804-821) · `test_a_projection_whose_bytes_do_not_match_its_digest_is_refused` (822-836) · `test_no_projection_means_no_task_context_and_a_stable_digest` (837-850) |
| refusal explanation | `test_a_refusal_still_produces_an_explanation_manifest` (851-867) |
| no model / no network | `test_composition_succeeds_with_network_and_model_access_denied` (868-889) · `test_the_compiler_modules_import_no_network_client` (890-930) |
| **source-value integrity** | `test_a_source_whose_revision_is_not_its_own_digest_is_refused` (931-945) · `test_a_source_that_decodes_to_nothing_is_refused` (946-956) · **`test_a_source_that_is_not_utf8_text_is_refused` (957-972)** · `test_a_source_with_a_blank_identity_or_path_is_refused` (1132-1141) |
| **frozen-DTO field guards** | `test_a_selection_with_a_blank_anchor_is_refused` (973-984) · `test_a_digest_field_that_is_not_a_sha256_is_refused` (985-1000) · `test_a_blank_required_field_is_refused` (1001-1007) · `test_a_negative_instruction_unit_index_is_refused` (1008-1016) · `test_an_instruction_unit_labelling_a_missing_composition_root_is_refused` (1017-1027) · `test_a_skill_identity_needs_both_an_origin_and_a_name` (1028-1034) · `test_a_specialization_path_outside_its_directory_is_refused` (1035-1042) · `test_a_digest_value_that_is_not_a_sha256_is_refused_by_the_shared_guard` (1142-1149) |
| **outcome shape** | `test_a_compilation_outcome_that_is_both_a_capsule_and_a_refusal_is_refused` (1043-1053) · `test_a_compilation_outcome_that_is_neither_is_refused` (1054-1062) |

Observed result on the current candidate: **50 passed** here; **104 passed** with the admission
module (54 collected there).

### Conventions

A new property gets a case that **varies exactly one fact** in the in-memory fixture. Do not
extend the fixture to mirror the shipped corpus: a corpus-mirroring fixture can only be mutated by
editing what is under test. The shipped-corpus end-to-end check belongs in
`mcp/tests/test_role_capsule_admission.py`.

### Invariants And Boundaries

- Every determinism assertion must be **falsifiable**. An order-insensitive or input-insensitive
  digest would make the whole group vacuous; that is what `test_reordering_the_composed_blocks_changes_the_semantic_digest`
  and `test_a_real_binding_change_does_move_the_semantic_digest` exist for.
- `test_the_compiler_modules_import_no_network_client` is a structural guard, not a behavioral
  one: composition must run with every socket refused.
- **The tool cases and the skill cases assert different things and must not be merged.** A tool
  request outside the admitted policy is *refused*; a declared skill reference is *carried*, and
  the only way it fails is a skill root file that was not admitted. A single "capability" case
  covering both would hide exactly the distinction the implementation draws.
- **The source-value guards belong here, not in the admission module**: revision-equals-digest,
  decodes-to-nothing, and non-UTF-8 are properties of a `CapsuleSource` value, and
  `test_a_source_that_is_not_utf8_text_is_refused` is the only case that proves the
  `source-not-utf8` code is reachable.
- This module tests the compiler; it does not test tree admission, the manifest parser's structural
  refusals, or the frozen vocabulary — those are the admission module's cases.
- A refusal case asserts its **own** status, so two refusal sites cannot drift into one
  indistinguishable assertion.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The module under test and its pipeline. [1]
- The carried skill channel these cases pin. [2]
- The `source-not-utf8` and revision/blank-content refusals the source-value cases pin. [3]
- The refusal codes the refusal cases assert. [4]
- The identity-resolution outcomes the duplicate and override cases pin. [5]
- The tool-policy narrowing the tool cases pin. [6]
- The outcome shape whose exactly-one-of rule the two outcome cases pin. [7]
- The admission cases live in the sibling module, not here, where the capsule composes only the operations its own role declares and the independently compared routing side is retired. [8]
- The corpus test this leaf was required to preserve; it was not edited and still passes. [9]

The falsifiability probe that exercised these cases (seeds M01–M10, `all 10 seeded mutations were
caught`) is **not** a product artifact and is deliberately not promoted into `mcp/tests/`. It lives
in the coordination task tree at
`tasks/agents-remember/260915_role-capsules-and-native-eve/notes/reports/caps-l2-mutation-probe.py`,
outside this repository, so it is named here rather than linked. It expires on the next change to
`mcp/tests/test_role_capsule_*.py`, at which point these shipped cases are its executable
replacement and its seed table must be re-anchored or retired.

### Cross-Repo References

No sibling-repository contract is exercised by these cases.

No meaningful cross-repo references found.
