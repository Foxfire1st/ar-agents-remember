# mcp/src/agents_remember/application/review_curator_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_curator_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:02:28+00:00 |
| lastVerifiedCommitHash | `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`|
| lastVerifiedCommitDate | 2026-09-27T07:57:14+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Read the curator records belonging to one resolved comparison and provide their existing immutable artifact references.

## Code Commentary

### Logic

Live reads address the current canonical authority; recorded reads select only the comparison manifest's unique reserved curator record pin. The bound digest is opened by the shared typed generation reader, and the entire artifact set, source line, assessment count and channel are checked. A missing pin with old uncaptured metadata stays not-selected; expected missing/corrupt pins are unavailable. Neither case follows today's canonical pointer.

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
| Live and recorded reads select different explicit owner addresses. | `review_curator_records` | mcp/src/agents_remember/application/review_curator_records.py:40-69 |
| Positive supplied records require complete matching owner provenance. | `require_curator_record_inputs` | mcp/src/agents_remember/application/review_curator_records.py:82-108 |
| History reads only the pinned immutable generation. | `_historical_records` | mcp/src/agents_remember/application/review_curator_records.py:111-139 |
| Uncaptured history is distinct from missing expected content. | `_without_pin` | mcp/src/agents_remember/application/review_curator_records.py:142-158 |

## Cross-Repo References

No separate repository supplies this contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | — | — |

## Update History

- 2026-09-27T05:02:28+00:00 — Created this source-mirrored card for the durable assessment-history boundary. Verification hash/date remain blank until normal closeout records the actual accepted code commit.
