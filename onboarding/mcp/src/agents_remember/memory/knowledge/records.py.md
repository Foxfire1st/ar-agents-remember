# mcp/src/agents_remember/memory/knowledge/records.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Decodes sealed invariant, family and membership rows from the derived index and computes their read-time content digests.

## Code Commentary

Typed columns, authorship and state-at-origin are decoded under their recorded schema. Revision and membership decoders verify the declared payload seals before returning values. The former row-building, source-anchor and predecessor write helpers were removed. This codec does not insert canonical records or authorize a writer; the index is a projection of admitted text knowledge.

### Logic

Typed columns are stored as canonical JSON, and `decode_typed_column` decodes through `decoded_json`, which
refuses duplicate keys so ambiguous stored text is a refusal rather than last-one-wins.

`decode_authorship` and `_LOCATOR_ADAPTER` (a `TypeAdapter` over the `SourceLocator`
discriminated union) are the typed-column specializations.

Row codecs: `decode_repository_row`, `decode_invariant_row` (which also derives
`invariant_row_digest` — the expected-row digest a label edit names), `decode_revision_row`
(`decode_predecessor_rows` is deleted with the predecessor edge tables).

**The graph half's codecs are all here too**: `family_row_digest` / `decode_family_row`,
`decode_family_revision_row`, `member_row_digest` / `decode_member_row`. Each expected-row digest is computed over a mapping carrying
an explicit `"table"` key, so a digest from one table can never be mistaken for another table's.

`decode_state_at_origin` narrows a
stored origin state to the two authored states and raises `KnowledgeStorageError` for anything else.

### Conventions

`decode_revision_row` verifies the seal on the way out: it rebuilds the aggregate from the stored columns,
recomputes `revision_payload_digest` and raises `KnowledgeStorageError` when the stored digest differs. A reader
that decoded a row without recomputing its digest would accept a rewritten payload as its own identity.

`decode_family_revision_row` applies the same rule to the family payload, and it still takes the predecessor tuple as an
argument: callers pass the empty tuple, since the predecessor edge tables are gone and decoded predecessors are always (). A cell rewritten behind a sealed revision therefore breaks the seal on read — the only way to change sealed
content without rewriting the row itself, and the reason the seal is verified rather than trusted.

### Invariants And Boundaries

- The clause order of `conditions`/`exclusions` is preserved through storage; cell order otherwise follows the stored row, since no predecessor set is decoded anymore.

- The row codecs never write and never decide a refusal: they convert. Refusal policy belongs to `store.py`, and
  the factories to `refusals.py`.

- A stored origin state outside `proposed`/`accepted` is a
  storage defect, not a refused request — hence `KnowledgeStorageError` rather than a typed `KnowledgeRefusal`.

- **Expected-row digests are table-scoped.** The `"table"` key inside each digest mapping means a
  `family_row_digest` can never validate a `source_anchor` row.

### Todos

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- `decode_revision_row` owns the current boundary described above. [12]
- `decode_family_revision_row` owns the current boundary described above. [13]
- `decode_member_row` owns the current boundary described above. [14]
- `decode_typed_column` owns the current boundary described above. [15]

- - The canonical JSON typed-column encoding used for every structured column. [16]
- - The read path re-derives the seal and treats a mismatch as a damaged store. [17]

- - The predecessor edge tables are gone, so no edge rows are decoded and decoded predecessors are always (). [18]

- - The family identity and family revision codecs, including the seal-verifying decode over the stored cells. [19]
- - The relation codecs and their table-scoped expected-row digests. [20]
- - The digest the read path recomputes, for both payloads. [21]
- - The canonical encoder and duplicate-key-refusing decoder this module stores through. [22]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
