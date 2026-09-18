# mcp/src/agents_remember/memory/knowledge/schema_v9.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/schema_v9.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate |  2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

**The append is one tuple and one protocol, not a second schema.** `APPENDED_TABLES` names exactly the
six tables in the order the encoder serializes them, and it is the only place the generation's table set
is spelled. `schema_generations._append_generation` reads it together with `APPENDED_COLUMNS`,
`APPENDED_PRIMARY_KEYS`, `APPENDED_JSON_COLUMNS`, `APPENDED_FEATURES`, `APPENDED_TABLE_DDL`,
`APPENDED_INDEX_DDL` and `APPENDED_TRIGGERS` — the eight names `_AppendedGeneration` declares — and
composes generation 9 as `base.tables + appended.APPENDED_TABLES`, `{**base.columns, **appended.…}` for
the four mappings, and `base.index_ddl + appended.APPENDED_INDEX_DDL`, so every earlier declaration
survives by construction. **The number is the composition's, not this module's**: the file declares no
`GENERATION_N` constant and no schema-name string of its own, which is what lets a parallel leaf that
must renumber change a name and a base argument rather than re-derive an append.

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
are the composition contract `_AppendedGeneration` reads, the `CENSUS_*` tuples are the vocabularies,
and the three private helpers (`_vocabulary_closes`, `_record_table_ddl`, `_claim_parent`) exist only to
render the DDL mapping and are never imported elsewhere. The DDL text is written so the leading key
column is spelled exactly once — `key_columns.split(",", maxsplit=1)[0].strip()` — with the comment
stating why, and the primary key line reuses the same `key_columns` string, so a single-column key and a
composite key take the identical code path. `__all__` is absent, as in every other generation module:
the eight `APPENDED_*` names are the published surface by convention, and nothing here is renamed or
re-exported.

### Invariants And Boundaries

- **Append-only, and the append is the only sanctioned way to add a table.** Generation 9's tables follow
  generation 8's exactly, every earlier name keeps the exact column tuple, primary key and typed-JSON
  set it declared, and no `ALTER TABLE` against an earlier generation's table appears in the module — the
  rule is `KS-R10@v1` §1.3's, and `schema_generations.descends_from` is its one predicate.
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
- **This module holds no generation number and no schema name.** The number, the schema-name string and
  the base argument live in `schema_generations.__compose_generation_9`, so the append's content is the
  only thing this file owns.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows below ground the card's claims in the declarations themselves: the six appended tables and the
eight names the composition reads, the declared columns, keys, typed-JSON sets, vocabularies, DDL
rendering and triggers, and the composition function in the registry that turns this module's literals
into generation 9.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what it appends and why: six tables, an additive-only file, and the refusal of a wide row because each census entry is a record kind with its own identity. | `APPENDED_TABLES` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:1-53; mcp/src/agents_remember/memory/knowledge/schema_v9.py:61-68 |
| The six tables generation 9 appends, in the order the encoder serializes them, appended after generation 8's thirty-four. | `APPENDED_TABLES`; `GENERATION_9` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:59-68; mcp/src/agents_remember/memory/knowledge/schema_generations.py:433-450 |
| The declared column order of each appended table, which is what the encoder orders rows by and what the record group's INSERT statements are written against. | `APPENDED_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:117-173 |
| The declared primary keys: one identity column per record table, and a relation keyed by its whole recorded content so re-recording one relation is one row. | `APPENDED_PRIMARY_KEYS` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:175-190 |
| The typed-JSON columns: provenance in all six tables and the exact unparsed content on the inventory row, held as a document so a reader can compare it byte for byte with the artifact. | `APPENDED_JSON_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:192-204 |
| The closed vocabularies the DDL constrains, with the three dispositions a curator's authored assessment may record and the reason that column is the nullable one. | `CENSUS_ARTIFACT_KINDS`; `CENSUS_PARSE_OUTCOMES`; `CENSUS_INVENTORY_STATES`; `CENSUS_CLAIM_KINDS`; `CENSUS_APPLICABILITY`; `CENSUS_DISPOSITION_KINDS`; `CENSUS_DISPOSITION_STATES`; `CENSUS_EVIDENCE_STATES`; `CENSUS_ASSESSMENT_DISPOSITIONS`; `CENSUS_REALIZATION_STATES`; `CENSUS_LINK_KINDS`; `CENSUS_TARGET_STATES` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:70-115 |
| Which column of which table is closed by which vocabulary, so a value added to a vocabulary is a value the schema already admits. | `_VOCABULARY_CHECKS`; `_vocabulary_closes` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:206-242 |
| The one DDL renderer: key, body, not-null provenance, declared primary key, vocabulary closes, repository foreign key and optional parent edge, closed `STRICT`. | `_record_table_ddl` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:245-264 |
| The composite parent edge the two claim relations declare, plus the disposition link's own parent edge written inline at its table, and the DDL mapping both are rendered through. | `_claim_parent`; `APPENDED_TABLE_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:267-274; mcp/src/agents_remember/memory/knowledge/schema_v9.py:277-332; mcp/src/agents_remember/memory/knowledge/schema_v9.py:305-327 |
| The six rendered table declarations, each naming its own key columns and body. | `APPENDED_TABLE_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:277-327 |
| The seven declared indexes, each covering the reverse direction of a declared lookup rather than a forward scan. | `APPENDED_INDEX_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:329-343 |
| The trigger pair every appended table gets, with the reason nothing is exempt: a census row has no lifecycle field a later operation is entitled to move. | `APPENDED_TRIGGERS` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:345-361 |
| The declared-empty feature tuple, present so this generation states the same fact its predecessor does. | `APPENDED_FEATURES` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:363-368 |
| The composition function that turns this module's literals into generation 9, as generation 8 with one module's declarations appended. | `_compose_generation_9`; `_append_generation`; `_AppendedGeneration` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:439-450; mcp/src/agents_remember/memory/knowledge/schema_generations.py:243-270; mcp/src/agents_remember/memory/knowledge/schema_generations.py:98-113 |
| Generation 9's own identity in the registry, and the created generation a new store declares. | `GENERATION_9_SCHEMA_NAME`; `GENERATIONS`; `CURRENT_GENERATION` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:226-226; mcp/src/agents_remember/memory/knowledge/schema_generations.py:452-466; mcp/src/agents_remember/memory/knowledge/schema_generations.py:479-482 |
| The additive rule as one predicate — the appended tables follow the base's exactly and every earlier name keeps its column tuple, its primary key and its typed-JSON set — and the composition commentary that spells the rule out as a generation appending tables and never retyping, reordering or dropping an earlier generation's, with each successor's own composer beside it. | `descends_from`; `_compose_generation_5`; `_compose_generation_9` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:273-296; mcp/src/agents_remember/memory/knowledge/schema_generations.py:341-346; mcp/src/agents_remember/memory/knowledge/schema_generations.py:347-358; mcp/src/agents_remember/memory/knowledge/schema_generations.py:435-452 |
| Where the census record kinds and their relations are registered as payload shapes, which is why this generation appends relations rather than a wide table. | `CENSUS_PAYLOAD_MODELS`; `PAYLOAD_MODELS` | mcp/src/agents_remember/models/knowledge/census.py:339-350; mcp/src/agents_remember/memory/knowledge/record_envelope.py:172-187 |
| Where the write path takes its column order and its vocabulary closes from, so a column added to a table without a statement is a storage error rather than a mis-ordered write. | `_inventory_columns`; `_decode_closed` | mcp/src/agents_remember/memory/knowledge/census_records.py:163-183; mcp/src/agents_remember/memory/knowledge/census_records.py:186-200 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The module declares SQLite DDL text, column
tuples, primary keys, typed-JSON sets and trigger bodies for one local database schema; every name it
references is another declaration in the same package or a table of the same dataset, and nothing here
reaches another repository, another dataset or a remote.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T19:56:45+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the one enforced `citation_anchor_absent_from_range` row in this document.** The generation-9 identity row cited `schema_generations.py:476-479` (the `GENERATIONS_BY_KEY` mapping and the comment above the created generation) for `CURRENT_GENERATION`, which is declared at `482`; the range was widened to `479-482`. The claim, the anchors and the other two ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for generation 9's appended tables. It records the six tables — the census's three record kinds and the three relations they resolve through — the eight `APPENDED_*` names `_AppendedGeneration` reads and `_append_generation` composes, the declared column orders, the three relation primary keys that make re-recording a relation idempotent, and the twelve trigger names that seal every census observation against update and delete with the reason no table is exempt. It states why the leaf appends three records and three relations rather than one wide table — `KS-R21@v1` §6.2's "a census record kind with its own identity", and an envelope that cannot express a relation — why no census table carries a content-address, logical digest or fingerprint column, and why `observed_doc_type`, `claim_kind` and `applicability` are recorded facts the census's own readers consume. It also records the deliberate absences: no `GENERATION_N` constant and no schema-name string in this module, no `ALTER TABLE` anywhere in the package, and an empty `APPENDED_FEATURES` declared rather than omitted. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
