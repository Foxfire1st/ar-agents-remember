# mcp/src/agents_remember/application/review_curator_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_curator_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:05:09+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Read the curator records belonging to one resolved comparison and provide their existing immutable artifact references.

## Code Commentary

### Logic

Live reads address the current canonical authority; recorded reads select only the comparison manifest's unique reserved curator record pin. The bound digest is opened by the shared typed generation reader, and the entire artifact set, source line, assessment count and channel are checked. A missing pin with old uncaptured metadata stays not-selected; expected missing/corrupt pins are unavailable. Neither case follows today's canonical pointer.

**An unreadable owner reads as `unavailable`, never as a failed review (MIK-L25 Q8, fixed in MIK-L31 and accepted at
2026-09-30T05:36:19).** A closed leaf can bind about a hundred owner artifacts (ICR-L47 binds 94); with them
missing, the owner's error named every path and the channel detail listed them again (24,725 characters), over the
20,000-character prose bound, so the pydantic `ValidationError` failed the whole review. `_unreadable_detail`
keeps the landed wording (`The curator owner could not be read (<paths>): <error>`) whenever it fits
`PROSE_MAX_LENGTH`; only a detail over the bound names the count and the first `_NAMED_ARTIFACTS` (3) artifacts
(`_artifacts_named`: "<n> bound artifacts, listed as unreadable; the first are …") and bounds the owner's own error
to `_ERROR_CHARACTERS` (4,000) with a stated remainder (`_bounded`). The channel's `unreadable` field still lists
every artifact. On L25's 29 unconverted reads, 26 are byte-identical to base; the only 3 that differ are the ICR
L47 subject+records reads, which were a `ValidationError` on base and are now a `review` with the assessments
channel `unavailable` and 94 unreadable artifacts.

Positive explicit inputs must equal the immutable owner assessment objects, complete artifact set and one exact assessment channel. Omitted, duplicate or incompatible provenance refuses before capture. Explicit empty inputs retain their meaning and do not trigger an implicit live-owner lookup.

### Conventions

Use the existing typed owners and exact recorded identities. Keep operation evidence and candidate provenance in task notes.

### Invariants And Boundaries

Reserved owner names identify trusted curator inputs, not arbitrary evidence citations. The bridge returns records and availability; it does not author assessments, infer a semantic result or discard other readable channels. A non-applicable plane remains explicit unavailable metadata.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured. The repository declarations below support this contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The cited owners carry the behavior and failure boundaries described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| Live and recorded reads select different explicit owner addresses; an unreadable owner is an `unavailable` channel with every artifact listed. | `review_curator_records` | mcp/src/agents_remember/application/review_curator_records.py:41-70 |
| The detail keeps its landed wording when it fits the prose bound, and otherwise names the count and the first three artifacts with the error bounded. | `_NAMED_ARTIFACTS`; `_ERROR_CHARACTERS`; `_unreadable_detail`; `_artifacts_named`; `_bounded` | mcp/src/agents_remember/application/review_curator_records.py:78-105 |
| Both branches pinned apart: 100 artifacts summarised, 10 kept exactly (review F6, R2-2). | `_curator_channel`; `test_a_leaf_binding_many_missing_curator_artifacts_reads_as_unavailable` | mcp/tests/test_review_assessment_history.py:422-434; mcp/tests/test_review_assessment_history.py:437-460 |
| Positive supplied records require complete matching owner provenance. | `require_curator_record_inputs` | mcp/src/agents_remember/application/review_curator_records.py:118-144 |
| History reads only the pinned immutable generation. | `_historical_records` | mcp/src/agents_remember/application/review_curator_records.py:147-175 |
| Uncaptured history is distinct from missing expected content. | `_without_pin` | mcp/src/agents_remember/application/review_curator_records.py:178-194 |

## Cross-Repo References

No separate repository supplies this contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | — | — |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Logic records the MIK-L25 Q8 fix carried to L31 (ruling 2026-09-29T22:22:37) and accepted at 05:36:19: an over-length unreadable-owner detail is summarised (count, first three artifacts, error bounded at 4,000 characters) and a detail that fits keeps its landed wording exactly (review F6 at 06:10:21, pinned apart by R2-2 at 06:47:03). The first row is reworded; two rows added.
- 2026-09-30T07:52:59+00:00: Generated citation repair: `require_curator_record_inputs` repointed to mcp/src/agents_remember/application/review_curator_records.py:118-144. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T07:52:59+00:00: Generated citation repair: `_historical_records` repointed to mcp/src/agents_remember/application/review_curator_records.py:147-175. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-27T05:02:28+00:00 — Created this source-mirrored card for the durable assessment-history boundary. Verification hash/date remain blank until normal closeout records the actual accepted code commit.
