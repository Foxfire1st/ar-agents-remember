# mcp/src/agents_remember/memory/knowledge/schema_v6.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Generation 6's appended tables, as pinned data.** Six tables — `family_composition`,
`family_composition_policy`, `family_composition_policy_version`, `family_revision_route`,
`family_revision_context` and `family_revision_context_revision` — carrying the authored edges
between exact family revisions, the versioned traversal policy those edges may declare, the family
*revision*'s canonical owning route, and the authored explanatory context with its append-only
revision chain.

This module owns **only what generation 6 appends**. Generation 1's ten tables, generation 2's six,
generation 3's four, generation 4's one and generation 5's one stay declared, verbatim, in
`schema.py`, `schema_v2.py`, `schema_v3.py`, `schema_v4.py` and `schema_v5.py`; nothing here
redeclares, reorders, renames, retypes or drops one of them, and **no `ALTER TABLE` against an earlier
generation's table appears anywhere in this package**. A card that describes generation 6 as
replacing, restating or re-declaring an earlier generation is false: the append is the whole
mechanism, and `KS-R10@v1` §1.3 makes appending the only sanctioned way to add a table.

**This module was renumbered once, and the number is not a claim.** `KS-R17@v1` was authored as
generation 5; a sibling leaf (`KS-R18@v1`) landed its own generation 5 first on the accumulated line,
so this append was renumbered to 6 and now descends from *that* generation rather than from generation
4. The append's content is unchanged by the renumber: only the module name, the constant, the schema
name and the base argument moved. That is exactly the property `_append_generation` exists to give.

**Why these are new tables and not columns on an existing one.** Three facts drive the shape, and each
is a refusal of the convenient alternative:

- `family_revision_route` records the canonical owning route of the **revision aggregate**. That is a
  different fact from generation 2's `family_route`, which records the *identity*'s governing route.
  Because an append is the only sanctioned way to add a table, the revision-altitude association is a
  table of its own rather than a column added to one of generation 2's joins.
- The explanatory context is a **family-specific record**, deliberately not an instance of the general
  `explanation` facet table. The two immutability doctrines differ — this context is immutable with a
  change being a newly identified revision, while the general `explanation` carries a mutable
  `current_revision_id` designation — and this table mints **no content address**: it declares no
  digest column, so the prose cannot become a second identity authority.
- The declared policy is **not** a column pair on the edge. A policy is its own authored record with
  its own immutable version set, and the edge names `(policy_id, policy_version_id)` together or
  leaves both `NULL`. Two nullable text columns on the edge would make identity-without-version and
  version-without-identity representable; the composite foreign key refuses them structurally.

## Code Commentary

### Logic

The module is pure data: it defines **no functions and no classes**. Its whole surface is eight module
constants, each a member of the generation record `schema_generations.GENERATION_6` composes:

- `APPENDED_TABLES` — the ordered six-name tuple, appended after generation 5's twenty-two, so
  generation 6's manifest **begins with** generation 5's, unchanged. The order is load-bearing: it is
  the order the encoder serializes tables in. The registry's total is therefore **28 tables**.
- `APPENDED_COLUMNS` — the declared column order of each table. `family_composition` declares
  `repository_id`, `composition_id`, `from_family_revision_id`, `to_family_revision_id`, `policy_id`,
  `policy_version_id`, `provenance`.
- `APPENDED_PRIMARY_KEYS` — the declared primary keys. `family_revision_route`'s key is
  `(repository_id, family_revision_id)`, so "at most one canonical owning route per family revision"
  is a constraint of the table rather than a rule the write path remembers.
- `APPENDED_JSON_COLUMNS` — declared per table rather than omitted, so "no typed-JSON column" is
  stated rather than inferred.
- `APPENDED_TABLE_DDL` — six `STRICT` `CREATE TABLE` statements. `family_composition` carries two
  composite foreign keys to `family_revision(repository_id, revision_id)` and **no** polymorphic
  `(target_kind, target_id)` column and no `related_to`: a wrong endpoint kind — an invariant
  revision, an anchor, a claim, a facet record — is unrepresentable rather than merely rejected.
  `CHECK (from_family_revision_id <> to_family_revision_id)` catches the one-node cycle.
  `family_composition_policy_version` declares four `CHECK`s (`declared_version <> ''`,
  `direction IN ('forward', 'reverse', 'both')`, `depth_bound >= 1`, `widened_scope <> ''`). Every
  foreign key is `NO ACTION … DEFERRABLE INITIALLY DEFERRED`, exactly as the earlier generations
  declare theirs.
- `APPENDED_INDEX_DDL` — nine indexes. Two of them are the declared unique tuple for the edge, and the
  reason is a SQLite fact worth carrying: **a table `UNIQUE` constraint over a nullable column does not
  enforce uniqueness for `NULL`s**, because SQLite treats every `NULL` as distinct in a unique key. A
  single table constraint over the nullable `policy_id` would therefore not have stopped a second
  *bare* edge — the default state — from being stored beside the first. The rule is declared as two
  **partial unique indexes** instead (`family_composition_pair_with_policy` with
  `WHERE policy_id IS NOT NULL`, and `family_composition_pair_without_policy` with
  `WHERE policy_id IS NULL`), and the write path's own duplicate lookup refuses the state with a typed
  refusal before either is reached.
- `APPENDED_TRIGGERS` — twelve triggers, a no-repoint/no-rewrite and a no-delete pair for each of the
  six tables. The idiom is the one the earlier generations use: the operation's preconditions exist to
  return a **typed refusal**, and these exist so a changeset, a repair script or a future code path
  that forgot the rule still cannot rewrite an authored row or drop one.
- `APPENDED_FEATURES` — the **empty** tuple, declared rather than omitted. Generation 6 requires no
  SQLite feature the earlier generations do not already require.

### Conventions

- Every table is `STRICT`, every primary-key column is declared `NOT NULL` explicitly, and every
  foreign key is composite and `DEFERRABLE INITIALLY DEFERRED`, exactly as the twenty-two shipped
  tables are.
- **Index names are a local choice — with one exception that is not.** An index may not carry a
  table's name, because SQLite refuses a second object under one identifier. The index over the edge's
  `policy_version_id` is therefore named `family_composition_policy_version_edge` rather than after
  the table it points at; the collision was found only when the DDL was actually executed.
- A chain's **first context revision names itself** in `predecessor_revision_id`, which is the stored
  representation of "no predecessor". The alternative, a nullable column, would make "first"
  indistinguishable from "the caller left it out".
- The module imports nothing from the package: it is data the composer reads, not behaviour that reads
  the database.

### Invariants And Boundaries

- **Additive-only, structurally.** `descends_from(GENERATION_6, GENERATION_5, GENERATION_5.tables)`
  is the published predicate: the appended tables follow generation 5's exactly, and every one of
  generation 5's names keeps the exact column tuple, primary key and typed-JSON set it declared. A new
  generation appends, and never retypes, reorders, renames or drops an earlier one's.
- **Generation 1 does not move.** Generation 1's fingerprint is pinned and recomputed by the registry's
  own case; this module adds nothing to any of generation 1's tables and states no `ALTER TABLE`.
- **No composition row carries a content address, a logical digest or a fingerprint column.** The
  context's identity is the key pair the substrate already uses for an authored row.
- **No row and no table here duplicates task status, seat ownership, lifecycle gates or approval
  authority.** Nothing here becomes an independently editable competing contract.
- **Boundary.** This module declares structure and nothing else: it writes no rows, performs no
  validation, returns no refusal and owns no behaviour. Writing an edge is
  `memory/knowledge/compositions.py`; deciding which generation a dataset is, is
  `schema_generations.py`.
- **Not admissible, recorded so it is not re-proposed:** a recursive CTE for the composition cycle
  check. `KS-R17@v1` §4.4 requires the shipped shared lineage rule to be reused, and a second walk
  beside it is exactly the drift the rule exists to prevent.

### Todos

None recorded. This generation's own fingerprint is computed by composition in
`schema_generations.py` rather than recorded here.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The six-name appended-table tuple whose prefix rule makes generation 6's manifest begin with generation 5's twenty-two tables. [1]
- The declared column order the encoder serializes rows through, including the edge's nullable `(policy_id, policy_version_id)` pair. [2]
- The declared composite primary keys, including the route table's key that makes "at most one canonical owning route per family revision" a constraint. [3]
- The declared typed-JSON mapping, so "no JSON column" is stated per table rather than inferred. [4]
- **The six `STRICT` `CREATE TABLE` statements: the two typed endpoint keys with no polymorphic target column, the one-node-cycle `CHECK`, and the four policy `CHECK`s.** [5]
- **The index-name collision, recorded where the rename happened: an index may not carry a table's name.** [6]
- **The declaration the collision renamed: the index over the edge's `policy_version_id`.** [7]
- **The declared unique tuple as two partial unique indexes, because a table `UNIQUE` over a nullable column does not enforce uniqueness for `NULL`s.** [8]
- The twelve immutability triggers, a no-repoint and a no-delete pair per table. [9]
- The declared-but-empty feature tuple, so "no new SQLite feature" is stated rather than inferred. [10]
- **The one generic append that composes every generation, and generation 6's own one-line call naming `GENERATION_5` as its base.** [11]
- **The published additive predicate the generation case uses.** [12]
- The registry whose last entry is the newest supported generation — generation 8 since `KS-R13@v1` renumbered its append — and the created generation it names. [13]
- The created store's own schema name, so a created dataset declares `ar-knowledge-sqlite/v6`. [14]
- **The case that measures the append, the six names, `descends_from` and the created generation.** [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
