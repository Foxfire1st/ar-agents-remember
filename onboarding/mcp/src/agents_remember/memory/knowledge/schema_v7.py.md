# mcp/src/agents_remember/memory/knowledge/schema_v7.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/schema_v7.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T09:20+02:00 |
| lastVerifiedCommitHash |  `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate |  2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l12` uncommitted source; base `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Generation 7's appended tables: the evidence claim, its three join tables, and the verification
observation. This module owns **only what generation 7 appends** and declares no table of an earlier
generation, so the additive rule `KS-R10@v1` §1.3 states is a property of the file rather than of a
review.

**The number is the landing's, not the branch's, and that distinction is the first thing a reader
needs.** `KS-R12@v1` was built in parallel with `KS-R17@v1` and `KS-R18@v1`, each reading the registry
as `(1, 2, 3, 4)` and so each registering *generation 5* on its own branch. The landing resolved the
collision by appending in landing order: this leaf's five tables became **generation 7**, composed onto
generation 6, which is generation 5 plus `KS-R17@v1`'s six composition tables, which is generation 4
plus `KS-R18@v1`'s `citation_binding`. So this module was `schema_v5.py` on the branch and is
`schema_v7.py` here, and the code it declares is unchanged by that renumber. A card that reads
`generation 5` as this module's number is reading a pre-sync branch state.

## Code Commentary

### Logic

Five appended tables, named once in `APPENDED_TABLES`: `evidence_claim`, the two subject join tables
`evidence_claim_invariant_subject` and `evidence_claim_facet_subject`, `evidence_claim_coverage`, and
`verification_observation`. The declaration is split the way every earlier generation splits it —
columns, primary keys, typed-JSON columns, DDL, index DDL, triggers and features — and none of those
groups mentions a generation 1–6 table.

**Append, never rewrite.** There is no `ALTER TABLE` anywhere in this module, and no statement that
redeclares, reorders, renames, retypes or drops an inherited name. A generation-7 composition is
generation 6's registry plus these five tables, and the case
`test_the_observation_generation_appends_and_inherits_by_name` asserts that inheritance **against the
generation this leaf descends from, by name** — `GENERATION_7.columns[table] ==
GENERATION_6.columns[table]` for every inherited table and `GENERATION_7.tables[: len(GENERATION_6.tables)] ==
GENERATION_6.tables` — rather than against a hard-coded table list. A further renumber therefore changes
two operand names and nothing else.

**The execution vocabulary is closed in the DDL as well as in the vocabulary.** `EXECUTION_RESULT_MEMBERS`
is the five members `passed`, `failed`, `error`, `skipped` and `not_run`, and `_EXECUTION_RESULT_CHECK`
renders them into the column's own `CHECK` list. The value is public precisely because a generation's DDL
is pinned structure and cannot import the vocabulary that names it; a case asserts the tuple equals the
vocabulary's own list so the stored `CHECK` and the typed field cannot drift apart. **There is no
sufficiency member**: the members name what a run did, and `not_run` is stored as `not_run`.

**The three join tables are the structural half of the claim.** The two subject tables are one row per
subject kind, each with its own foreign key, so *the table is the kind check*: a claim whose subject is an
invariant revision cannot reach the facet table, because the only column that table declares references
`record_revision`. A polymorphic subject column with a kind discriminator is not merely unused here — it
does not exist, so a misspelled kind, a dangling identity and a wrong-kind target are unrepresentable
rather than refused. `evidence_claim_coverage` carries one checked foreign-key group per claimed-coverage
kind, following the shipped `facet_attachment` idiom, plus one column the attachment does not need:
`covered_identity`, `NOT NULL`, carrying the endpoint's identity so that "one endpoint is covered once"
is a key rather than a hope. SQLite does not compare `NULL`s for equality in a key, so a key over the two
nullable endpoint columns would let the same claim list the same endpoint twice; an `''` spelling in the
unpopulated column would instead be a value its own foreign key rejects.

**The observation keeps the run as a row, not as prose.** `verification_observation` stores the snapshot
identity, the code candidate tree, the command name and its verbatim identity, the artifact path, size and
sha256, whether that digest was checked against the bytes, the execution result, the run environment, and
the optional publication reference. `verification_observation_no_rewrite` and its `_no_delete` sibling
seal every revision row, so a second run is a second record rather than an edit.

### Conventions

A generation module states its own declarations and nothing else; the registry composes it. Column order
is part of a generation's contract, so a codec that inserts rows derives its statement from the declared
order instead of restating it.

### Invariants And Boundaries

- **The declared tables are the writable set's source.** `APPENDED_TABLES` is what the mutable-table union
  and the schema census read, so a table that is not declared here cannot be written by a command.
- **`EXECUTION_RESULT_MEMBERS` and the vocabulary's `EXECUTION_RESULTS` are one contract.** The DDL cannot
  import the vocabulary, so the tuple is public and a case compares the two lists; widening one without the
  other fails.
- **No table of this module carries a content address, a logical digest or a fingerprint.** A revision's
  seal is `record_revision.content_digest` on the envelope's own aggregate; the one digest this generation
  stores is the sha256 of an **external artifact's bytes**, which is an identity of something outside the
  database.
- **Nothing here migrates.** A dataset whose recorded generation predates these tables is refused by the
  write path with the observed and required versions as facts; no table is created implicitly and
  `PRAGMA user_version` does not move.
- **The generation this module is composed into is resolved at the registry, not here.** This module never
  names its own number in a table declaration; the version facts live in
  `memory/knowledge/schema_generations.py`, which is where the landing's renumber was applied and where a
  further one would be.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The five appended tables, in declaration order — the only names this generation adds. | `APPENDED_TABLES` | mcp/src/agents_remember/memory/knowledge/schema_v7.py:69-74 |
| The appended columns, primary keys and typed-JSON columns, one group per declaration plane. | `APPENDED_COLUMNS`; `APPENDED_PRIMARY_KEYS`; `APPENDED_JSON_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v7.py:77-121; mcp/src/agents_remember/memory/knowledge/schema_v7.py:128-140; mcp/src/agents_remember/memory/knowledge/schema_v7.py:148-153 |
| The closed five-member execution vocabulary the column's own `CHECK` carries, and the public tuple that keeps the DDL and the typed field from drifting. | `EXECUTION_RESULT_MEMBERS`; `_EXECUTION_RESULT_CHECK` | mcp/src/agents_remember/memory/knowledge/schema_v7.py:161-161; mcp/src/agents_remember/memory/knowledge/schema_v7.py:163-164 |
| The five tables' DDL and the indexes over the two join tables and the observation's recorded candidate. | `APPENDED_TABLE_DDL`; `APPENDED_INDEX_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v7.py:167-265; mcp/src/agents_remember/memory/knowledge/schema_v7.py:303-324 |
| The no-rewrite and no-delete triggers that make a second run a second record. | `APPENDED_TRIGGERS` | mcp/src/agents_remember/memory/knowledge/schema_v7.py:337-378 |
| The generation this one is composed onto, by name, and the composition that names this module as generation 7's append. | `GENERATION_6`; `_compose_generation_7`; `GENERATION_7` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:377-387; mcp/src/agents_remember/memory/knowledge/schema_generations.py:378-378; mcp/src/agents_remember/memory/knowledge/schema_generations.py:389-389; mcp/src/agents_remember/memory/knowledge/schema_generations.py:396-396; mcp/src/agents_remember/memory/knowledge/schema_generations.py:407-407 |
| The schema name generation 7 declares, and the registry whose last entry is now the created generation — generation 8 as of `KS-R13@v1`, so this leaf's own generation stays declared and no longer the tip. | `GENERATION_7_SCHEMA_NAME`; `GENERATIONS`; `CURRENT_GENERATION` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:208-208; mcp/src/agents_remember/memory/knowledge/schema_generations.py:425-434; mcp/src/agents_remember/memory/knowledge/schema_generations.py:447-447; mcp/src/agents_remember/memory/knowledge/schema_generations.py:214-214; mcp/src/agents_remember/memory/knowledge/schema_generations.py:224-224; mcp/src/agents_remember/memory/knowledge/schema_generations.py:456-456; mcp/src/agents_remember/memory/knowledge/schema_generations.py:479-479 |
| The generation the write path requires before any supporting-record row may exist. | `REQUIRED_EVIDENCE_GENERATION` | mcp/src/agents_remember/memory/knowledge/evidence.py:88-88 |
| The case that asserts the append and the inheritance against the generation this leaf descends from, by name. | "def test_the_observation_generation_appends_and_inherits_by_name(" | mcp/tests/test_knowledge_evidence_observations.py:906-928 |
| The case that asserts a write against an older generation is refused with both versions as facts. | "def test_an_observation_write_against_an_older_generation_is_refused(" | mcp/tests/test_knowledge_evidence_observations.py:847-870 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A table declaration is a property of the
dataset, and a dataset's identity excludes Git commits, ledger rows and checkout locations.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T09:20+02:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): created this one-to-one card for **generation 7's** five appended tables. It records the five-table append, the by-name inheritance assertion against generation 6, the closed five-member execution vocabulary with no sufficiency member, and the structural rule that the join table *is* the kind check. **The generation number and the module's own name are the landing's, and the card says so**: this leaf was built in parallel with `KS-R17@v1` and `KS-R18@v1`, all three read the registry as `(1, 2, 3, 4)`, and the landing appended them in landing order so that this leaf's tables became generation 7 and its module `schema_v7.py` — the declaration itself unchanged by the renumber. This card carries **no `lastVerifiedCommitHash`**: the constructs it cites exist only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
