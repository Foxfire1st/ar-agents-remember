# mcp/tests/test_role_capsule_compiler.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_role_capsule_compiler.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T09:38+02:00 |
| lastVerifiedCommitHash | `f7619b3dced6198cc54956997f7718738918b846` |
| lastVerifiedCommitDate | 2026-09-18T06:38:27+02:00|
| governingOverview      | `overview.md`                              |

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

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test and its pipeline. | `compile_role_capsule`; `semantic_digest` | mcp/src/agents_remember/models/role_capsules/compiler.py:90-153; mcp/src/agents_remember/models/role_capsules/compiler.py:225-272 |
| The carried skill channel these cases pin. | `skill_references`; `CapsuleSkillReference` | mcp/src/agents_remember/models/role_capsules/compiler.py:154-193; mcp/src/agents_remember/models/role_capsules/types.py:414-434 |
| The `source-not-utf8` and revision/blank-content refusals the source-value cases pin. | `CapsuleSource` | mcp/src/agents_remember/models/role_capsules/sources.py:50-95 |
| The refusal codes the refusal cases assert. | `CAPSULE_STATUSES` | mcp/src/agents_remember/models/role_capsules/statuses.py:27-41 |
| The identity-resolution outcomes the duplicate and override cases pin. | `resolve_instructions`; `_require_one_identity` | mcp/src/agents_remember/models/role_capsules/resolution.py:135-191; mcp/src/agents_remember/models/role_capsules/resolution.py:221-261 |
| The tool-policy narrowing the tool cases pin. | `narrow_tool_requests` | mcp/src/agents_remember/models/role_capsules/tools.py:24-58 |
| The outcome shape whose exactly-one-of rule the two outcome cases pin. | `CapsuleCompilationOutcome` | mcp/src/agents_remember/application/role_capsules/compilation.py:46-88 |
| The admission cases live in the sibling module, not here. | `test_every_shipped_role_compiles_to_the_routing_its_own_role_file_declares` | mcp/tests/test_role_capsule_admission.py:469-518 |
| The corpus test this leaf was required to preserve; it was not edited and still passes. | `ROLE_ORDER`; `OPERATION_KEYS` | mcp/tests/test_role_instruction_corpus.py:32-42; mcp/tests/test_role_instruction_corpus.py:56-64 |

The falsifiability probe that exercised these cases (seeds M01–M10, `all 10 seeded mutations were
caught`) is **not** a product artifact and is deliberately not promoted into `mcp/tests/`. It lives
in the coordination task tree at
`tasks/agents-remember/260915_role-capsules-and-native-eve/notes/reports/caps-l2-mutation-probe.py`,
outside this repository, so it is named here rather than linked. It expires on the next change to
`mcp/tests/test_role_capsule_*.py`, at which point these shipped cases are its executable
replacement and its seed table must be re-anchored or retired.

## Cross-Repo References

No sibling-repository contract is exercised by these cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T09:38+02:00 — 260915-CAPS-L2 curator: corrected against the A3 candidate, which grew this module **872 → 1149 lines** and **33 → 49 test functions (50 collected)**. Added the two new property groups the repairs introduced — the carried **skill-reference** cases (`test_the_worker_fixture_carries_the_skill_reference_it_declares`, `test_a_skill_reference_without_its_admitted_root_file_is_refused`) and the **source-value integrity** cases (`test_a_source_that_is_not_utf8_text_is_refused` and its revision/blank-content siblings) — plus the frozen-DTO field guards and the two outcome-shape cases. Recorded the invariant that the tool cases and the skill cases assert different things and must not be merged, and that the source-value guards belong here rather than in the admission module. Refreshed every range. Verification metadata stays at the leaf base commit — the closeout stamps the real code commit.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the 33 compiler cases
  added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the one-fact
  in-memory fixture rationale, the nine property groups, the falsifiability requirement on the
  determinism assertions (and why two cases were added after a vacuous probe), and the
  structural no-network guard. Verification metadata is left at the leaf base commit because the
  source is uncommitted — the governed closeout stamps the real code commit.
