# mcp/src/agents_remember/memory/knowledge/evidence_records.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Row codecs between the supporting-record vocabulary and generation 7's declared columns, in both
directions, plus the row and revision digests the guards compare against.

**One table's codec lives beside it, and this module still answers for it.** The
`verification_observation` row codec (`observation_cells`, `OBSERVATION_COLUMNS`, `observation_row`,
`observation_row_digest`, `decode_observation_row` and their column-group decoders) is owned by
[`evidence_observation_rows.py`](evidence_observation_rows.py.md) since `260921-ICR-L57`, and every one
of those public names is imported here and kept in `__all__`. Callers — `evidence.py`,
`evidence_read.py` and the evidence test modules — still name `evidence_records` for them; no import
site changed.

## Code Commentary

### Logic

Every conversion in both directions lives here, so the column order, the canonical JSON text form of a
typed column and the digest recomputation have exactly one owner per table. The repository's file-size
rail is the reason it is not larger: no module may cross 1200 lines. When the module reached 1210 lines,
`260921-ICR-L57` moved the observation's row codec, the one codec with no dependency on the claim
codecs, into its own module and re-exported it, leaving 1006 lines here.

**Two seals are recomputed on the way out rather than trusted**, on the shipped rule that a row whose text
was rewritten behind its identity must not be served as the revision that identity names: a claim
revision's `content_digest` and an observation revision's `content_digest` are re-derived from the stored
payload. `decode_record_revision_row`, `decode_claim_row`, `decode_subject_row`, `decode_coverage_row` and
`decode_observation_row` are the decode half (the last one re-exported from the observation module).

The **observable-row digests** are the other half of the same idea. A claim's ledger row, a subject edge, a
claimed-coverage edge and an observation's own row are not sealed revisions, so an operation that names one
of them by digest computes that digest from the row as it stands: `evidence_claim_row_digest`,
`subject_row_digest`, `coverage_row_digest` and `observation_row_digest`. The read path exposes the same
values, so a caller carries an expectation straight from a read instead of deriving a second identity
scheme.

**`OBSERVATION_COLUMNS` is a declared order, not a convenience** — the insert statement is derived from
it. That order, the cells and the private column-group decoders are described on
[`evidence_observation_rows.py`](evidence_observation_rows.py.md), their owner.

**The envelope digests are computed here rather than borrowed from the facet codecs.** This leaf appends
its own tables and its own record kinds; a shared digest helper would have to be a new function in the facet
module, which is another leaf's file, and an evidence claim's identity would then be defined by a module
that does not own it. The formula is the shipped one, restated here for the same reason a generation
restates the DDL it extends: the *value* is part of this record's contract, and a case asserts the two agree
field by field.

`CLAIM_BY_ID` and the five sibling statements beside it are the read queries whose declared order columns
land in `read_queries.py`.

**The claim identities have a listing of their own, and it is not the record read** (`ICR-R14@v1`).
`claim_ids` runs `CLAIM_IDS_OF_REPOSITORY` — the same repository-scoped identity statement
`all_claims` reads whole — and decodes nothing. It exists because "which claims does this namespace
record" and "what does this claim say" are different questions: a composing reader that wants to serve
a damaged claim's identity while its siblings are still supplied needs the **listing** without the
decode, and then reads each identity through `claim_record`, the owner's own single-record reader.
`all_claims` is unchanged and stays the convenient all-or-nothing form (`_identities_of` over the same
statement); `claim_ids` is the listing half, so the two can never come to disagree about which
identities exist. The split is what makes the per-record isolation in
[`application/review_evidence_records.py`](../../application/review_evidence_records.py.md)
reachable at all: with only `all_claims`, one undecodable claim made the whole collection one refusal.

### Conventions

A codec module owns row ↔ value conversion and nothing else: no policy, no refusal, no judgement. A digest
function is named after the row it seals, and the sealed revision digests are recomputed rather than read
back from the row's own text.

### Invariants And Boundaries

- **Column order is contract.** A statement derived from the declared order and a codec derived from the
  same order cannot disagree; a statement that restates the order can.
- **A digest is computed from the row as it stands.** No path in this module returns a stored digest of an
  observable row without recomputing it.
- **The listing and the record read are two answers, and neither is derived from the other.** A
  caller that must survive one damaged record reads the identities and then reads each record; the
  listing never decodes a payload, and `all_claims` is not re-implemented beside it — both run the
  same `CLAIM_IDS_OF_REPOSITORY` statement, so an identity that exists is listed once.
- **No blob, no second content store.** The only digest here that describes something outside the database
  is the artifact reference's, and it is carried as text.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The revision payload version and the envelope draft the pair of rows is written from. [1]
- The envelope row and its digest — the ledger pair every record kind shares. [2]
- The revision row, its recomputed seal, and the decode that re-derives it rather than trusting the row's text. [3]
- The claim's ledger row and its observable-row digest. [4]
- The subject edge's row, its table and revision column, and its observable-row digest. [5]
- The claimed-coverage edge's row and its observable-row digest. [6]
- **The observation's row codec is imported from its own module and kept in this module's registered surface, so callers keep naming this module.** [7]
- The callers that reach the observation codec through this module. [8]
- The read statements whose declared order columns live in the read-queries module. [9]
- **The claim-identity listing, decoding nothing, and the whole-listing form unchanged beside it: both run the same identity statement, so the two cannot disagree about which identities exist.** [10]
- **The single-record reader each listed identity is then read through, which is what makes a per-record guard possible without a second reader.** [11]
- **The composing reader this listing exists for: one identity read at a time, a damaged claim named while its siblings are supplied.** [12]
- **The registered surface gained exactly one name (`claim_ids`), and the case that measures the isolation it makes reachable.** [13]
- The case that asserts there is no blob column and no second content store. [14]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
