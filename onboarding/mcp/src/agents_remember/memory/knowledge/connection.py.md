# mcp/src/agents_remember/memory/knowledge/connection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/connection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c`|
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The connection, pragma and schema-validation boundary of the knowledge store: what a connection **is**, which
pragmas are set and verified, how an empty database becomes a schema generation, and how an existing one is
checked against the generation **it declares** rather than the one this code happens to be built as.

## Code Commentary

### Logic

`BUSY_TIMEOUT_MILLISECONDS = 1000` is the bounded lock policy: wait this long for a competing writer, then refuse
as busy rather than block indefinitely. The operation never retries against a re-read snapshot.

`open_database` creates the parent directory, opens an `apsw.Connection` and applies the connection contract.
`apply_connection_contract` sets `busy_timeout`, sets `foreign_keys=ON` and then **reads the pragma back**,
raising `KnowledgeStorageError` if the build did not accept it — without enforcement a deferred constraint never
fires and every "the database refuses it" guarantee would silently become an intention.

`create_or_validate_schema` inspects `sqlite_schema` for any existing table: on an empty database it runs one
generation's DDL inside one immediate transaction and then writes `PRAGMA user_version`; on a populated one it
delegates to `inspect_schema`. **Initialization declares a generation; it does not select one.** An empty database
has no version to read, so "the dataset decides" cannot govern this path: creation asks
`schema_generations.generation_of_new_store()` for the newest generation this build supports (`CURRENT_GENERATION`,
generation 2) and takes the DDL *and* the version marker from that one record, instead of reading the running
build's `SCHEMA_USER_VERSION` and its module-level DDL. The version marker is still written **after** the DDL
commits, so a crash between the two leaves a complete but unversioned database that the next open refuses instead
of guessing — the opposite order could leave a database claiming a generation it does not have.

`fetch_one` is the shared "the row, if there is one" reader: one `next(iter(...), None)` over a parameterized
statement, returning a plain tuple or `None`. Every reader in the package asks that question, and this is the one
owner of the shape — the graph modules' ten reads call it rather than repeating the pattern at each call site.

`inspect_schema` **selects the generation from the database itself**, then requires *that* generation's structure:
it resolves `PRAGMA user_version` against the generation registry (never against the running build), calls
`_require_declared_tables(connection, declared)` (every table the selected generation declares is present and every
table's declared column tuple is identical to that generation's manifest) and `_require_declared_triggers(connection,
declared)` (no immutability trigger of that generation is missing). The returned `KnowledgeSchemaIdentity` carries
the selected generation's `schema_name`, `user_version` and recorded `fingerprint`, so the identity a caller receives
describes the dataset that was opened rather than the build that opened it — a generation-1 database therefore
reports `ar-knowledge-sqlite/v1` and the pinned generation-1 fingerprint even on a build whose newest generation is
generation 2. Every refusal this module raises for a database's declared structure is still fail-closed and still
names the fact that was missing. A version the registry does not contain is refused by the registry lookup before
these checks run: it is not migrated, repaired or re-read under another generation to obtain a green result.

`immediate_transaction` returns the `_ImmediateTransaction` context manager, whose `__enter__` runs
`BEGIN IMMEDIATE` (write lock taken before the first read) and whose `__exit__` rolls back on any exception without
suppressing it.

`open_read_only_database` opens one existing database through `SQLITE_OPEN_READONLY` and sets only
`busy_timeout`. **Verification uses it on purpose**: a pass that could repair the file it is checking would prove
only that the repair worked, and a snapshot whose identity is confirmed by a writable connection is not confirmed
by a reader. `foreign_keys` is deliberately not set there, because no statement that connection runs writes a row.
`journal_mode` reads and lowercases the connection's current `PRAGMA journal_mode`, which is how a staged copy
proves the mode it actually carries rather than the mode a caller asked for.

`discard_closed_wal_peers` unlinks the `-wal`/`-shm` peers of one database that no connection holds. **Its
boundary is the correction this leaf made, and the correction is about what it cannot know:** it cannot tell
whether another connection — in this process or another — still has the database open, and it does not need to,
because SQLite checkpoints its WAL and removes both peer files itself when the last connection closes cleanly.
What the unlink can do instead is **destroy committed content**: a reader holding a read transaction blocks that
checkpoint, so a writer's committed frames are still only in the WAL when a closing writer unlinks it, and the
committed rows are then absent from the main file and the database is left unreadable until it is rebuilt. That is
the failure the function's earlier docstring claimed was impossible, and it is reachable in this store's intended
multi-consumer shape (one consumer reading while another writes). The function remains for a caller that has
**independently established** that no connection holds the database — an offline repair, or an enclosure cleanup
that owns the file exclusively — and **no close path in this package may call it**: `OpenedKnowledgeStore.close`
no longer does (see `store.py.md`), and every ordinary close relies on SQLite instead.

### Conventions

- Keeping this boundary separate from the mutation logic is deliberate: the mutation then reads as a sequence of
  typed checks rather than a mix of SQLite plumbing and identity rules.
- **One key space, and it is the dataset's.** An open SQLite file declares its generation through
  `PRAGMA user_version` alone — the application schema name is not stored in the file — so this module resolves a
  database's generation by version and reports the generation's *own* `schema_name` afterwards. A caller that holds
  a name instead (a portable artifact, which does carry one) resolves a different key space in
  `schema_generations`; the two are not interchangeable.
- The registry is the only schema source this module consults. `connection.py` no longer imports the `schema`
  declarations module at all: creation, validation and the identity it returns all route through
  `schema_generations`, so there is one place where "which generations exist" is answered.

### Invariants And Boundaries

- `foreign_keys` is verified rather than assumed, and a build that will not enforce it makes the store refuse to
  operate at all.
- A partial schema is refused rather than written through: SQLite session changesets can silently omit a table
  that exists on only one side, which is exactly the schema mismatch the merge preflight must catch.
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
- **`discard_closed_wal_peers` is not a close-time call and its safety is a caller precondition, not a property of
  this function.** It cannot know whether another connection holds the database, so a caller may use it only after
  establishing exclusive ownership of the file. An unconditional call on close destroyed a committed batch
  whenever a reader held a read transaction — the defect 260915-KS-L4 corrected by removing the call rather than
  making it conditional; SQLite removes its own peers on the last clean close.

### Todos

None recorded for this leaf's slice. The former todo here — that `discard_closed_wal_peers` ran unconditionally
from `OpenedKnowledgeStore.close()` while its docstring claimed it ran only after the last connection closed, and
that a future leaf switching the journal mode should revisit it — is **closed by 260915-KS-L4**: the call was
removed from `close()` and the function's boundary restated as a caller precondition. Do not reintroduce a close-
time call; the durability case that reaches the failure is
`mcp/tests/test_knowledge_candidate_workspace.py::test_a_live_reader_does_not_let_the_write_boundarys_close_lose_the_commit`.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The bounded lock policy and its no-retry rule. | `BUSY_TIMEOUT_MILLISECONDS` | mcp/src/agents_remember/memory/knowledge/connection.py:23-23 |
| The verified foreign-key contract that fails closed on a build without enforcement. | `apply_connection_contract` | mcp/src/agents_remember/memory/knowledge/connection.py:35-49 |
| The read-only connection every identity confirmation uses, so a pass cannot repair what it checks. | `open_read_only_database` | mcp/src/agents_remember/memory/knowledge/connection.py:52-63 |
| The journal mode read back from a connection rather than requested of it. | `journal_mode` | mcp/src/agents_remember/memory/knowledge/connection.py:69-72 |
| The shared one-row reader every graph read is built on. | `fetch_one` | mcp/src/agents_remember/memory/knowledge/connection.py:72-85 |
| Create-on-empty versus validate-on-existing, and the post-commit version marker. | `create_or_validate_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:88-108 |
| The existing database is checked for generation, exact table columns and the full trigger set. | `inspect_schema`; `_require_declared_tables`; `_require_declared_triggers` | mcp/src/agents_remember/memory/knowledge/connection.py:106-122; mcp/src/agents_remember/memory/knowledge/connection.py:181-200; mcp/src/agents_remember/memory/knowledge/connection.py:203-215 |
| The single immediate transaction whose exit rolls back without suppressing the failure. | `immediate_transaction`; `_ImmediateTransaction` | mcp/src/agents_remember/memory/knowledge/connection.py:131-134; mcp/src/agents_remember/memory/knowledge/connection.py:137-154 |
| The peer unlink whose safety is a caller precondition: no connection may hold the database, and no close path in this package may call it. | `discard_closed_wal_peers` | mcp/src/agents_remember/memory/knowledge/connection.py:150-172 |
| The graph readers that reuse the one-row helper. | `get_anchor`; `get_family_revision`; `get_family_member`; `get_realization_claim` | mcp/src/agents_remember/memory/knowledge/anchors.py:138-152; mcp/src/agents_remember/memory/knowledge/families.py:267-284; mcp/src/agents_remember/memory/knowledge/memberships.py:230-240; mcp/src/agents_remember/memory/knowledge/realizations.py:246-256 |
| The declared generation the validation compares against. | `SCHEMA_USER_VERSION`; `CANONICAL_TABLES`; `CANONICAL_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema.py:26-42; mcp/src/agents_remember/memory/knowledge/schema.py:47-112 |
| The close that no longer calls the peer unlink, and why. | `close` | mcp/src/agents_remember/memory/knowledge/store.py:136-147 |
| The durability node that reaches the state an unconditional unlink destroyed. | "test_a_live_reader_does_not_let_the_write_boundarys_close_lose_the_commit" | mcp/tests/test_knowledge_candidate_workspace.py:206-246 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): **retired this card's account of schema validation as a comparison against the build's single constant, and corrected the create path with it.** The card said `inspect_schema` "refuses an unexpected `user_version`" and then checked "the manifest"; that was true only while one generation existed and is now false in both directions — a generation-1 database opened by this generation-2 build is legitimate and must be checked against *generation 1*, while an unregistered version must be refused before any table check. The corrected card records the two directions the registry splits the boundary into: `create_or_validate_schema` **declares** (an empty database has no version to read, so creation asks `generation_of_new_store()` for `CURRENT_GENERATION`, generation 2, and takes that record's DDL and `user_version`), and `inspect_schema` **selects** (it reads `PRAGMA user_version` from the dataset, resolves it against the registry, and requires *that* generation's tables, column lists and triggers, reporting that generation's `schema_name`, `user_version` and recorded `fingerprint`). The failure site that used to gate this leaf is gone rather than relocated: a version-1 candidate opened by generation-2 code is no longer refused for being version 1 — it is accepted and validated as generation 1, and only a *structurally* non-conforming database is refused. The card now also states the single-key-space rule (an open file declares version only; the name it reports is the resolved generation's own) and that `connection.py` no longer imports the `schema` declarations module. The verified-pragma contract, the create-versus-validate split, the post-commit version marker, `open_read_only_database`, `journal_mode` and the `discard_closed_wal_peers` boundary are unchanged from L4. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): **corrected this card's account of `discard_closed_wal_peers`, and closed the todo it carried.** The card previously said the function "unlinks `-wal`/`-shm` peers for a database whose last connection is closed" and filed the gap as a todo because `OpenedKnowledgeStore.close()` called it unconditionally while its docstring claimed otherwise. The gap was not harmless — the reviewer established that the unconditional unlink **destroyed a committed batch** whenever a reader held a read transaction (the reader blocks SQLite's checkpoint, so committed frames are still only in the WAL when the closing writer unlinks it, leaving the committed rows absent from the main file). The call is now **removed** from `close()` rather than made conditional, because the function cannot know whether another connection holds the database; its new boundary is a caller precondition that may be satisfied only by a caller that owns the file exclusively (offline repair, enclosure cleanup). The corrected card states that boundary, records that no close path in this package may call it, and adds the two functions this leaf introduced here — `open_read_only_database` (the read-only connection every identity confirmation and staged-copy check uses, so a pass cannot repair what it checks) and `journal_mode` (the mode read back from a connection rather than requested of it). The verified-pragma contract, the create-versus-validate split and the fail-closed schema refusals are unchanged from L1/L2. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): recorded the one addition this leaf made to the boundary — `fetch_one`, the shared "the row, if there is one" reader now used by all ten graph reads, which keeps that shape in one owner instead of repeated at each call site — plus the two boundaries it does not cross (no identity rule, no domain row). The verified-pragma contract, the create-versus-validate split and the fail-closed schema refusals are unchanged from L1 and are the reason the graph modules' foreign-key guarantees hold. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new connection/schema-validation boundary. It records the verified-pragma rule, the create-versus-validate split and the two fail-closed schema refusals. Verification metadata remains empty until closeout stamps the code commit.
