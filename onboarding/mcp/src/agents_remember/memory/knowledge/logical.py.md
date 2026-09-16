# mcp/src/agents_remember/memory/knowledge/logical.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/logical.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `76c7697ca275a8d2764729145c950c166f3f9ec3`|
| lastVerifiedCommitDate | 2026-09-16T10:27:28+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

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
- The module imports `schema`, `connection.fetch_one` and `models.knowledge` only; it writes nothing.

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
  prefixed digest *on top of* this body.

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
| The declared primary key per canonical table, including the non-leading-column case. | `PRIMARY_KEYS` | mcp/src/agents_remember/memory/knowledge/logical.py:30-60 |
| The typed JSON columns decoded at the portable boundary. | `JSON_COLUMNS` | mcp/src/agents_remember/memory/knowledge/logical.py:62-72 |
| The body version and the digest over the canonical body. | `_BODY_VERSION`; `logical_digest`; `logical_body` | mcp/src/agents_remember/memory/knowledge/logical.py:74-98 |
| The row ordering, the cell decoding and the JSON-text-is-not-knowledge rule. | `_rows_of`; `_cell` | mcp/src/agents_remember/memory/knowledge/logical.py:134-163 |
| The key-versus-manifest honesty check. | `_require_declared_keys` | mcp/src/agents_remember/memory/knowledge/logical.py:166-184 |
| The identity packaging and the defensive namespace read. | `snapshot_identity`; `require_bound_repository` | mcp/src/agents_remember/memory/knowledge/logical.py:101-110; mcp/src/agents_remember/memory/knowledge/logical.py:113-131 |
| The table and column manifest this module derives its body from. | `CANONICAL_TABLES`; `CANONICAL_COLUMNS`; `schema_fingerprint` | mcp/src/agents_remember/memory/knowledge/schema.py:26-42; mcp/src/agents_remember/memory/knowledge/schema.py:47-112; mcp/src/agents_remember/memory/knowledge/schema.py:362-392 |
| The kernel canonical encoder the digest is computed through. | `sha256_digest` | mcp/src/agents_remember/kernel/canonical_json.py:34-38 |
| The JSON decoder a typed column is compared through, which refuses ambiguous stored text. | `decoded_json` | mcp/src/agents_remember/kernel/canonical_json.py:46-62 |
| The store method that exposes the live identity to a caller cheaply. | `snapshot_identity` | mcp/src/agents_remember/memory/knowledge/store.py:303-317 |
| The batch precondition this identity is compared against inside the transaction. | `_require_bound_context` | mcp/src/agents_remember/memory/knowledge/candidate.py:148-183 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The digest deliberately excludes Git commits and
ledger rows, so nothing here reads a second repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the new canonical logical dataset identity. It records what the body includes (all ten tables in manifest order, primary-key row order, typed JSON decoded) and what it deliberately excludes, the non-leading-column primary-key case that made the encoder's own honesty check necessary, the separate `body_version`, and the reuse rule that later publication and merge leaves compare this digest instead of defining a second encoder. Verification metadata remains empty until closeout stamps the code commit.
