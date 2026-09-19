# mcp/src/agents_remember/memory/knowledge/census_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/census_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T17:15+02:00 |
| lastVerifiedCommitHash |  `562cef4ca64de5b11712d5165d24e78c9a035312`|
| lastVerifiedCommitDate |  2026-09-19T17:51:43+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The row codecs and the in-transaction write step for the truth-coverage census's record group: three
envelope-backed record kinds — an inventory row, an assessable claim and a migration disposition — and
the three relations they resolve through, written as one envelope row, one sealed revision and one
record-table row inside the caller's open transaction. The module states its own division of labour at
the top: the generic `knowledge_record`/`record_revision` codec is **reused** from
`facet_records`, so a stored revision's seal is verified against the one digest definition rather than
a second copy of it, and the payload is validated through the **envelope seam**
(`record_envelope.validate_record_payload`), which is the one place any write path decides whether a
payload is admissible — this module declares the `(kind, record_schema)` triples and nothing else about
admissibility. **It opens no transaction of its own**: the step is an `apply_*` function taking the
caller's already-open `OpenedKnowledgeStore`, because that is how every record group in the package
participates in the batch, and a record group that opened its own would be a second write path. The
read side is here too — one declared `SELECT` per census table, each ordered by its own key, plus the
three per-record digest readers a caller carries an expectation from.

## Code Commentary

### Logic

**One step, one dispatch, and no second write path.** `apply_census_command` is the group's whole write
surface: it requires the generation, then the governing route, then dispatches on the command type to
`_apply_inventory_row`, `_apply_claim` or `_apply_disposition`, and every refusal is **raised** rather
than returned so the transaction carrying a record and its revision aborts whole — a refused command
leaves no envelope row, no revision and no relation behind, and an earlier command's rows in the same
batch roll back with it. The batch reaches it through `batch_commands._apply_family_census`, which is
selected by `CENSUS_COMMAND_KINDS` in the `_APPLY_FAMILIES` table, and the same kind set is checked
before any row exists by `batch_preconditions._census_check` through `_CENSUS_DECLARATIONS`; the module
owns no entry point of its own and no bulk writer beside the batch.

**Two inserts per record, in the destination's declared column order.** `_write_envelope` runs
`EFFECT_RECORD_INSERT` and `EFFECT_REVISION_INSERT` through `store.write`, the second with the store's
repository id prepended to `record_revision_row(...)`'s tuple; `_foundation` supplies both statements
and the values they take, and `RecordRevisionDraft` carries the record id, the revision id and the
declared schema. Column order is load-bearing rather than cosmetic: the revision statement's parameters
follow `schema_v2.APPENDED_COLUMNS["record_revision"]` name for name, so a column added to the
generation without a statement here is a storage error rather than a silently mis-ordered write. The
`_Foundation` dataclass exists so a caller cannot transpose `record_insert` and `revision_insert`, and
`_written_entry` builds the receipt entry through `RecordIdentity.model_construct` — the store computed
every field, so re-validating it would be work without a decision.

**The declared generation is the dataset's own, and an older dataset is refused rather than migrated.**
`REQUIRED_CENSUS_GENERATION` is `schema_generations.CURRENT_GENERATION` (generation 9),
`require_census_generation` compares it with `store.generation.user_version`, returns when the observed
version is at least the required one, and otherwise raises `KnowledgeRefused` with the code
`unsupported_schema` and a `next_action` that says the census is written into a dataset created at the
current generation and that an older dataset "is read through its own generation and is never migrated
in place".

**Reference resolution happens here, in command order, and not in the precondition.** An absent
`governing_route_id` is the explicit ungoverned state and is never refused; a **named** route that does
not exist is a dangling reference and is refused by `_require_governing_route` through
`missing_expected_row_refusal(operation=CENSUS_OPERATION, table="route", record_id=route_id)`, which is
what keeps "slices are keyed by recorded routes" true instead of aspirational. The record's
`authority_home` is inherited from the bound repository's row (`store.get_repository()`) rather than
authored, and a store with no repository row raises `KnowledgeStorageError` instead of writing a null
one. `_admissible` calls the envelope seam for the `(kind, schema)` pair and raises the seam's own
`KnowledgeRefusal` back as `KnowledgeRefused`, so an unregistered kind or an undeclared payload field is
the shipped `invalid_payload` refusal rather than a storage error.

**Four closed-vocabulary decoders, one per column family, and none of them coerces.** `_decode_closed`
stringifies a stored value, checks it against the schema module's own declared tuple — the same tuple
`_vocabulary_closes` renders into the table's `CHECK ... IN` lines — and raises `KnowledgeStorageError`
naming both the column and the admitted set when the value is outside it, because "coercing it into the
nearest member would serve a state the vocabulary does not have". The eleven typed wrappers
(`_decode_outcome`, `_decode_artifact_kind`, `_decode_inventory_state`, `_decode_claim_kind`,
`_decode_applicability`, `_decode_disposition`, `_decode_disposition_state`, `_decode_evidence_state`,
`_decode_assessment`, `_decode_realization_state`, `_decode_link_kind`, `_decode_target_state`,
`_decode_lifecycle`) each name one column and one vocabulary, so a mismatch between a column and the set
it is checked against is a visible line rather than a positional accident. `_decode_assessment` is the
one wrapper that admits the null column and maps it to `None` — the unassessed state, never a fourth
disposition. `_decode_provenance` decodes the stored typed JSON, reconstructs a nested `Authorship`
mapping into the model, and converts a pydantic `ValidationError` into `KnowledgeStorageError`;
`_decode_text` returns `None` for a recorded absence.

**Read back by one statement per table, ordered by the table's own key.** `_rows` executes a declared
statement against `store.connection` with the store's repository id bound first and returns plain
tuples. `read_inventory_rows`, `read_claims` and `read_dispositions` each build their payload from
**named** row indices — never a star select — and each one first resolves its envelope facts through
`_envelope_of`, which reads `knowledge_record` for the addressed kind and returns one `_EnvelopeEntry`
per record id. A census row whose envelope is absent gets `_UNKNOWN_ENVELOPE`, whose empty
`record_schema` makes `_require_declared_schema` refuse by name instead of serving a row assembled from
an envelope that was never written. `_EnvelopeEntry` is a `NamedTuple` rather than a bare triple
because its three fields travel together through three functions, and a positional triple read by index
"is where the wrong field gets the right name"; a relation row's provenance is inherited from its
claim's or disposition's own stored column instead of being supplied a second time, because a relation
carrying an independently supplied baseline would be an observation whose baseline nobody checked.

**Identity is computed for a receipt and never stored.** `_row_digest` hashes
`{"table", "record_id", "values"}` through `kernel.canonical_json.sha256_digest`, and its docstring
states the reason it is not a column: "the census records mint no identity of their own, and a stored
digest column on a census table would be a second identity authority beside the envelope's sealed
revision". `inventory_row_digest`, `claim_digest` and `disposition_digest` are the three expectation
readers: each executes its own `*_BY_ID` statement, returns `None` when the identity is not stored, and
otherwise digests the same value slice the write path put in its receipt — `tuple(row[2:11])` for the
inventory row, `tuple(row[2:7])` for the claim, `tuple(row[2:5])` for the disposition — so a caller
carries an expectation straight from a read rather than deriving a second identity scheme that could
disagree with the one it read. Those three readers are what `candidate_records._RECORD_READERS`
registers for `census_inventory_row`, `census_claim` and `census_disposition`; the three relation tables
are deliberately absent from that table, because each is written only as part of the aggregate that owns
it, so no command addresses one and no expectation could name a state a command could produce.

### Conventions

Every shape this module reads or writes comes from the shipped vocabulary rather than a declaration
repeated here: `CensusInventoryRowPayload` and its siblings, the three commands, the three read-back
types, every closed vocabulary alias and the six `(kind, record_schema)` constants are imported from
`models/knowledge/census.py`, and the receipt entry is `models/knowledge/candidate.RecordIdentity`.
The closed **value** tuples are imported, not re-spelled — the twelve `CENSUS_*` tuples from
`schema_v9` beside the DDL they constrain — so a vocabulary that gained a value in the model is a value
this decoder already admits. Lifecycle constants come from the shared base
(`PROPOSED_STATE`, `ACCEPTED_STATE`) and `CENSUS_RECORD_LIFECYCLE` is the one alias that binds a census
record to `proposed`. Vocabularies and ports that belong to another leaf are imported rather than
re-declared: `validate_record_payload` from `record_envelope`, `RecordRevisionDraft` and
`record_revision_row` from `facet_records`, `encode_authorship` and `encode_typed_column` from
`records`, `sha256_digest` and `decoded_json` from `kernel.canonical_json`, `routes` for the route
existence check, and `KnowledgeRefused`, `KnowledgeStorageError`, `missing_expected_row_refusal` and
`refusal` from `refusals`. Module-private helpers carry a leading underscore (`_Foundation`,
`_EnvelopeEntry`, `_inventory_columns`, `_decode_closed`, the eleven vocabulary decoders, `_row_digest`,
`_rows`, `_envelope_of`, `_require_declared_schema`, `_decode_provenance`, `_written_entry`); the module
declares **no `__all__`**, and its public contribution is the operation pair `CensusOperation` /
`CENSUS_OPERATION`, the generation constant, the eight `*_INSERT` statements, the three `apply`-side
names, the three read functions and the three digest readers. Declarations that must agree are one
declaration: one `CENSUS_OPERATION` is named by the result and by every refusal, one `(kind, schema)`
pair travels as a single `declaration` argument into `_write_envelope`, and the eight statements are
module-level constants each executed from exactly one place.

### Invariants And Boundaries

- **There is no second write path.** `apply_census_command` runs only inside the caller's open
  transaction, is reached only from `batch_commands._apply_family_census`, and calls `store.write` for
  every row it creates; the module opens no connection, begins no transaction and exposes no bulk
  writer. A refused step leaves nothing behind because every refusal raises.
- **No census row carries an identity authority of its own.** `_row_digest` is computed in memory for a
  receipt and the three expectation readers recompute it from named row slices; no census table has a
  content-address, logical-digest or fingerprint column to write one into, and the content digest stays
  on `record_revision`, where the envelope's `record_revision_row` puts it.
- **A stored value outside its declared vocabulary is a storage error, not a coercion.** `_decode_closed`
  raises `KnowledgeStorageError` naming the column and the admitted set, so a row altered outside the
  operation cannot be served as the nearest admitted member.
- **An unenveloped row is refused, not served.** `_UNKNOWN_ENVELOPE` carries the empty schema so
  `_require_declared_schema` refuses a row whose `knowledge_record` entry is missing or declares another
  schema; `_authority_home` likewise raises rather than inventing a home for a store with no repository
  row.
- **The dataset's own generation decides, and an old dataset is never migrated.** `require_census_generation`
  compares `store.generation.user_version` with `REQUIRED_CENSUS_GENERATION` and refuses with
  `unsupported_schema`; there is no widening, repair or in-place extension of an older dataset here.
- **No author is derived and no relation carries a second baseline.** The command payload has no author
  field, the envelope's provenance comes from the admitted `Authorship`, and every relation row is given
  its parent record's own encoded provenance instead of one supplied beside it.
- **A relation is written only inside its owner's aggregate.** Evidence, realization and link rows are
  inserted in the same command as the claim or disposition they resolve, and are absent from
  `candidate_records._RECORD_READERS`, so no expectation can address a state no command could produce.
- **The module holds no route policy and no kind registry.** Route existence is asked of
  `routes.route_exists`, admissibility is asked of the envelope seam, and the generation that registers
  these tables is read from `schema_generations`; nothing here restates any of the three.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows below ground the card's claims in the declarations themselves: the module's own statement of
its division of labour, the eight declared statements, the generation gate and the route check, the
closed-vocabulary decoders, the three read paths with the envelope they resolve against, and the three
expectation readers that keep a caller's digest the value the write path already produced.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of its division of labour: the revision codec is reused from the facet group and admissibility belongs to the envelope seam, with no transaction opened here. | `RecordRevisionDraft`; `record_revision_row`; `validate_record_payload` | mcp/src/agents_remember/memory/knowledge/census_records.py:1-17; mcp/src/agents_remember/memory/knowledge/census_records.py:29-34 |
| The one operation this group serves, named once so a result and a refusal cannot disagree, and the proposed lifecycle every census record is written under. | `CENSUS_OPERATION`; `CENSUS_RECORD_LIFECYCLE` | mcp/src/agents_remember/memory/knowledge/census_records.py:95-102 |
| The generation that registers these tables, bound to the registry's newest entry rather than to a literal number. | `REQUIRED_CENSUS_GENERATION`; `CURRENT_GENERATION` | mcp/src/agents_remember/memory/knowledge/census_records.py:118-120; mcp/src/agents_remember/memory/knowledge/schema_generations.py:482-482 |
| The two envelope statements and the six record-and-relation statements, each declared once with the destination table's own column order so a column added to the generation cannot be written mis-ordered. | `EFFECT_RECORD_INSERT`; `EFFECT_REVISION_INSERT`; `INVENTORY_ROW_INSERT`; `CLAIM_INSERT`; `DISPOSITION_INSERT`; `CLAIM_EVIDENCE_INSERT`; `CLAIM_REALIZATION_INSERT`; `DISPOSITION_LINK_INSERT` | mcp/src/agents_remember/memory/knowledge/census_records.py:122-160; mcp/src/agents_remember/memory/knowledge/schema_v2.py:63-72 |
| The column builder for the inventory row, whose provenance is the table's own typed-JSON column and which deliberately omits the authored envelope that `knowledge_record` already holds. | `_inventory_columns`; `inventory_row_row` | mcp/src/agents_remember/memory/knowledge/census_records.py:163-183; mcp/src/agents_remember/memory/knowledge/census_records.py:284-292 |
| The closed-vocabulary decoder that refuses a stored value outside its admitted set instead of coercing it, and the eleven typed wrappers that each name one column and one vocabulary. | `_decode_closed`; `_decode_outcome`; `_decode_assessment` | mcp/src/agents_remember/memory/knowledge/census_records.py:186-200; mcp/src/agents_remember/memory/knowledge/census_records.py:203-275 |
| The provenance decoder that rebuilds a nested authorship and turns a pydantic failure into a storage error, and the text decoder whose null is a recorded absence. | `_decode_provenance`; `_decode_text` | mcp/src/agents_remember/memory/knowledge/census_records.py:733-747; mcp/src/agents_remember/memory/knowledge/census_records.py:278-281 |
| The generation gate — the dataset's own recorded version compared with the one that registers these tables, refused as `unsupported_schema` with a next action that forbids migration in place — and the entry step it opens: generation, then governing route, then one envelope write plus one record-table write inside the caller's transaction, with every refusal raised. | `require_census_generation`; `apply_census_command`; `_apply_inventory_row`; `_apply_claim`; `_apply_disposition` | mcp/src/agents_remember/memory/knowledge/census_records.py:373-398; mcp/src/agents_remember/memory/knowledge/census_records.py:401-419; mcp/src/agents_remember/memory/knowledge/census_records.py:529-551; mcp/src/agents_remember/memory/knowledge/census_records.py:554-600; mcp/src/agents_remember/memory/knowledge/census_records.py:603-638 |
| The governing-route rule: an absent route is the explicit ungoverned state, a named route that does not exist is refused through the shipped missing-row refusal the removal paths use. | `_require_governing_route`; `route_exists`; `missing_expected_row_refusal` | mcp/src/agents_remember/memory/knowledge/census_records.py:422-436; mcp/src/agents_remember/memory/knowledge/routes.py:259-269; mcp/src/agents_remember/memory/knowledge/refusals.py:514-528 |
| Admissibility asked of the envelope seam and the seam's refusal returned as this group's raised refusal, plus the inherited authority home that raises when the store has no repository row. | `_admissible`; `_authority_home` | mcp/src/agents_remember/memory/knowledge/census_records.py:439-451; mcp/src/agents_remember/memory/knowledge/census_records.py:514-526 |
| The envelope write and its two statements, carried as one frozen value so a caller cannot transpose the record insert and the revision insert, and the receipt entry built without re-validation because the store computed every field. | `_write_envelope`; `_Foundation`; `_foundation`; `_written_entry`; `RecordIdentity` | mcp/src/agents_remember/memory/knowledge/census_records.py:454-473; mcp/src/agents_remember/memory/knowledge/census_records.py:476-511; mcp/src/agents_remember/memory/knowledge/census_records.py:105-115; mcp/src/agents_remember/models/knowledge/candidate.py:293-315 |
| The relation row builders, each inheriting its parent record's own stored provenance rather than accepting a second baseline from a caller. | `claim_evidence_row`; `claim_realization_row`; `disposition_link_row` | mcp/src/agents_remember/memory/knowledge/census_records.py:327-343; mcp/src/agents_remember/memory/knowledge/census_records.py:346-356; mcp/src/agents_remember/memory/knowledge/census_records.py:359-370 |
| The row digest that is computed rather than stored, with the reason spelled out: a stored digest column would be a second identity authority beside the envelope's sealed revision. | `_row_digest` | mcp/src/agents_remember/memory/knowledge/census_records.py:641-649 |
| The one declared statement per census table, each ordering by its own key, and the envelope read that reconstructs a row's lifecycle, governing route and record schema from `knowledge_record`. | `_INVENTORY_ROW_SELECT`; `_ENVELOPE_ROUTES_SELECT`; `_envelope_of` | mcp/src/agents_remember/memory/knowledge/census_records.py:654-684; mcp/src/agents_remember/memory/knowledge/census_records.py:706-714 |
| The sentinel envelope whose empty schema makes the declared-schema check refuse by name, and the check itself. | `_UNKNOWN_ENVELOPE`; `_require_declared_schema` | mcp/src/agents_remember/memory/knowledge/census_records.py:717-730 |
| The three read paths that rebuild the frozen payloads from named row indices and attach the relations they own, together with the one declared statement per census table that each reads through. | `read_inventory_rows`; `read_claims`; `read_dispositions`; `_INVENTORY_ROW_SELECT`; `_CLAIM_SELECT`; `_DISPOSITION_SELECT` | mcp/src/agents_remember/memory/knowledge/census_records.py:750-778; mcp/src/agents_remember/memory/knowledge/census_records.py:781-829; mcp/src/agents_remember/memory/knowledge/census_records.py:832-868; mcp/src/agents_remember/memory/knowledge/census_records.py:654-680 |
| The three expectation readers, each digests the same value slice the write path put in its receipt and returns nothing when the identity is not stored. | `inventory_row_digest`; `claim_digest`; `disposition_digest`; `_INVENTORY_ROW_BY_ID` | mcp/src/agents_remember/memory/knowledge/census_records.py:893-901; mcp/src/agents_remember/memory/knowledge/census_records.py:904-911; mcp/src/agents_remember/memory/knowledge/census_records.py:914-923; mcp/src/agents_remember/memory/knowledge/census_records.py:877-882 |
| Where the group joins the one candidate operation: the census apply step selected by the group's own command-kind set, and the same set checked before any row exists. | `_apply_family_census`; `_census_check`; `_CENSUS_DECLARATIONS`; `_CENSUS_KINDS` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:328-349; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:1320-1353; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:1354-1358; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:365-365 |
| The registry that makes the three record tables addressable by an expectation while the three relation tables are deliberately absent, and the union that admits exactly the eight tables a census command writes. | `_RECORD_READERS`; `CENSUS_ONLY_WRITABLE_TABLES`; `CENSUS_WRITABLE_TABLES` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:277-315; mcp/src/agents_remember/memory/knowledge/candidate_records.py:106-112; mcp/src/agents_remember/models/knowledge/census.py:362-373 |
| The schema tuples the decoders check against, declared beside the DDL they render into so the model and the schema cannot become two different sets of admitted values. | `CENSUS_PARSE_OUTCOMES`; `CENSUS_DISPOSITION_KINDS`; `CENSUS_ARTIFACT_KINDS`; `CENSUS_INVENTORY_STATES` | mcp/src/agents_remember/memory/knowledge/schema_v9.py:78-83; mcp/src/agents_remember/memory/knowledge/schema_v9.py:93-101; mcp/src/agents_remember/memory/knowledge/schema_v9.py:73-77; mcp/src/agents_remember/memory/knowledge/schema_v9.py:84-84 |
| The same tuples imported by the migration parser and inventory, whose import-time guards make each closed set a subset of the vocabulary the schema declares. | `CENSUS_PARSE_OUTCOMES`; `CENSUS_ARTIFACT_KINDS`; `CENSUS_INVENTORY_STATES` | mcp/src/agents_remember/memory/migration/parse.py:39-54; mcp/src/agents_remember/memory/migration/parse.py:112-113; mcp/src/agents_remember/memory/migration/inventory.py:117-122 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every row it writes lands in one local SQLite
dataset through the store it is handed, every value it reads is a stored column of that dataset, and the
one external fact it consults — whether a named route exists — is answered by a `SELECT` against the same
connection.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-19T17:15+02:00 — 260915-KS-L28 curator (uncommitted change set on `ar/260915-ks-l28`, base `497d9e9f`): M1-4 anchor repair, re-read against the code worktree at `e7998504`. Five rows were wrong. The expectation-reader row was rotated by one (`_INVENTORY_ROW_BY_ID` was answered with the range of `inventory_row_digest` and so on); each now cites its own extent `:893-901`, `:904-911`, `:914-923`, `:877-882`. The census-apply row's paths were crossed across the two modules: `_census_check` and `_CENSUS_DECLARATIONS` live in `batch_preconditions.py` (`:1320-1353`, `:1354-1358`) and `_CENSUS_KINDS` in `batch_preconditions.py:365`, while only `_apply_family_census` is in `batch_commands.py:328-349`. `CURRENT_GENERATION` moved to `schema_generations.py:482-482` and `route_exists` to `routes.py:259-269` (both files changed after this card's stamp). The schema-tuple row was split: one row now cites each tuple's declaration in `schema_v9.py` (each paired positionally), and a second row carries the migration parser and inventory import guards that the first row's finding had claimed. Every other row was re-checked and stands (the import and DDL-column rows are deliberate mention anchors). No claim was deleted or softened. The stamp is unchanged because `2dcacb27`'s content for this file is byte-identical to `e7998504` (`git diff 2dcacb27 HEAD` is empty).- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for the census record group's row codecs and in-transaction write step. It records the three record kinds and the three relations they resolve through, the eight declared INSERT statements whose parameter order is the destination generation's own column order, and the two-insert envelope write that `_Foundation` carries as one value so the record insert and the revision insert cannot be transposed. It states the refusals that make the step all-or-nothing — `unsupported_schema` from `require_census_generation` against a dataset older than generation 9, the missing-row refusal for a named route that does not exist beside the never-refused absent route, `KnowledgeStorageError` from `_decode_closed` for a stored value outside its declared vocabulary, from `_require_declared_schema` for a row whose envelope is absent or declares another schema, and from `_authority_home` for a store with no repository row — and the deliberate absence of a second write path, since every row is written through `store.write` inside the batch's own transaction. It also records that the census mints no stored identity: `_row_digest` is computed in memory for a receipt, the three expectation readers recompute it from named row slices, and the module holds no `__all__`. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
