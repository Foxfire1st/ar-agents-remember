# mcp/src/agents_remember/memory/knowledge/schema_v6.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/schema_v6.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T09:20+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The six-name appended-table tuple whose prefix rule makes generation 6's manifest begin with generation 5's twenty-two tables. | `APPENDED_TABLES` | mcp/src/agents_remember/memory/knowledge/schema_v6.py:92-99 |
| The declared column order the encoder serializes rows through, including the edge's nullable `(policy_id, policy_version_id)` pair. | `APPENDED_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v6.py:101-148 |
| The declared composite primary keys, including the route table's key that makes "at most one canonical owning route per family revision" a constraint. | `APPENDED_PRIMARY_KEYS` | mcp/src/agents_remember/memory/knowledge/schema_v6.py:153-164 |
| The declared typed-JSON mapping, so "no JSON column" is stated per table rather than inferred. | `APPENDED_JSON_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v6.py:171-178 |
| **The six `STRICT` `CREATE TABLE` statements: the two typed endpoint keys with no polymorphic target column, the one-node-cycle `CHECK`, and the four policy `CHECK`s.** | `APPENDED_TABLE_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v6.py:180-300 |
| **The index-name collision, recorded where the rename happened: an index may not carry a table's name.** | `family_composition_policy_version_edge` | mcp/src/agents_remember/memory/knowledge/schema_v6.py:305-306 |
| **The declaration the collision renamed: the index over the edge's `policy_version_id`.** | `family_composition_policy_version_edge` | mcp/src/agents_remember/memory/knowledge/schema_v6.py:312-312 |
| **The declared unique tuple as two partial unique indexes, because a table `UNIQUE` over a nullable column does not enforce uniqueness for `NULL`s.** | `family_composition_pair_with_policy`; `family_composition_pair_without_policy` | mcp/src/agents_remember/memory/knowledge/schema_v6.py:316-316; mcp/src/agents_remember/memory/knowledge/schema_v6.py:320-320 |
| The twelve immutability triggers, a no-repoint and a no-delete pair per table. | `APPENDED_TRIGGERS` | mcp/src/agents_remember/memory/knowledge/schema_v6.py:343-404 |
| The declared-but-empty feature tuple, so "no new SQLite feature" is stated rather than inferred. | `APPENDED_FEATURES` | mcp/src/agents_remember/memory/knowledge/schema_v6.py:412-412 |
| **The one generic append that composes every generation, and generation 6's own one-line call naming `GENERATION_5` as its base.** | `_append_generation`; `_compose_generation_6` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:222-245; mcp/src/agents_remember/memory/knowledge/schema_generations.py:346-357; mcp/src/agents_remember/memory/knowledge/schema_generations.py:361-369; mcp/src/agents_remember/memory/knowledge/schema_generations.py:248-248; mcp/src/agents_remember/memory/knowledge/schema_generations.py:372-387 |
| **The published additive predicate the generation case uses.** | `descends_from` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:276-299 |
| The registry whose last entry is the newest supported generation — generation 8 since `KS-R13@v1` renumbered its append — and the created generation it names. | `GENERATIONS`; `CURRENT_GENERATION` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:425-434; mcp/src/agents_remember/memory/knowledge/schema_generations.py:447-447; mcp/src/agents_remember/memory/knowledge/schema_generations.py:456-469; mcp/src/agents_remember/memory/knowledge/schema_generations.py:479-482 |
| The created store's own schema name, so a created dataset declares `ar-knowledge-sqlite/v6`. | `GENERATION_6_SCHEMA_NAME` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:223-223 |
| **The case that measures the append, the six names, `descends_from` and the created generation.** | "test_the_registered_generation_appends_the_six_tables_to_the_generation_it_descends_from" | mcp/tests/test_knowledge_family_composition.py:376-376 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T19:56:45+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the three enforced `citation_anchor_absent_from_range` rows in this document** (two table rows). (a) The registry row cited `schema_generations.py:456-456` (the comment above the registry) for `GENERATIONS` and `479-479` (the comment above the created generation) for `CURRENT_GENERATION`; both ranges were widened to the declarations they name (`456-469`, `479-482`). (b) The composition row cited `372-372` (the comment above generation 6's append) for `_compose_generation_6`; the range was widened to `372-387`, which reaches the `def` at `375`, its `base=GENERATION_5` body and the `GENERATION_6 = _compose_generation_6()` record the claim's second half names. Claims, anchors and the other ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `descends_from` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:276-299. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_the_registered_generation_appends_the_six_tables_to_the_generation_it_descends_from" repointed to mcp/tests/test_knowledge_family_composition.py:376-376. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `GENERATION_6_SCHEMA_NAME` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:223-223. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `GENERATION_6_SCHEMA_NAME` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 1 claim(s) here (1 x citation_claim_reopened). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `GENERATION_6_SCHEMA_NAME` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:20:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **split this card out of a union I had written against the wrong module, and renumbered every generation reference.** The post-sync merge had left the composition half merged into `schema_v5.py.md`, which is a sibling leaf's citation-binding generation; the code side renumbered this leaf's append to **generation 6** descending from `GENERATION_5`, so the composition half belongs to `schema_v6.py` and `schema_v5.py.md` was restored to its own card verbatim. The card states that **generation 6 is a strict append** — six tables on top of generation 5's twenty-two, no `ALTER TABLE`, generations 1–5 byte-identical, `descends_from(GENERATION_6, GENERATION_5, GENERATION_5.tables)` the published predicate, 28 tables in the created store — and that **the renumber moved only a module name, a constant, a schema name and a base argument, never the append's content**, which is the property `_append_generation` exists to give. It records the two SQLite subtleties found by executing the DDL: **an index may not carry a table's name** (hence `family_composition_policy_version_edge`), and **a table `UNIQUE` over a nullable column does not enforce uniqueness for `NULL`s** (hence two partial unique indexes over the nullable `policy_id`). It records why the revision-altitude route is a new table rather than a column on generation 2's identity-level join, why the explanatory context is a family-specific immutable record and not the general mutable `explanation` facet, and why the policy is its own version set rather than a nullable column pair. Verification metadata is the merged base commit `15fe8678`: the code commit for this leaf's own diff does not exist yet and closeout owns that stamp.
