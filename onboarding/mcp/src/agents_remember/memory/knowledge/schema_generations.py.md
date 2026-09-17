# mcp/src/agents_remember/memory/knowledge/schema_generations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/schema_generations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T19:11+00:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**A schema generation is data, and selecting one is a read of the dataset.** This module owns the
registry of supported `(schema name, user_version)` generations, the pinned generation-1 record with
its fingerprint constant and its drift gate, and the three dispatch functions that resolve a
dataset's generation from the dataset itself.

It exists because the shipped shape could not hold two generations honestly. `SCHEMA_USER_VERSION`,
`CANONICAL_TABLES` and `schema_fingerprint()` described the *running build*, every reader compared a
dataset against that, and the logical encoder built its table mapping from the live manifest. Adding
any table to the build therefore changed the digest of a version-1 dataset that had not changed.
Generation 1 is now pinned as a record so an unchanged version-1 dataset keeps its version-1
identity exactly, while a generation-2 dataset digests under generation 2.

This module is the leaf `260915-KS-L10` addition that supersedes the "the schema is one build-time
singleton" account: `schema.py` still owns generation 1's declarations verbatim, and this module
owns which generations exist and how one is chosen.

## Code Commentary

### Logic

- `SchemaGeneration` is a frozen record of everything a generation must be able to answer about
  itself: `schema_name`, `user_version`, the ordered `tables` manifest, per-table `columns`,
  `primary_keys` and `json_columns`, the required-SQLite-feature tuple `features`, `table_ddl`,
  `index_ddl`, `triggers`, and `fingerprint`. The key and typed-JSON registries are part of the
  pinned structure rather than derivations: the encoder orders each table's rows by its key tuple and
  decodes its typed-JSON columns, and **neither is recoverable from the DDL** — generation 1's DDL
  never spells `json_valid`, and a key tuple is declared data the encoder checks against the column
  list rather than reads out of DDL text.
- `GENERATION_1` delegates every field to `schema.py`'s shipped declarations and takes its
  `fingerprint` from the recorded constant `GENERATION_1_FINGERPRINT`
  (`bae805d6443a42ca65f733149cb3dc694ea89d3e40554c56480f17cb51edab0b`, read at revision `420669c4`,
  the pre-refactor branch head). Nothing in this module restates generation 1's tables, DDL or
  triggers.
- `GENERATION_2` is **composed** from generation 1 as an explicit append —
  `GENERATION_1.tables + schema_v2.APPENDED_TABLES` with the per-table maps merged — and its
  `fingerprint` is *computed* from the composed record rather than recorded. Generation 1's is a
  constant; generation 2's is derived. `GENERATIONS` is ordered oldest first, so the newest supported
  generation is its last entry rather than a second literal that could drift from the tuple.
- `structure_manifest` and `structure_fingerprint` are functions **of a record**, not of the build.
  That is what lets generation 1's recorded data be recomputed against its constant instead of
  against the code that produced it, and it is the one fingerprint definition in the package.
- Dispatch has three shapes and the distinction is load-bearing. `generation_of_database(connection)`
  reads `PRAGMA user_version` and resolves by **version alone** — an open SQLite file does not carry
  the application schema name, and the name `connection.inspect_schema` reports is the build's.
  `generation_of_artifact(envelope, operation)` resolves by the **pair** `(schema, userVersion)` and is
  **type-strict before it is a lookup**: `generation_for_key` returns `None` for a non-`int` version,
  because in Python `1 == 1.0 == True` and all three hash alike, so a dict-keyed lookup would resolve
  `1.0` and `true` to generation 1 — which the shipped reader deliberately refuses.
  `generation_of_new_store()` is **not a selection**: an empty database has no version to read, so
  creation declares `CURRENT_GENERATION` (the newest supported one, `GENERATIONS[-1]`). This is the
  only place a build's own generation decides anything, and it decides only what brand-new data
  declares.
- `declared_columns_for` and `declared_json_columns_for` answer a registry-wide question for exactly
  one caller: the portable reader's canonical-form gate renders an artifact *before* deciding whether
  its declared generation is supported, so a document whose header names an unregistered generation
  must still be spelled the way the build would write it. Requirement 1.3's additive rule makes a
  single answer well defined; more than one answer raises rather than picking.
- `generation_for_name` is a name-to-record resolution for a caller that has already selected, not
  dispatch, and it refuses an unknown name rather than approximating one.

### Conventions

- The module contains **no SQL text at all**. It carries the registry and the dispatch; every DDL
  string it fingerprints comes from `schema.py` (generation 1) or `schema_v2.py` (generation 2).
- Expected failures have two different shapes and they are not interchangeable. A **missing
  generation** is a returned `KnowledgeRefusal` on the artifact path (`unsupported_schema`, built by
  `export_refusals.unsupported_schema_refusal`), because a caller supplied a document; an **unknown
  version** on the open path is a raised `KnowledgeStorageError`, because the dataset is a file the
  caller asked the code to open. A **drifted pin** is a raised `KnowledgeSchemaPinError`, because it
  is a defect rather than an expected outcome.
- Refusal renderings are deliberately split: the type-strict refusal keeps the *single* generation's
  own version string as `expected` (a generation-1 artifact still renders `"1"`), while the
  unregistered-pair refusal renders the joined registry listing. The two state different facts, and
  `declared_version_string` exists so the first can stay as shipped.
- `index_name` derives an index's name by splitting its `CREATE INDEX` statement. It validates
  nothing: a malformed statement yields a wrong name silently, which is acceptable only because the
  caller passes the module's own DDL constants.

### Invariants And Boundaries

- **The pin fails, it does not warn, and it is never re-pinned.** `require_pinned_generation_unchanged`
  recomputes a generation's fingerprint from its recorded data and raises `KnowledgeSchemaPinError`
  when it differs; `require_pinned_generation_1_unchanged` is the generation-1 wrapper. The recovery
  for drift is to correct the change — generation 1's recorded data was edited, or the encoder
  changed what it covers — never to write the new value into the constant.
- **Additive-only, structurally.** Generation 2's manifest begins with generation 1's ten tables in
  generation 1's order and generation 2's columns for each of the first ten names are generation 1's.
  A generation that reorders, renames, retypes, drops or weakens an earlier generation's declaration
  is a schema divergence and is escalated, not expressed here — which is why the governing-route
  association lives in generation-2 tables rather than as a column appended to a generation-1 table.
- **An unknown generation is refused, never migrated.** Not repaired, not re-created, and never
  re-read under a different generation to obtain a green result. No migration or cutover operation
  exists in this leaf, and the in-flight version-1 candidate disposition is that it stays version 1.
- **Versions are distinct per supported generation.** The open path has only one key to read, so the
  registry's version lookup is total over what a file can declare.
- **Boundary.** This module does not own a generation's declarations (they belong to `schema.py` and
  `schema_v2.py`), does not open or create a database (`connection.py` calls it), does not encode a
  body (`logical.py` takes the selected record), and does not decide a merge's input validation
  (`merge_schema.selected_generation` calls it and turns a disagreement into a refusal).

### Todos

- Requirement 4.2's confinement rule names "no escaping symlink at resolution" alongside the path
  forms. `routes.normalize_route_path` refuses the machine-location and traversal forms by name but
  performs no symlink resolution, so that clause of the confinement claim has no implementation in
  this package. Recorded here rather than silently dropped; whether resolution belongs at authoring
  time or at comparison time is an open design question for a later leaf.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The frozen generation record and the eleven fields a generation must answer for itself; the key and typed-JSON registries are part of the pinned structure, not derivable from DDL. | `SchemaGeneration` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:54-79 |
| Generation 1's pinned fingerprint constant, recorded with the revision and command it was read at — measured data with provenance, not an assertion. | `GENERATION_1_FINGERPRINT` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:145 |
| Generation 2 composed as an explicit append over generation 1, its fingerprint derived from the composition; the registry ordered oldest first. | `GENERATION_2` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:189; mcp/src/agents_remember/memory/knowledge/schema_generations.py:193 |
| The only place a build's own generation decides anything, and it decides only what a created store declares. | `generation_of_new_store` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:227-230 |
| The drift gate that fails rather than warns, and the generation-1 wrapper. | `require_pinned_generation_unchanged` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:208-218 |
| The one fingerprint definition, now a function of a record rather than of the running build. | `structure_manifest` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:82-92 |
| Open-path dispatch by version alone, and the hard refusal of an unregistered version. | `generation_of_database` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:234-251 |
| Artifact-path dispatch by pair, type-strict on the version before the lookup. | `generation_of_artifact` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:369-402 |
| The registry-wide column frame the portable canonical-form gate needs for an unregistered document. | `declared_columns_for` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:259-287 |
| Generation 1's declared tables, columns, keys, JSON columns, DDL, triggers and features — the declarations this module delegates to and never restates. | `CANONICAL_TABLES` | mcp/src/agents_remember/memory/knowledge/schema.py:29-42 |
| Generation 2's appended tables, which `GENERATION_2` is composed from. | `APPENDED_TABLES`; `APPENDED_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:42-49; mcp/src/agents_remember/memory/knowledge/schema_v2.py:51-76 |
| The open path that calls this module's dispatch and the creation path that declares a generation. | `inspect_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:91-121 |
| The encoder that takes the selected generation instead of reading build globals. | `logical_body_from_tables` | mcp/src/agents_remember/memory/knowledge/logical.py:95-129 |
| The merge preflight that refuses inputs whose generations disagree before any session exists. | `selected_generation` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:110-155 |
| The shipped code the artifact dispatch returns, and the type-strict rendering it preserves. | `unsupported_schema_refusal` | mcp/src/agents_remember/memory/knowledge/export_refusals.py:78-102 |
| The pin, its dispatch and the generation-2 digest behaviour, exercised in both directions. | `test_the_pinned_generation_1_fingerprint_recomputes_to_its_recorded_constant`; `test_a_version_1_merge_on_the_generation_2_build_selects_generation_1` | mcp/tests/test_knowledge_schema_generations.py:1-283; mcp/tests/test_knowledge_merge_generations_and_envelope.py:1-311 |
| The test support that builds a real generation-1 dataset from generation 1's own recorded DDL, for cases that must observe a generation-1 fact. | `create_generation_1_store` | mcp/tests/generation_test_support.py:1-77 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A generation is a property of a dataset,
and a dataset's identity deliberately excludes Git commits, ledger rows and checkout locations.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T20:39:57+00:00: Generated citation repair: `generation_of_artifact` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:369-402. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:39:57+00:00: Generated citation repair: `APPENDED_TABLES`; `APPENDED_COLUMNS` repointed to mcp/src/agents_remember/memory/knowledge/schema_v2.py:42-49; mcp/src/agents_remember/memory/knowledge/schema_v2.py:51-76. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): created this one-to-one card for the generation registry. It records the three things a reader must not get wrong — a generation is a frozen record rather than the running build, dispatch reads the dataset (version alone for an open file, the type-strict pair for an artifact) while only *creation* declares a generation, and the pin fails rather than warns and is never re-pinned to whatever the code now computes. It records the two different expected-failure shapes (returned refusal on the artifact path, raised error on the open path and for drift), the additive-only rule that decides where the governing-route association may live, and generation 1's fingerprint constant with the revision it was measured at. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
