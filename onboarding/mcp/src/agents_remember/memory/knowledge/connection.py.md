# mcp/src/agents_remember/memory/knowledge/connection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/connection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash | `60e0820e6cb3b1d160518b9f8c7ac6241323a281`|
| lastVerifiedCommitDate | 2026-09-15T22:46:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

## Purpose

The connection, pragma and schema-validation boundary of the knowledge store: what a connection **is**, which
pragmas are set and verified, how an empty database becomes this schema generation, and how an existing one is
checked against the generation this code assumes.

## Code Commentary

### Logic

`BUSY_TIMEOUT_MILLISECONDS = 1000` is the bounded lock policy: wait this long for a competing writer, then refuse
as busy rather than block indefinitely. The operation never retries against a re-read snapshot.

`open_database` creates the parent directory, opens an `apsw.Connection` and applies the connection contract.
`apply_connection_contract` sets `busy_timeout`, sets `foreign_keys=ON` and then **reads the pragma back**,
raising `KnowledgeStorageError` if the build did not accept it — without enforcement a deferred constraint never
fires and every "the database refuses it" guarantee would silently become an intention.

`create_or_validate_schema` inspects `sqlite_schema` for any existing table: on an empty database it runs the
declared DDL inside one immediate transaction and then writes `PRAGMA user_version`; on a populated one it
delegates to `inspect_schema`. The version marker is written **after** the DDL commits, so a crash between the two
leaves a complete but unversioned database that the next open refuses instead of guessing — the opposite order
could leave a database claiming a generation it does not have.

`inspect_schema` refuses an unexpected `user_version`, then calls `_require_declared_tables` (every canonical table
present and every table's declared column tuple identical to the manifest) and `_require_declared_triggers` (no
immutability trigger missing), returning the `KnowledgeSchemaIdentity` with the current fingerprint.

`immediate_transaction` returns the `_ImmediateTransaction` context manager, whose `__enter__` runs
`BEGIN IMMEDIATE` (write lock taken before the first read) and whose `__exit__` rolls back on any exception without
suppressing it.

`discard_closed_wal_peers` unlinks `-wal`/`-shm` peers for a database whose last connection is closed.

### Conventions

Keeping this boundary separate from the mutation logic is deliberate: the mutation then reads as a sequence of
typed checks rather than a mix of SQLite plumbing and identity rules.

### Invariants And Boundaries

- `foreign_keys` is verified rather than assumed, and a build that will not enforce it makes the store refuse to
  operate at all.
- A partial schema is refused rather than written through: SQLite session changesets can silently omit a table
  that exists on only one side, which is exactly the schema mismatch the merge preflight must catch.
- Missing immutability triggers refuse at open, because a database without them can rewrite a sealed revision and
  therefore is not this schema.
- The transaction boundary rolls back on failure and never suppresses the caller's exception.

### Todos

`discard_closed_wal_peers` runs unconditionally from `OpenedKnowledgeStore.close()`, so its docstring claim that it
runs "only after the last connection is closed" is broader than the enforcement; harmless today because the default
journal mode is not WAL and no peer is created, but a future leaf that switches the journal mode should revisit it
(owned by KS-R04).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The bounded lock policy and its no-retry rule. | `BUSY_TIMEOUT_MILLISECONDS` | mcp/src/agents_remember/memory/knowledge/connection.py:23-25 |
| The verified foreign-key contract that fails closed on a build without enforcement. | `apply_connection_contract` | mcp/src/agents_remember/memory/knowledge/connection.py:37-51 |
| Create-on-empty versus validate-on-existing, and the post-commit version marker. | `create_or_validate_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:54-66 |
| The existing database is checked for generation, exact table columns and the full trigger set. | `inspect_schema`; `_require_declared_tables`; `_require_declared_triggers` | mcp/src/agents_remember/memory/knowledge/connection.py:69-84; mcp/src/agents_remember/memory/knowledge/connection.py:127-157 |
| The single immediate transaction whose exit rolls back without suppressing the failure. | `immediate_transaction`; `_ImmediateTransaction` | mcp/src/agents_remember/memory/knowledge/connection.py:87-110 |
| The declared generation the validation compares against. | `SCHEMA_USER_VERSION`; `CANONICAL_TABLES`; `CANONICAL_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema.py:26-42; mcp/src/agents_remember/memory/knowledge/schema.py:47-112 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new connection/schema-validation boundary. It records the verified-pragma rule, the create-versus-validate split and the two fail-closed schema refusals. Verification metadata remains empty until closeout stamps the code commit.
