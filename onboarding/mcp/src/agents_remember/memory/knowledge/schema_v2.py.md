# mcp/src/agents_remember/memory/knowledge/schema_v2.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Generation 2's appended tables, as pinned data.** Six tables — `route`, the `knowledge_record`
envelope, `record_revision`, and the three governing-route joins — with their column orders, key
tuples, typed-JSON column sets, DDL, indexes and immutability triggers.

This module owns **only what generation 2 appends**. Generation 1's ten tables stay declared verbatim
in `schema.py`; nothing here redeclares, reorders, renames, retypes or drops one of them. That is
requirement 1.3 as a hard rule rather than a convention, and it is the reason the governing-route
association is expressed as new join tables instead of as a `governing_route_id` column added to
`source_anchor`, `invariant` or `family`: appending a column to a generation-1 table would change
that table's declared column set, and generation 1's own record must keep declaring the table without
it.

## Code Commentary

### Logic

The module is pure declaration data. Its eight APPENDED_* constants are consumed after the base tables by schema_generations._compose to build CURRENT_GENERATION. The historical generation-2 grouping identifies these six appended tables; this build does not expose an openable generation-2 schema.

- `APPENDED_TABLES` — the ordered tuple `("route", "knowledge_record", "record_revision",
  "source_anchor_route", "invariant_route", "family_route")`. The order is load-bearing: it is the
  order the encoder serializes them in, and it is appended after generation 1's ten so generation 2's
  manifest **begins with** generation 1's, unchanged.
- `APPENDED_COLUMNS`, `APPENDED_PRIMARY_KEYS`, `APPENDED_JSON_COLUMNS` — the per-table declared
  column order, key tuple and typed-JSON set the encoder orders and decodes rows through.
- `APPENDED_TABLE_DDL` — one `CREATE TABLE` per appended table.
- `APPENDED_INDEX_DDL` — nine indexes, each covering the reverse direction of a declared lookup.
- `APPENDED_TRIGGERS` — eight immutability triggers.
- `APPENDED_FEATURES` — `("json_functions",)`, the one SQLite feature generation 2 needs beyond
  generation 1's set, because `json_valid` now appears in a `CHECK`.

Why the tables are shaped this way:

- **`route`** carries a repository-relative code-path scope and a self-referencing parent. The
  self-reference is `ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED` like every shipped foreign
  key, so one transaction may insert a whole hierarchy without depending on insert order. The
  one-node cycle is a `CHECK (parent_route_id IS NULL OR parent_route_id <> route_id)`; the longer
  cycle is found by a recursive-CTE walk run inside the same transaction before commit
  (`routes.require_acyclic_routes`).
- **`knowledge_record`** is the envelope, and it carries **no content address, no logical digest and
  no fingerprint column**. That absence is the enforcement of requirement 3.3: a table with no
  identity-valued column cannot quietly become a second identity authority later. It carries `kind`,
  `authority_home`, `lifecycle`, `record_schema` and a nullable `governing_route_id` referencing
  `route`. `record_schema` names the frozen payload shape its `kind` resolves to; it is **not** a
  fingerprint.
- **`record_revision`** is where the payload lives, because `Doc13:85` puts "revision payload/schema"
  on the revision rather than on the envelope. `payload` is the typed-JSON column —
  `TEXT NOT NULL CHECK (json_valid(payload))` — which is what `storage-design.md:97` means by
  `TEXT_JSON`, and it is why generation 2 adds `json_functions` to its feature set. The revision also
  carries `content_digest`, an optional predecessor and provenance.
- **The three `*_route` tables** associate a shipped generation-1 entity with the route that governs
  it: `source_anchor_route`, `invariant_route`, `family_route`. Each takes the governed entity's key
  as its **own primary key**, which makes "at most one governing route per governed row" a constraint
  of the table rather than a convention, and each foreign key names one exact table, which is the
  endpoint-kind compatibility `Doc13:102` requires of a scoped association.

### Conventions

- Every table is `STRICT`, every primary-key column is declared `NOT NULL` explicitly, and every
  foreign key is composite and `DEFERRABLE INITIALLY DEFERRED`, exactly as the ten shipped tables are.
- Trigger messages share the shipped `immutable_revision:` prefix retained from the canonical database schema. The former map_sqlite_error mapper was retired; the trigger declarations remain part of the derived-index schema. The eight triggers refuse: rewriting a sealed record
  revision (`record_revision_no_rewrite`, covering `record_schema`, `payload`,
  `predecessor_revision_id`, `content_digest` and `provenance`), deleting one
  (`record_revision_no_delete`), rebinding an envelope's identity (`knowledge_record_no_rebind`),
  rebinding or deleting a route (`route_no_rebind`, `route_no_delete`), and repointing a governing
  association (`source_anchor_route_no_repoint`, `invariant_route_no_repoint`,
  `family_route_no_repoint`).
- Index names are a local choice, not contract; each covers the reverse direction of a lookup the
  package performs (`route_parent`, `route_path`, `knowledge_record_kind`,
  `knowledge_record_governing_route`, `record_revision_record`, `record_revision_predecessor`, and
  one route index per join table).

### Invariants And Boundaries

- **No `ALTER TABLE` appears anywhere in this module or in this package.** The single occurrence of
  the phrase in this file is inside its own docstring, as the prohibition. A generation that changed
  a column of an earlier generation is a schema divergence, not a generation.
- The ordered composition preserves the base tables and their declared columns, primary keys and typed-JSON sets while adding this block. The full derived-index schema is pinned by its recorded structural fingerprint, rather than selected from per-generation records.
- **The envelope holds no identity.** It mints none, derives none and overrides none; `payload_digest`
  stays where generation 1 put it, on the revision aggregate that owns it; `Repository` remains the
  authority home.
- **Immutability is enforced by the database, not only by the operation.** These triggers exist so a
  changeset, a repair script or a future code path that forgot the rule still cannot rewrite a sealed
  revision or repoint a sealed association. The operations' own preconditions exist to return a typed
  refusal; the triggers exist so that forgetting them still cannot corrupt the record.
- This module declares derived-index structure only: no row writing, payload validation, refusal or migration. The former canonical database record writer associated with these tables was retired. schema_generations composes and validates the one supported index schema.
- **Not admissible, recorded so it is not re-proposed:** adding `governing_route_id` to a generation-1
  table. Requirement 1.3 forbids changing a generation-1 table's declared column set, and the
  additive check rejects it.

### Todos

None recorded. The concrete record groups the envelope will carry (`EvidenceClaim`,
`DetectionSignal`, …) are later leaves; this module declares the envelope they will use and the one
internal conformance kind that exercises its seam.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The ordered appended-table tuple whose prefix rule makes generation 2's manifest begin with generation 1's ten tables. [1]
- The declared column order, key tuple and typed-JSON set per appended table — the encoder's ordering and decoding inputs. [2]
- The six `STRICT` `CREATE TABLE` statements, including the route self-reference and its one-node cycle `CHECK`, and the typed-JSON payload column with `json_valid`. [3]
- The nine reverse-direction indexes, including the governing-route lookup index. [4]
- The eight immutability triggers: sealed revisions cannot be rewritten or deleted, identities cannot be rebound, and a governing association cannot be repointed. [5]
- The one added required feature, which is part of the fingerprint because it is part of the manifest. [6]

- The ordered appended declarations compose into the one pinned derived-index schema. [7]

- The shipped generation-1 tables this module appends after and never touches. [8]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
