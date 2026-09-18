# mcp/src/agents_remember/memory/knowledge/schema_generations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/schema_generations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**A schema generation is data, and selecting one is a read of the dataset.** This module owns the
registry of supported `(schema name, user_version)` generations — five of them since `KS-R18@v1` — the
pinned generation-1 record with its fingerprint constant and its drift gate, and the three dispatch
functions that resolve a dataset's generation from the dataset itself.

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
  constant; generations 2's through 5's are derived. `GENERATIONS` is ordered oldest first, so the
  newest supported generation is its last entry rather than a second literal that could drift from
  the tuple — and `CURRENT_GENERATION = GENERATIONS[-1]` is that entry, which is why a *created* store
  declares version **5** while an existing generation-4 dataset keeps declaring 4.
- **Four generations compose by the same explicit append, and the append is the whole additive
  rule.** `_compose_generation_3` puts `schema_v3.APPENDED_TABLES` (four authored-judgment tables)
  after generation 2's sixteen, `_compose_generation_4` puts `schema_v4.APPENDED_TABLES` (the one
  detection-sequence table) after generation 3's twenty, and `_compose_generation_5` puts
  `schema_v5.APPENDED_TABLES` (the one citation-binding table) after generation 4's twenty-one — each
  merging the appended columns, primary keys and typed-JSON sets into the predecessor's maps and
  concatenating the index and feature tuples. The composed result satisfies
  `GENERATION_5.tables[: len(GENERATION_4.tables)] == GENERATION_4.tables` with generation 4's columns,
  keys and JSON registries for every inherited name, which is why no `ALTER TABLE` against an earlier
  generation's table exists anywhere in the package. **The idiom is now five instances of one shape**,
  and it is stated once here rather than re-derived by each new leaf: explicit append, prefix equality
  asserted by the generation it descends from, `ALTER TABLE` nowhere.
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

**The supporting-record group landed as generation 7, composed onto generation 6.** `_compose_generation_7` is written as the same explicit append generations 2 to 6 are — `base=GENERATION_6`, `schema_name=GENERATION_7_SCHEMA_NAME`, and the appended table set merged into generation 6's maps — so `GENERATION_7.tables[: len(GENERATION_6.tables)] == GENERATION_6.tables` and generation 7's columns for every inherited name *are* generation 6's. That prefix equality is the whole of the additive rule: a generation appends tables and never retypes, reorders or drops an earlier generation's, and this module contains no `ALTER TABLE`. `GENERATIONS` is `(1, 2, 3, 4, 5, 6, 7)`, so `CURRENT_GENERATION` is the last entry rather than a second literal: a *new* store declares version 7 while a generation-6 dataset that already exists keeps declaring version 6 and is read through generation 6's own record. **The number is the landing's:** this leaf was built in parallel with `KS-R17@v1` and `KS-R18@v1`, all three read the registry as `(1, 2, 3, 4)` and each registered generation 5 on its own branch, and the landing appended them in landing order — the citation binding as generation 5, the six composition tables as generation 6, this leaf's five tables as generation 7. The module this leaf authored as `schema_v5.py` therefore landed as `schema_v7.py`, and the renumber changed the module's name and its two composition operands and nothing else. Both record groups' payload shapes are registered in the record envelope; generation 7's own tables are the relations an evidence claim resolves and the observation's recorded columns.

### Conventions

- The module contains **no SQL text at all**. It carries the registry and the dispatch; every DDL
  string it fingerprints comes from `schema.py` (generation 1), `schema_v2.py` (generation 2),
  `schema_v3.py` (generation 3), `schema_v4.py` (generation 4) or `schema_v5.py` (generation 5).
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
- **Additive-only, structurally, and asserted per generation.** Generation 2's manifest begins with
  generation 1's ten tables in generation 1's order and generation 2's columns for each of the first ten
  names are generation 1's; generation 3's begins with generation 2's sixteen; generation 4's begins with
  generation 3's twenty; generation 5's begins with generation 4's twenty-one. A generation that reorders, renames, retypes, drops or weakens an earlier
  generation's declaration is a schema divergence and is escalated, not expressed here — which is why the
  governing-route association lives in generation-2 tables rather than as a column appended to a
  generation-1 table, and why the detection record group's payload shapes live in the envelope registry
  rather than as columns generation 4 would have had to add to `knowledge_record`.
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

### 260915-KS-L17 — One Composition Function, And The Registry That Now Holds Six Generations

**The five near-duplicate composition functions collapsed into one.** Generations 2, 3, 4, 5 and 6 are now
each a one-line call to a single generic `_append_generation(base=…, schema_name=…, user_version=…,
appended=…)`, which returns `base`'s declarations with one module's appended: `tables` by
concatenation, `columns` / `primary_keys` / `json_columns` / `table_ddl` / `triggers` by merge,
`index_ddl` and `features` by concatenation, and the fingerprint recomputed by composition rather than
recorded. A leaf that must renumber its generation — because another leaf landed the same number first
on the accumulated line — therefore changes **a name and a base argument**, not a re-derivation.

**`descends_from` is the additive rule as one published predicate.** It checks the appended-tables
prefix **and** that every one of the base's own names keeps its exact column tuple, primary key and
typed-JSON set. Its third argument is the base's own `tables` tuple, so a caller states *which* base it
checked by passing that base's declaration rather than a literal that could drift from it. The
composition leaf's generation case uses it as
`descends_from(GENERATION_6, GENERATION_5, GENERATION_5.tables)`.

**The registry is ordered oldest first, and that order is the only "newest" switch.** `GENERATIONS`
now holds **six** members (`GENERATION_1` … `GENERATION_6`), `CURRENT_GENERATION = GENERATIONS[-1]`,
and `generation_of_new_store()` returns it — so a **created** store declares
`ar-knowledge-sqlite/v6` at `user_version = 6` with **28** tables (generation 5's twenty-two plus
this leaf's six), while an existing generation-5 dataset still reports generation 5. Generation 5's
own append (`citation_binding`, one table) is a sibling leaf's and is untouched here. There is no
second "new store" literal to drift from the tuple.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The frozen generation record and the eleven fields a generation must answer for itself; the key and typed-JSON registries are part of the pinned structure, not derivable from DDL. | `SchemaGeneration` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:115-140 |
| Generation 1's pinned fingerprint constant, recorded with the revision and command it was read at — measured data with provenance, not an assertion. | `GENERATION_1_FINGERPRINT` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:206-206 |
| Generation 2 composed as an explicit append over generation 1, its fingerprint derived from the composition. | `GENERATION_2` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:299-299 |
| **Generation 3 composed as an explicit append over generation 2, and generation 4 as the same append over generation 3 — the prefix equality that is the additive rule.** | `GENERATION_3`; `_compose_generation_4`; `GENERATION_4` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:306-306; mcp/src/agents_remember/memory/knowledge/schema_generations.py:309-317; mcp/src/agents_remember/memory/knowledge/schema_generations.py:320-320; mcp/src/agents_remember/memory/knowledge/schema_generations.py:327-327 |
| **The registry, ordered oldest first, and the created generation defined as its last entry rather than as a second literal — eight generations since `KS-R13@v1` renumbered its append to generation 8, so `CURRENT_GENERATION` is generation 8 while a generation-7 dataset keeps declaring 7.** | `GENERATIONS`; `CURRENT_GENERATION` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:425-434; mcp/src/agents_remember/memory/knowledge/schema_generations.py:447-447 |
| The schema name generation 4 declares, and the three names before it. | `GENERATION_4_SCHEMA_NAME` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:211-211 |
| The only place a build's own generation decides anything, and it decides only what a created store declares. | `generation_of_new_store` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:469-472 |
| The drift gate that fails rather than warns, and the generation-1 wrapper. | `require_pinned_generation_unchanged` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:450-460 |
| The one fingerprint definition, now a function of a record rather than of the running build. | `structure_manifest` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:143-153 |
| Open-path dispatch by version alone, and the hard refusal of an unregistered version. | `generation_of_database` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:475-492 |
| Artifact-path dispatch by pair, type-strict on the version before the lookup. | `generation_of_artifact` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:610-643 |
| The registry-wide column frame the portable canonical-form gate needs for an unregistered document. | `declared_columns_for` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:501-527 |
| The frozen generation record and the eleven fields a generation must answer for itself; the key and typed-JSON registries are part of the pinned structure, not derivable from DDL. | `SchemaGeneration` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:115-140 |
| Generation 1's pinned fingerprint constant, recorded with the revision and command it was read at — measured data with provenance, not an assertion. | `GENERATION_1_FINGERPRINT` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:206-206 |
| Generation 2 composed as an explicit append over generation 1, its fingerprint derived from the composition. | `GENERATION_2` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:299-299 |
| **Generation 3 composed as an explicit append over generation 2, and generation 4 as the same append over generation 3 — the prefix equality that is the additive rule.** | `GENERATION_3`; `_compose_generation_4`; `GENERATION_4` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:205-230; mcp/src/agents_remember/memory/knowledge/schema_generations.py:232-256; mcp/src/agents_remember/memory/knowledge/schema_generations.py:258-320; mcp/src/agents_remember/memory/knowledge/schema_generations.py:16-20 |
| **The registry, ordered oldest first, and the created generation defined as its last entry rather than as a second literal.** | `GENERATIONS`; `CURRENT_GENERATION` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:425-434; mcp/src/agents_remember/memory/knowledge/schema_generations.py:447-447 |
| The schema name generation 4 declares, and the three names before it. | `GENERATION_4_SCHEMA_NAME` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:211-211 |
| The only place a build's own generation decides anything, and it decides only what a created store declares. | `generation_of_new_store` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:469-472 |
| The drift gate that fails rather than warns, and the generation-1 wrapper. | `require_pinned_generation_unchanged` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:198-322 |
| The one fingerprint definition, now a function of a record rather than of the running build. | `structure_manifest` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:143-153 |
| Open-path dispatch by version alone, and the hard refusal of an unregistered version. | `generation_of_database` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:475-492 |
| Artifact-path dispatch by pair, type-strict on the version before the lookup. | `generation_of_artifact` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:610-643 |
| The registry-wide column frame the portable canonical-form gate needs for an unregistered document. | `declared_columns_for` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:501-527 |
| Generation 1's declared tables, columns, keys, JSON columns, DDL, triggers and features — the declarations this module delegates to and never restates. | `CANONICAL_TABLES` | mcp/src/agents_remember/memory/knowledge/schema.py:29-42 |
| Generation 2's appended tables, which `GENERATION_2` is composed from. | `APPENDED_TABLES`; `APPENDED_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:42-49; mcp/src/agents_remember/memory/knowledge/schema_v2.py:51-76 |
| The open path that calls this module's dispatch and the creation path that declares a generation. | `inspect_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:91-121 |
| The encoder that takes the selected generation instead of reading build globals. | `logical_body_from_tables` | mcp/src/agents_remember/memory/knowledge/logical.py:95-129 |
| The merge preflight that refuses inputs whose generations disagree before any session exists. | `selected_generation` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:110-155 |
| The shipped code the artifact dispatch returns, and the type-strict rendering it preserves. | `unsupported_schema_refusal` | mcp/src/agents_remember/memory/knowledge/export_refusals.py:78-102 |
| The pin, its dispatch and the generation-2 digest behaviour, exercised in both directions. | `test_the_pinned_generation_1_fingerprint_recomputes_to_its_recorded_constant`; `test_a_version_1_merge_on_the_generation_2_build_selects_generation_1` | mcp/tests/test_knowledge_schema_generations.py:1-283; mcp/tests/test_knowledge_merge_generations_and_envelope.py:1-311 |
| The test support that builds a real generation-1 dataset from generation 1's own recorded DDL, for cases that must observe a generation-1 fact. | `create_generation_1_store` | mcp/tests/generation_test_support.py:1-77 |
| **The generation-5 append measured by the generation it descends from, and the registry sequence checked as a structural fact — contiguous `1..N` with `ar-knowledge-sqlite/vN` names in register order — rather than as a hand-written list.** | `test_generation_5_appends_to_generation_4_without_touching_its_twenty_one_tables`; `test_the_registered_generation_appends_only_and_the_preceding_ones_are_unchanged` | mcp/tests/test_knowledge_citation_bindings.py:118-135; mcp/tests/test_knowledge_facets.py:1009-1103 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A generation is a property of a dataset,
and a dataset's identity deliberately excludes Git commits, ledger rows and checkout locations.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T08:36:42+00:00: Generated citation repair: `SchemaGeneration` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:115-140. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `GENERATION_1_FINGERPRINT` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:206-206. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `GENERATION_2` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:299-299. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `GENERATION_4_SCHEMA_NAME` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:211-211. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `generation_of_new_store` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:469-472. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `require_pinned_generation_unchanged` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:450-460. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `structure_manifest` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:143-153. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `generation_of_database` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:475-492. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `generation_of_artifact` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:610-643. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `declared_columns_for` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:501-527. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `SchemaGeneration` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:115-140. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `GENERATION_1_FINGERPRINT` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:206-206. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `GENERATION_2` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:299-299. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `GENERATION_4_SCHEMA_NAME` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:211-211. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `generation_of_new_store` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:469-472. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `structure_manifest` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:143-153. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `generation_of_database` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:475-492. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `generation_of_artifact` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:610-643. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `declared_columns_for` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:501-527. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:25:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **corrected this document for the landing's generation renumber.** `KS-R12@v1` was built in parallel with `KS-R17@v1` and `KS-R18@v1`; all three read the registry as `(1, 2, 3, 4)` and each registered *generation 5* on its own branch. The landing appended them in landing order, so this leaf's five supporting-record tables became **generation 7** and the module authored as `schema_v5.py` landed as **`schema_v7.py`**. The body above now names generation 7, generation 6 as its base, `GENERATIONS` as `(1, 2, 3, 4, 5, 6, 7)` and `CURRENT_GENERATION` as the created generation, and it states that reading `generation 5` as this record group's number is a pre-sync branch state — generation 5 is the citation binding's. The declarations themselves are unchanged by the renumber; only the module's name and its two composition operands moved.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `GENERATION_2` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:292-292. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `GENERATION_3`; `_compose_generation_4`; `GENERATION_4` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:306-306; mcp/src/agents_remember/memory/knowledge/schema_generations.py:309-317; mcp/src/agents_remember/memory/knowledge/schema_generations.py:320-320. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `GENERATION_2` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:292-292. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 9 generated projection bullet(s) by hand while resolving the memory sync** — `GENERATION_1_FINGERPRINT`, `GENERATION_2`, `GENERATION_4_SCHEMA_NAME`, `generation_of_new_store`, `require_pinned_generation_unchanged`, `structure_manifest`, `generation_of_database`, `generation_of_artifact` and 1 further anchor(s). Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T05:00:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): **re-read the registry and the composition this leaf changed, and corrected three claims to the measured values.** The registry now holds **five** generations, `CURRENT_GENERATION = GENERATIONS[-1]`, and `generation_of_new_store()` returns `ar-knowledge-sqlite/v5` at `user_version = 5` — so a created store declares generation 5 with **27** tables while a generation-4 dataset still reports generation 4. The four near-duplicate composition functions are now one-line calls to a single generic `_append_generation`, and `descends_from` is the additive rule as one published predicate whose third argument is the base's own tables tuple. The two `_compose_generation_4` rows were re-cited by hand to the declaration's real extent and the `GENERATIONS` row to the tuple's, because what had moved them was a projection rather than a read. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read every citation this card carries against the current source and repaired the ranges this leaf's addition moved.** This entry recorded generation 5 as generation 4 plus the five appended tables, the prefix equality that is the whole of the additive rule, and `CURRENT_GENERATION = GENERATIONS[-1]` as the reason a new store declares 5 while a generation-4 dataset keeps declaring 4. Verification metadata is unchanged and the code commit does not exist yet; closeout owns that stamp.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): **re-read this card against the current source and moved every number the leaf moved.** `KS-R18@v1` appends generation 5, so the body's registry count is now **five** and the append paragraph names all four composed successors — `_compose_generation_3`, `_compose_generation_4` and `_compose_generation_5` are five instances of one shape (explicit append, prefix equality asserted by the generation it descends from, `ALTER TABLE` nowhere), which the card now states once instead of re-deriving per generation. `CURRENT_GENERATION = GENERATIONS[-1]` is recorded as *why* a created store now declares version **5** while an existing generation-4 dataset keeps declaring 4, and the additive-only invariant gains generation 5's prefix over generation 4's twenty-one names. Ten citation ranges were **re-cited by hand** against the working tree — `GENERATION_1_FINGERPRINT` `:155-161` → `:161-161`, `GENERATION_2` `:201-208` → `:185-208`, the composition row re-split across `:214-230` / `:232-256` / `:258-267` with generation 5's own `:274-291` / `:293-293`, `GENERATION_4_SCHEMA_NAME` split so generation 5's name is named rather than absorbed, `generation_of_new_store` `:297-307` → `:340-343`, `require_pinned_generation_unchanged` `:285-321` → `:321-331`, `generation_of_database` `:310-346` → `:346-363`, `generation_of_artifact` `:445-481` → `:481-514`, `declared_columns_for` `:336-372` → `:372-398` — and one range the mechanical pass had left naming one line twice (`GENERATIONS`; `CURRENT_GENERATION` at `:318-318`) was corrected to name the registry's own lines and the assignment's. One new row records the leaf's generation-5 append case and the L11 registry case this leaf re-scoped additively. Verification metadata advances to the leaf's base commit `e963a01c` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T03:15:00+00:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): **re-read every citation this card carries against the current source, corrected the ones the leaf moved, and replaced six generated projection bullets with this entry.** The body now states the registry as **four** generations and the append idiom once for all three successors: generations 2, 3 and 4 are each composed by the same explicit append, each predecessor's columns, primary keys and typed-JSON registries surviving for every inherited name — which is the additive rule the leaf's generation 4 must satisfy, and the reason the detection payload shapes live in the envelope registry instead of as columns generation 4 would have had to add to an earlier generation's table. `CURRENT_GENERATION = GENERATIONS[-1]` is recorded as *why* a created store declares version 4 while an existing generation-3 dataset keeps declaring 3. Six rows were **re-cited by hand** rather than machine-projected — `GENERATION_1_FINGERPRINT` (:149 → :155), `GENERATION_2` (:194 → :201), `generation_of_new_store` (:227 → :304), `require_pinned_generation_unchanged` (:245 → :285), `generation_of_database` (:270 → :310), `generation_of_artifact` (:405 → :445) and `declared_columns_for` (:296 → :336) — and the five projection bullets that had produced those ranges, plus the one for `APPENDED_TABLES` on the schema_v2 row, are removed: a mechanically projected range is unverified evidence, and an agent has now read each declaration it points at. Two new rows record generations 3 and 4 with the registry and the created-generation definition. Verification metadata advances to the leaf's base commit `4264dcc9` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-17T19:11:00+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): created this one-to-one card for the generation registry. It records the three things a reader must not get wrong — a generation is a frozen record rather than the running build, dispatch reads the dataset (version alone for an open file, the type-strict pair for an artifact) while only *creation* declares a generation, and the pin fails rather than warns and is never re-pinned to whatever the code now computes. It records the two different expected-failure shapes (returned refusal on the artifact path, raised error on the open path and for drift), the additive-only rule that decides where the governing-route association may live, and generation 1's fingerprint constant with the revision it was measured at. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
