# mcp/src/agents_remember/memory/knowledge/schema.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Generation 1's declarations, verbatim, plus the structural manifest and fingerprint of a generation
*record*.** One module owns generation 1's canonical table list, the exact DDL text, the trigger set,
the index set and the required SQLite feature set, so a reader compares its view of a database
against a declared generation instead of against prose.

It is no longer the whole schema story, and the earlier account that described it as *the* versioned
schema is superseded. Since 260915-KS-L10 a schema is a **registry of frozen generations**, owned by
`schema_generations.py`: this module declares generation 1 and the machinery that fingerprints a
generation, `schema_generations.GENERATION_1` delegates every field to these declarations rather than
restating them, and generation 2's declarations live in `schema_v2.py`.

## Code Commentary

### Logic

`SCHEMA_USER_VERSION = 1` is **generation 1's** `user_version` rather than the build's current version.
It enters generation 1's fingerprint, so it keeps this value for as long as generation 1 exists, and it
no longer moves when the schema grows; a created store declares
`schema_generations.CURRENT_GENERATION` (generation 2 in this build) instead.
`CANONICAL_TABLES` declares generation 1's manifest order — `repository`, `invariant`, `invariant_revision`,
`invariant_predecessor`, `family`, `family_revision`, `family_predecessor`, `source_anchor`, `family_member`,
`realization_claim`. `CANONICAL_COLUMNS` declares the exact column order per table, which a reader uses for
positional changeset rows rather than asking the database.

`TABLE_DDL` holds the ten `STRICT` tables. Every primary-key column is declared `NOT NULL` explicitly, because a
nullable key in an ordinary rowid table is a documented SQLite quirk that would silently defeat primary-key
identity. Foreign keys are composite and `ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED`, and both predecessor
tables carry `CHECK (child_revision_id <> parent_revision_id)`.

`INDEX_DDL` declares eight indexes, each covering the reverse direction of a declared lookup.
`IMMUTABILITY_TRIGGERS` declares fifteen triggers whose names are part of the contract because the merge preflight
compares them. `REQUIRED_SQLITE_FEATURES` names `strict_tables`, `deferrable_foreign_keys`,
`trigger_raise_abort` and `recursive_cte`.

`schema_manifest()` returns the compared structure (schema name, user version, table columns, sorted trigger and
index names, features); `schema_fingerprint()` hashes the manifest together with the exact table, trigger and
index DDL text; `create_schema_statements()` returns the ordered DDL — tables in manifest order, then indexes,
then triggers in sorted name order. `_index_name` derives a name from its `CREATE INDEX` statement.

Since 260915-KS-L10 the manifest, fingerprint and statement builders are driven by a **generation record**
(`SchemaGeneration`) rather than by this module's own globals, so generation 1's recorded data can be recomputed
against its pinned constant instead of against the code that produced it; `schema_generations.py` owns that record
and the gate that compares the two. `PRIMARY_KEYS` and `JSON_COLUMNS` also live here now — relocated from
`logical.py` with byte-identical declarations, which re-exports them — because a generation record must be
assembled without importing the module that consumes it.

`REQUIRED_SQLITE_FEATURES` describes **generation 1's** feature set; generation 2 adds `json_functions` because its
`record_revision.payload` column is `TEXT NOT NULL CHECK (json_valid(payload))`.

### Conventions

Two decisions are stated once in the module docstring and are load-bearing:

- **Every canonical table is created by this version, including the seven L1 does not write.** A session
  changeset can only carry operations for tables both sides already have, and a table present on one side only is
  exactly the schema mismatch the merge preflight must refuse; creating the shape once means later leaves extend
  behaviour inside a stable schema instead of migrating it.
- **Immutability is enforced by the database, not only by the operation.** A trigger refuses the write even when
  it arrives from a changeset, a repair script or a future code path that forgot the rule. The operation's own
  preconditions exist to return a *typed refusal*; the triggers exist so that forgetting them still cannot rewrite
  a sealed revision.

### Invariants And Boundaries

- **A schema change is a new registered generation, never a silent edit of an existing one** — and this leaf
  changed what that sentence means. The earlier form of this invariant read *"a schema change is a new generation
  (`ar-knowledge-sqlite/v2` with `SCHEMA_USER_VERSION = 2`)"*, which is now **wrong**: `SCHEMA_USER_VERSION` stays
  `1` because it is generation 1's `user_version` and is inside generation 1's fingerprint. A new shape is a new
  `SchemaGeneration` record (`GENERATION_2` = `ar-knowledge-sqlite/v2` / `2`), and a created store declares
  `CURRENT_GENERATION` rather than this constant.
- **Generation 1's declarations and fingerprint are frozen.** Generation 2's manifest begins with generation 1's
  ten tables in this order with these exact declared columns, keys and typed-JSON sets; a generation that would
  reorder, rename, retype, drop or weaken any of them is a schema divergence, not a member of the registry. **No
  `ALTER TABLE` against one of these tables is admissible**, which is why generation 2's governing-route
  association is expressed as new join tables in `schema_v2.py`.
- All fifteen triggers raise with an `immutable_revision:`-prefixed message so `map_sqlite_error` steers a
  trigger-originated error to that code. Generation 2 adds eight more triggers in `schema_v2.py` under the same
  prefix convention.
- `invariant.display_label` is deliberately **mutable** (the `invariant_no_rebind` trigger covers only
  `repository_id`/`invariant_id`): the friendly label is separate from identity, and a label edit names the row it
  expects through `invariant_row_digest`.

### Todos

None recorded. `REQUIRED_SQLITE_FEATURES` is declared and consumed as a manifest member; no runtime probe asserts
the features beyond what the DDL itself requires to succeed.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The canonical table manifest order, which a later leaf's logical encoder must follow. [1]
- The declared column order per table, used for positional changeset rows. [2]
- The ten `STRICT` tables with explicit NOT NULL keys, composite deferred FKs and the self-edge CHECK. [3]
- The fifteen immutability triggers whose names the merge preflight compares. [4]
- The structural manifest and the fingerprint over manifest plus DDL text. [5]
- The ordered DDL the creation path executes. [6]
- The open-time validation that refuses a partial schema or a dropped trigger. [7]
- The label's deliberate mutability is what the `invariant_no_rebind` trigger's column list encodes. [8]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
