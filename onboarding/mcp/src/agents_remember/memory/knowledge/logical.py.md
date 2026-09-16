# mcp/src/agents_remember/memory/knowledge/logical.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/logical.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `3332a4ce7029777d49feca22b499350435a9f83c`|
| lastVerifiedCommitDate | 2026-09-16T11:50:16+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The canonical logical identity of one knowledge dataset.** Two databases are the same knowledge exactly when
their canonical logical bodies are equal, and this module owns that body. It serializes the supported schema
version and every canonical table — including empty ones — in manifest order, each row ordered by its declared
primary key and each field in declared column order, with typed JSON columns decoded to JSON values.

It exists because the batch needs a *content* identity it can compare inside one transaction: the logical digest
is what a `ChangeBatch` names as its precondition and what `MutationResult` reports before and after, so "did
this batch change anything?" is a question about records rather than about SQLite page layout. Later requirements
(`KS-R04` publication, `KS-R05` merge) are expected to compare the same digest between a live candidate, a closed
published database and a captured memory tree.

## Code Commentary

### Logic

- `logical_body` returns the exact structure the digest seals:
  `{body_version, schema, user_version, schema_fingerprint, tables}`, where `tables` maps **every** canonical
  table in `schema.CANONICAL_TABLES` order to its rows — an empty table is present as an empty list, so a table
  that appears or disappears is a difference. `logical_digest` hashes that body through the kernel canonical
  encoder.
- `_rows_of` selects the table's declared columns, sorts by the declared primary key, and `_cell` decodes a
  typed JSON column (`decoded_json`) while every other column is compared as its exact stored text. A difference
  that lives only in the stored JSON *text* — key order, whitespace, escaping — is therefore not a difference in
  knowledge, and a decode failure is a `KnowledgeStorageError`, not a digest of garbage.
- `PRIMARY_KEYS` records each table's DDL `PRIMARY KEY` list, and **these are not always the leading columns**:
  `invariant_revision` keys `(repository_id, revision_id)` while `invariant_id` sits between them. A row is
  ordered by its key, not by declaration order.
- `_require_declared_keys` is the honesty check between that table and the manifest: every key column must exist
  in the table's declared column list, and no key may repeat a column. It verifies the property the encoder
  actually depends on, because only the DDL can state the real key and the schema module owns that.
- `snapshot_identity(connection, repository, schema_name)` packages the digest as a `SnapshotIdentity`, and
  `require_bound_repository` is the second, defensive read of the namespace row that raises a
  `KnowledgeStorageError` when the database is unbound or bound elsewhere.
- **`dataset_identity(database_path)` is the file-level entry point this leaf added**, and it exists because the
  publication half compares a *file at a path* with a live candidate. It opens the database through
  `connection.open_read_only_database` — a pass that could repair the file it is checking would prove only that
  the repair worked, and a snapshot whose identity is confirmed by a writable connection is not confirmed by a
  reader — validates the declared schema generation, resolves the bound namespace, and returns the identity those
  two facts scope. Every failure is a `KnowledgeStorageError` rather than a returned value, so a caller comparing
  identities can name the path it could not read instead of treating it as empty.
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
  guessing from the value's text.
- `_BODY_VERSION` (`ar-knowledge-logical-body/v1`) is a separate version from the SQL schema version: the
  encoding of the identity can change without the schema changing, and vice versa.
- The module imports `schema`, `connection.{fetch_one,inspect_schema,open_read_only_database}` and
  `models.knowledge` only; it writes nothing. The read-only opener is the one dependency the file-level entry
  point added, and it is a *connection* dependency rather than a new owner.
- **A file-level identity is read only, and its failures are defects.** `dataset_identity` raises
  `KnowledgeStorageError` instead of returning a value or a refusal, because "I could not read this file" is not
  an identity and a caller must not be able to confuse the two.

### Invariants And Boundaries

- **Same knowledge, same digest, wherever it lives.** File copies, `VACUUM` and JSON text reshaping leave the
  digest unchanged; a real JSON value change moves it.
- **All ten tables participate.** The body is derived from `schema.CANONICAL_TABLES`, not from a hand-kept list,
  so a table added to the schema cannot silently leave the identity.
- **The digest is not a seal of authorship or approval.** It covers stored rows only; provenance is inside the
  rows it hashes, but a semantic judgement is not representable anywhere in this module.
- **Boundary.** This module owns the encoder and the row ordering. It does not decide when a comparison is a
  refusal (the batch's `_require_bound_context` does), and it does not own the SQL schema, the codecs or the
  connection contract.
- **Reuse rule for later leaves.** `logical_digest` is the one encoder: a later leaf that needs a dataset
  identity reuses it rather than defining a second one. The design's export envelope adds a format marker and a
  prefixed digest *on top of* this body. The publication half consumes it in both directions — a live candidate
  through `store.snapshot_identity()`, a closed file through `dataset_identity` — which is why the two can be
  compared at all.
- **An ambiguous namespace is refused, not resolved.** `bound_repository` raises when the file holds more than one
  repository row rather than choosing one; a dataset this package addresses is bound to exactly one namespace, and
  more than one row means the file is not a dataset this code wrote.
- **A file-level identity is read-only.** `dataset_identity` opens the file in a mode that cannot write it, so a
  comparison pass can never repair the artifact it is measuring.

### Todos

None recorded for this slice. `_require_declared_keys` verifies key columns exist, and it deliberately does not
verify that the declared key *equals* the DDL's — that comparison is the schema owner's, and the reviewer verified
the current table against the live DDL by hand (nine exact matches plus `repository`'s column-level primary key).

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
| The typed JSON columns decoded at the portable boundary. | `JSON_COLUMNS` | mcp/src/agents_remember/memory/knowledge/logical.py:69-76 |
| The body version and the digest over the canonical body. | `_BODY_VERSION`; `logical_digest`; `logical_body` | mcp/src/agents_remember/memory/knowledge/logical.py:79-79; mcp/src/agents_remember/memory/knowledge/logical.py:82-85; mcp/src/agents_remember/memory/knowledge/logical.py:88-103 |
| The row ordering, the cell decoding and the JSON-text-is-not-knowledge rule. | `_rows_of`; `_cell` | mcp/src/agents_remember/memory/knowledge/logical.py:184-198; mcp/src/agents_remember/memory/knowledge/logical.py:201-213 |
| The key-versus-manifest honesty check. | `_require_declared_keys` | mcp/src/agents_remember/memory/knowledge/logical.py:216-234 |
| The identity packaging and the defensive namespace read. | `snapshot_identity`; `require_bound_repository` | mcp/src/agents_remember/memory/knowledge/logical.py:106-115; mcp/src/agents_remember/memory/knowledge/logical.py:163-181 |
| **The file-level identity entry point this leaf added, and the ambiguous-namespace read it depends on.** | `dataset_identity`; `bound_repository` | mcp/src/agents_remember/memory/knowledge/logical.py:118-138; mcp/src/agents_remember/memory/knowledge/logical.py:141-160 |
| The read-only connection the file-level entry point must use, so a comparison cannot repair what it measures. | `open_read_only_database`; `inspect_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:55-66; mcp/src/agents_remember/memory/knowledge/connection.py:106-122 |
| The table and column manifest this module derives its body from. | `CANONICAL_TABLES`; `CANONICAL_COLUMNS`; `schema_fingerprint` | mcp/src/agents_remember/memory/knowledge/schema.py:26-42; mcp/src/agents_remember/memory/knowledge/schema.py:47-112; mcp/src/agents_remember/memory/knowledge/schema.py:362-392 |
| The kernel canonical encoder the digest is computed through. | `sha256_digest` | mcp/src/agents_remember/kernel/canonical_json.py:34-38 |
| The JSON decoder a typed column is compared through, which refuses ambiguous stored text. | `decoded_json` | mcp/src/agents_remember/kernel/canonical_json.py:46-62 |
| The store method that exposes the live identity to a caller cheaply, and the sibling half of every comparison. | `snapshot_identity` | mcp/src/agents_remember/memory/knowledge/store.py:304-318 |
| The publication half that consumes this identity in both directions. | `publication_state`; `dataset_identity` | mcp/src/agents_remember/memory/knowledge/materialization.py:34-99; mcp/src/agents_remember/memory/knowledge/publication.py:215-249 |
| The batch precondition this identity is compared against inside the transaction. | `_require_bound_context` | mcp/src/agents_remember/memory/knowledge/candidate.py:148-183 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The digest deliberately excludes Git commits and
ledger rows, so nothing here reads a second repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): **recorded the file-level half of the dataset identity.** The card's `KS-R04` forward reference is now the shipped contract: `dataset_identity` reads one database *file*'s identity through a read-only connection — so a comparison pass can never repair the artifact it measures — and `bound_repository` is the read that makes "a dataset this code addresses" precise by refusing more than one namespace row instead of picking one. The card now states that the publication half consumes this module in both directions (a live candidate through `store.snapshot_identity()`, a closed file through `dataset_identity`), which is why the two can be compared at all, and that every file-level failure is a `KnowledgeStorageError` rather than an identity a caller could mistake for a measurement. Citation ranges were re-derived against the working tree, four rows whose ranges no longer held their anchors were corrected, and this card's `governingOverview` link was repaired from `../../overview.md` — the application route — to the three-level path from `knowledge/`. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the new canonical logical dataset identity. It records what the body includes (all ten tables in manifest order, primary-key row order, typed JSON decoded) and what it deliberately excludes, the non-leading-column primary-key case that made the encoder's own honesty check necessary, the separate `body_version`, and the reuse rule that later publication and merge leaves compare this digest instead of defining a second encoder. Verification metadata remains empty until closeout stamps the code commit.
