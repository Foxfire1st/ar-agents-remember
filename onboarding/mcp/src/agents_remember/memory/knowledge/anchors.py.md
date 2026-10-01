# mcp/src/agents_remember/memory/knowledge/anchors.py

## Governing Overview

[memory route overview](../overview.md)

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
  `DELETE`, and both now live in the in-transaction helper `delete_anchor`, which the candidate-change
  batch composes as well. **The asymmetry a removal consumer must know:** unlike the membership and
  claim removals, `remove_source_anchor` carries **no** expected row digest, so the two checks above
  are what make it safe rather than a stale-caller comparison. The anchor payload is immutable by the
  `source_anchor_no_rewrite` trigger and a repeat removal refuses, so nothing unsafe is reachable
  today — but it is a deliberate open item for whoever reworks removals, not an oversight to fix in
  passing.
- `find_claim_citing_anchor` deliberately lives here rather than in `realizations.py`: "may this
  anchor be removed" is the anchor's own lifetime question, and the anchor module must not depend on
  the claim module's internals to answer it.
- `insert_anchor_row` is the narrow write hook the realization operation and the candidate-change
  batch call so a newly authored anchor and its claim commit as one act of authorship. It is also
  where the duplicate rule now lives: an identical re-declaration writes nothing, and the same
  identity carrying a different payload refuses `duplicate_identity` with both digests — an anchor
  records the location the author attributed, so silently accepting a different one under the same
  identity would serve a location nobody authored.

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
- **Removal is guarded by the caller's expectation — for two of the three removable kinds.** A
  membership removal and a claim removal name the row digest they expect; an anchor removal does not
  and is guarded instead by the payload trigger plus the citing-claim check. Do not read the three
  removals as one contract.
- **The in-transaction helpers assume the caller's transaction.** `insert_anchor_row` and
  `delete_anchor` write through `store.write` and are composed by both the single-record operations
  and the batch; nothing enforces that a caller holds the lock and the transaction.
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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The storage-versus-resolution separation this module is built around. [1]
- Anchor creation and the provenance-attaching construction point. [2]
- The in-transaction write hook the realization operation and the batch command reuse, with the duplicate rule it now carries. [3]
- The anchor-lifetime read: whether a stored claim still cites this anchor. [4]
- The read surface. [5]
- The same read against a bare connection, for a caller that holds one without a store — the curation intake resolving a reused anchor (leaf `260915-KS-L47`). [6]
- Explicit removal, with its two refusals both evaluated before the delete. [7]
- The in-transaction removal helper the batch command composes, and the absence of an expected row digest on the anchor removal request. [8]
- The in-transaction removal helper the batch command composes, and the absence of an expected row digest on the anchor removal request. [9]
- The anchor-codec row and digest, which derive the canonical identity text at the storage boundary. [10]
- The locator union and the confined relative-path rule this module stores without resolving. [11]
- The refusal factories this module's refusals come from. [12]
- The declared `source_anchor` table, its index and its payload trigger. [13]
The requirement this module's first delivered slice belongs to: requirement packet `KS-R02@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
