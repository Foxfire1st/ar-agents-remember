# mcp/src/agents_remember/memory/knowledge/schema_v4.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Generation 4's appended table, as pinned data.** One table — `detection_run_signal` — carrying the
recorded order of one detection run's signals: a position, the run it belongs to and the signal
recorded at that position.

This module owns **only what generation 4 appends**. Generation 1's ten tables stay declared verbatim
in `schema.py`, generation 2's six in `schema_v2.py` and generation 3's four in `schema_v3.py`; nothing
here redeclares, reorders, renames, retypes or drops one of them, and no `ALTER TABLE` against an
earlier generation's table appears anywhere in the package. Generation 4's append is the same explicit
composition generations 2 and 3 use, so the additive rule is a property of the composed generation
record rather than a convention a reader has to check by hand.

**Why one table and not a record group.** A detection signal and a detection run are *typed records*,
and `KS-R10@v1`'s envelope already holds them: `knowledge_record` carries the kind, the authority home,
the lifecycle and the governing route, and `record_revision` carries the frozen payload and its
content digest. Both payload shapes are registered in
`agents_remember.memory.knowledge.record_envelope.PAYLOAD_MODELS` under
`(detection_signal, detection-signal/v1)` and `(detection_run, detection-run/v1)`, so a signal's
required field set, its closed vocabularies and its construction refusals are declared **once**, in
`models/knowledge/detection.py`, rather than restated as columns here. What the envelope cannot express
is the *sequence*: `KS-R14@v1` requirement 3.3 makes reproducibility a comparison of two **ordered
sequences**, so the order is a stored fact of its own rather than a tuple inside one revision's payload.

## Code Commentary

### Logic

The module is pure declaration data. Its APPENDED_* constants are consumed after schema_v3 by schema_generations._compose to build CURRENT_GENERATION, the one derived-index schema. The historical generation-4 grouping is the detection-order table block, not a separately openable schema.

- `APPENDED_TABLES` — the ordered tuple `("detection_run_signal",)`, appended after generation 3's
  twenty so generation 4's manifest **begins with** generation 3's, unchanged. The order is
  load-bearing: it is the order the encoder serializes tables in.
- `APPENDED_COLUMNS` — the declared column order `repository_id`, `run_id`, `ordinal`, `signal_id`.
  The encoder orders rows through this tuple, so it is pinned structure rather than a derivation from
  the DDL text.
- `APPENDED_PRIMARY_KEYS` — `("repository_id", "run_id", "ordinal")`, the declared primary key as the
  DDL declares it. The encoder orders a table's rows by this tuple.
- `APPENDED_JSON_COLUMNS` — an **explicitly empty** frozenset for the table, declared rather than
  omitted so a reader does not infer "no typed-JSON column" from an absence. The sequence is two opaque
  identities and a position; every structured fact about a signal or a run lives in the registered
  payload on `record_revision`.
- `APPENDED_TABLE_DDL` — one `STRICT` `CREATE TABLE`. `ordinal` is part of the primary key, so one run
  cannot record two signals in one position, and `UNIQUE (repository_id, run_id, signal_id)` means one
  run cannot record one signal twice. Together they make the declared total order over signal identity
  a **constraint of the table** instead of a rule the write path remembers. Both endpoints are
  composite foreign keys to `knowledge_record(repository_id, record_id)` — the run and the signal — so
  a sequence can only name records the same store holds and a signal cannot be attributed to a run by
  prose. `CHECK (ordinal >= 0)` refuses a negative position, and every foreign key is `NO ACTION …
  DEFERRABLE INITIALLY DEFERRED` exactly as the sixteen shipped tables declare theirs.
- `APPENDED_INDEX_DDL` — one index, `detection_run_signal_signal` over
  `(repository_id, signal_id)`, covering the reverse direction of a declared lookup: "which runs
  recorded this signal". Index names are a local choice, not contract.
- `APPENDED_TRIGGERS` — two triggers, `detection_run_signal_no_reorder` (BEFORE UPDATE OF `run_id`,
  `ordinal`, `signal_id`) and `detection_run_signal_no_delete` (BEFORE DELETE). Their messages share
  the shipped `immutable_revision:` prefix, retained from the canonical database schema. The former map_sqlite_error mapper was retired; the triggers remain index-schema constraints. The idiom is the one generations 2 and 3 use: the operation's own preconditions exist to
  return a **typed refusal**, and the triggers exist so a changeset, a repair script or a future code
  path that forgot the rule still cannot rewrite a recorded run's sequence or drop one of its signals.
- `APPENDED_FEATURES` — the **empty** tuple, declared rather than omitted. Generation 4 needs no SQLite
  feature generation 3 does not already require: one table with checked foreign-key groups, a composite
  unique key, an index and triggers are all covered by `strict_tables`, `deferrable_foreign_keys`,
  `trigger_raise_abort` and `json_functions`.

### Conventions

- Every table is `STRICT`, every primary-key column is declared `NOT NULL` explicitly, and every
  foreign key is composite and `DEFERRABLE INITIALLY DEFERRED`, exactly as the twenty shipped tables
  are.
- **The declaration states its own absences.** Both the typed-JSON mapping and the feature tuple are
  present and empty rather than missing, matching generation 3's declaration style.
- The module imports nothing from the package: it is data the composer reads, not behaviour that reads
  the database.

### Invariants And Boundaries

- The ordered _compose preserves earlier table declarations while appending this table block. Its complete result is checked against the pinned derived-index fingerprint. The former GENERATION_3 and GENERATION_4 records and their prefix-comparison API are retired.
- **No detection row carries a content address, a logical digest or a fingerprint column, and none is
  added here.** The content digest belongs to `record_revision`, where `Doc13:85` already puts it — the
  signal *observed* a digest and does not become one.
- **Immutability is enforced by the database, not only by the operation.** Requirement 3.4's "never
  overwrites the recorded one" is about the run, and a run's order is what a second write would have to
  move to present a re-execution as the recorded run.
- This module declares derived-index structure only: no row writing, payload validation, refusal or migration. The former canonical database record writer associated with these tables was retired. schema_generations composes and validates the one supported index schema.
- **Not admissible, recorded so it is not re-proposed:** a `detection_signal`/`detection_run` column
  group on this table. The payload models are the shape, and a second declaration as SQL columns would
  be a second place for the same field set to drift.

### Todos

None recorded. Generation 4's own fingerprint is computed by composition in `schema_generations.py`
rather than recorded here.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The ordered appended-table tuple whose prefix rule makes generation 4's manifest begin with generation 3's twenty tables. [1]
- The declared column order the encoder serializes rows through. [2]
- The declared composite primary key, which is also the encoder's row-ordering tuple. [3]
- **The declared-but-empty typed-JSON mapping, so "no JSON column" is stated rather than inferred.** [4]
- **The one `STRICT` `CREATE TABLE`: ordinal in the key, the unique signal key, the checked position and the two composite foreign keys to the envelope.** [5]
- The one reverse-direction index, covering "which runs recorded this signal". [6]
- **The two immutability triggers, with the shared `immutable_revision:` prefix and the two distinct refusals they raise.** [7]
- The declared-but-empty feature tuple, so "no new SQLite feature" is stated rather than inferred. [8]

- The ordered appended declarations compose into the one pinned derived-index schema. [9]


- This build creates and reads the single v9 derived-index schema; another declared database version is refused. [10]


- The ordered appended declarations compose into the one pinned derived-index schema. [12]


- This build creates and reads the single v9 derived-index schema; another declared database version is refused. [13]


### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
