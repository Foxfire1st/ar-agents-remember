# mcp/src/agents_remember/memory/knowledge/schema_v9.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Generation 9's appended tables: the truth-coverage census's three record kinds — the inventory row, the
assessable claim and the migration disposition — and the three relations they resolve through (a claim's
evidence, a claim's realization attribution, and the records a disposition links to). This module owns
**only what generation 9 appends** and declares no table of an earlier generation, so the additive rule
`KS-R10@v1` §1.3 states is a property of the file rather than of a review: generation 1's ten tables,
generation 2's six, generation 3's four, generation 4's one, generation 5's one, generation 6's six,
generation 7's five and generation 8's one stay declared verbatim in their own modules — this module's
docstring enumerates the first seven of those and generation 8 states the same fact for its own single
appended table — and no `ALTER TABLE` against an earlier generation's table appears anywhere in this
package.
**The reason it appends three records and three relations rather than one wide table** is stated in the
module docstring: `Doc12:49-55` states the census's record list and `KS-R21@v1` §6.2 settles that each
entry is "a **census record kind with its own identity** -- not a column set on one wide table, and not a
report section", while the envelope "carries a kind, an authority home, a lifecycle, a governing route
and one sealed payload, and it cannot express a relation". Keeping the inventory row its own record is
also what lets a surface with **no onboarding** exist in the census at all, "it can have no claim". The
appended manifest is six tables, seven indexes and twelve immutability triggers, and
`APPENDED_FEATURES` is empty because generation 9 needs no SQLite feature generation 8 does not already
require.

## Code Commentary

### Logic

APPENDED_TABLES names the six tables in serialization order. The eight APPENDED_* declarations satisfy schema_generations._AppendedTables. _compose appends this module last after schema.py and schema_v2 through schema_v8, preserving earlier declarations and producing CURRENT_GENERATION. This module has no schema-name string or generation-number constant; there is one supported derived-index schema rather than a registry of openable generations.

**Six tables in one declared column order, and three of the columns are recorded facts rather than
derivations.** Each entry of `APPENDED_COLUMNS` is the exact order the generation's encoder orders rows
by, and `APPENDED_PRIMARY_KEYS` declares the key the DDL declares: the three record tables are keyed by
their single identity column, and every relation is keyed by its **whole recorded content** —
`(repository_id, claim_id, evidence_ref)`, `(repository_id, claim_id, realization_ref)` and
`(repository_id, disposition_id, link_kind, target_ref)` — so "the same fact recorded twice" is one row
rather than two observations and re-running an import at the same baseline is an idempotent insert
instead of a duplicate append. Three columns exist because a reader needs the observed fact:
`census_inventory_row.observed_doc_type` is what the parser **read** off the artifact, so the
cardinality rule that decides which census claim a curator classifies reads a stored value instead of
re-deriving one at read time; `census_claim.claim_kind` admits `unclassified` as a **value of the closed
vocabulary** rather than a NULL a reader could take for "not yet read"; and `census_claim.applicability`
is the field the eligibility rule reads, so the accounting `N = T + F + U + P` is taken over the claims
recorded `assessable` while a piece recorded `historical_non_applicable` carries its disposition without
entering `N`.

**The DDL is rendered from the same declarations the constraints are.** `_record_table_ddl` writes each
table's `repository_id`, its leading key column once whether the key is single or composite, the body,
the not-null `provenance` column, the declared `PRIMARY KEY`, the vocabulary closes, the repository
foreign key and any parent edge, and closes the statement `STRICT`. `_vocabulary_closes` renders one
`CHECK (column IN (...))` line per entry of `_VOCABULARY_CHECKS` from the module-level vocabulary tuples,
so a value added to a vocabulary is a value the DDL already admits and the two cannot drift into
different sets of admitted values. `_claim_parent` returns the composite `(repository_id, claim_id)`
edge the two claim relations declare, and the disposition link declares its own
`(repository_id, disposition_id)` parent inline; all three are `ON DELETE NO ACTION DEFERRABLE
INITIALLY DEFERRED`, so a relation cannot outlive or precede the record it resolves. `provenance` is the
typed-JSON column on the shipped idiom in all six tables, and `unparsed_content` is the deliberate second
one on the inventory row, held as a document "so that a reader can compare it byte for byte with the
artifact instead of matching against a re-escaped string".

**No census table carries an identity authority of its own, and that is a property of the declared
columns.** The docstring states it directly — the census records carry "**no content-address, no logical
digest and no fingerprint column**", and none is added here — and the reason is stated with it: "no
second identity authority" is a property of the declared columns, and the content digest stays on
`record_revision`, where the envelope puts it. What `knowledge_record` and `record_revision` already
carry (the kind, the governing route, the record schema, the authorship, the frozen payload and its
digest) is not restated as a column here either, because that "would be a second declaration of one
fact"; the census tables hold the census's own observed fields and nothing the envelope already holds.

**Sealed against update and delete by the same trigger idiom the earlier generations use.**
`APPENDED_TRIGGERS` is built by two comprehensions over `APPENDED_TABLES` — `{table}_no_update` and
`{table}_no_delete` — each a `BEFORE UPDATE`/`BEFORE DELETE` trigger whose body is
`SELECT RAISE(ABORT, 'immutable_census_row: …')`, so "a census observation is never rewritten in place"
is a property of the schema rather than a rule the write path remembers. The comment beside the mapping
records why nothing is exempt: "unlike a citation binding, a census row has no lifecycle field a later
operation is entitled to move". `APPENDED_INDEX_DDL` declares seven indexes, each covering the reverse
direction of a declared lookup — outcome and source route on the inventory row, claim kind and
applicability on the claim, evidence and realization reference on the two claim relations, and target
reference on the disposition link — so "which claims cite this evidence", "which dispositions point at
this record" and the parse census's outcome report do not walk a whole table.

### Conventions

The module is declaration-only: it imports one name (`Mapping` from `collections.abc`, used by four
annotations) and **executes nothing but literals and comprehensions** — there is no database handle, no
`import apsw`, no I/O and no `GENERATION_N` constant of its own. The vocabulary tuples are the single
declaration for two consumers each: `_vocabulary_closes` renders them into `CHECK ... IN` lines here,
and `census_records` imports the same tuples to decode a stored value against the vocabulary its own
`CHECK` enforces, while `memory/migration/parse.py` and `memory/migration/inventory.py` assert their own
closed vocabularies are subsets of these at import. Names are split by role: the `APPENDED_*` mappings
are the composition contract `_AppendedTables` reads, the `CENSUS_*` tuples are the vocabularies,
and the three private helpers (`_vocabulary_closes`, `_record_table_ddl`, `_claim_parent`) exist only to
render the DDL mapping and are never imported elsewhere. The DDL text is written so the leading key
column is spelled exactly once — `key_columns.split(",", maxsplit=1)[0].strip()` — with the comment
stating why, and the primary key line reuses the same `key_columns` string, so a single-column key and a
composite key take the identical code path. `__all__` is absent, as in every other generation module:
the eight `APPENDED_*` names are the published surface by convention, and nothing here is renamed or
re-exported.

### Invariants And Boundaries

- Earlier table definitions are preserved by the one ordered schema composition. _compose adds these declarations after the earlier modules, and require_pinned_schema_unchanged verifies the complete structural fingerprint. The former descends_from predicate and generation registry were retired with the canonical database.
- **No second identity authority.** There is no content-address, logical digest or fingerprint column on
  any of the six tables, and the content digest stays on `record_revision`; identity is the declared
  primary key and nothing else.
- **A relation is keyed by its whole recorded content.** The three relation keys include every recorded
  column, so re-recording the same relation is one row, and each relation declares a deferred foreign key
  to the record it belongs to.
- **A census observation cannot be rewritten or dropped.** Every table carries a `no_update` and a
  `no_delete` trigger raising `immutable_census_row`, and no table is exempt because a census row has no
  lifecycle field a later operation is entitled to move.
- **The schema refuses what it can so the write path is not the only guard.** Every closed vocabulary is
  a `CHECK ... IN` rendered from the one declaration the payload models also use, and
  `assessment_disposition` is the one nullable closed column, because an absent value is the unassessed
  state rather than a fourth disposition.
- **What the envelope already carries is not restated.** The kind, the authority home, the lifecycle, the
  governing route, the record schema, the authored provenance, the payload and its digest are columns of
  `knowledge_record` and `record_revision`, not of a census table.
- **Generation 9 requires no new SQLite feature.** `APPENDED_FEATURES` is the empty tuple declared rather
  than omitted, because checked vocabularies, composite foreign-key groups, indexes and trigger aborts
  are all covered by what generation 8 already declares.
- This module holds no schema name or number. SCHEMA_NAME, SCHEMA_USER_VERSION and CURRENT_GENERATION identify the one derived-index schema in schema_generations.py; _compose consumes this module as its final appended block.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The rows below ground the card's claims in the declarations themselves: the six appended tables and the
eight names the composition reads, the declared columns, keys, typed-JSON sets, vocabularies, DDL
rendering and triggers, and the composition function in the registry that turns this module's literals
into generation 9.

- The module's own statement of what it appends and why: six tables, an additive-only file, and the refusal of a wide row because each census entry is a record kind with its own identity. [1]

- The ordered appended declarations compose into the one pinned derived-index schema. [2]

- The declared column order of each appended table, which is what the encoder orders rows by and what the record group's INSERT statements are written against. [3]
- The declared primary keys: one identity column per record table, and a relation keyed by its whole recorded content so re-recording one relation is one row. [4]
- The typed-JSON columns: provenance in all six tables and the exact unparsed content on the inventory row, held as a document so a reader can compare it byte for byte with the artifact. [5]
- The closed vocabularies the DDL constrains, with the three dispositions a curator's authored assessment may record and the reason that column is the nullable one. [6]
- Which column of which table is closed by which vocabulary, so a value added to a vocabulary is a value the schema already admits. [7]
- The one DDL renderer: key, body, not-null provenance, declared primary key, vocabulary closes, repository foreign key and optional parent edge, closed `STRICT`. [8]
- The composite parent edge the two claim relations declare, plus the disposition link's own parent edge written inline at its table, and the DDL mapping both are rendered through. [9]
- The six rendered table declarations, each naming its own key columns and body. [10]
- The seven declared indexes, each covering the reverse direction of a declared lookup rather than a forward scan. [11]
- The trigger pair every appended table gets, with the reason nothing is exempt: a census row has no lifecycle field a later operation is entitled to move. [12]
- The declared-empty feature tuple, present so this generation states the same fact its predecessor does. [13]

- The ordered appended declarations compose into the one pinned derived-index schema. [14]


- This build creates and reads the single v9 derived-index schema; another declared database version is refused. [15]


- The ordered appended declarations compose into the one pinned derived-index schema. [16]


### Cross-Repo References

No cross-repository behavior is implemented in this file. The module declares SQLite DDL text, column
tuples, primary keys, typed-JSON sets and trigger bodies for one local database schema; every name it
references is another declaration in the same package or a table of the same dataset, and nothing here
reaches another repository, another dataset or a remote.

No meaningful cross-repo references found.
