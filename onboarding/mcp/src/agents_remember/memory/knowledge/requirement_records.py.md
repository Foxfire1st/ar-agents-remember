# mcp/src/agents_remember/memory/knowledge/requirement_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/requirement_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `a066550591eb3116ae008cc0d57f3558b0af52c5` |
| lastVerifiedCommitDate | 2026-09-18T07:03:08+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l19` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Row codecs for the requirement-revision record group, which stores nothing of its own.** A
requirement revision *is* an envelope record: one `knowledge_record` row naming the
`requirement_revision` kind and the route that governs it, plus one `record_revision` row per
immutable revision holding the payload and its content digest. This module owns the SQL text for
those five statements and the two frozen dataclasses they produce — it executes nothing.

**Why the record group needs a codec rather than a table.** `KS-R19@v1` requirement 1.1 forbids a
second envelope, a second revision aggregate and a new identity mechanism; the delivered envelope
already carries record identity, `kind`, `authority_home`, `lifecycle`, the governing route, and the
immutable revision with its frozen payload, content digest and predecessor. A table holding
per-revision state would *be* the second revision aggregate the packet forbids, so the record group
lives in the shipped tables and declares only the shape of the rows it puts there.

## Code Commentary

### Logic

- Two `(kind, record_schema)`-symmetrical statement pairs. `REQUIREMENT_RECORD_INSERT` (50-53) and
  `REQUIREMENT_REVISION_INSERT` (55-58) name every column explicitly, so a column added to the
  envelope tables cannot silently change what this record group writes.
- `requirement_record_row` (106-131) and `requirement_revision_row` (134-152) build the row tuples
  from a request. **`kind`, `record_schema` and `lifecycle` are declared here, not accepted from the
  caller** — the shipped `lifecycle` column is therefore always `"proposed"` even when the payload's
  `state_at_origin` is `accepted`, which is the storage-plane half of "records an acceptance, never
  produces one". `authority_home` is read from the store's own repository row
  (`requirements.py:_authority_home`), so a caller cannot declare a home it is not writing into.
- The **seal is recomputed on the way out**, not trusted: `decode_requirement_revision_row` (176-216)
  recomputes the content digest and refuses a row that does not match it — a payload rewritten behind
  its identity is never served as that revision.
- `_validated_payload` (219-240) resolves the frozen model **from `PAYLOAD_MODELS`** rather than by
  the name this module happens to hold, so the read path validates through the same registry the write
  path admitted through. A stored payload that no longer validates is a storage defect, not a refusal.

### Conventions

- **Two different failure kinds, deliberately.** A caller error in the request is a `KnowledgeRefusal`
  returned by `requirements.py`; a row that cannot be decoded is a raised `KnowledgeStorageError`.
  Nothing here returns a refusal receipt, because nothing here is reachable by a caller who could
  have passed something different.
- **The generic envelope tuple is reused, not restated.** The revision tuple and its digest come from
  `facet_records.record_revision_row` / `record_revision_digest` (34-38), so the envelope's row shape
  and its identity are computed in exactly one place for every record group that uses the envelope.
- Both row types are `@dataclass(frozen=True)`, so a decoded row is a value.

### Invariants And Boundaries

- **No execution.** This module declares SQL text and decodes tuples; it holds no connection, takes no
  connection parameter, and cannot write on any path.
- **A mismatched row is a refused decode, never a coerced one.** A record row whose kind or schema is
  not this record group's declared pair, a payload that is not a JSON object, a payload that does not
  validate, and a digest that does not match all raise rather than being repaired into a value.
- **The damage message names the recovery.** A digest mismatch says the row was altered behind its
  identity, that the store should be treated as damaged, and that the revision should be recovered
  from an intact snapshot — it does not invite the reader to accept the row.
- **Boundary.** This module does not own the envelope's columns (`schema_v2.py`), the payload seam
  (`record_envelope.py`), the operation surface or its guards (`requirements.py`), or the derived
  views (`requirement_views.py`).

### Todos

None recorded. There is no production caller of this record group yet: no MCP tool and no serving
route wires `record_requirement_revision` or `read_requirement_revisions`, so these codecs are
reachable today only through the module's Python API.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two INSERTs this record group writes through: every envelope column named, no column inferred. | `REQUIREMENT_RECORD_INSERT`; `REQUIREMENT_REVISION_INSERT` | mcp/src/agents_remember/memory/knowledge/requirement_records.py:50-58 |
| The three SELECTs it reads back: one record row, every record row of the kind, every revision of one record. | `REQUIREMENT_RECORD_ROW`; `REQUIREMENT_RECORD_ROWS_OF_KIND`; `REQUIREMENT_REVISION_ROWS` | mcp/src/agents_remember/memory/knowledge/requirement_records.py:60-74 |
| The frozen record row a decoded row becomes. | `StoredRequirementRecord` | mcp/src/agents_remember/memory/knowledge/requirement_records.py:77-88 |
| The frozen revision row a decoded row becomes. | `StoredRequirementRevision` | mcp/src/agents_remember/memory/knowledge/requirement_records.py:89-105 |
| The record-row builder: `kind`, `record_schema`, `lifecycle` and the authority home declared by the record group rather than accepted from the caller. | `requirement_record_row` | mcp/src/agents_remember/memory/knowledge/requirement_records.py:106-133 |
| The revision-row builder, which reuses the generic envelope tuple and digest. | `requirement_revision_row` | mcp/src/agents_remember/memory/knowledge/requirement_records.py:134-154 |
|**The seal recomputed on the way out — a row altered behind its identity is refused rather than served.**|`decode_requirement_revision_row`| mcp/src/agents_remember/memory/knowledge/requirement_records.py:176-218 |
| The frozen model resolved from the registry the write path admitted through, not by name. | `_validated_payload` | mcp/src/agents_remember/memory/knowledge/requirement_records.py:219-240 |
|The generic envelope revision tuple and digest this record group reuses instead of restating.|`record_revision_row`; `record_revision_digest`| mcp/src/agents_remember/memory/knowledge/facet_records.py:193-208 |
| The envelope tables these statements address, and the immutable-revision trigger that backs the codec's seal. | `record_revision_no_rewrite`; `APPENDED_TABLE_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:103-224 |
|The record-group operation surface these codecs serve, including the authority home it reads from the store.|`record_requirement_revision`; `_authority_home`| mcp/src/agents_remember/memory/knowledge/requirements.py:89-112; mcp/src/agents_remember/memory/knowledge/requirements.py:504-514 |
| The row-codec round trip and the tampered-payload case that proves the seal. | "test_the_revision_row_codec_round_trips_through_the_envelope_tuple" | mcp/tests/test_knowledge_requirement_revisions.py:548-581 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:05+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): created this one-to-one card for the requirement record group's row codec. It records that the record group deliberately has no table of its own and why (a per-revision state table would be the second revision aggregate `KS-R19@v1` requirement 1.1 forbids), the two failure kinds it keeps apart (a returned refusal for a caller's request versus a raised `KnowledgeStorageError` for a row that cannot be decoded), and the two facts a reader would otherwise have to re-derive: `kind`, `record_schema` and `lifecycle` are **declared by the record group rather than accepted from the caller** — which is why the envelope's `lifecycle` stays `proposed` even for an `accepted` origin payload — and the stored seal is **recomputed on read** so a payload rewritten behind its identity is refused instead of served. It also records that the revision tuple and its digest are **reused from `facet_records`** rather than restated, so the envelope's identity is computed in one place for every record group, and the standing fact that no production module imports this record group yet. Verification metadata advances to the leaf's base commit `e963a01c` because the body was read against the current source; the code commit does not exist yet and closeout owns that stamp.
