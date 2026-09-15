# mcp/src/agents_remember/memory/knowledge/records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash | `60e0820e6cb3b1d160518b9f8c7ac6241323a281`|
| lastVerifiedCommitDate | 2026-09-15T22:46:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

## Purpose

The row codecs between the typed knowledge vocabulary and the declared columns. Every conversion in both
directions lives here, so the column order, the canonical JSON text form of a typed column and the digest
recomputation have exactly one owner.

## Code Commentary

### Logic

Typed columns are stored as canonical JSON: `encode_typed_column` dumps `model_dump(mode="json")` through
`kernel.canonical_json.canonical_json_bytes`, and `decode_typed_column` decodes through `decoded_json`, which
refuses duplicate keys so ambiguous stored text is a refusal rather than last-one-wins.

`encode_authorship`/`decode_authorship` and `_LOCATOR_ADAPTER` (a `TypeAdapter` over the `SourceLocator`
discriminated union) are the typed-column specializations.

Row codecs: `repository_row`/`decode_repository_row`, `invariant_row`/`decode_invariant_row` (which also derives
`invariant_row_digest` — the expected-row digest a label edit names), `revision_row` (the exact twelve-column
tuple), `decode_revision_row`, `predecessor_rows` (sorted), `decode_predecessor_rows`,
`anchor_row`/`decode_anchor_row`, and `row_mapping` (which pairs one row with its declared column names for
diagnostics and tests, using `zip(..., strict=True)`).

`sealed_revision_from_draft` turns a `RevisionDraft` into a complete `InvariantRevision`, sorting the predecessor
set because it enters the digest, and seeding the digest before calling `models.knowledge.digest.sealed_revision`.
`decode_state_at_origin` narrows a stored origin state to the two authored states and raises
`KnowledgeStorageError` for anything else.

### Conventions

`decode_revision_row` verifies the seal on the way out: it rebuilds the aggregate from the stored columns,
recomputes `revision_payload_digest` and raises `KnowledgeStorageError` when the stored digest differs. A reader
that decoded a row without recomputing its digest would accept a rewritten payload as its own identity.

### Invariants And Boundaries

- The clause order of `conditions`/`exclusions` is preserved through storage; only the predecessor **set** is
  sorted, because that order is not authored information while clause order is.
- The row codecs never write and never decide a refusal: they convert. Refusal policy belongs to `store.py`, and
  the factories to `refusals.py`.
- A stored origin state outside `proposed`/`accepted` is a storage defect, not a refused request — hence
  `KnowledgeStorageError` rather than a typed `KnowledgeRefusal`.
- `anchor_row`/`decode_anchor_row` exist for the schema's `source_anchor` table, which this leaf does not write;
  they are the codec the read/diff leaves reuse.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical JSON typed-column encoding used for every structured column. | `encode_typed_column`; `decode_typed_column` | mcp/src/agents_remember/memory/knowledge/records.py:38-49 |
| The read path re-derives the seal and treats a mismatch as a damaged store. | `decode_revision_row` | mcp/src/agents_remember/memory/knowledge/records.py:135-169 |
| Sealing a draft, including the sorted predecessor set that enters the digest. | `sealed_revision_from_draft` | mcp/src/agents_remember/memory/knowledge/records.py:172-194 |
| The exact twelve-column revision tuple written by the operation. | `revision_row` | mcp/src/agents_remember/memory/knowledge/records.py:116-132 |
| The predecessor edge rows and their sorted decode. | `predecessor_rows`; `decode_predecessor_rows` | mcp/src/agents_remember/memory/knowledge/records.py:197-205 |
| The anchor codec for the table this leaf does not write but the read/diff leaves reuse. | `anchor_row`; `decode_anchor_row` | mcp/src/agents_remember/memory/knowledge/records.py:208-226 |
| The digest the read path recomputes. | `revision_payload_digest` | mcp/src/agents_remember/models/knowledge/digest.py:48-51 |
| The canonical encoder and duplicate-key-refusing decoder this module stores through. | `canonical_json_bytes`; `decoded_json` | mcp/src/agents_remember/kernel/canonical_json.py:27-31; mcp/src/agents_remember/kernel/canonical_json.py:46-61 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new row codec module. It records that the read path re-derives the seal, that only the predecessor set is sorted, and that an out-of-vocabulary stored origin state is a storage defect rather than a refusal. Verification metadata remains empty until closeout stamps the code commit.
