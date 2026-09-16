# mcp/src/agents_remember/memory/knowledge/connection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/connection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate | 2026-09-16T08:41:27+02:00|
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

`fetch_one` is the shared "the row, if there is one" reader: one `next(iter(...), None)` over a parameterized
statement, returning a plain tuple or `None`. Every reader in the package asks that question, and this is the one
owner of the shape — the graph modules' ten reads call it rather than repeating the pattern at each call site.

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
- **This module decides no identity rule and writes no domain row.** It is the boundary that makes the store's
  guarantees enforceable; the rules themselves belong to `store.py` and the graph modules.
- **One owner per repeated question.** A reader that needs "the row, if there is one" calls `fetch_one` rather
  than re-deriving the shape, so a change to how a single row is fetched is one change.

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
| The bounded lock policy and its no-retry rule. | `BUSY_TIMEOUT_MILLISECONDS` | mcp/src/agents_remember/memory/knowledge/connection.py:26-26 |
| The verified foreign-key contract that fails closed on a build without enforcement. | `apply_connection_contract` | mcp/src/agents_remember/memory/knowledge/connection.py:38-52 |
| The shared one-row reader every graph read is built on. | `fetch_one` | mcp/src/agents_remember/memory/knowledge/connection.py:55-68 |
| Create-on-empty versus validate-on-existing, and the post-commit version marker. | `create_or_validate_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:71-85 |
| The existing database is checked for generation, exact table columns and the full trigger set. | `inspect_schema`; `_require_declared_tables`; `_require_declared_triggers` | mcp/src/agents_remember/memory/knowledge/connection.py:86-103; mcp/src/agents_remember/memory/knowledge/connection.py:144-163; mcp/src/agents_remember/memory/knowledge/connection.py:164-174 |
| The single immediate transaction whose exit rolls back without suppressing the failure. | `immediate_transaction`; `_ImmediateTransaction` | mcp/src/agents_remember/memory/knowledge/connection.py:104-129 |
| The graph readers that reuse the one-row helper. | `get_anchor`; `get_family_revision`; `get_family_member`; `get_realization_claim` | mcp/src/agents_remember/memory/knowledge/anchors.py:130-144; mcp/src/agents_remember/memory/knowledge/families.py:215-232; mcp/src/agents_remember/memory/knowledge/memberships.py:176-186; mcp/src/agents_remember/memory/knowledge/realizations.py:213-223 |
| The declared generation the validation compares against. | `SCHEMA_USER_VERSION`; `CANONICAL_TABLES`; `CANONICAL_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema.py:26-42; mcp/src/agents_remember/memory/knowledge/schema.py:47-112 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): recorded the one addition this leaf made to the boundary — `fetch_one`, the shared "the row, if there is one" reader now used by all ten graph reads, which keeps that shape in one owner instead of repeated at each call site — plus the two boundaries it does not cross (no identity rule, no domain row). The verified-pragma contract, the create-versus-validate split and the fail-closed schema refusals are unchanged from L1 and are the reason the graph modules' foreign-key guarantees hold. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new connection/schema-validation boundary. It records the verified-pragma rule, the create-versus-validate split and the two fail-closed schema refusals. Verification metadata remains empty until closeout stamps the code commit.
