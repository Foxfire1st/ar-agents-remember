# mcp/tests/test_role_capsule_admission.py

## Governing Overview

[tests overview](overview.md)

## Purpose

Focused checks for the **shipped corpus end to end**, source admission, the composition-manifest
parser, and the frozen vocabulary — the boundaries a later leaf consumes. This is the only module
in the role-capsule suite that touches the **real** tree; the compiler module builds its own
fixture so a failure names one boundary instead of a whole corpus.

**43 test functions → 54 collected cases** (several are parametrized over the **ten** shipped roles
and the **nine** operations).

## Code Commentary

### Logic

Fixtures and helpers: `corpus_tree` (104-117), `request_for` (118-129), `worker_binding` (130-147),
`_shipped_parsed` (395-398), `_shipped_request` (399-422), `_shipped_binding` (423-452),
**`declared_inherits` (453-466)**, `_shipped_document` (852-855), `_refuse` (856-865),
`_manifest_with` (866-942).

The cases group into seven boundaries:

| Group | Cases | Demonstrates |
| --- | --- | --- |
| vocabulary | `test_the_frozen_vocabulary_is_exactly_the_ten_roles_and_nine_operations` (149-155) · `test_the_role_and_operation_literals_agree_with_their_runtime_tuples` (156-162) · `test_the_launcher_is_a_seat_kind_and_not_a_role` (163-168) · `test_every_documented_refusal_code_is_registered_exactly_once` (169-187) | the registry is exactly **ten roles / nine operations**; the ambient launcher is a routing condition, not an eleventh role; the PEP 695 literals and their runtime tuples cannot drift; the refusal-code set is complete and duplicate-free |
| root-local admission | `test_admission_reads_every_requested_source_with_its_content_digest` (278-292) · `test_admission_is_reproducible_over_one_unchanged_tree` (293-303) · `test_admission_refuses_a_path_that_escapes_its_root` (304-313) · `test_admission_refuses_a_missing_source_instead_of_skipping_it` (314-322) · `test_admission_refuses_a_root_that_is_not_a_directory` (323-329) · `test_admission_refuses_the_same_path_requested_twice` (330-337) · **`test_an_unreadable_source_returns_a_refusal_rather_than_raising` (338-390)** — which now also drives the **emptied-source (`source-empty`) seed** at 358-390 · `test_a_source_root_that_is_not_a_path_is_refused` (1149-1159) | digest-carrying reads; reproducibility; traversal, missing source, bad root, double request and unreadable source all refused rather than skipped; an **emptied admitted source refuses by name** rather than raising out of the value layer (D25) |
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
tree. Parametrizing over all **ten** roles and all **nine** operations is what makes "every shipped role
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
  (`source-not-utf8`, the **`source-empty`** code added by D25's repair, and the admission codes)
  are deliberately not members and are asserted in the compiler module.
- Only this module may read the real corpus; the compiler module deliberately does not.
- Adding a shipped role or operation requires no new case — the parametrization picks it up — but
  adding one **with no source**, or whose routing disagrees with its own role file, must make the
  routing-agreement cases fail.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The frozen vocabulary and its completeness guard the vocabulary group pins. [1]
- The manifest parser the shipped-manifest group exercises against the real file. [2]
- The admission boundary the admission group refuses through. [3]
- The both-directions plan validation, including the skill-root gate. [4]
- **The carried skill channel** these cases pin, and the helper that names a skill identity. [5]
- The application entry point that converts an admission refusal into an outcome value — including an **emptied source**, whose refusal reaches the caller as a value rather than as an escaping exception (D25). [6]
- The real corpus this module is the only role-capsule test to read. [7]
- The sibling module that owns the compiler's own property cases. [8]

### Cross-Repo References

No sibling-repository contract is exercised by these cases.

No meaningful cross-repo references found.
