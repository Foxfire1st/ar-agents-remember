# mcp/src/agents_remember/memory/knowledge/anchors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/anchors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate | 2026-09-16T08:41:27+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

## Purpose

The anchor half of the knowledge graph: an authored source location, stored exactly as recorded.
**Storage and resolution are different concerns.** An anchor records the repository-relative path,
the source identity the author attributed and the locator shape; it is written and read back without
consulting a filesystem, a Git object or a parser. Whether that location still resolves in a selected
snapshot is a fact a later reader reports — a missing source is never a reason to retire a stored
attribution.

This module owns the `source_anchor` table. It is the only owner of an anchor's lifetime: removal is
explicit, by identity, one row at a time, and never while a stored realization claim still cites it.

## Code Commentary

### Logic

- `create_source_anchor` resolves the bound namespace, takes the candidate lock, and runs one
  immediate transaction. `source_anchor_from_draft(draft, provenance)` is the single construction
  point that attaches the provenance envelope to the caller's draft, so a caller never supplies its
  own provenance.
- An identical re-declaration answers `state="no_change"`; the same identity carrying a different
  stored payload is `duplicate_identity` with both digests in `expected`/`observed`.
- `remove_source_anchor` refuses when the row is absent (`missing_expected_row`) and refuses when a
  stored claim cites it (`relationship_constraint` naming the citing claim). Both checks precede the
  `DELETE`.
- `find_claim_citing_anchor` deliberately lives here rather than in `realizations.py`: "may this
  anchor be removed" is the anchor's own lifetime question, and the anchor module must not depend on
  the claim module's internals to answer it.
- `insert_anchor_row` is the narrow write hook the realization operation calls so a newly authored
  anchor and its claim commit as one act of authorship.

### Conventions

- Reads go through `connection.fetch_one` and hand the stored row to `records.decode_anchor_row`.
  No reader builds its own tuple-checking shape.
- Every mutating entry point takes the opened store as its first argument and reuses the store's
  `_exclusive_candidate_lock` and `_within_immediate`; the failure context names this module's
  operation and table so a mapped SQLite failure reports the real row.
- Refusals are returned as a typed result through `_anchor_result` / `_anchor_refusal`, never raised
  past the public operation.

### Invariants And Boundaries

- **No resolution, ever, on the write path.** Nothing here opens a file, reads a Git object or runs a
  parser; an absent path and an unsupported locator kind both round-trip byte-for-byte.
- **An anchor is never removed because its source disappeared.** The only permitted reasons to remove
  one are an explicit caller request carrying the expected row digest and the absence of any citing
  claim.
- **Removal is guarded by the caller's expectation.** The request carries the row digest the caller
  believes it is deleting, so a stale caller cannot delete whatever now carries the identity it
  remembered.
- **One lock, one transaction.** A refusal leaves the anchor table exactly as it was.
- **Boundary.** The anchor's stored identity columns are protected by the `source_anchor_no_rewrite`
  payload trigger and by the deferred foreign key; there is no update path in this module at all.
- **Not this module's job.** Memberships, family revisions and the realization *relation* belong to
  their own modules; this one owns only the location record and its lifetime. Resolution of a stored
  anchor against a selected source snapshot is `KS-R07`.

### Todos

None recorded for this slice. Anchor *resolution* is unimplemented by design and is not a debt of this
module: the storage design and `retrieval-review-design.md` assign resolution (exact blob,
recorded-blob mismatch, path absent, unsupported locator, non-text) to `KS-R07`.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The storage-versus-resolution separation this module is built around. | "Storage and resolution are different concerns." | mcp/src/agents_remember/memory/knowledge/anchors.py:3-4 |
| Anchor creation and the provenance-attaching construction point. | `create_source_anchor`; `source_anchor_from_draft` | mcp/src/agents_remember/memory/knowledge/anchors.py:49-70; mcp/src/agents_remember/memory/knowledge/anchors.py:90-106 |
| The narrow write hook the realization operation reuses inside its own transaction. | `insert_anchor_row` | mcp/src/agents_remember/memory/knowledge/anchors.py:107-112 |
| The anchor-lifetime read: whether a stored claim still cites this anchor. | `find_claim_citing_anchor` | mcp/src/agents_remember/memory/knowledge/anchors.py:113-129 |
| The read surface. | `get_anchor` | mcp/src/agents_remember/memory/knowledge/anchors.py:130-144 |
| Explicit removal, with its two refusals both evaluated before the delete. | `remove_source_anchor`; `_delete_anchor` | mcp/src/agents_remember/memory/knowledge/anchors.py:145-166; mcp/src/agents_remember/memory/knowledge/anchors.py:167-189 |
| The anchor-codec row and digest, which derive the canonical identity text at the storage boundary. | `anchor_row`; `anchor_row_digest`; `decode_anchor_row` | mcp/src/agents_remember/memory/knowledge/records.py:226-236; mcp/src/agents_remember/memory/knowledge/records.py:366-381; mcp/src/agents_remember/memory/knowledge/records.py:237-246 |
| The locator union and the confined relative-path rule this module stores without resolving. | `SourceAnchorDraft`; `SourceAnchor`; `SourceLocator` | mcp/src/agents_remember/models/knowledge/source.py:81-124; mcp/src/agents_remember/models/knowledge/source.py:125-128; mcp/src/agents_remember/models/knowledge/source.py:79-81 |
| The refusal factories this module's refusals come from. | `duplicate_anchor_refusal`; `referenced_anchor_refusal`; `missing_expected_row_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:420-441; mcp/src/agents_remember/memory/knowledge/refusals.py:553-567; mcp/src/agents_remember/memory/knowledge/refusals.py:514-530 |
| The declared `source_anchor` table, its index and its payload trigger. | `source_anchor`; `source_anchor_path`; `source_anchor_no_rewrite` | mcp/src/agents_remember/memory/knowledge/schema.py:218-230; mcp/src/agents_remember/memory/knowledge/schema.py:276-276; mcp/src/agents_remember/memory/knowledge/schema.py:336-340 |
| The requirement this module's first delivered slice belongs to. | `KS-R02@v1` | ar-coordination/tasks/agents-remember/260915_knowledge-substrate/requirements/KS-R02-v1-registered-family-and-realization-graph.md |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the new anchor module. It records the storage-versus-resolution separation as the module's governing boundary (no filesystem, Git object or parser is consulted on any path; an absent source never retires an attribution), the explicit identity-plus-expected-digest removal guarded by a citing-claim check, the `find_claim_citing_anchor` placement rationale, and the reserved `source_anchor_path` index that exists for the `KS-R07` resolution read rather than for anything this leaf runs. Verification metadata remains empty until closeout stamps the code commit.
