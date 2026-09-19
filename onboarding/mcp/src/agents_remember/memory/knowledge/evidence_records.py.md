# mcp/src/agents_remember/memory/knowledge/evidence_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/evidence_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:20+02:00 |
| lastVerifiedCommitHash |  `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate | 2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l12` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Row codecs between the supporting-record vocabulary and generation 7's declared columns, in both
directions, plus the row and revision digests the guards compare against.

## Code Commentary

### Logic

Every conversion in both directions lives here, so the column order, the canonical JSON text form of a
typed column and the digest recomputation have exactly one owner per table. The module is the largest of
this leaf's new files and the repository's file-size rail is the reason it is not larger: no module may
cross 1200 lines.

**Two seals are recomputed on the way out rather than trusted**, on the shipped rule that a row whose text
was rewritten behind its identity must not be served as the revision that identity names: a claim
revision's `content_digest` and an observation revision's `content_digest` are re-derived from the stored
payload. `decode_record_revision_row`, `decode_claim_row`, `decode_subject_row`, `decode_coverage_row` and
`decode_observation_row` are the decode half.

The **observable-row digests** are the other half of the same idea. A claim's ledger row, a subject edge, a
claimed-coverage edge and an observation's own row are not sealed revisions, so an operation that names one
of them by digest computes that digest from the row as it stands: `evidence_claim_row_digest`,
`subject_row_digest`, `coverage_row_digest` and `observation_row_digest`. The read path exposes the same
values, so a caller carries an expectation straight from a read instead of deriving a second identity
scheme.

**`OBSERVATION_COLUMNS` is a declared order, not a convenience.** The observation's insert statement is
derived from it, so a column added to the codec and not to the statement — or the reverse — cannot produce a
silently shifted row. The decode helpers `_snapshot_of_columns`, `_artifact_of_columns`,
`_publication_of_columns` and `_toolchain_of_column` rebuild the typed sub-objects from that same order.

**The envelope digests are computed here rather than borrowed from the facet codecs.** This leaf appends
its own tables and its own record kinds; a shared digest helper would have to be a new function in the facet
module, which is another leaf's file, and an evidence claim's identity would then be defined by a module
that does not own it. The formula is the shipped one, restated here for the same reason a generation
restates the DDL it extends: the *value* is part of this record's contract, and a case asserts the two agree
field by field.

`CLAIM_BY_ID` and the five sibling statements beside it are the read queries whose declared order columns
land in `read_queries.py`.

### Conventions

A codec module owns row ↔ value conversion and nothing else: no policy, no refusal, no judgement. A digest
function is named after the row it seals, and the sealed revision digests are recomputed rather than read
back from the row's own text.

### Invariants And Boundaries

- **Column order is contract.** A statement derived from the declared order and a codec derived from the
  same order cannot disagree; a statement that restates the order can.
- **A digest is computed from the row as it stands.** No path in this module returns a stored digest of an
  observable row without recomputing it.
- **No blob, no second content store.** The only digest here that describes something outside the database
  is the artifact reference's, and it is carried as text.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The revision payload version and the envelope draft the pair of rows is written from. | `RECORD_REVISION_PAYLOAD_VERSION`; `EnvelopeDraft` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:76-76; mcp/src/agents_remember/memory/knowledge/evidence_records.py:83-96 |
| The envelope row and its digest — the ledger pair every record kind shares. | `envelope_record_row`; `envelope_record_row_digest` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:99-109; mcp/src/agents_remember/memory/knowledge/evidence_records.py:113-134 |
| The revision row, its recomputed seal, and the decode that re-derives it rather than trusting the row's text. | `record_revision_row`; `record_revision_digest`; `decode_record_revision_row` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:150-160; mcp/src/agents_remember/memory/knowledge/evidence_records.py:164-177; mcp/src/agents_remember/memory/knowledge/evidence_records.py:182-215 |
| The claim's ledger row and its observable-row digest. | `claim_row`; `evidence_claim_row_digest` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:221-224; mcp/src/agents_remember/memory/knowledge/evidence_records.py:227-238 |
| The subject edge's row, its table and revision column, and its observable-row digest. | `subject_row`; `subject_table`; `subject_revision_column`; `subject_row_digest` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:263-271; mcp/src/agents_remember/memory/knowledge/evidence_records.py:274-279; mcp/src/agents_remember/memory/knowledge/evidence_records.py:282-287; mcp/src/agents_remember/memory/knowledge/evidence_records.py:290-299 |
| The claimed-coverage edge's row and its observable-row digest. | `coverage_row`; `coverage_row_digest` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:329-341; mcp/src/agents_remember/memory/knowledge/evidence_records.py:344-353 |
| The observation's cells and the declared column order the insert statement is derived from. | `observation_cells`; `OBSERVATION_COLUMNS` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:398-435; mcp/src/agents_remember/memory/knowledge/evidence_records.py:442-459 |
| The observation's row, its observable-row digest and the typed sub-object rebuilds. | `observation_row`; `observation_row_digest`; `_artifact_of_columns`; `_publication_of_columns` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:463-467; mcp/src/agents_remember/memory/knowledge/evidence_records.py:470-486; mcp/src/agents_remember/memory/knowledge/evidence_records.py:511-532; mcp/src/agents_remember/memory/knowledge/evidence_records.py:536-552 |
| The read statements whose declared order columns live in the read-queries module. | `CLAIM_BY_ID`; `OBSERVATION_BY_ID` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:659-659; mcp/src/agents_remember/memory/knowledge/evidence_records.py:678-679 |
| The case that asserts there is no blob column and no second content store. | "def test_there_is_no_blob_column_and_no_second_content_store(" | mcp/tests/test_knowledge_evidence_observations.py:871-905 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 1 claim(s) here (1 x citation_claim_reopened). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.

- 2026-09-18T04:20:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): created this one-to-one card for the supporting records' row codecs. It records the single owner per table for order, canonical text and digests, the two seals recomputed on the way out, the observable-row digests, and why the envelope digests are restated here rather than borrowed from the facet codecs. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
