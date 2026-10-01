# mcp/src/agents_remember/memory/knowledge/schema_generations.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**A schema generation is data, and selecting one is a read of the dataset.** This module owns the
registry of supported `(schema name, user_version)` generations — **nine** of them, generation 9 being
the newest — the pinned generation-1 record with its fingerprint constant and its drift gate, and the
three dispatch functions that resolve a dataset's generation from the dataset itself.

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
  constant; generations 2's through 9's are derived. `GENERATIONS` is ordered oldest first, so the
  newest supported generation is its last entry rather than a second literal that could drift from
  the tuple — and `CURRENT_GENERATION = GENERATIONS[-1]` is that entry, which is why a *created* store
  declares version **9** while an existing generation-8 dataset keeps declaring 8.
- **Every generation from 2 to 9 composes by the same explicit append, and the append is the whole
  additive rule.** `_compose_generation_3` puts `schema_v3.APPENDED_TABLES` (four authored-judgment
  tables) after generation 2's sixteen, `_compose_generation_4` puts `schema_v4.APPENDED_TABLES` (the
  one detection-sequence table) after generation 3's twenty, and `_compose_generation_5` puts
  `schema_v5.APPENDED_TABLES` (the one citation-binding table) after generation 4's twenty-one — each
  merging the appended columns, primary keys and typed-JSON sets into the predecessor's maps and
  concatenating the index and feature tuples. The composed result satisfies
  `GENERATION_9.tables[: len(GENERATION_8.tables)] == GENERATION_8.tables` with generation 8's columns,
  keys and JSON registries for every inherited name, which is why no `ALTER TABLE` against an earlier
  generation's table exists anywhere in the package. **The idiom is now eight instances**, and seven of
  them are one-line calls to the one shared helper: `_compose_generation_2`, `_3`, `_4`, `_6`, `_7`,
  `_8` and `_9` each call `_append_generation(base=…, schema_name=…, user_version=…, appended=…)`,
  while `_compose_generation_5` still spells its own composition out field by field. The rule is
  stated once here rather than re-derived by each new leaf: explicit append, prefix equality asserted
  by the generation it descends from, `ALTER TABLE` nowhere.
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
  generation 3's twenty; generation 5's begins with generation 4's twenty-one; generation 6's begins with
  generation 5's twenty-two; generation 7's begins with generation 6's twenty-eight; generation 8's begins
  with generation 7's thirty-three; and generation 9's begins with generation 8's thirty-four, gaining the
  census's six tables — its three record kinds and the three relations they resolve through. A generation that reorders, renames, retypes, drops or weakens an earlier
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

### 260915-KS-L21 — Generation 9, And The Registry That Now Holds Nine

**The truth-coverage census registered as generation 9, by the composed append this module already had.**
`GENERATION_9_SCHEMA_NAME` is `ar-knowledge-sqlite/v9`; `_compose_generation_9()` is the same one-line call
to `_append_generation` generations 2, 3, 4, 6, 7 and 8 are, over `base=GENERATION_8`, `user_version=9` and
`appended=schema_v9`; and `GENERATION_9 = _compose_generation_9()`. The six tables the census's own module
appends are its three record kinds (`census_inventory_row`, `census_claim`, `census_disposition`) and the
three relations they resolve through (`census_claim_evidence`, `census_claim_realization`,
`census_disposition_link`), so generation 7's thirty-three tables become generation 8's thirty-four and
generation 9's **forty**, with `GENERATION_9.tables[: len(GENERATION_8.tables)] == GENERATION_8.tables` and
generation 8's columns, primary keys and typed-JSON sets for every inherited name. The census's payload
shapes are registered in the record envelope for the same reason the authored-effect group's are: what the
envelope cannot express is a *relation* between records, which is why this generation appends relations and
not a wide table.

**The registry's last entry moved, and nothing else about selection did.** `GENERATIONS` is now
`(GENERATION_1 … GENERATION_9)`, so `CURRENT_GENERATION = GENERATIONS[-1]` is generation 9 and
`generation_of_new_store()` declares `ar-knowledge-sqlite/v9` at `user_version = 9` — while a
generation-8 dataset that already exists keeps declaring 8 and is read through generation 8's own record,
exactly as every earlier generation is. There is still no second "new store" literal to drift from the
tuple, and this module still contains no migration or cutover operation.

**The module docstring's generation list moved with it.** Its `GENERATION_9` bullet is new and states the
six-table append and the created-generation fact; the `GENERATION_8` bullet was rewritten into the past
tense and now describes what generation 8 *was*, the way the bullets before it already read. The L17
section below records the registry as it stood when that leaf landed — six members and a created store at
`v6` — and that is that leaf's landing record; the registry this card states in its Logic section is the
nine-member one generation 9 closes.

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The frozen generation record and the eleven fields a generation must answer for itself; the key and typed-JSON registries are part of the pinned structure, not derivable from DDL. [1]
- Generation 1's pinned fingerprint constant, recorded with the revision and command it was read at — measured data with provenance, not an assertion. [2]
- Generation 2 composed as an explicit append over generation 1, its fingerprint derived from the composition. [3]
- **Generation 3 composed as an explicit append over generation 2, and generation 4 as the same append over generation 3 — the prefix equality that is the additive rule.** [4]
- **The registry, ordered oldest first, and the created generation defined as its last entry rather than as a second literal — nine generations since the census's append registered generation 9, so `CURRENT_GENERATION` is generation 9 while a generation-8 dataset keeps declaring 8.** [5]
- The schema name generation 4 declares, and the three names before it. [6]
- The only place a build's own generation decides anything, and it decides only what a created store declares. [7]
- The drift gate that fails rather than warns, and the generation-1 wrapper. [8]
- The one fingerprint definition, now a function of a record rather than of the running build. [9]
- Open-path dispatch by version alone, and the hard refusal of an unregistered version. [10]
- Artifact-path dispatch by pair, type-strict on the version before the lookup. [11]
- The registry-wide column frame the portable canonical-form gate needs for an unregistered document. [12]
- The frozen generation record and the eleven fields a generation must answer for itself; the key and typed-JSON registries are part of the pinned structure, not derivable from DDL. [13]
- Generation 1's pinned fingerprint constant, recorded with the revision and command it was read at — measured data with provenance, not an assertion. [14]
- Generation 2 composed as an explicit append over generation 1, its fingerprint derived from the composition. [15]
- **Generation 3 composed as an explicit append over generation 2, and generation 4 as the same append over generation 3 — the prefix equality that is the additive rule.** [16]
- **The registry, ordered oldest first, and the created generation defined as its last entry rather than as a second literal.** [17]
- The schema name generation 4 declares, and the three names before it. [18]
- The only place a build's own generation decides anything, and it decides only what a created store declares. [19]
- The drift gate that fails rather than warns, and the generation-1 wrapper. [20]
- The one fingerprint definition, now a function of a record rather than of the running build. [21]
- Open-path dispatch by version alone, and the hard refusal of an unregistered version. [22]
- Artifact-path dispatch by pair, type-strict on the version before the lookup. [23]
- The registry-wide column frame the portable canonical-form gate needs for an unregistered document. [24]
- **Generation 9 composed by the same generic append generations 2, 3, 4, 6, 7 and 8 use, over generation 8 and `schema_v9`'s six census tables.** [25]
- **The schema name generation 9 declares — `ar-knowledge-sqlite/v9`, the name a created store now carries.** [26]
- **The six tables generation 9 appends: the census's three record kinds and the three relations they resolve through, appended after generation 8's thirty-four.** [27]
- **The shared append itself, and the published predicate that states the additive rule: the appended-tables prefix plus every inherited name keeping its exact column tuple, primary key and typed-JSON set.** [28]
- Generation 1's declared tables, columns, keys, JSON columns, DDL, triggers and features — the declarations this module delegates to and never restates. [29]
- Generation 2's appended tables, which `GENERATION_2` is composed from. [30]
- The open path that calls this module's dispatch and the creation path that declares a generation. [31]
- The encoder that takes the selected generation instead of reading build globals. [32]
- The merge preflight that refuses inputs whose generations disagree before any session exists. [33]
- The shipped code the artifact dispatch returns, and the type-strict rendering it preserves. [34]
- The pin, its dispatch and the generation-2 digest behaviour, exercised in both directions. [35]
- The test support that builds a real generation-1 dataset from generation 1's own recorded DDL, for cases that must observe a generation-1 fact. [36]
- **The generation-5 append measured by the generation it descends from, and the registry sequence checked as a structural fact — contiguous `1..N` with `ar-knowledge-sqlite/vN` names in register order — rather than as a hand-written list.** [37]

### Cross-Repo References

No cross-repository behavior is implemented in this file. A generation is a property of a dataset,
and a dataset's identity deliberately excludes Git commits, ledger rows and checkout locations.

No meaningful cross-repo references found.
