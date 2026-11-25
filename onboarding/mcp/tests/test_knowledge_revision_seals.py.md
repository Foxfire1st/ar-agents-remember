# mcp/tests/test_knowledge_revision_seals.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The sealed revision payloads, at the model and through the read path. A revision's
`payload_digest` seals the authored cells of its stored row: a row whose text was rewritten behind its identity is
refused on decode rather than served as the revision that identity names. The predecessors field
is still inside the digest — sealing with and without a predecessor changes it — but decoded
predecessors are always `()`: the edge tables are gone with the schema (rule 1), so there is no
edge table left to tamper with. This module owns the executable evidence for that seal on both
payloads:

- the digest covers authored cells and excludes derived standing;
- the aggregates refuse self-contradictory construction (a predecessor named twice, a revision as
  its own predecessor, or an unrecognized state);
- each decoder case reads a stored row into a Python list, changes its statement or guarantee
  cell, and requires the production decoder to refuse the altered input with a payload-digest
  error. These cases do not rewrite the database.

## Code Commentary

### Logic

- The digest node is field-isolating: the two seeds differ **only** in
  the predecessor set, so omitting `"predecessors"` from the canonical payload seals both to one
  digest and fails the node. The construction node refuses self-contradictory aggregates.
- The two decoder cases assert the stored predecessor state first (`predecessors == ()`),
  change one cell in a copied row, and require `KnowledgeStorageError` with the payload-digest
  message rather than an altered aggregate.

### Conventions

- This module exists because of a review finding: the round-1 disclosure claimed "every guard this leaf
  added is load-bearing" while no mutation of the sealing field was caught by any node in the
  repository (sealed finding `260915-KS-L2-RV-1`). That is an earlier review-origin account; the current module docstring describes the seal
  boundaries without recording that review finding.
- Copied-row tampering is checked for both payloads: the invariant statement and the family
  guarantee.
- The decoder cases assert the stored predecessor state before altering the copied row and
  requiring a payload-digest refusal.

### Invariants And Boundaries

- **The predecessor set is inside both payloads.** The payload version strings differ
  (`invariant-revision-payload/v1` vs `family-revision-payload/v1`) precisely because the two seal
  different field sets, so a digest can never be mistaken for the other object's identity.
- **A stored revision's identity covers its stored row**, so a cell edited behind the seal is a
  storage defect rather than a new revision.
- **The production decoders verify the seal.** The two decoder cases require refusal of
  altered copied-row inputs; they do not measure a later store read after database mutation.
- **Boundary.** This module owns the sealed-field evidence only. The digest mechanism itself is
  `models/knowledge/digest.py` and the recomputation on read is `memory/knowledge/records.py`;
  neither is re-implemented here.

### Todos

None recorded for this slice. The node-count and mutation-array claims this module backs were corrected
in the fix-verification round; the corrected accounting is in the worker report's `C2`/`C3` rows rather
than being restated here.

The regression compares the same revision read in proposed and reviewed states and requires equal authored payload digests.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- Why this module owns the shared seal evidence rather than either single-graph module. [1]








> Retained earlier citation wording: - The knowledge identity-branching fixture artifact names contract:knowledge-identity-branching-fixture as its replacement and test_knowledge_revision_seals.py as an exact consumer. These declarations do not establish execution.



### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

### Repo-Internal References (continued)






- The same revision keeps its seal when derived standing differs. [16]

- The unit-regression lane selects mcp/tests/test_knowledge_revision_seals.py. [9]

- The knowledge identity-branching fixture artifact names contract:knowledge-identity-branching-fixture as its replacement and test_knowledge_revision_seals.py as an exact consumer. These declarations do not establish execution. [10]

- The payloads that seal the predecessor set, one per revision kind. [7]
- The read-path recomputation that turns a row whose stored cells were rewritten behind its seal into a storage defect. [8]

- The field-isolating digest node for the invariant payload. [3]
- The family revision test changes the guarantee in a copied stored row and requires decode_family_revision_row to refuse with payload digest. [4]
- The invariant revision test changes the statement in a copied stored row and requires decode_revision_row to refuse with payload digest. [5]
