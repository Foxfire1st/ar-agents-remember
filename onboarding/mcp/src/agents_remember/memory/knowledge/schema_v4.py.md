# mcp/src/agents_remember/memory/knowledge/schema_v4.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/schema_v4.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| lastVerifiedCommitDate | 2026-09-18T07:49:45+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l18` uncommitted source; base `e963a01c` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

The module is pure data: it defines **no functions and no classes**. Its whole surface is seven module
constants, and each is a member of the generation record `schema_generations.GENERATION_4` composes:

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
  the shipped `immutable_revision:` prefix, so `map_sqlite_error` steers a trigger-originated error to
  that code. The idiom is the one generations 2 and 3 use: the operation's own preconditions exist to
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

- **Additive-only, structurally.** `GENERATION_4.tables[: len(GENERATION_3.tables)] ==
  GENERATION_3.tables`, and generation 4's columns, primary keys and typed-JSON registries for each of
  generation 3's twenty names are generation 3's declared ones. That prefix equality is the whole of
  the additive rule; a new generation appends, and never retypes, reorders, renames or drops an earlier
  one's.
- **No detection row carries a content address, a logical digest or a fingerprint column, and none is
  added here.** The content digest belongs to `record_revision`, where `Doc13:85` already puts it — the
  signal *observed* a digest and does not become one.
- **Immutability is enforced by the database, not only by the operation.** Requirement 3.4's "never
  overwrites the recorded one" is about the run, and a run's order is what a second write would have to
  move to present a re-execution as the recorded run.
- **Boundary.** This module declares structure and nothing else: it writes no rows, performs no
  validation, returns no refusal and owns no behaviour. Writing a run is
  `memory/knowledge/detection.py`; deciding which generation a dataset is, is `schema_generations.py`.
- **Not admissible, recorded so it is not re-proposed:** a `detection_signal`/`detection_run` column
  group on this table. The payload models are the shape, and a second declaration as SQL columns would
  be a second place for the same field set to drift.

### Todos

None recorded. Generation 4's own fingerprint is computed by composition in `schema_generations.py`
rather than recorded here.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The ordered appended-table tuple whose prefix rule makes generation 4's manifest begin with generation 3's twenty tables. | `APPENDED_TABLES` | mcp/src/agents_remember/memory/knowledge/schema_v4.py:45-47 |
| The declared column order the encoder serializes rows through. | `APPENDED_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v4.py:49-56 |
| The declared composite primary key, which is also the encoder's row-ordering tuple. | `APPENDED_PRIMARY_KEYS` | mcp/src/agents_remember/memory/knowledge/schema_v4.py:58-62 |
| **The declared-but-empty typed-JSON mapping, so "no JSON column" is stated rather than inferred.** | `APPENDED_JSON_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v4.py:64-71 |
| **The one `STRICT` `CREATE TABLE`: ordinal in the key, the unique signal key, the checked position and the two composite foreign keys to the envelope.** | `APPENDED_TABLE_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v4.py:73-93 |
| The one reverse-direction index, covering "which runs recorded this signal". | `APPENDED_INDEX_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v4.py:95-99 |
| **The two immutability triggers, with the shared `immutable_revision:` prefix and the two distinct refusals they raise.** | `APPENDED_TRIGGERS`; "immutable_revision: a recorded detection sequence cannot be reordered" | mcp/src/agents_remember/memory/knowledge/schema_v4.py:101-116 |
| The declared-but-empty feature tuple, so "no new SQLite feature" is stated rather than inferred. | `APPENDED_FEATURES` | mcp/src/agents_remember/memory/knowledge/schema_v4.py:118-123 |
| **The generation record this module's data is composed into, and the append that keeps generation 3's prefix intact.** | `_compose_generation_4`; `GENERATION_4` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:232-258 |
| **The registry whose last entry is the newest supported generation — generation 5 since `KS-R18@v1`, so the created store declares 5 while a generation-4 dataset keeps declaring 4 — and the created generation it names.** | `GENERATIONS`; `CURRENT_GENERATION` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:299-305; mcp/src/agents_remember/memory/knowledge/schema_generations.py:318-318 |
| **The envelope registry the two detection payload shapes are registered in, which is why this generation appends one table and not a record group.** | `PAYLOAD_MODELS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:103-132 |
| The write path that inserts the sequence rows under this table's composite keys. | `_write_run` | mcp/src/agents_remember/memory/knowledge/detection.py:316-348 |
| **The case that measures the additive rule, the append order, the `STRICT` shape, the key tuple and the two triggers.** | "test_generation_4_appends_only_and_the_first_twenty_names_are_generation_3_s" | mcp/tests/test_knowledge_detection_signals.py:724-751 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T07:45+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `a0665505`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the range recorded in the row above is the one that now holds its anchor. The anchors concerned: `PAYLOAD_MODELS`. No claim wording changed, and the verification metadata advances to the landed base because the claims were re-read against the current source.
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): **re-read the registry claim against the construct as it now stands.** `KS-R18@v1` appends generation 5, so `GENERATIONS[-1]` — the entry a created store declares — is generation 5 rather than generation 4, and the claim now states that consequence explicitly instead of leaving the reader to infer it. The one range the mechanical pass had left naming a single line twice is corrected to name the registry's own lines and the assignment's, so each row's anchor resolves to one extent. No other row of this card was changed. Verification metadata advances to the leaf's base commit `e963a01c` because the claim was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T05:15+02:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): created this one-to-one card for generation 4's appended table. It records the one-table append and why: the detection payload shapes are registered in the record envelope, so what the envelope cannot express — the *sequence* — is the only thing this generation stores. It records `ordinal` in the primary key together with `UNIQUE (repository_id, run_id, signal_id)` as the two constraints that make the declared total order over signal identity a table property rather than a write-path habit, the two composite foreign keys to `knowledge_record` that keep attribution structural, the two immutability triggers with their shared `immutable_revision:` prefix and their two distinct messages, the declared-but-empty typed-JSON mapping and feature tuple (absences stated rather than inferred), and the prefix equality `GENERATION_4.tables[: len(GENERATION_3.tables)] == GENERATION_3.tables` that is the whole additive rule. Verification metadata is the leaf's base commit `4264dcc9`: the code commit does not exist yet and closeout owns that stamp.
