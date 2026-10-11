# mcp/src/agents_remember/memory/knowledge/view_source.py

## Governing Overview


[memory route overview](../overview.md)

## Purpose


Provides the read-only StoreViewReader port over a selected index snapshot.

## Code Commentary


The reader projects typed invariant/family/revision/member/realization values and provenance from the supplied connection and snapshot. `open_view_reader` opens that snapshot read-only and returns the handle and reader; the caller owns closing the handle. The former store_view_reader(OpenedKnowledgeStore) bridge is removed. This read port neither selects a substitute canonical store nor admits mutations.

**Recorded rows out, and no decision taken.** The module's docstring states the division in one
sentence — the reader "performs **no** selection, **no** ordering and **no** classification" — and
names the consequence: `application/knowledge_views` owns what a view selects and how it orders it,
and each of those decisions carries a provenance class there, so an ordering introduced in this file
would be an unclassified one. The statements here therefore filter on exactly the values that address
a row — the bound `repository_id` and, for one kind, the `kind` itself — and each returns rows in the
store's own recorded order, which is what `rows` calls "recorded order" and what the view layer then
re-orders on one admitted input through `order_candidates`, withholding what it cannot classify
rather than falling back to a database order.

**Read-only by handle, not by discipline.** `open_view_reader` opens the database through
`open_read_only_database`, which constructs the APSW connection with `apsw.SQLITE_OPEN_READONLY` and
sets only the busy timeout — the read-only flag, not a convention, is what makes a refused view leave
the dataset byte-identical instead of relying on a rollback somebody remembers. The function returns
the reader together with the raw connection, deliberately: the caller owns the connection's lifetime,
so this module cannot leak one and a caller cannot forget that it opened something;
`application/knowledge_views` closes it in a `finally` beside the call. `StoreViewReader` holds the
already-open connection, the repository id and the snapshot, and no path at all.

**The snapshot is resolved from the dataset, never asserted.** Both entry points compose
`KnowledgeReadSnapshot` from facts they read rather than facts a caller supplies: the store's
`repository_id`, the schema name the store was opened as (`identity.schema_name`), the logical digest
returned by `dataset_identity(database_path)` — which opens the file read-only, selects the generation
the dataset declares, validates the bound namespace and returns the identity those two facts scope —
and the schema identity's own `fingerprint` as the context digest. `snapshot()` returns exactly that
value, so a view cannot be handed a snapshot the reader did not read.

**One statement per question, with the columns named.** The envelope tables are gone, so there is no generic envelope read: each question has its own statement naming its columns rather than selecting a star, so a column added later cannot silently change what a view reads. `REGISTERED_REALIZATIONS` and `REGISTERED_FAMILIES` are the
two registered totals, each counted from its own table. Generation 1's own entities are read by their
own statements instead of being copied into the envelope: `INVARIANT_REVISIONS` and `FAMILY_REVISIONS`
each left-join their revision table, `FAMILY_MEMBERS` reads the membership rows, and
`REALIZATION_CLAIMS` joins `source_anchor` so a claim arrives with the path, source identity and
locator it attributes. The attachment statement is deleted with the facet tables: no authored-attachment read remains.

**A statement answers the question it was written for, and the port method is what says which question
that is.** Membership is a recorded entity with its own table, so `family_member_rows` executes `FAMILY_MEMBERS` and nothing else. `_member_row` builds the row from the statement's own column order, and it
keeps only what was recorded: the two ids travel in the payload under the names the view layer reads
(`family_revision_id`, `invariant_revision_id`), the row kind and schema are `family_member` and
`family-member/v1`, and the `change_locus` a view puts on such a row is the *view's* decision — this
module performs no selection and no classification, so it does not choose one here. The member row is
cached under its own statement key like every other read, so two views over one reader cannot disagree
about a family's membership because a write landed between them.

**Typed JSON is decoded through the shipped decoder, and nothing is defaulted.** `_sequence` turns a
recorded list column into a tuple of strings through `decode_typed_column`, returning the empty tuple
for null; `_text` renders one scalar as text or `None`; `_provenance_author` decodes a stored
provenance envelope, reads its `actor_ref` mapping entry and returns `None` when the row carries no
author — never a default, because the point of an authored classification is that a named actor wrote
it. The builders decode typed columns inline (`_text`/`_sequence`); the shared `_decode_row` envelope path and its not-a-JSON-object refusal are deleted with the envelope tables.

**One row builder per recorded shape.** `_invariant_row`, `_family_row`, `_member_row` and
`_realization_row` construct `ViewSourceRow` from the fixed column order their
statement declares: each names its `record_kind` and `record_schema`, fills the fields it has
(`revision_id`, `lifecycle`, `author_ref`) and builds the `payload` mapping from named columns — conditions and
exclusions through `_sequence`. The attachment builder is deleted with the facet tables. `_member_row` is the membership path and
is the one builder whose result carries **no** `change_locus`: which locus a membership row belongs to
is the view's classification decision, and this module classifies nothing.

**Every read is cached, counted and answered as a typed error rather than an empty result.**
`StoreViewReader` keeps a per-key `_cache` for the reader's lifetime — keyed by the
invariant, family, membership and realization statements — so two views built over one reader cannot disagree about
a kind's rows merely because a write landed between them. `_count` reads the single count row and raises `ViewReaderError` when the statement
returns none; `registered_counts` returns the two totals as `ViewSourceCounts`.
`anchor_state` returns `not_requested` when no resolver was supplied or the resolver answers nothing,
raising `ViewReaderError` when the resolver it was built with is not callable.

This module declares no model of its own: every shape it returns comes from the shipped vocabulary,
`ViewSourceRow` and `ViewSourceCounts` from `models/knowledge/view.py` and `KnowledgeReadSnapshot` from
`models/knowledge/read.py`, so `extra="forbid"` and `frozen=True` reach these rows from the shared base
rather than from a declaration repeated here. Declarations that must agree are one declaration: each
SQL statement is a single module-level constant executed from one place, and the four
record-schema literals the entity builders write (`invariant-revision/v1`,
`family-revision/v1`, `family-member/v1`, `realization-claim/v1`) are spelled once each in
their own builder.

- **This module selects nothing, orders nothing and classifies nothing.** Its statements filter on the
  bound repository id and the addressed kind or endpoint only, and they return the store's recorded
  order; every ordering a view displays is imposed one layer up with a provenance class, and every row
  this module could not classify is withheld there rather than defaulted here.
- **Read-only by handle.** The connection comes from `open_read_only_database`, which passes
  `apsw.SQLITE_OPEN_READONLY`, so no statement this module runs can write; a refused view leaves the
  dataset byte-identical as a property of the handle, and the caller owns closing it.
- **The snapshot is resolved, never asserted.** Both entry points build `KnowledgeReadSnapshot` from
  `dataset_identity(...).logical_digest`, the inspected schema identity and the store's own repository
  id, and `snapshot()` returns that composition unchanged; no caller-supplied snapshot is accepted.
- **No path is held and no second connection is opened.** `StoreViewReader` is constructed from an
  already-open connection, the repository id and the snapshot, so it cannot re-open the database at
  another revision behind the caller's back.
- **An unanswerable read is raised, not absorbed.** `ViewReaderError` covers
  a stored payload that is not a JSON object, a count statement that returned no row and a
  resolver that is not callable, because an empty result and an unreadable input are different facts.
- **No author is invented.** `_provenance_author` returns `None` for a row with no recorded actor
  instead of a default, so "nobody recorded this" never renders as "someone did".
- **No caller text reaches SQL.** Every statement is a fixed module-level constant with only bound parameters, so no substituted token in this file is ever caller text.
- **The reader owns no table and no generation rule.** It reads the eight logical tables the projection fills, exactly as the single schema module declares them.
- **One declared statement has exactly one caller, and it is the port method written for it.**
  `FAMILY_MEMBERS` is a module-level statement that `__all__` does not list; it is executed from
  `StoreViewReader.family_member_rows` and from nowhere else, and `family_member_rows` is the port method
  that makes the family view's membership read possible at all.
- **Membership is read from its own table.** `family_member` lives in its own table;
  the port declares `family_member_rows` so that read is a typed method call rather
  than a string a caller can spell wrong, and `_member_row` is the only row builder for that statement.

## Evidence


### Repo-Internal References

- `StoreViewReader` owns the current boundary described above. [19]
- `open_view_reader` owns the current boundary described above. [20]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

The reader answers a port declared one layer up and feeds a view layer that decides everything this
module refuses to decide; the tables it reads are the eight logical tables the single schema declares. The rows
below cite the reader's statements, builders and entry points, the vocabulary it imports rather than
re-declares, and the layer where selection, ordering and provenance classification actually happen.

- The reader's own statement of its division of labour: recorded rows out, no selection, no ordering and no classification, because every such decision carries a provenance class one layer up. [21]
- The read-only handle this module opens through, with the read-only APSW flag and the busy timeout it does set. [22]
- The snapshot composed from the dataset's own identity rather than a caller's assertion. [23]
- The per-question statements, each naming its columns rather than selecting by a star so a later column cannot change what a view sees. [24]
- The two registered totals, each counted from its own table and returned as one counts value. [25]
- Each entity read by its own statement: invariant revisions, family revisions, memberships and realization claims. [26]
- The family-membership read: its own statement, executed from its own port method. [27]
- The realization-claim read and the source anchor it joins, so a claim arrives with the location it attributes. [28]
- No attachment read remains: the facet tables are deleted. [29]
- The typed-JSON decoding and the never-defaulted author lookup every stored payload passes through. [30]
- The reader class, built from an already-open connection and the declared snapshot, holding no path of its own, and the port it answers. [31]
- The snapshot accessor, the registered counts and the per-statement read with its lifetime cache. [32]
- The entity row readers plus the count helper that refuses an empty count result. [33]
- The anchor-state answer: not-requested when there is no resolver, a typed error when the resolver is not callable. [34]
- The row builders, each naming its record kind and schema and building its payload from named columns. [35]
- Where selection and ordering actually live, with an unclassifiable value withheld rather than defaulted. [36]
- The eight logical tables the single schema declares. [37]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The reader reads one local database at one
path through a read-only handle, every identity it returns is a store-local row identity or a declared
vocabulary member, and nothing here reaches another repository, another dataset or a remote.

No meaningful cross-repo references found.
