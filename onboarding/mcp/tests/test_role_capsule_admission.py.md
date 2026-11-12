# mcp/tests/test_role_capsule_admission.py

## Governing Overview

[overview](overview.md)

## Purpose

Focused checks for the **shipped corpus end to end**, source admission, the composition-manifest
parser, and the frozen vocabulary — the boundaries a later leaf consumes. This module reads the shipped tree; the audience, launch and manifest-edge suites also read real corpus bytes. The compiler property module retains a synthetic fixture.

## Code Commentary

### Logic

The cases by boundary:

| Group | Cases | Demonstrates |
| --- | --- | --- |
| vocabulary | `test_the_frozen_vocabulary_is_exactly_the_eight_roles_and_nine_operations` · `test_the_role_and_operation_literals_agree_with_their_runtime_tuples` · `test_the_launcher_is_a_seat_kind_and_not_a_role` · `test_every_documented_refusal_code_is_registered_exactly_once` | the registry is exactly **eight roles / nine operations**; the ambient launcher is a routing condition, not a ninth role; the PEP 695 literals and their runtime tuples cannot drift; the refusal-code set is complete and duplicate-free |
| root-local admission | `test_admission_reads_every_requested_source_with_its_content_digest` · `test_admission_is_reproducible_over_one_unchanged_tree` · `test_admission_refuses_a_path_that_escapes_its_root` · `test_admission_refuses_a_missing_source_instead_of_skipping_it` · `test_admission_refuses_a_root_that_is_not_a_directory` · `test_admission_refuses_the_same_path_requested_twice` · **`test_an_unreadable_source_returns_a_refusal_rather_than_raising`** — which also drives the **emptied-source (`source-empty`) seed** | digest-carrying reads; reproducibility; traversal, missing source, bad root, double request and unreadable source all refused rather than skipped; an **emptied admitted source refuses by name** rather than raising out of the value layer |
| manifest parsing | `test_the_shipped_manifest_parses_and_agrees_with_the_frozen_vocabulary` · `test_every_role_and_operation_the_shipped_manifest_declares_has_a_source` · `test_every_tool_the_shipped_manifest_requests_exists_in_the_public_roster` · `test_a_manifest_that_disagrees_with_the_frozen_vocabulary_is_refused` · `test_a_manifest_whose_applicability_contradicts_itself_is_refused` · `test_a_manifest_that_routes_two_identities_at_one_file_is_refused` · `test_the_manifest_parser_refuses_each_metadata_defect` | the real manifest parses and agrees with the frozen vocabulary; a declared tool id outside the published roster is an error, not an inert request; each structural defect has its own refusal |
| **routing agreement** | **`test_every_operation_a_role_declares_resolves_to_one_corpus_block`** · **`test_a_role_capsule_composes_only_operations_the_role_declares`** · **`test_every_shipped_role_compiles_deterministically_under_every_declared_operation`** · **`test_every_shipped_role_composes_exactly_its_declared_unit_set`** · **`test_no_core_unit_can_enter_any_shipped_role_capsule`** · `test_an_admitted_core_source_is_inert_for_a_role_capsule` | the manifest's operations plane and each role's declared routing name real, distinct corpus blocks; every role/operation capsule composes exactly `role:<role>` and `operation:<operation>`, never a neighbouring operation or a shared Core block; extra admitted core sources leave the delivered text and semantic digest unchanged while omitting the every-role digest source refuses as `missing-required-instruction` |
| delivered prose | `test_a_role_capsule_carries_no_frontmatter_from_any_composed_source` · `test_the_frontmatter_strip_only_removes_a_closed_leading_block` | a delivered block carries no skill-registry frontmatter and no typed composition metadata, keeps its remaining prose and its whole-source revision; an unterminated or absent frontmatter block is left alone |
| **the carried skill channel** | **`test_a_shipped_role_declaring_a_skill_actually_carries_the_reference`** · **`test_every_shipped_role_that_declares_a_skill_carries_one_reference_per_declaration`** · **`test_a_role_declaring_no_skills_returns_an_empty_reference_tuple`** · **`test_the_skill_revision_follows_the_admitted_skill_bytes`** · `test_a_skill_reference_whose_root_file_is_not_admitted_is_refused` | a declared skill is **carried** with its own revision, one reference per declaration; a role declaring none gets an empty tuple; the revision tracks the admitted bytes; a skill whose root file is not admitted is refused, never silently dropped |
| launcher and shipped corpus | `test_a_worker_capsule_composes_only_its_own_role_block` · `test_the_launcher_seat_compiles_from_the_shipped_manifest` · `test_emptying_the_launcher_operations_refuses_instead_of_compiling` · `test_a_role_whose_routing_needs_an_absent_launcher_block_is_refused` · `test_a_launcher_whose_own_block_is_absent_is_refused_by_name` | the launcher is a seat kind with its own permitted operations; emptying `launcher.operations` refuses by design; a missing launcher block is refused **by name** |
| admitted-set guards | `test_a_source_set_with_no_admitted_bytes_is_refused` · `test_a_duplicate_path_admitted_to_the_compiler_is_refused` · `test_an_admitted_set_without_the_composition_manifest_is_refused` | the admitted set is proven against the locked plan in both directions |

Traversal is refused for a parametrized set including `../outside.md`, `/etc/passwd`,
`core/../../outside.md`, and the empty string.

### Conventions

A fixture-building case uses `tmp_path`; only the shipped-corpus and routing groups read the real
tree. Parametrizing over all **eight** roles and all **nine** operations is what makes "every shipped role
compiles to its declared routing" a corpus claim rather than a single-role claim. The synthetic compiler property module remains distinct; this module is not the only reader of real bytes.

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
  (`source-not-utf8`, the **`source-empty`** code and the admission codes) are deliberately not
  members; `source-not-utf8` is asserted in the compiler module and `source-empty` in this module's
  emptied-source seed.
- The compiler property module deliberately uses a synthetic corpus; admission, audience, launch and manifest-edge modules have distinct real-corpus responsibilities.
- Adding a shipped role or operation requires no new case — the parametrization picks it up — but
  adding one **with no source**, or whose routing disagrees with its own role file, must make the
  routing-agreement cases fail.

### Todos

None recorded.

## Current audience, delivery and evidence contract

Six edge functions live in `test_role_capsule_manifest_edges.py`: role lookup, specialization shape, absent override winner, invalid source root, a manifest dropped mid-compile and the composing-root accessor. `_shipped_request` also admits role-addressed step details, and the frontmatter check removes audience metadata from expected delivered text while keeping the whole-source revision.

The every-role digest source remains required while additional admitted shared core stays out of rendered instructions. Omission of that digest refuses by name. Delivered-prose comparison removes only closed typed composition metadata and retains the complete remaining prose; the revision still addresses whole source bytes. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

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

- The sibling module that owns the compiler's own property cases. [8]

### Cross-Repo References

No sibling-repository contract is exercised by these cases.

No meaningful cross-repo references found.


- compile_admitted_capsule returns a CapsuleCompilationOutcome for admission or compilation refusals, with a manifest in both shapes and exactly one of result/error. Empty admitted instruction text raises the typed source-empty error; errors from reading the shared block or compiling are caught and returned as refusal outcomes. [6]

- Admission tests read the shipped lifecycle manifest and form role/operation requests and bindings. The separate manifest-edge module checks lookup, malformed selections and composing roots; the audience module compiles declared role/operation pairs and checks addressed operation content against pinned seals. [7]

- The shipped request includes role-addressed declared details in its admitted skill sources. The no-frontmatter check independently reconstructs delivered prose after removing a closed leading frontmatter block and typed composition-metadata lines, while retaining the complete source revision; deletion, relocation, leaked metadata and wrong-revision controls must fail. Six edge concerns are defined in the distinct manifest-edge module: lookup, specialization shape/blank identity, absent override winner, invalid root, missing selected manifest and composing roots. [9]

- The every-role digest source remains required while additional admitted shared core stays out of rendered instructions. Omission of that digest refuses by name. Delivered-prose comparison removes only closed typed composition metadata and retains the complete remaining prose; the revision still addresses whole source bytes. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [10]
