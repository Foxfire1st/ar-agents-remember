# mcp/tests/test_role_capsule_admission.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_role_capsule_admission.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T09:38+02:00 |
| lastVerifiedCommitHash | `e9300687218205ec1c4b0b86f96d3ac7c2f344d3` |
| lastVerifiedCommitDate | 2026-09-16T09:41:55+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tests overview](overview.md)

## Purpose

Focused checks for the **shipped corpus end to end**, source admission, the composition-manifest
parser, and the frozen vocabulary — the boundaries a later leaf consumes. This is the only module
in the role-capsule suite that touches the **real** tree; the compiler module builds its own
fixture so a failure names one boundary instead of a whole corpus.

**43 test functions → 54 collected cases** (several are parametrized over the nine shipped roles
and the eight operations).

## Code Commentary

### Logic

Fixtures and helpers: `corpus_tree` (100-114), `request_for` (115-126), `worker_binding` (127-145),
`_shipped_parsed` (359-362), `_shipped_request` (363-386), `_shipped_binding` (387-416),
**`declared_inherits` (417-430)**, `_shipped_document` (816-819), `_refuse` (820-829),
`_manifest_with` (830-906).

The cases group into seven boundaries:

| Group | Cases | Demonstrates |
| --- | --- | --- |
| vocabulary | `test_the_frozen_vocabulary_is_exactly_the_nine_roles_and_eight_operations` (146-152) · `test_the_role_and_operation_literals_agree_with_their_runtime_tuples` (153-159) · `test_the_launcher_is_a_seat_kind_and_not_a_tenth_role` (160-165) · `test_every_documented_refusal_code_is_registered_exactly_once` (166-184) | the registry is exactly nine roles / eight operations; the ambient launcher is a routing condition, not a tenth role; the PEP 695 literals and their runtime tuples cannot drift; the refusal-code set is complete and duplicate-free |
| root-local admission | `test_admission_reads_every_requested_source_with_its_content_digest` (275-289) · `test_admission_is_reproducible_over_one_unchanged_tree` (290-300) · `test_admission_refuses_a_path_that_escapes_its_root` (301-310) · `test_admission_refuses_a_missing_source_instead_of_skipping_it` (311-319) · `test_admission_refuses_a_root_that_is_not_a_directory` (320-326) · `test_admission_refuses_the_same_path_requested_twice` (327-334) · `test_an_unreadable_source_returns_a_refusal_rather_than_raising` (335-358) · `test_a_source_root_that_is_not_a_path_is_refused` (1146-1156) | digest-carrying reads; reproducibility; traversal, missing source, bad root, double request and unreadable source all refused rather than skipped |
| manifest parsing | `test_the_shipped_manifest_parses_and_agrees_with_the_frozen_vocabulary` (185-196) · `test_every_role_and_operation_the_shipped_manifest_declares_has_a_source` (197-218) · `test_every_tool_the_shipped_manifest_requests_exists_in_the_public_roster` (219-228) · `test_a_manifest_that_disagrees_with_the_frozen_vocabulary_is_refused` (229-240) · `test_a_manifest_whose_applicability_contradicts_itself_is_refused` (241-254) · `test_a_manifest_that_routes_two_identities_at_one_file_is_refused` (255-274) · `test_the_manifest_parser_refuses_each_metadata_defect` (910-931) · `test_the_specializations_field_must_be_an_array_when_present` (1095-1109) | the real manifest parses and agrees with the frozen vocabulary; a declared tool id outside the published roster is an error, not an inert request; each structural defect has its own refusal |
| **routing agreement** | **`test_every_role_file_declares_the_core_blocks_and_operations_it_inherits` (433-470)** · **`test_every_shipped_role_compiles_to_the_routing_its_own_role_file_declares` (471-520)** · **`test_every_shipped_role_compiles_deterministically_under_every_declared_operation` (521-543)** · **`test_every_shipped_role_composes_exactly_its_manifest_declared_routing` (698-728)** | the compiled routing and each role's own canonical source agree — the cross-check that keeps the manifest honest against the prose it routes to |
| **the carried skill channel** | **`test_a_shipped_role_declaring_a_skill_actually_carries_the_reference` (586-605)** · **`test_every_shipped_role_that_declares_a_skill_carries_one_reference_per_declaration` (606-620)** · **`test_a_role_declaring_no_skills_returns_an_empty_reference_tuple` (621-659)** · **`test_the_skill_revision_follows_the_admitted_skill_bytes` (660-697)** · `test_a_skill_reference_whose_root_file_is_not_admitted_is_refused` (1037-1060) · `test_an_unknown_skill_name_is_refused_by_the_manifest_accessor` (1200-1212) | a declared skill is **carried** with its own revision, one reference per declaration; a role declaring none gets an empty tuple; the revision tracks the admitted bytes; a missing or unknown skill is refused, never silently dropped |
| launcher and shipped corpus | `test_a_worker_capsule_composes_only_its_own_role_block` (544-585) · `test_the_launcher_seat_compiles_from_the_shipped_manifest` (729-765) · `test_emptying_the_launcher_operations_refuses_instead_of_compiling` (766-818) · `test_a_role_whose_routing_needs_an_absent_launcher_block_is_refused` (932-941) · `test_a_launcher_whose_own_block_is_absent_is_refused_by_name` (1061-1076) | the launcher is a seat kind with its own permitted operations; emptying `launcher.operations` refuses by design; a missing launcher block is refused **by name** |
| admitted-set and lookup guards | `test_a_source_set_with_no_admitted_bytes_is_refused` (942-967) · `test_a_duplicate_path_admitted_to_the_compiler_is_refused` (968-990) · `test_an_admitted_set_without_the_composition_manifest_is_refused` (991-1036) · `test_an_admitted_set_that_drops_the_manifest_mid_compile_is_refused` (1157-1186) · `test_an_override_whose_replacement_file_is_absent_is_refused` (1110-1145) · `test_a_declared_instruction_with_a_blank_identity_is_refused` (1187-1199) · `test_the_role_lookup_answers_through_the_one_narrowing_gate` (1077-1094) · `test_composing_roots_answers_what_each_seat_kind_can_actually_contribute` (1213-1261) | the admitted set is proven against the locked plan in both directions; the role lookup has exactly one narrowing gate; `composing_roots` answers what each seat kind can actually contribute |

Traversal is refused for a parametrized set including `../outside.md`, `/etc/passwd`,
`core/../../outside.md`, and the empty string.

Observed result on the current candidate: **54 passed** here; **104 passed** with the compiler
module (50 collected there).

### Conventions

A fixture-building case uses `tmp_path`; only the shipped-corpus and routing groups read the real
tree. Parametrizing over all nine roles and all eight operations is what makes "every shipped role
compiles to its declared routing" a corpus claim rather than a single-role claim. This module, not
the compiler module, owns every case that reads real bytes.

### Invariants And Boundaries

- **The literal/tuple agreement case is load-bearing.** The frozen registry is declared twice by
  necessity — the PEP 695 literal for the type checker and the tuple for runtime selection — and
  this case is what keeps them in step. Note the asymmetry the implementer recorded: PEP 695
  `type` aliases do **not** answer `get_args`, so the ruff-preferred alias form silently produced
  an *empty* runtime registry. The duplication is deliberate and test-guarded.
- `test_every_tool_the_shipped_manifest_requests_exists_in_the_public_roster` holds every declared
  tool id against the published roster. A declared id outside it must fail here, because the
  manifest declaring a tool is a **request**, and an unpublished request is a defect rather than a
  silently inert entry.
- **The skill cases here prove the channel is *carried*, not narrowed.** There is no permission
  assertion over a skill reference anywhere in this module — the assertions are about counts per
  declaration, the empty tuple for a role declaring none, and the revision tracking admitted
  bytes. Do not add a policy assertion to a skill case; that would invent a behavior the
  implementation does not have.
- `test_every_documented_refusal_code_is_registered_exactly_once` is the completeness guard for
  `CAPSULE_STATUSES`. It covers the **compiler** tuple; the source-value codes raised outside it
  (`source-not-utf8` and the admission codes) are deliberately not members and are asserted in the
  compiler module.
- Only this module may read the real corpus; the compiler module deliberately does not.
- Adding a shipped role or operation requires no new case — the parametrization picks it up — but
  adding one **with no source**, or whose routing disagrees with its own role file, must make the
  routing-agreement cases fail.

### Todos

None recorded.

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The frozen vocabulary and its completeness guard the vocabulary group pins. | `CAPSULE_ROLES`; `CAPSULE_OPERATIONS`; `CAPSULE_STATUSES` | mcp/src/agents_remember/models/role_capsules/vocabulary.py:64-75; mcp/src/agents_remember/models/role_capsules/vocabulary.py:77-89; mcp/src/agents_remember/models/role_capsules/statuses.py:27-41 |
| The manifest parser the shipped-manifest group exercises against the real file. | `parse_composition_manifest`; `_require_one_path_serves_one_identity`; `_require_operation_applicability_agrees`; `_require_role_skills_are_declared` | mcp/src/agents_remember/models/role_capsules/manifest.py:168-216; mcp/src/agents_remember/models/role_capsules/manifest.py:513-553; mcp/src/agents_remember/models/role_capsules/manifest.py:554-601; mcp/src/agents_remember/models/role_capsules/manifest.py:479-508 |
| The admission boundary the admission group refuses through. | `admit_capsule_sources`; `_require_confined_relative` | mcp/src/agents_remember/application/role_capsules/sources.py:78-94; mcp/src/agents_remember/application/role_capsules/sources.py:169-196 |
| The both-directions plan validation, including the skill-root gate. | `admit_source_set`; `_require_declared_skills_present` | mcp/src/agents_remember/models/role_capsules/source_set.py:91-108; mcp/src/agents_remember/models/role_capsules/source_set.py:195-228 |
| **The carried skill channel** these cases pin, and the helper that names a skill identity. | `skill_references`; `skills_declared_identity`; `CapsuleSkillReference` | mcp/src/agents_remember/models/role_capsules/compiler.py:154-193; mcp/src/agents_remember/models/role_capsules/sources.py:126-138; mcp/src/agents_remember/models/role_capsules/types.py:414-434 |
| The application entry point that converts an admission refusal into an outcome value. | `compile_admitted_capsule`; `CapsuleCompilationOutcome` | mcp/src/agents_remember/application/role_capsules/compilation.py:89-122; mcp/src/agents_remember/application/role_capsules/compilation.py:46-88 |
| The real corpus this module is the only role-capsule test to read. | `"schema": "ar-role-capsule-composition/v1"` | skills/l-01-agent-lifecycles/composition-manifest.json:1-4 |
| The sibling module that owns the compiler's own property cases. | `test_identical_input_compiles_to_identical_ordered_content_and_digest` | mcp/tests/test_role_capsule_compiler.py:377-388 |

## Cross-Repo References

No sibling-repository contract is exercised by these cases.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T09:38+02:00 — 260915-CAPS-L2 curator: corrected against the A3 candidate, which grew this module **429 → 1258 lines** and **30 → 43 test functions (54 collected)**. The old four-group summary no longer described the file: added the three groups the repairs introduced — **routing agreement** (each role's own file must declare the blocks and operations it inherits, and the compiled routing must agree with it across all declared operations), the **carried skill channel** (one reference per declaration, empty tuple for a role declaring none, revision tracking admitted bytes, missing/unknown skill refused), and the **admitted-set and lookup guards** (no-admitted-bytes, duplicate path, manifest dropped mid-compile, blank identity, single narrowing gate, `composing_roots`). Recorded the invariant that no skill case carries a permission assertion, because the channel is carried rather than narrowed. Refreshed every range, including the helper inventory, which now names `declared_inherits` and the `_manifest_with` builder. Verification metadata stays at the leaf base commit — the closeout stamps the real code commit.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the 30 admission,
  manifest-parser and vocabulary cases added by the deterministic capsule compiler leaf
  (`CAPS-R02@v1`). Records the four boundary groups, the deliberate literal/tuple duplication and
  its silent-empty-registry hazard, the public-roster guard on declared tool ids, the
  `CAPSULE_STATUSES` completeness guard, and the rule that only this module reads the real corpus.
  Verification metadata is left at the leaf base commit because the source is uncommitted — the
  governed closeout stamps the real code commit.
