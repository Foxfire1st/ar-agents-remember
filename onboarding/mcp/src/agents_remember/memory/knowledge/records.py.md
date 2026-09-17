# mcp/src/agents_remember/memory/knowledge/records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e`|
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[memory route overview](../../../overview.md)

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

**The graph half's codecs are all here too**, one per table the relation modules write: `family_row` /
`family_row_digest` / `decode_family_row`, `family_revision_row` / `sealed_family_revision_from_draft` /
`decode_family_revision_row`, `family_predecessor_rows`, `anchor_row_digest`, `member_row` / `member_row_digest` /
`decode_member_row`, and `claim_row` / `claim_row_digest` / `decode_claim_row`. Each builder's column order
matches the table's `CANONICAL_COLUMNS` entry, and each expected-row digest is computed over a mapping carrying
an explicit `"table"` key, so a digest from one table can never be mistaken for another table's.

`sealed_revision_from_draft` turns a `RevisionDraft` into a complete `InvariantRevision`, sorting the predecessor
set because it enters the digest, and seeding the digest before calling `models.knowledge.digest.sealed_revision`;
`sealed_family_revision_from_draft` does the same for a `FamilyRevisionDraft`. `decode_state_at_origin` narrows a
stored origin state to the two authored states and raises `KnowledgeStorageError` for anything else, and
`stored_realization_role` narrows a stored role against the closed `RealizationRole` vocabulary the same way — an
unrecognised stored role is a storage defect, never a new role.

The canonical identity text is derived here rather than accepted from a caller: `anchor_row` writes
`str(anchor.anchor_id)` and `decode_anchor_row` reconstructs `UUID(str(row[1]))`, which is what lets the
vocabulary declare a real `UUID` field.

### Conventions

`decode_revision_row` verifies the seal on the way out: it rebuilds the aggregate from the stored columns,
recomputes `revision_payload_digest` and raises `KnowledgeStorageError` when the stored digest differs. A reader
that decoded a row without recomputing its digest would accept a rewritten payload as its own identity.

`decode_family_revision_row` applies the same rule to the family payload, and it takes the predecessor set as an
argument for a reason: the caller (`families.get_family_revision`) reads the **stored predecessor edges** from
`family_predecessor` and passes them in, so the digest is recomputed over the stored row *plus* the stored edges.
An edge edited behind a sealed revision therefore breaks the seal on read — the only way to change a sealed
predecessor set without rewriting the row itself, and the reason the seal is verified rather than trusted.

### Invariants And Boundaries

- The clause order of `conditions`/`exclusions` is preserved through storage; only the predecessor **set** is
  sorted, because that order is not authored information while clause order is.
- The row codecs never write and never decide a refusal: they convert. Refusal policy belongs to `store.py`, and
  the factories to `refusals.py`.
- A stored origin state outside `proposed`/`accepted`, or a stored role outside the closed vocabulary, is a
  storage defect, not a refused request — hence `KnowledgeStorageError` rather than a typed `KnowledgeRefusal`.
- **A codec owns its table's column order.** The builders here are the only place a row tuple is constructed, and
  each must match `schema.CANONICAL_COLUMNS`; a builder that drifts is caught by the schema-conformance node that
  compares `PRAGMA table_info` against the manifest for all ten tables.
- **Expected-row digests are table-scoped.** The `"table"` key inside each digest mapping means a
  `family_row_digest` can never validate a `source_anchor` row.
- `anchor_row`/`decode_anchor_row` were declared by L1 for a table nothing wrote; they now carry the anchor
  module's writes and reads, and the canonical identity text they derive is what makes the `UUID` field legal.

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
| The canonical JSON typed-column encoding used for every structured column. | `encode_typed_column`; `decode_typed_column` | mcp/src/agents_remember/memory/knowledge/records.py:56-61; mcp/src/agents_remember/memory/knowledge/records.py:64-67 |
| The read path re-derives the seal and treats a mismatch as a damaged store. | `decode_revision_row` | mcp/src/agents_remember/memory/knowledge/records.py:153-189 |
| Sealing a draft, including the sorted predecessor set that enters the digest. | `sealed_revision_from_draft` | mcp/src/agents_remember/memory/knowledge/records.py:190-214 |
| The exact twelve-column revision tuple written by the operation. | `revision_row` | mcp/src/agents_remember/memory/knowledge/records.py:134-152 |
| The predecessor edge rows and their sorted decode. | `predecessor_rows`; `decode_predecessor_rows` | mcp/src/agents_remember/memory/knowledge/records.py:215-225 |
| The anchor codec, which derives the canonical identity text at the storage boundary. | `anchor_row`; `anchor_row_digest`; `decode_anchor_row` | mcp/src/agents_remember/memory/knowledge/records.py:226-236; mcp/src/agents_remember/memory/knowledge/records.py:366-381; mcp/src/agents_remember/memory/knowledge/records.py:237-246 |
| The family identity and family revision codecs, including the seal-verifying decode that reads the stored edges. | `family_row`; `family_revision_row`; `sealed_family_revision_from_draft`; `decode_family_revision_row`; `family_predecessor_rows` | mcp/src/agents_remember/memory/knowledge/records.py:253-286; mcp/src/agents_remember/memory/knowledge/records.py:287-302; mcp/src/agents_remember/memory/knowledge/records.py:303-326; mcp/src/agents_remember/memory/knowledge/records.py:327-356; mcp/src/agents_remember/memory/knowledge/records.py:357-365 |
| The relation codecs and their table-scoped expected-row digests. | `member_row`; `member_row_digest`; `decode_member_row`; `claim_row`; `claim_row_digest`; `decode_claim_row` | mcp/src/agents_remember/memory/knowledge/records.py:382-391; mcp/src/agents_remember/memory/knowledge/records.py:392-412; mcp/src/agents_remember/memory/knowledge/records.py:413-428; mcp/src/agents_remember/memory/knowledge/records.py:429-440; mcp/src/agents_remember/memory/knowledge/records.py:441-462; mcp/src/agents_remember/memory/knowledge/records.py:463-483 |
| The closed stored-role vocabulary a stored row is narrowed against. | `stored_realization_role` | mcp/src/agents_remember/memory/knowledge/records.py:484-498 |
| The digest the read path recomputes, for both payloads. | `revision_payload_digest`; `family_revision_payload_digest` | mcp/src/agents_remember/models/knowledge/digest.py:55-58; mcp/src/agents_remember/models/knowledge/digest.py:93-96 |
| The canonical encoder and duplicate-key-refusing decoder this module stores through. | `canonical_json_bytes`; `decoded_json` | mcp/src/agents_remember/kernel/canonical_json.py:27-31; mcp/src/agents_remember/kernel/canonical_json.py:46-61 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T06:49:47+00:00: Generated citation repair: `encode_typed_column`; `decode_typed_column` repointed to mcp/src/agents_remember/memory/knowledge/records.py:56-61; mcp/src/agents_remember/memory/knowledge/records.py:64-67. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): **superseded the L1 statement that the anchor codec is for a table nothing writes**, and extended the card to the graph half. The anchor codec now carries the anchor module's writes and reads, and the canonical identity text it derives (`str(anchor.anchor_id)`) is what makes the vocabulary's real `UUID` field legal. Fifteen codecs were added for the family, family-revision, family-predecessor, membership and claim tables; the family-revision decode recomputes the seal over the stored row **plus the stored predecessor edges**, and every expected-row digest is table-scoped by construction. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new row codec module. It records that the read path re-derives the seal, that only the predecessor set is sorted, and that an out-of-vocabulary stored origin state is a storage defect rather than a refusal. Verification metadata remains empty until closeout stamps the code commit.
