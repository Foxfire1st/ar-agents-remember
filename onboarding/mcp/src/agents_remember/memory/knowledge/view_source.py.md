# mcp/src/agents_remember/memory/knowledge/view_source.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/view_source.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T17:15+02:00 |
| lastVerifiedCommitHash | `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
| lastVerifiedCommitDate | 2026-09-20T12:31:16+02:00|
| reviewedWorkingCandidate | candidate `ar/260915-ks-l41-ar`, uncommitted; base `756c47b37fa16324a836a44336655413d10fffaa` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The reader port's implementation and the only place a view's data comes from: `StoreViewReader` reads
the envelope table and the revision table the `KS-R10@v1` generation pair owns, reads generation 1's
own entities by their own statements, decodes every stored payload through the shipped typed-JSON
decoder, and hands the view layer flat `ViewSourceRow` values beside the two registered totals and the
anchor-resolution state. **It deliberately has no selection, no ordering and no classification** — that
division is the contract, and the reason is stated in its own docstring: `application/knowledge_views`
owns what a view selects and `application/knowledge_view_render` owns how it orders it, every one of
those decisions carrying a provenance class there, so an order imposed at this layer would have no
class and gap A-G5 would be open one layer lower and harder to see. It also has **no writable handle
and no path of its own**: the connection comes from `open_read_only_database`, so the strongest
statement available to this code is a `SELECT`, and the reader is constructed from an already-open
connection and the snapshot the dataset declares, so it cannot re-open the database at another
revision behind the caller's back.

## Code Commentary

### Logic

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

**One statement per question, with the columns named.** `RECORDS_OF_KIND` is the envelope-and-revision
read: it selects `record_id`, `kind`, `record_schema`, `lifecycle`, `governing_route_id`,
`revision_id`, `payload` and `provenance`, left-joining `record_revision` on the repository and record
keys, and it names its columns rather than selecting a star so a column added by a later generation
cannot silently change what a view reads. `REGISTERED_REALIZATIONS` and `REGISTERED_FAMILIES` are the
two registered totals, each counted from its own table. Generation 1's own entities are read by their
own statements instead of being copied into the envelope: `INVARIANT_REVISIONS` and `FAMILY_REVISIONS`
each left-join their revision table, `FAMILY_MEMBERS` reads the membership rows, and
`REALIZATION_CLAIMS` joins `source_anchor` so a claim arrives with the path, source identity and
locator it attributes. `ATTACHMENTS_OF_ENDPOINT` is one statement for the authored attachments of one
exact endpoint, and its endpoint column is substituted from `ENDPOINT_COLUMNS` — the declared
vocabulary mapping each endpoint kind to the column it populates — so no string a caller supplies can
reach the SQL.

**A statement answers the question it was written for, and the port method is what says which question
that is.** Membership is a generation-1 entity with its own table, and it is not copied into the
envelope, so `family_member_rows` executes `FAMILY_MEMBERS` and not `rows("family_member")`. The
distinction is not stylistic: the generic envelope read answers for `knowledge_record` /
`record_revision` kinds, and asking it for a kind those tables never carry returns **no rows on a
dataset that holds them** — an empty answer a view then reports as `completeWithinDeclaredScope: true`
for a family it never read. `_member_row` builds the row from the statement's own column order, and it
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
it. `_decode_row` decodes the revision payload and raises `ViewReaderError` when the stored value is
not a JSON object, so an unreadable payload cannot arrive at a view as an empty mapping.

**One row builder per recorded shape.** `_invariant_row`, `_family_row`, `_member_row`,
`_realization_row` and `_attachment_row` construct `ViewSourceRow` from the fixed column order their
statement declares: each names its `record_kind` and `record_schema`, fills the envelope fields it has
(`revision_id`, `lifecycle`, `author_ref`) and builds the `payload` mapping from named columns — conditions and
exclusions through `_sequence`, the attachment's payload through the decoded facet object whose
`facet_kind` becomes the row's `record_kind`. `_decode_row` is the envelope path, taking `kind`,
`record_schema`, `record_id`, `revision_id`, `lifecycle`, `governing_route_id` and `author_ref` from
the stored columns and the payload from the decoded revision. `_member_row` is the membership path and
is the one builder whose result carries **no** `change_locus`: which locus a membership row belongs to
is the view's classification decision, and this module classifies nothing.

**Every read is cached, counted and answered as a typed error rather than an empty result.**
`StoreViewReader` keeps a per-key `_cache` for the reader's lifetime — keyed by record kind, by the
invariant, family, membership and realization statements, and by
`attachments:{endpoint_kind}:{endpoint_id}` — so two views built over one reader cannot disagree about
a kind's rows merely because a write landed between them. `_count` reads the single count row and raises `ViewReaderError` when the statement
returns none; `registered_counts` returns the two totals as `ViewSourceCounts`. `attachment_rows`
refuses an unregistered endpoint kind with `ViewReaderError` before it builds a statement, and
`anchor_state` returns `not_requested` when no resolver was supplied or the resolver answers nothing,
raising `ViewReaderError` when the resolver it was built with is not callable.

**Two entry points, and the anchor resolver is passed in rather than resolved here.**
`store_view_reader` builds the reader over an `OpenedKnowledgeStore` and its
`KnowledgeSchemaIdentity`, and `open_view_reader` opens the file read-only and returns the reader
beside the handle to close; both compose the snapshot identically. `resolve_anchor` is an argument
because resolving one needs the read context the application layer owns and this package sits below
that layer, and `__all__` names the six public names this module adds: the two count statements, the
envelope statement, `StoreViewReader` and the two entry points.

### Conventions

This module declares no model of its own: every shape it returns comes from the shipped vocabulary,
`ViewSourceRow` and `ViewSourceCounts` from `models/knowledge/view.py` and `KnowledgeReadSnapshot` from
`models/knowledge/read.py`, so `extra="forbid"` and `frozen=True` reach these rows from the shared base
rather than from a declaration repeated here. Declarations that must agree are one declaration: each
SQL statement is a single module-level constant executed from one place, the endpoint column is looked
up in the imported `ENDPOINT_COLUMNS` mapping instead of being written into a query, and the five
record-schema literals the entity and attachment builders write (`invariant-revision/v1`,
`family-revision/v1`, `family-member/v1`, `realization-claim/v1`, `facet/v1`) are spelled once each in
their own builder.
Vocabularies and ports that belong to another leaf are imported rather than re-declared —
`decode_typed_column` from `records.py`, `dataset_identity` from `logical.py`,
`open_read_only_database` from `connection.py`, `OpenedKnowledgeStore` from `store.py`,
`ENDPOINT_COLUMNS` from `models/knowledge/facet.py`, and `AnchorResolutionState` plus
`KnowledgeReadSnapshot` from `models/knowledge/read.py`. Module-private
helpers carry a leading underscore (`_text`, `_sequence`, `_provenance_author`, `_count`, `_read_kind`
and the six row builders), the six public names are the ones `__all__` lists, and the reader's own
storage is a single private `_cache` keyed by what was read rather than a second index of the store.

### Invariants And Boundaries

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
- **An unanswerable read is raised, not absorbed.** `ViewReaderError` covers an unregistered endpoint
  kind, a stored payload that is not a JSON object, a count statement that returned no row and a
  resolver that is not callable, because an empty result and an unreadable input are different facts.
- **No author is invented.** `_provenance_author` returns `None` for a row with no recorded actor
  instead of a default, so "nobody recorded this" never renders as "someone did".
- **No caller text reaches SQL.** The attachment statement's endpoint column is chosen from
  `ENDPOINT_COLUMNS`, and an endpoint kind outside that vocabulary is refused before a statement is
  built, so the one substituted token in this file is never caller text.
- **The reader owns no table and no generation rule.** It reads `knowledge_record`, `record_revision`
  and generation 1's own entity tables exactly as they are declared elsewhere; the envelope and
  revision pair is generation 2's appended structure, declared in `schema_v2.py` and not restated here.
- **One declared statement has exactly one caller, and it is the port method written for it.**
  `FAMILY_MEMBERS` is a module-level statement that `__all__` does not list; it is executed from
  `StoreViewReader.family_member_rows` and from nowhere else, and `family_member_rows` is the port method
  that makes the family view's membership read possible at all. The two travels together: the statement
  is the read, the method is the question, and a caller that reaches for the generic envelope read
  instead gets an empty answer the statement would not have given.
- **Membership is read from its own table, never through the envelope.** `family_member` is a
  generation-1 entity like `family` and `invariant`; it is not duplicated into
  `knowledge_record`/`record_revision`, so `rows("family_member")` answers "no rows" on a dataset that
  holds membership. The port declares `family_member_rows` so that read is a typed method call rather
  than a string a caller can spell wrong, and `_member_row` is the only row builder for that statement.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The reader answers a port declared one layer up and feeds a view layer that decides everything this
module refuses to decide; the tables it reads are declared by generations it does not own. The rows
below cite the reader's statements, builders and entry points, the vocabulary it imports rather than
re-declares, and the layer where selection, ordering and provenance classification actually happen.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reader's own statement of its division of labour: recorded rows out, no selection, no ordering and no classification, because every such decision carries a provenance class one layer up. | `ViewSourceRow` | mcp/src/agents_remember/memory/knowledge/view_source.py:1-21 |
| The read-only handle this module opens through, with the read-only APSW flag and the busy timeout it does set. | `open_read_only_database` | mcp/src/agents_remember/memory/knowledge/view_source.py:14-17; mcp/src/agents_remember/memory/knowledge/connection.py:52-63 |
| The snapshot composed from the dataset's own identity rather than a caller's assertion. | `dataset_identity`; `KnowledgeReadSnapshot` | mcp/src/agents_remember/memory/knowledge/view_source.py:19-20; mcp/src/agents_remember/memory/knowledge/logical.py:153-175; mcp/src/agents_remember/models/knowledge/read.py:291-297 |
| The envelope-and-revision read, with its columns named rather than selected by a star so a later column cannot change what a view sees. | `RECORDS_OF_KIND` | mcp/src/agents_remember/memory/knowledge/view_source.py:48-59 |
| The two registered totals, each counted from its own table and returned as one counts value. | `REGISTERED_REALIZATIONS`; `REGISTERED_FAMILIES` | mcp/src/agents_remember/memory/knowledge/view_source.py:61-63; mcp/src/agents_remember/memory/knowledge/view_source.py:64-64 |
| Generation 1's own entities read by their own statements instead of being copied into the envelope. | `INVARIANT_REVISIONS`; `FAMILY_REVISIONS` | mcp/src/agents_remember/memory/knowledge/view_source.py:65-88 |
| The family-membership read: its own statement, executed from its own port method, with the comment recording why the generic envelope read could not answer it. | `FAMILY_MEMBERS`; `family_member_rows` | mcp/src/agents_remember/memory/knowledge/view_source.py:91-99; mcp/src/agents_remember/memory/knowledge/view_source.py:235-248; mcp/src/agents_remember/memory/knowledge/view_source.py:333-351 |
| The realization-claim read and the source anchor it joins, so a claim arrives with the location it attributes. | `REALIZATION_CLAIMS` | mcp/src/agents_remember/memory/knowledge/view_source.py:95-102 |
| The attachment read, whose endpoint column is chosen from the declared vocabulary instead of being interpolated from caller text. | `ENDPOINT_COLUMNS`; `ATTACHMENTS_OF_ENDPOINT` | mcp/src/agents_remember/models/knowledge/facet.py:300-305; mcp/src/agents_remember/memory/knowledge/view_source.py:105-118 |
| The typed-JSON decoding and the never-defaulted author lookup every stored payload passes through. | `_sequence`; `_provenance_author`; `decode_typed_column` | mcp/src/agents_remember/memory/knowledge/view_source.py:126-151; mcp/src/agents_remember/memory/knowledge/records.py:64-67 |
| The reader class, built from an already-open connection and the declared snapshot, holding no path of its own, and the port it answers — including the membership method the protocol declares so a caller cannot reach for the envelope kind by name. | `StoreViewReader`; `KnowledgeViewReader`; `family_member_rows` | mcp/src/agents_remember/memory/knowledge/view_source.py:154-173; mcp/src/agents_remember/models/knowledge/view.py:1068-1114; mcp/src/agents_remember/models/knowledge/view.py:1101-1110 |
| The snapshot accessor, the registered counts and the per-kind read with its lifetime cache. | `snapshot`; `registered_counts`; `rows`; `_cache` | mcp/src/agents_remember/memory/knowledge/view_source.py:175-197 |
| The entity row readers and the attachment read, plus the count helper that refuses an empty count result. | `invariant_rows`; `family_rows`; `realization_rows`; `attachment_rows`; `_count` | mcp/src/agents_remember/memory/knowledge/view_source.py:205-213; mcp/src/agents_remember/memory/knowledge/view_source.py:215-223; mcp/src/agents_remember/memory/knowledge/view_source.py:225-233; mcp/src/agents_remember/memory/knowledge/view_source.py:250-265; mcp/src/agents_remember/memory/knowledge/view_source.py:287-290 |
| The anchor-state answer: not-requested when there is no resolver, a typed error when the resolver is not callable. | `anchor_state`; `ViewReaderError` | mcp/src/agents_remember/memory/knowledge/view_source.py:267-283; mcp/src/agents_remember/models/knowledge/view.py:165-171; mcp/src/agents_remember/models/knowledge/view.py:771-771 |
| The row builders, each naming its record kind and schema and building its payload from named columns. | `_invariant_row`; `_family_row`; `_member_row`; `_realization_row`; `_attachment_row`; `_decode_row` | mcp/src/agents_remember/memory/knowledge/view_source.py:298-315; mcp/src/agents_remember/memory/knowledge/view_source.py:317-331; mcp/src/agents_remember/memory/knowledge/view_source.py:333-351; mcp/src/agents_remember/memory/knowledge/view_source.py:353-372; mcp/src/agents_remember/memory/knowledge/view_source.py:374-384; mcp/src/agents_remember/memory/knowledge/view_source.py:386-402 |
| Both entry points, with the anchor resolver passed in rather than resolved at this layer. | `store_view_reader`; `open_view_reader` | mcp/src/agents_remember/memory/knowledge/view_source.py:405-428; mcp/src/agents_remember/memory/knowledge/view_source.py:431-455 |
| Where selection and ordering actually live, with an unclassifiable value withheld rather than defaulted. | `order_candidates` | mcp/src/agents_remember/application/knowledge_view_render.py:278-313 |
| The envelope and revision tables generation 2 appends, and the opened store the reader is built over. | `APPENDED_TABLES`; `OpenedKnowledgeStore` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:42-49; mcp/src/agents_remember/memory/knowledge/store.py:95-103 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The reader reads one local database at one
path through a read-only handle, every identity it returns is a store-local row identity or a declared
vocabulary member, and nothing here reaches another repository, another dataset or a remote.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T05:24+02:00 — 260915-KS-L41 curator (uncommitted change set on `ar/260915-ks-l41-ar`, code base `756c47b3` at this leaf's cut and `f79f4db745ad00b908d6ce4871d0b4ab2320207c` after the L39 sync, memory base `da33325c` at the cut and `37d0787571bfbf92890049ee0614fa159012be39` after it): **body update for the membership read this leaf makes real, and the invariant this card stated backwards.** The card's own Invariants list said `FAMILY_MEMBERS` was "a module-level statement that `__all__` does not list and that no module or test in the shipped candidate references besides its own definition, so the family-membership read this leaf declares has no caller yet." That was true when it was written and is false now: L41 gave the statement its caller — `StoreViewReader.family_member_rows` (`memory/knowledge/view_source.py:235-248`) — and `_member_row` (`:333-351`) is the one row builder for it. The Invariants entries now say that, the Logic section gained a paragraph stating why the membership read is a port method rather than `rows("family_member")` (the envelope tables never carried the kind, so the named-kind read answered "no rows" on a dataset holding membership and the family view reported a guarantee, no members, no locations and a complete answer), the row-builder and cache paragraphs now name `_member_row` and the membership statement key, and the Conventions section counts six row builders and five record-schema literals rather than five and four. The reference table's membership row now cites the statement, the method and the builder, and its reader row carries the protocol method the port declares. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained as recorded — the candidate is uncommitted and the governed closeout owns the real stamp — and the superseded `ar/260915-ks-l20` candidate row is replaced by the `reviewedWorkingCandidate` row above, because two candidate rows for one card cannot both stand and no stamp was advanced or invented.
- 2026-09-19T17:15+02:00 — 260915-KS-L28 curator (uncommitted change set on `ar/260915-ks-l28`, base `497d9e9f`): M1-4 anchor repair, re-read against the code worktree at `e7998504`. Three rows were wrong. The attachment row had the two names and their modules swapped: the statement `ATTACHMENTS_OF_ENDPOINT` lives in this module at `:105-118` and the declared `ENDPOINT_COLUMNS` tuple lives in `models/knowledge/facet.py:300-305`, and the citations now follow the anchors' order. `KnowledgeViewReader` was cited at `models/knowledge/view.py:862-881`, which is `ReviewMatrixRow`; the protocol is at `:1032-1067`. `ViewReaderError` was cited at `models/knowledge/view.py:152-158`, which is the ordering-provenance rule; the class is at `:160-166`. Every other row was re-checked and stands (`ViewSourceRow` in the docstring range and `_cache` in the constructor range are deliberate mention anchors). No claim was deleted or softened. The stamp is unchanged because `d0c1d1cf`'s content for this file is byte-identical to `e7998504` (`git diff d0c1d1cf HEAD` is empty).- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): created this one-to-one card for the reader port's implementation. It records the division of labour that is the module's contract — envelope and revision rows out, no selection, no ordering and no classification, because those decisions carry their provenance class in the view layer — together with the read-only handle `open_read_only_database` gives, the snapshot resolved from the dataset's own identity rather than asserted, the eight SQL constants with the one substituted endpoint column taken from the declared vocabulary, the typed-JSON decoding, the per-kind row builders and the two entry points that pass the anchor resolver in. It also records the deliberate absences: no writable statement, no path of its own, no derived author, and the declared-but-uncalled family-membership statement. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
