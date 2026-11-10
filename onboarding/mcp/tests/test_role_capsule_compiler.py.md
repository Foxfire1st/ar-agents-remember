# mcp/tests/test_role_capsule_compiler.py

## Governing Overview

[overview](overview.md)

## Purpose

Focused behavioral checks for the deterministic role-capsule compiler. The compiler's contract is
a set of **observable properties**, and each case here pins one of them: identical admitted facts
and source bytes compile to identical ordered content and digest; ephemeral diagnostics do not move
that digest while a real change to an applicable block does; an unrelated role's source never
reaches a worker capsule; requested tools are narrowed while skill references are merely carried;
every documented refusal happens for its own reason and advertises its remedy; composition needs
neither model nor network; and an unknown role or operation is refused instead of falling back.

## Code Commentary

### Logic

The fixture is a small **in-memory corpus built to the canonical manifest schema**, so a case
varies exactly one fact. That is deliberate: *a fixture that mirrors the whole shipped corpus could
only be mutated by editing the things under test, which is how a vacuous assertion gets written.*
The fixture also carries a declared **skill reference**, so the
carried channel is exercised in the same one-fact style as everything else.

Fixture helpers and test extents below are line ranges in the current source. The fixture still varies one admitted fact per case and retains a declared skill-reference channel.

- `fixture_manifest_document`: lines 135-184.
- `manifest_bytes`: lines 187-190.
- `source_text`: lines 193-194.
- `skill_source`: lines 197-214.
- `make_source`: lines 217-232.
- `manifest_source`: lines 235-245.
- `all_sources`: lines 248-269.
- `selection_for`: lines 272-290.
- `worker_binding`: lines 293-314.
- `launcher_binding`: lines 317-327.
- `compile_worker`: lines 330-345.
- `failure`: lines 348-351.
- `replaced`: lines 354-369.

The two native-composition properties now assert role then operation and an inert admitted shared core. The separately selected legacy launcher case does not grant a role inherited operation. The combined unreadable-source case checks both blank text and non-UTF8 while distinguishing their errors. The unrelated-role case rewrites the unselected `role:curator` source, first proving the rewrite changed its bytes, and requires the worker capsule's digest and rendered text to stay identical.

Current source test inventory:

- `test_identical_input_compiles_to_identical_ordered_content_and_digest`: lines 377-386.
- `test_instruction_order_is_role_then_operation`: lines 389-407.
- `test_a_declared_but_unselected_specialization_changes_diagnostics_not_identity`: lines 410-429.
- `test_reordering_the_composed_blocks_changes_the_semantic_digest`: lines 432-454.
- `test_a_real_binding_change_does_move_the_semantic_digest`: lines 457-463.
- `test_changing_an_unrelated_role_leaves_the_worker_capsule_untouched`: lines 471-486.
- `test_changing_an_applicable_operation_block_changes_that_capsule`: lines 489-498.
- `test_a_shared_core_change_does_not_reach_a_role_capsule`: lines 501-521.
- `test_every_role_digest_is_sealed_without_composing_its_content`: lines 524-563.
- `test_unknown_role_is_refused_and_never_acquires_a_capsule`: lines 571-587.
- `test_unknown_operation_is_refused_instead_of_falling_back`: lines 590-595.
- `test_operation_the_role_cannot_run_is_refused_instead_of_substituted`: lines 598-603.
- `test_the_launcher_seat_composes_its_own_core_and_inherits_no_role_operation`: lines 606-625.
- `test_missing_mandatory_material_is_refused_rather_than_omitted`: lines 633-670.
- `test_a_source_the_manifest_does_not_declare_is_refused`: lines 673-677.
- `test_a_source_read_from_the_wrong_composition_root_is_refused`: lines 680-687.
- `test_repository_specialization_must_be_admitted_on_the_binding`: lines 690-695.
- `test_an_admitted_specialization_is_composed_after_the_operation`: lines 698-706.
- `test_duplicate_identity_with_byte_identical_content_collapses_to_one_block`: lines 714-733.
- `test_duplicate_identity_with_a_different_body_stops_compilation`: lines 736-754.
- `test_an_explicit_override_records_its_provenance_and_selects_the_winner`: lines 757-788.
- `test_an_override_that_supersedes_an_unselected_identity_is_refused`: lines 791-807.
- `test_an_override_that_pulls_an_earlier_tier_over_a_role_is_refused`: lines 810-828.
- `test_an_override_may_replace_a_block_from_a_later_tier`: lines 831-851.
- `test_two_overrides_for_one_identity_are_refused_as_unorderable`: lines 854-875.
- `test_a_tool_request_inside_the_policy_is_carried_but_not_granted`: lines 883-892.
- `test_a_tool_request_outside_the_admitted_policy_is_refused`: lines 895-902.
- `test_a_supplied_task_projection_is_carried_in_its_own_channel`: lines 910-925.
- `test_a_projection_whose_bytes_do_not_match_its_digest_is_refused`: lines 928-940.
- `test_no_projection_means_no_task_context_and_a_stable_digest`: lines 943-949.
- `test_a_refusal_still_produces_an_explanation_manifest`: lines 957-971.
- `test_composition_succeeds_with_network_and_model_access_denied`: lines 974-993.
- `test_the_compiler_modules_import_no_network_client`: lines 996-1025.
- `test_a_source_whose_revision_is_not_its_own_digest_is_refused`: lines 1037-1049.
- `test_a_source_with_no_readable_instruction_text_is_refused_by_name`: lines 1052-1079.
- `test_a_selection_with_a_blank_anchor_is_refused`: lines 1082-1091.
- `test_a_digest_field_that_is_not_a_sha256_is_refused`: lines 1094-1107.
- `test_a_blank_required_field_is_refused`: lines 1110-1114.
- `test_a_negative_instruction_unit_index_is_refused`: lines 1117-1123.
- `test_an_instruction_unit_labelling_a_missing_composition_root_is_refused`: lines 1126-1134.
- `test_a_skill_identity_needs_both_an_origin_and_a_name`: lines 1137-1141.
- `test_a_specialization_path_outside_its_directory_is_refused`: lines 1144-1149.
- `test_a_compilation_outcome_that_is_both_a_capsule_and_a_refusal_is_refused`: lines 1152-1160.
- `test_a_compilation_outcome_that_is_neither_is_refused`: lines 1163-1169.
- `test_a_skill_reference_without_its_admitted_root_file_is_refused`: lines 1172-1201.
- `test_the_worker_fixture_carries_the_skill_reference_it_declares`: lines 1204-1213.
- `test_a_source_with_a_blank_identity_or_path_is_refused`: lines 1241-1248.
- `test_a_digest_value_that_is_not_a_sha256_is_refused_by_the_shared_guard`: lines 1251-1258.

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

## Current audience, delivery and evidence contract

The minimal manifest fixture explicitly declares `audience: all` for every operation, keeping its unsectioned synthetic text whole under the expanded schema. Audience projection and malformed-marker launch behavior belong to the separate audience/manifest-edge suites.

A one-byte equal-length change to the declared every-role source changes semantic_digest while rendered role/operation instructions stay identical and no shared core instruction block composes. Omission of that required source refuses by identity and path. Static parsing of the final file finds 48 test function definitions; this is not collection or execution. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References


- The carried skill channel these cases pin. [2]
- The `source-not-utf8` and revision/blank-content refusals the source-value cases pin. [3]
- The refusal codes the refusal cases assert. [4]
- The identity-resolution outcomes the duplicate and override cases pin. [5]
- The tool-policy narrowing the tool cases pin. [6]

- The admission cases live in the sibling module, not here, where the capsule composes only the operations its own role declares and the independently compared routing side is retired. [8]

### Cross-Repo References

No sibling-repository contract is exercised by these cases.

No meaningful cross-repo references found.


- compile_role_capsule parses and selects the manifest scope, admits and resolves the source set, reads typed contract markers, projects operation audiences and strips those markers. It verifies the separate task projection, narrows tools, carries skills/details, seals the selected content plus every-role/detail revisions, and returns the capsule with an explanation manifest. [1]
- CapsuleCompilationOutcome requires exactly one of result and error while retaining a manifest in both shapes; the two compiler-suite controls construct both-present and both-absent outcomes and require ValueError. [7]

- The current instruction-corpus test declares the canonical role order and operation keys, checks every manifest role/operation source resolves, keeps launcher routing metadata separate, and rejects copied instruction prose in the manifest. These source-defined assertions establish no fresh run or earlier-leaf execution event. [9]

- fixture_manifest_document defines a complete synthetic registry whose operations use audience=all. The compiler suite declares determinism, instruction ordering, selected/unrelated-source digest and refusal cases; audience-section projection is exercised in the distinct audience module. The source does not itself prove that these are the only semantic changes since an earlier leaf. [10]

- A one-byte equal-length change to the declared every-role source changes semantic_digest while rendered role/operation instructions stay identical and no shared core instruction block composes. Omission of that required source refuses by identity and path. Static parsing of the final file finds 48 test function definitions; this is not collection or execution. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [11]
