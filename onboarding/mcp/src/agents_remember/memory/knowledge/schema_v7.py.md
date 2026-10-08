# mcp/src/agents_remember/memory/knowledge/schema_v7.py

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

Append, never rewrite. No declaration here changes an inherited table. schema_generations._compose appends this evidence/observation block after schema_v6 while preserving inherited column, key and typed-JSON mappings. The complete single derived-index schema is checked against its recorded fingerprint; the former GENERATION_6/GENERATION_7 records and their inheritance assertion are retired.

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

An appended-table module states its declarations and nothing else; _compose includes it in the single derived-index schema. Column and key order remain declared data that the encoder consumes rather than reconstructing from DDL.

### Invariants And Boundaries

- APPENDED_TABLES declares exactly this module's table block for composition and logical encoding. The former mutable-table union belonged to the retired canonical writer; these declarations grant no write admission.
- **`EXECUTION_RESULT_MEMBERS` and the vocabulary's `EXECUTION_RESULTS` are one contract.** The DDL cannot
  import the vocabulary, so the tuple is public and a case compares the two lists; widening one without the
  other fails.
- **No table of this module carries a content address, a logical digest or a fingerprint.** A revision's
  seal is `record_revision.content_digest` on the envelope's own aggregate; the one digest this generation
  stores is the sha256 of an **external artifact's bytes**, which is an identity of something outside the
  database.
- This module neither migrates nor writes rows. The index opener admits the one CURRENT_GENERATION schema and refuses another declared version; no earlier database is implicitly extended or migrated.
- **The generation this module is composed into is resolved at the registry, not here.** This module never
  names its own number in a table declaration; the version facts live in
  `memory/knowledge/schema_generations.py`, which is where the landing's renumber was applied and where a
  further one would be.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The five appended tables, in declaration order — the only names this generation adds. [1]
- The appended columns, primary keys and typed-JSON columns, one group per declaration plane. [2]
- The closed five-member execution vocabulary the column's own `CHECK` carries, and the public tuple that keeps the DDL and the typed field from drifting. [3]
- The five tables' DDL and the indexes over the two join tables and the observation's recorded candidate. [4]
- The no-rewrite and no-delete triggers that make a second run a second record. [5]

- The ordered appended declarations compose into the one pinned derived-index schema. [6]


- This build creates and reads the single v9 derived-index schema; another declared database version is refused. [7]


### Cross-Repo References

No cross-repository behavior is implemented in this file. A table declaration is a property of the
dataset, and a dataset's identity excludes Git commits, ledger rows and checkout locations.

No meaningful cross-repo references found.
