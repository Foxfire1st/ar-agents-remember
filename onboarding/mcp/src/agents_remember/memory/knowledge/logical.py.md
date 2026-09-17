# mcp/src/agents_remember/memory/knowledge/logical.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/logical.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c`|
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The canonical logical identity of one knowledge dataset.** Two databases are the same knowledge exactly when
their canonical logical bodies are equal, and this module owns that body. It serializes the schema generation the
dataset declares and every table of that generation's manifest — including empty ones — in manifest order, each
row ordered by its declared primary key and each field in declared column order, with typed JSON columns decoded
to JSON values.

It exists because the batch needs a *content* identity it can compare inside one transaction: the logical digest
is what a `ChangeBatch` names as its precondition and what `MutationResult` reports before and after, so "did
this batch change anything?" is a question about records rather than about SQLite page layout. Later requirements
(`KS-R04` publication, `KS-R05` merge) are expected to compare the same digest between a live candidate, a closed
published database and a captured memory tree.

## Code Commentary

### Logic

- **The encoder is parameterised over the selected generation, and that selection is the caller's.** `logical_body`,
  `logical_body_from_tables`, `logical_digest`, `logical_digest_of_tables`, `snapshot_identity`, `dataset_identity`,
  `_rows_of` and `_require_declared_keys` each take a generation — a `SchemaGeneration` record or its schema name —
  and read **that** generation's tables, columns, primary keys, typed-JSON sets, `user_version` and recorded
  fingerprint. `resolve_generation` is the one place the two spellings converge, and it refuses a name no registered
  generation declares rather than approximating one, so a digest is never assembled under a generation the registry
  does not contain.
- `logical_body` returns the exact structure the digest seals:
  `{body_version, schema, user_version, schema_fingerprint, tables}`, where `tables` maps **every** table of the
  selected generation's manifest to its rows — an empty table is present as an empty list, so a table that appears
  or disappears is a difference. `logical_digest` hashes that body through the kernel canonical encoder.
- **The body has one constructor, and the portable export uses it rather than re-assembling the structure.**
  `logical_body` scans the database and delegates the structure itself to `logical_body_from_tables`, which
  wraps an **already-encoded** table mapping in `body_version`/`schema`/`user_version`/`schema_fingerprint` — all
  four now read from the selected generation — and projects the mapping into that generation's declared table
  order; `logical_digest_of_tables` is the digest over it. The export decodes a table mapping out of an artifact
  rather than scanning a database, and the only acceptable way for it to obtain the *same* digest is to build
  the *same* body through the *same* function: a second assembly of those four fields would be a second digest
  definition, and a difference between the two would produce an export that cannot be re-imported. **There is
  one digest definition in this package, not two** — the `_require_declared_keys` honesty check runs in both
  paths because it lives in `logical_body_from_tables`, not only in the scanning entry point, and that constructor
  now also refuses a table mapping that omits a table its own generation declares: a body that covers part of its
  manifest would be a weaker check wearing this one's name, so it is rejected rather than digested.
- `_rows_of(connection, generation, table)` selects the table's declared columns, sorts by the declared primary key,
  and `_cell` decodes a typed JSON column (`decoded_json`) while every other column is compared as its exact stored
  text; the declared columns, the key tuple and the typed-JSON set now come from the generation record rather than
  from this module's module-level globals. A difference that lives only in the stored JSON *text* — key order,
  whitespace, escaping — is therefore not a difference in knowledge, and a decode failure is a
  `KnowledgeStorageError`, not a digest of garbage.
- **`cell_value` is the public spelling of that same decoder, and it exists so that a second reader does not
  become a second definition of what a stored cell means.** The selective read (`KS-R07`) decodes stored rows of
  its own, and the only acceptable way for it to obtain the *same* values this module hashes is to call the *same*
  function; a private re-implementation would let a read page and the logical digest disagree about a dataset's
  content. `cell_value` is a thin delegate to `_cell` — one decoder, two names, no second behaviour — added by
  260915-KS-L7 and used by `memory/knowledge/read_queries.py`.
- `PRIMARY_KEYS` records each table's DDL `PRIMARY KEY` list, and **these are not always the leading columns**:
  `invariant_revision` keys `(repository_id, revision_id)` while `invariant_id` sits between them. A row is
  ordered by its key, not by declaration order. Both `PRIMARY_KEYS` and `JSON_COLUMNS` now live in `schema.py`,
  where the rest of generation 1's pinned structure is declared, and this module **re-exports them under their
  shipped names** so an existing reader does not break. The declarations are byte-identical to the ones this
  module used to own; what changed is only where they are declared and that the encoder no longer reads them.
  They are generation 1's data: a reader of a table generation 2 appended finds no entry there at all, which is
  why the generation-aware spelling — `generation.primary_keys` / `generation.json_columns` — is what every
  encoder path now uses. They moved because a generation record has to be assembled *before* the registry can
  exist, and a record cannot be assembled from a module that must import the registry back to be imported itself.
- `_require_declared_keys(generation)` is the honesty check between that registry and the manifest, now run
  against the **selected** generation: every key column must exist in that generation's declared column list, and
  no key may repeat a column. It verifies the property the encoder actually depends on, because only the DDL can
  state the real key and the schema declaration owns that.
- `snapshot_identity(connection, repository, generation)` packages the digest as a `SnapshotIdentity`, reporting
  the selected generation's schema name as the identity's `schema_version`, and `require_bound_repository` is the
  second, defensive read of the namespace row that raises a `KnowledgeStorageError` when the database is unbound
  or bound elsewhere.
- **`dataset_identity(database_path)` is the file-level entry point this leaf added**, and it exists because the
  publication half compares a *file at a path* with a live candidate. It opens the database through
  `connection.open_read_only_database` — a pass that could repair the file it is checking would prove only that
  the repair worked, and a snapshot whose identity is confirmed by a writable connection is not confirmed by a
  reader — **selects the declared generation from the dataset itself** (`generation_of_database`), validates the
  bound namespace, and returns the identity those two facts scope. The generation is read once from the file and
  handed to `snapshot_identity`, so the digest is assembled under the same generation `inspect_schema` validated;
  every failure is a `KnowledgeStorageError` rather than a returned value, so a caller comparing identities can
  name the path it could not read instead of treating it as empty.
- **`bound_repository(connection)` is the read that makes "a dataset this code addresses" precise.** A dataset
  addressed through this package is bound to exactly one namespace, and the store's own initialization refuses a
  rebind; more than one row therefore means the file is *not* a dataset this code wrote, which is **refused rather
  than resolved by picking a row**. It returns `None` for no row at all, which is a different fact from an
  ambiguous one.
- **What the digest deliberately excludes** is as load-bearing as what it includes: SQLite page order, file
  paths, journal state, header counters, mtimes, Git commits, ledger rows, caches and rendered views. A candidate
  therefore has a content identity that survives being backed up, copied and reopened anywhere.

### Conventions

- Reading the body is a plain scan inside whatever transaction the caller already holds, so a mutation can
  compare the dataset before and after its own writes inside one transaction instead of trusting an earlier value.
- `JSON_COLUMNS` is a per-table set, so a new typed JSON column is added by naming it there rather than by
  guessing from the value's text. It is generation 1's set; a generation-aware reader reads the selected
  generation's `json_columns`, which is what `_rows_of` does.
- **Every generation-dependent fact is read from the record, never from a module global.** A caller selects a
  generation (`schema_generations.generation_of_database` for an open file, `…generation_of_artifact` for a
  portable artifact) and passes it — or its name — in; this module resolves the spelling but decides nothing about
  which generation a dataset is. Reading the module-level `PRIMARY_KEYS` / `JSON_COLUMNS` for a table a later
  generation appended would find no entry at all, and reading them for one of generation 1's names is correct only
  because later generations append tables without altering earlier ones.
- `_BODY_VERSION` (`ar-knowledge-logical-body/v1`) is a separate version from the SQL schema version: the
  encoding of the identity can change without the schema changing, and vice versa.
- The module imports `schema` (for the re-exported key and JSON registries), `schema_generations`,
  `connection.{fetch_one,inspect_schema,open_read_only_database}` and
  `models.knowledge` only; it writes nothing. The read-only opener is the one dependency the file-level entry
  point added, and it is a *connection* dependency rather than a new owner.
- **A file-level identity is read only, and its failures are defects.** `dataset_identity` raises
  `KnowledgeStorageError` instead of returning a value or a refusal, because "I could not read this file" is not
  an identity and a caller must not be able to confuse the two.

### Invariants And Boundaries

- **Same knowledge, same digest, wherever it lives.** File copies, `VACUUM` and JSON text reshaping leave the
  digest unchanged; a real JSON value change moves it.
- **The digest is total over its own generation's manifest.** The body is derived from the selected generation's
  declared table tuple, not from a hand-kept list, so a table added to a generation cannot silently leave the
  identity — and, because every manifest table must be present in the mapping, a body can never be digested over
  part of the manifest it names.
- **Digests are never taken over the intersection of two generations.** A generation-1 dataset digests over
  generation 1's ten tables — including the empty ones — and a generation-2 dataset over all sixteen, so an
  unchanged version-1 dataset keeps its version-1 digest after a later generation exists. **A table that appears
  or disappears *within* one generation is still a difference**, because an absent manifest table is an empty
  list rather than an omission and a mapping that omits one is refused; the two statements together are what make
  a cross-generation comparison a comparison of two stated generations rather than of an accidental overlap.
- **The digest is not a seal of authorship or approval.** It covers stored rows only; provenance is inside the
  rows it hashes, but a semantic judgement is not representable anywhere in this module.
- **Boundary.** This module owns the encoder and the row ordering. It does not decide when a comparison is a
  refusal (the batch's `_require_bound_context` does), and it does not own the SQL schema, the codecs or the
  connection contract.
- **Reuse rule for later leaves.** `logical_digest` is the one encoder: a later leaf that needs a dataset
  identity reuses it rather than defining a second one. The portable artifact adds a format marker and a header
  *on top of* this body and seals the same value, so `logicalDigest` in an artifact **is** the value
  `logical_digest`/`dataset_identity` returns for the dataset it carries — that equality is the contract, and
  it is what lets a consumer compare digests rather than bytes. It is an equality *under one generation*: the
  artifact's declared generation is the one its body was assembled under, and a reader that sealed generation 1's
  body under generation 2's manifest would produce a different value for the same dataset. **The body's structure
  is shared rather than duplicated**: `logical_body_from_tables` is the one constructor and the export path calls
  it, so the scan and the artifact cannot disagree about what the body is. The publication half consumes it in
  both directions — a live candidate through `store.snapshot_identity()`, a closed file through
  `dataset_identity` — which is why the two can be compared at all.
- **An ambiguous namespace is refused, not resolved.** `bound_repository` raises when the file holds more than one
  repository row rather than choosing one; a dataset this package addresses is bound to exactly one namespace, and
  more than one row means the file is not a dataset this code wrote.
- **A file-level identity is read-only.** `dataset_identity` opens the file in a mode that cannot write it, so a
  comparison pass can never repair the artifact it is measuring.

### Todos

None recorded for this slice. `_require_declared_keys` verifies key columns exist, and it deliberately does not
verify that the declared key *equals* the DDL's — that comparison is the schema declaration's owner, and the
reviewer verified the current table against the live DDL by hand (nine exact matches plus `repository`'s
column-level primary key). It now checks the selected generation's own key registry against the selected
generation's own column manifest, so a future generation that declared the two inconsistently is refused at digest
time rather than encoded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The declared primary key per canonical table, including the non-leading-column case. | `PRIMARY_KEYS` | mcp/src/agents_remember/memory/knowledge/logical.py:44-66 |
| The typed JSON columns decoded at the portable boundary. | `JSON_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema.py:154-162 |
| The body version and the digest over the canonical body. | `_BODY_VERSION`; `logical_digest`; `logical_body` | mcp/src/agents_remember/memory/knowledge/logical.py:50-50; mcp/src/agents_remember/memory/knowledge/logical.py:74-77; mcp/src/agents_remember/memory/knowledge/logical.py:88-99 |
| **The one body constructor, and the digest over an already-encoded table mapping — the entry point the portable export seals through, so the scan and the artifact cannot define the body twice.** | `logical_body_from_tables`; `logical_digest_of_tables` | mcp/src/agents_remember/memory/knowledge/logical.py:95-129; mcp/src/agents_remember/memory/knowledge/logical.py:132-135 |
| The row ordering, the cell decoding and the JSON-text-is-not-knowledge rule. | `_rows_of`; `_cell` | mcp/src/agents_remember/memory/knowledge/logical.py:221-237; mcp/src/agents_remember/memory/knowledge/logical.py:251-263 |
| **The public spelling of that one decoder, added by 260915-KS-L7 so the selective read and this digest cannot disagree about a stored cell.** | `cell_value` | mcp/src/agents_remember/memory/knowledge/logical.py:240-248 |
| The reader that calls it, instead of decoding a typed JSON column a second time. | `fetch_invariant_revisions`; `fetch_family_revisions` | mcp/src/agents_remember/memory/knowledge/read_queries.py:78-133 |
| The key-versus-manifest honesty check, now reached by both the scan and the artifact path. | `_require_declared_keys` | mcp/src/agents_remember/memory/knowledge/logical.py:250-268 |
| The identity packaging and the defensive namespace read. | `snapshot_identity`; `require_bound_repository` | mcp/src/agents_remember/memory/knowledge/logical.py:129-138; mcp/src/agents_remember/memory/knowledge/logical.py:186-204 |
| **The file-level identity entry point this leaf added, and the ambiguous-namespace read it depends on.** | `dataset_identity`; `bound_repository` | mcp/src/agents_remember/memory/knowledge/logical.py:141-161; mcp/src/agents_remember/memory/knowledge/logical.py:164-183 |
| The read-only connection the file-level entry point must use, so a comparison cannot repair what it measures. | `open_read_only_database`; `inspect_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:52-63; mcp/src/agents_remember/memory/knowledge/connection.py:106-122 |
| The table and column manifest this module derives its body from. | `CANONICAL_TABLES`; `CANONICAL_COLUMNS`; `schema_fingerprint` | mcp/src/agents_remember/memory/knowledge/schema.py:26-42; mcp/src/agents_remember/memory/knowledge/schema.py:47-112; mcp/src/agents_remember/memory/knowledge/schema.py:425-442 |
| The kernel canonical encoder the digest is computed through. | `sha256_digest` | mcp/src/agents_remember/kernel/canonical_json.py:34-38 |
| The JSON decoder a typed column is compared through, which refuses ambiguous stored text. | `decoded_json` | mcp/src/agents_remember/kernel/canonical_json.py:46-62 |
| The store method that exposes the live identity to a caller cheaply, and the sibling half of every comparison. | `snapshot_identity` | mcp/src/agents_remember/memory/knowledge/store.py:327-340 |
| The publication half that consumes this identity in both directions. | `publication_state`; `dataset_identity` | mcp/src/agents_remember/memory/knowledge/materialization.py:34-99; mcp/src/agents_remember/memory/knowledge/publication.py:215-249 |
| The batch precondition this identity is compared against inside the transaction. | `_require_bound_context` | mcp/src/agents_remember/memory/knowledge/candidate.py:148-183 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The digest deliberately excludes Git commits and
ledger rows, so nothing here reads a second repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): **replaced this card's central identity invariant, because the encoder is now parameterised over the selected generation.** The card asserted "**All ten tables participate.** The body is derived from `schema.CANONICAL_TABLES`" — that was the exact statement that stopped being true the moment a second generation existed, and it was worse than incomplete: a generation-1 dataset read under generation 2's live manifest would have digested over tables it does not have, silently changing the identity of data that never changed. The corrected invariant is the property that now holds: **the digest is total over its own generation's manifest** (a generation-1 dataset still digests over generation 1's ten tables including the empty ones, a generation-2 dataset over all sixteen), an absent manifest table is an empty list rather than an omission and a table mapping that omits one of its own generation's tables is **refused** rather than digested, a table that appears or disappears *within* one generation is still a difference, and **no digest is ever computed over the intersection of two generations**. Every entry point now takes a generation record or its schema name — `logical_body`, `logical_body_from_tables`, `logical_digest`, `logical_digest_of_tables`, `snapshot_identity`, `dataset_identity`, `_rows_of`, `_require_declared_keys` — with `resolve_generation` refusing a name no registered generation declares, and `snapshot_identity` reporting the selected generation's schema name as the identity's `schema_version`. The card also records the move a reader must not misread as a behaviour change: `PRIMARY_KEYS` and `JSON_COLUMNS` now live in `schema.py` (declarations byte-identical) and this module re-exports them under their shipped names, because a generation record must be assembled without importing the module that consumes it; `dataset_identity` now reads the generation from the file (`generation_of_database`) and hands that record to `snapshot_identity`, so the digest is assembled under the same generation `inspect_schema` validated. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): **recorded the one addition this leaf made — `cell_value`, the public spelling of the decoder every reader of a stored row uses.** It is a thin delegate to `_cell`, so there is still exactly one decoder, and it exists for the same reason the body has one constructor: the selective read decodes stored rows of its own, and a private re-implementation would let a read page and the logical digest disagree about what a dataset contains. The card states that consequence explicitly (one decoder, two names, no second behaviour) and names `memory/knowledge/read_queries.py` as its caller. The citation range for `_cell` was re-derived against the working tree, because the new public function sits between `_rows_of` and `_cell` and moved the private one down by eleven lines. Verification metadata is **not** advanced: the code commit does not exist and closeout owns the stamp.
- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): **recorded that the digest definition is now literally single.** The portable export needs to seal a table mapping it *decoded from an artifact* rather than scanned from a database, and the repair that made that honest was to give the body **one constructor** — `logical_body_from_tables`, with `logical_digest_of_tables` over it — which `logical_body` now delegates to instead of assembling `body_version`/`schema`/`user_version`/`schema_fingerprint` itself. This card records the consequence a later reader must not flatten: **there is one digest definition in this package, not two**, the export path seals the same value `logical_digest`/`dataset_identity` returns for a dataset (that equality *is* the artifact contract), and the `_require_declared_keys` honesty check runs in both paths because it lives in the shared constructor. Every citation range below was re-derived against the working tree, because the new functions moved every anchor after them. Verification metadata is **not** advanced: the code commit does not exist and closeout owns the stamp.
- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): **recorded the file-level half of the dataset identity.** The card's `KS-R04` forward reference is now the shipped contract: `dataset_identity` reads one database *file*'s identity through a read-only connection — so a comparison pass can never repair the artifact it measures — and `bound_repository` is the read that makes "a dataset this code addresses" precise by refusing more than one namespace row instead of picking one. The card now states that the publication half consumes this module in both directions (a live candidate through `store.snapshot_identity()`, a closed file through `dataset_identity`), which is why the two can be compared at all, and that every file-level failure is a `KnowledgeStorageError` rather than an identity a caller could mistake for a measurement. Citation ranges were re-derived against the working tree, four rows whose ranges no longer held their anchors were corrected, and this card's `governingOverview` link was repaired from `../../overview.md` — the application route — to the three-level path from `knowledge/`. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the new canonical logical dataset identity. It records what the body includes (all ten tables in manifest order, primary-key row order, typed JSON decoded) and what it deliberately excludes, the non-leading-column primary-key case that made the encoder's own honesty check necessary, the separate `body_version`, and the reuse rule that later publication and merge leaves compare this digest instead of defining a second encoder. Verification metadata remains empty until closeout stamps the code commit.
