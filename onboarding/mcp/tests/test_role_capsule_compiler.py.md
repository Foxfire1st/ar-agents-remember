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

The frozen source has **47 test function definitions** (static inspection). Collected case totals and execution results were not measured by this pass.

## Code Commentary

### Logic

The fixture is a small **in-memory corpus built to the canonical manifest schema**, so a case
varies exactly one fact. That is deliberate: *a fixture that mirrors the whole shipped corpus could
only be mutated by editing the things under test, which is how a vacuous assertion gets written.*
Since this leaf's review repairs, the fixture also carries a declared **skill reference**, so the
carried channel is exercised in the same one-fact style as everything else.

Fixture helpers and test extents below are read from the frozen source. The fixture still varies one admitted fact per case and retains a declared skill-reference channel.

- `fixture_manifest_document`: lines 140-188.
- `manifest_bytes`: lines 191-194.
- `source_text`: lines 197-198.
- `skill_source`: lines 201-218.
- `make_source`: lines 221-236.
- `manifest_source`: lines 239-249.
- `all_sources`: lines 252-273.
- `selection_for`: lines 276-294.
- `worker_binding`: lines 297-318.
- `launcher_binding`: lines 321-331.
- `compile_worker`: lines 334-349.
- `failure`: lines 352-355.
- `replaced`: lines 358-373.

The two native-composition properties now assert role then operation and an inert admitted shared core. The separately selected legacy launcher case does not grant a role inherited operation. The combined unreadable-source case checks both blank text and non-UTF8 while distinguishing their errors.

Current source test inventory:

- `test_identical_input_compiles_to_identical_ordered_content_and_digest`: lines 381-390.
- `test_instruction_order_is_role_then_operation`: lines 393-411.
- `test_a_declared_but_unselected_specialization_changes_diagnostics_not_identity`: lines 414-433.
- `test_reordering_the_composed_blocks_changes_the_semantic_digest`: lines 436-458.
- `test_a_real_binding_change_does_move_the_semantic_digest`: lines 461-467.
- `test_changing_an_unrelated_role_leaves_the_worker_capsule_untouched`: lines 475-483.
- `test_changing_an_applicable_operation_block_changes_that_capsule`: lines 486-495.
- `test_a_shared_core_change_does_not_reach_a_role_capsule`: lines 498-518.
- `test_unknown_role_is_refused_and_never_acquires_a_capsule`: lines 526-542.
- `test_unknown_operation_is_refused_instead_of_falling_back`: lines 545-550.
- `test_operation_the_role_cannot_run_is_refused_instead_of_substituted`: lines 553-558.
- `test_the_launcher_seat_composes_its_own_core_and_inherits_no_role_operation`: lines 561-580.
- `test_missing_mandatory_material_is_refused_rather_than_omitted`: lines 588-611.
- `test_a_source_the_manifest_does_not_declare_is_refused`: lines 614-618.
- `test_a_source_read_from_the_wrong_composition_root_is_refused`: lines 621-628.
- `test_repository_specialization_must_be_admitted_on_the_binding`: lines 631-636.
- `test_an_admitted_specialization_is_composed_after_the_operation`: lines 639-647.
- `test_duplicate_identity_with_byte_identical_content_collapses_to_one_block`: lines 655-674.
- `test_duplicate_identity_with_a_different_body_stops_compilation`: lines 677-695.
- `test_an_explicit_override_records_its_provenance_and_selects_the_winner`: lines 698-729.
- `test_an_override_that_supersedes_an_unselected_identity_is_refused`: lines 732-748.
- `test_an_override_that_pulls_an_earlier_tier_over_a_role_is_refused`: lines 751-769.
- `test_an_override_may_replace_a_block_from_a_later_tier`: lines 772-792.
- `test_two_overrides_for_one_identity_are_refused_as_unorderable`: lines 795-816.
- `test_a_tool_request_inside_the_policy_is_carried_but_not_granted`: lines 824-833.
- `test_a_tool_request_outside_the_admitted_policy_is_refused`: lines 836-843.
- `test_a_supplied_task_projection_is_carried_in_its_own_channel`: lines 851-866.
- `test_a_projection_whose_bytes_do_not_match_its_digest_is_refused`: lines 869-881.
- `test_no_projection_means_no_task_context_and_a_stable_digest`: lines 884-890.
- `test_a_refusal_still_produces_an_explanation_manifest`: lines 898-912.
- `test_composition_succeeds_with_network_and_model_access_denied`: lines 915-934.
- `test_the_compiler_modules_import_no_network_client`: lines 937-966.
- `test_a_source_whose_revision_is_not_its_own_digest_is_refused`: lines 978-990.
- `test_a_source_with_no_readable_instruction_text_is_refused_by_name`: lines 993-1020.
- `test_a_selection_with_a_blank_anchor_is_refused`: lines 1023-1032.
- `test_a_digest_field_that_is_not_a_sha256_is_refused`: lines 1035-1048.
- `test_a_blank_required_field_is_refused`: lines 1051-1055.
- `test_a_negative_instruction_unit_index_is_refused`: lines 1058-1064.
- `test_an_instruction_unit_labelling_a_missing_composition_root_is_refused`: lines 1067-1075.
- `test_a_skill_identity_needs_both_an_origin_and_a_name`: lines 1078-1082.
- `test_a_specialization_path_outside_its_directory_is_refused`: lines 1085-1090.
- `test_a_compilation_outcome_that_is_both_a_capsule_and_a_refusal_is_refused`: lines 1093-1101.
- `test_a_compilation_outcome_that_is_neither_is_refused`: lines 1104-1110.
- `test_a_skill_reference_without_its_admitted_root_file_is_refused`: lines 1113-1142.
- `test_the_worker_fixture_carries_the_skill_reference_it_declares`: lines 1145-1154.
- `test_a_source_with_a_blank_identity_or_path_is_refused`: lines 1182-1189.
- `test_a_digest_value_that_is_not_a_sha256_is_refused_by_the_shared_guard`: lines 1192-1199.

### Historical recorded run totals

The earlier card recorded **50 passed** here and **104 passed** with the admission module (**54 collected** there). It supplied no exact code-tree identity for that sentence. Those original values remain earlier card evidence; this inspection made no fresh test run or collected-case claim at C.

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
  `test_a_source_with_no_readable_instruction_text_is_refused_by_name` proves both blank-text refusal
  and reachability of the distinct `source-not-utf8` code.
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
- The corpus test preserved by the earlier leaf; this pass retains that historical evidence and asserts no fresh execution result. [9]

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
