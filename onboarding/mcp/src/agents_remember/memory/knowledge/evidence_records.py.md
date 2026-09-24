# mcp/src/agents_remember/memory/knowledge/evidence_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/evidence_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T21:55:00+02:00 |
| lastVerifiedCommitHash | `06ed70cfcde7e3860ee5b53435727e7512e4335c` |
| lastVerifiedCommitDate | 2026-09-24T10:53:01+02:00|
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
| **The claim-identity listing, decoding nothing, and the whole-listing form unchanged beside it: both run the same identity statement, so the two cannot disagree about which identities exist.** | `claim_ids`; `all_claims`; `CLAIM_IDS_OF_REPOSITORY` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:1042-1054; mcp/src/agents_remember/memory/knowledge/evidence_records.py:1057-1060; mcp/src/agents_remember/memory/knowledge/evidence_records.py:843-846 |
| **The single-record reader each listed identity is then read through, which is what makes a per-record guard possible without a second reader.** | `claim_record`; `claimed_coverage_of_claim` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:928-932; mcp/src/agents_remember/memory/knowledge/evidence_records.py:1124-1146 |
| **The composing reader this listing exists for: one identity read at a time, a damaged claim named while its siblings are supplied.** | `_claim_records`; `claim_ids` | mcp/src/agents_remember/application/review_evidence_records.py:498-521; mcp/src/agents_remember/application/review_evidence_records.py:548-572|
| **The registered surface gained exactly one name (`claim_ids`), and the case that measures the isolation it makes reachable.** | `__all__`; `test_a_damaged_evidence_claim_is_named_while_its_siblings_are_supplied` | mcp/src/agents_remember/memory/knowledge/evidence_records.py:1148-1180; mcp/tests/test_knowledge_review_evidence_channels.py:719-847 |
| The case that asserts there is no blob column and no second content store. | "def test_there_is_no_blob_column_and_no_second_content_store(" | mcp/tests/test_knowledge_evidence_observations.py:871-905 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T21:55:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **this owner gained one read, and it is a split rather than a new reader.** `claim_ids` (`memory/knowledge/evidence_records.py:1042-1054`) runs the existing `CLAIM_IDS_OF_REPOSITORY` statement and decodes nothing, so a composing reader can list the claim identities and then read each one through the owner's own single-record reader — which is what makes "one damaged claim is named while its siblings are still supplied" reachable at all under `ICR-R14@v1`. `all_claims` is **unchanged** and stays the all-or-nothing form over the same statement, so the listing and the whole-record read cannot come to disagree about which identities exist; the Logic section now states that split and the Conventions/Invariants record that neither is derived from the other. `__all__` gained exactly one name. **Citation accounting:** the four rows citing ranges into this file were re-read and are unchanged — this leaf's insertion sits at `:1042`, below every construct they name — and four rows were **added** for the listing, the single-record reader it pairs with, the one composing reader it exists for and the registered surface with the case that measures the isolation. Nothing was re-worded, and no row was dropped. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` now name the **production line this reading was against** — `d80a0513e928ef29a973527d09597c82c96fde87`, the master line's current tip and this leaf's base — replacing the previous pair rather than leaving a stamp no reading in this pass measured; the candidate is uncommitted, so no commit contains the content a stamp would claim to have verified, and the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates.
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 1 claim(s) here (1 x citation_claim_reopened). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.

- 2026-09-18T04:20:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): created this one-to-one card for the supporting records' row codecs. It records the single owner per table for order, canonical text and digests, the two seals recomputed on the way out, the observable-row digests, and why the envelope digests are restated here rather than borrowed from the facet codecs. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; what was actually read is this leaf's uncommitted working tree, and closeout owns the stamp once the code commit exists.
