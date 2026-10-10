# mcp/src/agents_remember/memory/knowledge/connection.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Opens a selected derived knowledge index read-only and checks or creates its one declared schema on an explicitly supplied connection.

## Code Commentary

`open_read_only_database` uses APSW read-only flags and a bounded busy timeout. `create_or_validate_schema` creates only the current declared schema when the supplied database is empty, inside an immediate transaction, then sets user_version; otherwise it inspects the existing schema. Inspection checks the declared tables, columns and triggers. Transaction errors roll back and propagate. The retired connection-contract helper and canonical-store WAL/journal selection are absent; this module does not turn an index read into an authoring connection.

### Logic

`BUSY_TIMEOUT_MILLISECONDS = 1000` is the bounded lock policy: wait this long for a competing writer, then refuse
as busy rather than block indefinitely. The operation never retries against a re-read snapshot.

`create_or_validate_schema` inspects `sqlite_schema` for any existing table: on an empty database it runs one
generation's DDL inside one immediate transaction and then writes `PRAGMA user_version`; on a populated one it
delegates to `inspect_schema`. **Initialization declares a generation; it does not select one.** An empty database
has no version to read, so "the dataset decides" cannot govern this path: creation asks
`schema_generations.generation_of_new_store()` for the newest generation this build supports (`CURRENT_GENERATION`,
`ar-knowledge-sqlite/v9`, user_version 9) and takes the DDL *and* the version marker from that one record, instead of reading the running
build's `SCHEMA_USER_VERSION` and its module-level DDL. The version marker is still written **after** the DDL
commits, so a crash between the two leaves a complete but unversioned database that the next open refuses instead
of guessing — the opposite order could leave a database claiming a generation it does not have.

`fetch_one` is the shared "the row, if there is one" reader: one `next(iter(...), None)` over a parameterized
statement, returning a plain tuple or `None`. Every reader in the package asks that question, and this is the one
owner of the shape — the graph modules' three reads call it rather than repeating the pattern at each call site.

`inspect_schema` **selects the generation from the database itself**, then requires *that* generation's structure:
it resolves `PRAGMA user_version` against the generation registry (never against the running build), calls
`_require_declared_tables(connection, declared)` (every table the selected generation declares is present and every
table's declared column tuple is identical to that generation's manifest) and `_require_declared_triggers(connection,
declared)` (no immutability trigger of that generation is missing). The returned `KnowledgeSchemaIdentity` carries
the selected generation's `schema_name`, `user_version` and recorded `fingerprint`, so the identity a caller receives
describes the dataset that was opened rather than the build that opened it. Every refusal this module raises for a database's declared structure is still fail-closed and still
names the fact that was missing. A version the registry does not contain is refused by the registry lookup before
these checks run: it is not migrated, repaired or re-read under another generation to obtain a green result.

`immediate_transaction` returns the `_ImmediateTransaction` context manager, whose `__enter__` runs
`BEGIN IMMEDIATE` (write lock taken before the first read) and whose `__exit__` rolls back on any exception without
suppressing it.

`open_read_only_database` opens one existing database through `SQLITE_OPEN_READONLY` and sets only
`busy_timeout`. **Verification uses it on purpose**: a pass that could repair the file it is checking would prove
only that the repair worked, and a snapshot whose identity is confirmed by a writable connection is not confirmed
by a reader. `foreign_keys` is deliberately not set there, because no statement that connection runs writes a row.

### Conventions

- **One key space, and it is the dataset's.** An open SQLite file declares its generation through
  `PRAGMA user_version` alone — the application schema name is not stored in the file — so this module resolves a
  database's generation by version and reports the generation's *own* `schema_name` afterwards. A caller that holds
  a name instead (a portable artifact, which does carry one) resolves a different key space in
  `schema_generations`; the two are not interchangeable.
- The registry is the only schema source this module consults. `connection.py` no longer imports the `schema`
  declarations module at all: creation, validation and the identity it returns all route through
  `schema_generations`, so there is one place where "which generations exist" is answered.

### Invariants And Boundaries

- Missing immutability triggers refuse at open, because a database without them can rewrite a sealed revision and
  therefore is not this schema. The trigger set it is measured against is the **selected generation's**, so each
  registered generation is held to its own declarations.
- **A database's generation is read, never assumed.** `inspect_schema` measures an existing database against the
  generation that database declares (through `PRAGMA user_version` resolved against the registry) and returns that
  generation's identity. The build's own newest generation decides exactly one thing in this module — what a
  *created* store declares — because an empty database has no declaration to read.
- **A generation this build does not register is refused, not interpreted.** An unregistered `user_version` raises
  before any table, column or trigger check, so no read of a foreign generation's structure can pass as a validation
  of a supported one.
- The transaction boundary rolls back on failure and never suppresses the caller's exception.
- **This module decides no identity rule and writes no domain row.** It is the boundary that makes the store's
  guarantees enforceable; the rules themselves belong to `store.py` and the graph modules.
- **One owner per repeated question.** A reader that needs "the row, if there is one" calls `fetch_one` rather
  than re-deriving the shape, so a change to how a single row is fetched is one change.
- **A verification read cannot write.** `open_read_only_database` is the connection every identity confirmation
  and every staged-copy check uses; a confirmation made through a writable connection would not be a confirmation.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- `open_read_only_database` owns the current boundary described above. [13]
- `create_or_validate_schema` owns the current boundary described above. [14]
- `inspect_schema` owns the current boundary described above. [15]

- - The bounded lock policy and its no-retry rule. [16]
- - The read-only connection every identity confirmation uses, so a pass cannot repair what it checks. [17]
- - The shared one-row reader every graph read is built on. [18]
- - Create-on-empty versus validate-on-existing, and the post-commit version marker. [19]
- - The existing database is checked for generation, exact table columns and the full trigger set. [20]
- - The single immediate transaction whose exit rolls back without suppressing the failure. [21]
- - The graph readers that reuse the one-row helper. [22]
- - The close that no longer calls the peer unlink, and why. [23]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
