# mcp/tests/test_knowledge_revision_seals.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The sealed revision payloads, on **both** lineage graphs and through the read path. The predecessor set
is inside every revision digest, which is what binds a stored revision identity to the exact edge set it
was authored with. This module owns the executable evidence for that field on both payloads, because
neither single-graph module owns the shared mechanism:

- the invariant payload (L1) is exercised for its aggregate round-trip but never for the field alone, so
  a payload that dropped the predecessor set would keep every L1 node green;
- the family payload has the same shape, and its seal node lives in
  `test_knowledge_family_revision.py` next to the revision rules it belongs to.

Each digest node holds **every other field equal**, and each read node edits the edge *table* behind a
stored row — the only way to change a sealed predecessor set without rewriting the row itself — then
asserts that reading the revision back refuses rather than serving a revision whose identity no longer
describes it.

## Code Commentary

### Logic

- The two digest nodes (`test_an_invariant_revision_digest_seals_its_predecessor_set` and its family
  sibling in `test_knowledge_family_revision.py`) are field-isolating: the two seeds differ **only** in
  the predecessor set, so removing `"predecessors"` from the matching canonical payload makes the node
  fail at its own digest assertion with two identical digests.
- The four read nodes are the read-path half. Each asserts the pre-edit stored state first, then
  performs a raw `INSERT` or `DELETE` on `family_predecessor` / `invariant_predecessor` behind the seal,
  then asserts that the reader raises `KnowledgeStorageError` with the payload-digest message rather
  than returning the altered aggregate.
- The raw edge statements are module constants (`_FAMILY_EDGE_INSERT`, `_FAMILY_EDGE_DELETE`,
  `_INVARIANT_EDGE_INSERT`, `_INVARIANT_EDGE_DELETE`) because a raw write through the operation is
  exactly what the seal is supposed to prevent.

### Conventions

- This module exists because of a review finding: the round-1 disclosure claimed "every guard this leaf
  added is load-bearing" while no mutation of the sealing field was caught by any node in the
  repository (sealed finding `260915-KS-L2-RV-1`). Its docstring records that origin, so a later reader
  knows why the file exists rather than treating it as duplicate coverage.
- Both directions of edge tampering are covered on both graphs: an added edge and an independently
  **removed** edge.
- The read nodes assert the pre-mutation state before mutating, so a no-op raw write would leave the
  read succeeding and fail the node — the assertion cannot pass for an incidental reason.

### Invariants And Boundaries

- **The predecessor set is inside both payloads.** The payload version strings differ
  (`invariant-revision-payload/v1` vs `family-revision-payload/v1`) precisely because the two seal
  different field sets, so a digest can never be mistaken for the other object's identity.
- **A stored revision's identity covers its stored edges**, read from the database alongside the row,
  so an edge edited behind the seal is a storage defect rather than a new revision.
- **The seal is verified on read, not only computed on write** — that is what the four read nodes
  establish.
- **Boundary.** This module owns the sealed-field evidence only. The family revision *rules* are
  `test_knowledge_family_revision.py`; the relation payload triggers are
  `test_knowledge_relation_rules.py`. The digest mechanism itself is
  `models/knowledge/digest.py` and the recomputation on read is `records.py`; neither is re-implemented
  here.

### Todos

None recorded for this slice. The node-count and mutation-array claims this module backs were corrected
in the fix-verification round; the corrected accounting is in the worker report's `C2`/`C3` rows rather
than being restated here.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- Why this module owns the shared seal evidence rather than either single-graph module. [1]
- The four raw edge statements the read nodes mutate with. [2]
- The field-isolating digest node for the invariant payload. [3]
- The two family read nodes (added and removed edge behind the seal). [4]
- The two invariant read nodes (added and removed edge behind the seal). [5]
- The field-isolating family digest node this module's invariant sibling mirrors. [6]
- The payloads that seal the predecessor set, one per revision kind. [7]
- The read-path recomputation that turns a tampered edge into a storage defect. [8]
- The unit-regression lane row this module is registered by. [9]
- The fixture contract that names this module as an exact consumer. [10]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
