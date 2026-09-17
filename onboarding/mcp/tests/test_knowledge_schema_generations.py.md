# mcp/tests/test_knowledge_schema_generations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_schema_generations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T22:00+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](../overview.md)

## Purpose

The case module for the selectable schema generations: the pin, the gate's **failing** direction, type-strict
dispatch, and generation-relative identity. This is one of the leaf's own new test modules, and its docstring states
the rule it is written to: each case protects one consequential fact of requirement 2 rather than a code path, because
a gate observed only in the passing direction is a comment with a test-shaped decoration.

## Code Commentary

### Logic

The module is marked `pytestmark = pytest.mark.evidence_unit` and imports the registry under test directly
(`GENERATION_1`, `GENERATION_2`, `CURRENT_GENERATION`, `GENERATION_1_FINGERPRINT`, `KnowledgeSchemaPinError`,
`structure_fingerprint`, `generation_for_key`, `generation_for_name`, `generation_for_version`, `generation_of_database`,
`generation_of_new_store`, `create_schema_statements`, and both pin gates), plus `create_generation_1_store` from the
shared support module, the connection helpers and the logical encoder.

- `test_the_pinned_generation_1_fingerprint_recomputes_to_its_recorded_constant` asserts the recorded constant, the
  recomputed fingerprint and the passing gate all agree — the pin is checkable rather than trusted.
- `test_the_pin_gate_fails_when_one_recorded_generation_1_field_is_perturbed` is parametrized over three separate
  perturbations — one table's DDL string, one trigger's body, one table's column tuple. Each is applied to a copy made
  with `dataclasses.replace` rather than to the module's own record, so the case measures the gate instead of corrupting
  the registry the rest of the suite reads; it asserts the recomputed fingerprint differs **and** that
  `require_pinned_generation_unchanged` raises `KnowledgeSchemaPinError` matching `no longer fingerprints as pinned`.
- `test_generation_2_appends_to_generation_1_without_touching_its_first_ten_tables` makes Example 1's two comparisons
  directly: generation 2's table prefix equals generation 1's tables, every one of those names keeps generation 1's
  columns, generation 2 has strictly more tables, and its schema name, `user_version` and fingerprint are its own.
- `test_the_artifact_key_lookup_is_type_strict_on_the_declared_version` asserts integer `1` and `2` resolve while
  `1.0`, `"1"`, `None` and `3` return `None`, and it states the hazard in the case itself: a loose boolean really does
  equal `1` in Python.
- `test_an_unregistered_version_is_refused_rather_than_repaired_or_re_read` writes a file declaring
  `PRAGMA user_version = 99` and asserts both `generation_of_database` and `inspect_schema` raise
  `KnowledgeStorageError` matching `unsupported schema`, while `generation_for_version(99)` is `None`.
- `test_creation_declares_the_newest_supported_generation_and_selection_reads_the_dataset` covers the load-bearing
  split: `create_or_validate_schema` produces `CURRENT_GENERATION`'s name, version and fingerprint,
  `generation_of_new_store()` is `CURRENT_GENERATION`, and a dataset read back through `generation_of_database` is the
  same generation.
- `test_a_generation_2_table_row_enters_the_generation_2_digest` is the executable acceptance check for the digest
  behaviour: `route` starts empty in `logical_body`, a route row is inserted, and the digest must change. Its docstring
  records the failure it exists for — the shipped encoder built its table mapping from the build's live manifest, so a
  table that manifest did not name was invisible and adding and populating one left the digest byte-identical.
- `test_a_generation_1_dataset_keeps_its_own_body_under_generation_1` builds a real version-1 dataset through the
  support module and asserts its body carries generation 1's schema name, `user_version`, pinned fingerprint and ten
  tables in declared order. It then shows the two neighbouring facts: a generation-2 body over that same table set is
  refused because it does not carry generation 2's tables (`does not carry`), and once those tables are added empty the
  same rows digest differently — the same rows are a different dataset under generation 2, never a continuation of the
  generation-1 identity.
- `test_a_generation_1_dataset_is_still_validated_by_the_registry_it_declares` opens a version-1 file read-only and
  asserts generation-2 code resolves it to generation 1, with `inspect_schema` reporting generation 1's name, version
  and pinned fingerprint.
- `test_every_supported_generation_declares_its_own_key_and_json_registries` asserts the key registries cover each
  generation's tables, that `record_revision`'s key and typed-JSON columns are what generation 2 declares, that every
  generation-1 name keeps generation 1's typed-JSON set, that `generation_for_name` resolves its own name and refuses
  an unknown one, that `json_functions` belongs to generation 2 alone, and that the create statements contain
  `json_valid` and no `ALTER TABLE`.

### Conventions

- Assertions address the registry's own declarations (`GENERATION_1`/`GENERATION_2` fields) rather than duplicating
  expected tables, columns or fingerprints as literals.
- Perturbations are applied to copies; the module never rebinds the shared records.
- Refusals are measured by exception type and message fragment on the open path, and by return value on the artifact
  path — the two shapes the production module distinguishes.

### Invariants And Boundaries

- **Generation 1's pinned fingerprint and every version-1 dataset's identity must not move.** The perturbed-input case
  and the generation-1 body case are the two directions of that claim, and the module records that the recovery for
  drift is to correct the change, never to re-pin the constant.
- **Additive-only.** Generation 2's manifest begins with generation 1's tables and keeps generation 1's columns for
  each of them; a reordering, renaming, retyping, dropping or weakening of an earlier generation's declaration is a
  divergence to escalate, not a union of generations — which is also why no `ALTER TABLE` may appear in a generation's
  create statements.
- **This module is a case module, not a fixture home.** The version-1 dataset it needs comes from
  `generation_test_support.create_generation_1_store`; the module owns no shared setup of its own.

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
| The module's stated contract: one consequential fact per case, and a gate must be observed in its failing direction. | "a gate observed only in the passing direction" | mcp/tests/test_knowledge_schema_generations.py:1-16 |
| The pin is checkable: constant, recomputed fingerprint and the passing gate agree. | `test_the_pinned_generation_1_fingerprint_recomputes_to_its_recorded_constant` | mcp/tests/test_knowledge_schema_generations.py:67-72 |
| The gate's failing direction, parametrized over three perturbed fields applied to copies of the record. | `test_the_pin_gate_fails_when_one_recorded_generation_1_field_is_perturbed` | mcp/tests/test_knowledge_schema_generations.py:63-106 |
| Generation 2 appends to generation 1 without touching its first ten tables. | `test_generation_2_appends_to_generation_1_without_touching_its_first_ten_tables` | mcp/tests/test_knowledge_schema_generations.py:121-131 |
| Type-strict artifact dispatch: `1.0` and `true` do not resolve to generation 1. | `test_the_artifact_key_lookup_is_type_strict_on_the_declared_version` | mcp/tests/test_knowledge_schema_generations.py:122-134 |
| An unregistered version is refused rather than migrated, repaired or re-read. | `test_an_unregistered_version_is_refused_rather_than_repaired_or_re_read` | mcp/tests/test_knowledge_schema_generations.py:137-155 |
| Creation declares the newest supported generation while selection reads the dataset. | `test_creation_declares_the_newest_supported_generation_and_selection_reads_the_dataset` | mcp/tests/test_knowledge_schema_generations.py:158-172 |
| A generation-2 table row must enter the generation-2 digest, which the live-manifest encoder failed to do. | `test_a_generation_2_table_row_enters_the_generation_2_digest` | mcp/tests/test_knowledge_schema_generations.py:175-204 |
| An unchanged version-1 dataset reproduces its own body and identity, and the same rows under generation 2 are a different dataset. | `test_a_generation_1_dataset_keeps_its_own_body_under_generation_1` | mcp/tests/test_knowledge_schema_generations.py:207-240 |
| A version-1 file opened by generation-2 code validates and reports generation 1. | `test_a_generation_1_dataset_is_still_validated_by_the_registry_it_declares` | mcp/tests/test_knowledge_schema_generations.py:243-258 |
| Every generation's key and typed-JSON registries, and the no-`ALTER TABLE` rule over the create statements. | `test_every_supported_generation_declares_its_own_key_and_json_registries` | mcp/tests/test_knowledge_schema_generations.py:400-422 |
| The symbols the cases drive, including the pinned constant and the gate. | `GENERATION_1_FINGERPRINT`; `require_pinned_generation_unchanged`; `generation_of_database`; `generation_of_new_store` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:145; mcp/src/agents_remember/memory/knowledge/schema_generations.py:208-218; mcp/src/agents_remember/memory/knowledge/schema_generations.py:233-250; mcp/src/agents_remember/memory/knowledge/schema_generations.py:227-230 |
| The encoder whose table mapping and digest the generation cases measure. | `logical_body`; `logical_digest`; `logical_body_from_tables` | mcp/src/agents_remember/memory/knowledge/logical.py:80; mcp/src/agents_remember/memory/knowledge/logical.py:74; mcp/src/agents_remember/memory/knowledge/logical.py:95 |
| The creation and inspection paths the cases call. | `create_or_validate_schema`; `inspect_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:88; mcp/src/agents_remember/memory/knowledge/connection.py:111 |
| The shared support that builds a genuine version-1 dataset for the generation-1 cases. | `create_generation_1_store` | mcp/tests/generation_test_support.py:34-54 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T20:39:57+00:00: Generated citation repair: `test_the_pinned_generation_1_fingerprint_recomputes_to_its_recorded_constant` repointed to mcp/tests/test_knowledge_schema_generations.py:67-72. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:39:57+00:00: Generated citation repair: `test_generation_2_appends_to_generation_1_without_touching_its_first_ten_tables` repointed to mcp/tests/test_knowledge_schema_generations.py:121-131. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:39:57+00:00: Generated citation repair: `test_every_supported_generation_declares_its_own_key_and_json_registries` repointed to mcp/tests/test_knowledge_schema_generations.py:400-422. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T22:00+02:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`; the module is untracked in the leaf's code worktree): created this one-to-one card for the leaf's new generation-registry case module. It records the ten cases, the perturbed-copy technique that makes the pin gate observable in its failing direction, the creation-versus-selection split, the digest regression the generation-2 case guards, and the generation-1 body/identity claim.
