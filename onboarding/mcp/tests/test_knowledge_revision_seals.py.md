# mcp/tests/test_knowledge_revision_seals.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The sealed revision payloads, at the model and through the read path. A revision's
`payload_digest` seals its stored row: a row whose text was rewritten behind its identity is
refused on decode rather than served as the revision that identity names. The predecessors field
is still inside the digest — sealing with and without a predecessor changes it — but decoded
predecessors are always `()`: the edge tables are gone with the schema (rule 1), so there is no
edge table left to tamper with. This module owns the executable evidence for that seal on both
payloads:

- the digest covers the stored cells (the seal unit test pins one field's contribution);
- the aggregates refuse self-contradictory construction (a predecessor named twice, a revision as
  its own predecessor, acceptance mismatches);
- each read node rewrites one stored cell behind a sealed row — the only way to change sealed
  content without rewriting the row through the writer, which recomputes the seal — then asserts
  that decoding the row refuses rather than serving content its identity no longer describes.

## Code Commentary

### Logic

- The digest node is field-isolating: the two seeds differ **only** in
  the predecessor set, so omitting `"predecessors"` from the canonical payload seals both to one
  digest and fails the node. The construction node refuses self-contradictory aggregates.
- The two read nodes are the read-path half. Each asserts the pre-edit stored state first
  (including `predecessors == ()`), then rewrites one stored cell behind the seal, then asserts
  that the decode raises `KnowledgeStorageError` with the payload-digest message rather
  than returning the altered aggregate.

### Conventions

- This module exists because of a review finding: the round-1 disclosure claimed "every guard this leaf
  added is load-bearing" while no mutation of the sealing field was caught by any node in the
  repository (sealed finding `260915-KS-L2-RV-1`). Its docstring records that origin, so a later reader
  knows why the file exists rather than treating it as duplicate coverage.
- Both directions of cell tampering are covered on both payloads: the invariant statement and the
  family guarantee.
- The read nodes assert the pre-mutation state before mutating, so a no-op raw write would leave the
  read succeeding and fail the node — the assertion cannot pass for an incidental reason.

### Invariants And Boundaries

- **The predecessor set is inside both payloads.** The payload version strings differ
  (`invariant-revision-payload/v1` vs `family-revision-payload/v1`) precisely because the two seal
  different field sets, so a digest can never be mistaken for the other object's identity.
- **A stored revision's identity covers its stored row**, so a cell edited behind the seal is a
  storage defect rather than a new revision.
- **The seal is verified on read, not only computed on write** — that is what the two read nodes
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


- The field-isolating digest node for the invariant payload. [3]


- The family revision test detects a stored guarantee cell rewritten behind its seal and requires decode_family_revision_row to refuse with payload digest. [4]


- The invariant revision test detects a stored statement cell rewritten behind its seal and requires decode_revision_row to refuse with payload digest. [5]

- The payloads that seal the predecessor set, one per revision kind. [7]

- The read-path recomputation that turns a row whose stored cells were rewritten behind its seal into a storage defect. [8]

- The unit-regression lane row this module is registered by. [9]


> Retained earlier citation wording: - The knowledge identity-branching fixture artifact names contract:knowledge-identity-branching-fixture as its replacement and test_knowledge_revision_seals.py as an exact consumer. These declarations do not establish execution. [10]



### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

- The knowledge identity-branching fixture artifact names contract:knowledge-identity-branching-fixture as its replacement and test_knowledge_revision_seals.py as an exact consumer. These declarations do not establish execution. [10]
