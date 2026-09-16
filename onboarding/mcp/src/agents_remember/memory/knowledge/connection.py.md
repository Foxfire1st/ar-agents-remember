# mcp/src/agents_remember/memory/knowledge/connection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/connection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `3332a4ce7029777d49feca22b499350435a9f83c`|
| lastVerifiedCommitDate | 2026-09-16T11:50:16+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

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
| The bounded lock policy and its no-retry rule. | `BUSY_TIMEOUT_MILLISECONDS` | mcp/src/agents_remember/memory/knowledge/connection.py:26-26 |
| The verified foreign-key contract that fails closed on a build without enforcement. | `apply_connection_contract` | mcp/src/agents_remember/memory/knowledge/connection.py:38-52 |
| The read-only connection every identity confirmation uses, so a pass cannot repair what it checks. | `open_read_only_database` | mcp/src/agents_remember/memory/knowledge/connection.py:55-66 |
| The journal mode read back from a connection rather than requested of it. | `journal_mode` | mcp/src/agents_remember/memory/knowledge/connection.py:69-72 |
| The shared one-row reader every graph read is built on. | `fetch_one` | mcp/src/agents_remember/memory/knowledge/connection.py:75-88 |
| Create-on-empty versus validate-on-existing, and the post-commit version marker. | `create_or_validate_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:91-103 |
| The existing database is checked for generation, exact table columns and the full trigger set. | `inspect_schema`; `_require_declared_tables`; `_require_declared_triggers` | mcp/src/agents_remember/memory/knowledge/connection.py:106-122; mcp/src/agents_remember/memory/knowledge/connection.py:174-192; mcp/src/agents_remember/memory/knowledge/connection.py:194-204 |
| The single immediate transaction whose exit rolls back without suppressing the failure. | `immediate_transaction`; `_ImmediateTransaction` | mcp/src/agents_remember/memory/knowledge/connection.py:124-128; mcp/src/agents_remember/memory/knowledge/connection.py:130-148 |
| The peer unlink whose safety is a caller precondition: no connection may hold the database, and no close path in this package may call it. | `discard_closed_wal_peers` | mcp/src/agents_remember/memory/knowledge/connection.py:150-172 |
| The graph readers that reuse the one-row helper. | `get_anchor`; `get_family_revision`; `get_family_member`; `get_realization_claim` | mcp/src/agents_remember/memory/knowledge/anchors.py:138-152; mcp/src/agents_remember/memory/knowledge/families.py:267-284; mcp/src/agents_remember/memory/knowledge/memberships.py:230-240; mcp/src/agents_remember/memory/knowledge/realizations.py:246-256 |
| The declared generation the validation compares against. | `SCHEMA_USER_VERSION`; `CANONICAL_TABLES`; `CANONICAL_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema.py:26-42; mcp/src/agents_remember/memory/knowledge/schema.py:47-112 |
| The close that no longer calls the peer unlink, and why. | `close` | mcp/src/agents_remember/memory/knowledge/store.py:113-124 |
| The durability node that reaches the state an unconditional unlink destroyed. | "test_a_live_reader_does_not_let_the_write_boundarys_close_lose_the_commit" | mcp/tests/test_knowledge_candidate_workspace.py:206-246 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): **corrected this card's account of `discard_closed_wal_peers`, and closed the todo it carried.** The card previously said the function "unlinks `-wal`/`-shm` peers for a database whose last connection is closed" and filed the gap as a todo because `OpenedKnowledgeStore.close()` called it unconditionally while its docstring claimed otherwise. The gap was not harmless — the reviewer established that the unconditional unlink **destroyed a committed batch** whenever a reader held a read transaction (the reader blocks SQLite's checkpoint, so committed frames are still only in the WAL when the closing writer unlinks it, leaving the committed rows absent from the main file). The call is now **removed** from `close()` rather than made conditional, because the function cannot know whether another connection holds the database; its new boundary is a caller precondition that may be satisfied only by a caller that owns the file exclusively (offline repair, enclosure cleanup). The corrected card states that boundary, records that no close path in this package may call it, and adds the two functions this leaf introduced here — `open_read_only_database` (the read-only connection every identity confirmation and staged-copy check uses, so a pass cannot repair what it checks) and `journal_mode` (the mode read back from a connection rather than requested of it). The verified-pragma contract, the create-versus-validate split and the fail-closed schema refusals are unchanged from L1/L2. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): recorded the one addition this leaf made to the boundary — `fetch_one`, the shared "the row, if there is one" reader now used by all ten graph reads, which keeps that shape in one owner instead of repeated at each call site — plus the two boundaries it does not cross (no identity rule, no domain row). The verified-pragma contract, the create-versus-validate split and the fail-closed schema refusals are unchanged from L1 and are the reason the graph modules' foreign-key guarantees hold. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new connection/schema-validation boundary. It records the verified-pragma rule, the create-versus-validate split and the two fail-closed schema refusals. Verification metadata remains empty until closeout stamps the code commit.
