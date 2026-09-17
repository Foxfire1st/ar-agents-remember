# mcp/tests/test_knowledge_revision_seals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_revision_seals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `9c12e8b1ec027b8bb07f4c0cc79ef99a655ff890`|
| lastVerifiedCommitDate | 2026-09-18T01:58:08+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Why this module owns the shared seal evidence rather than either single-graph module. | "neither single-graph module owns the shared mechanism" | mcp/tests/test_knowledge_revision_seals.py:5-5 |
| The four raw edge statements the read nodes mutate with. | `_FAMILY_EDGE_INSERT`; `_FAMILY_EDGE_DELETE`; `_INVARIANT_EDGE_INSERT`; `_INVARIANT_EDGE_DELETE` | mcp/tests/test_knowledge_revision_seals.py:37-41; mcp/tests/test_knowledge_revision_seals.py:42-46; mcp/tests/test_knowledge_revision_seals.py:47-51; mcp/tests/test_knowledge_revision_seals.py:52-56 |
| The field-isolating digest node for the invariant payload. | "test_an_invariant_revision_digest_seals_its_predecessor_set" | mcp/tests/test_knowledge_revision_seals.py:63-95 |
| The two family read nodes (added and removed edge behind the seal). | "test_a_family_revision_read_refuses_after_a_predecessor_edge_is_added"; "test_a_family_revision_read_refuses_after_a_predecessor_edge_is_deleted" | mcp/tests/test_knowledge_revision_seals.py:96-123; mcp/tests/test_knowledge_revision_seals.py:124-148 |
| The two invariant read nodes (added and removed edge behind the seal). | "test_an_invariant_revision_read_refuses_after_a_predecessor_edge_is_added"; "test_an_invariant_revision_read_refuses_after_a_predecessor_edge_is_deleted" | mcp/tests/test_knowledge_revision_seals.py:149-170; mcp/tests/test_knowledge_revision_seals.py:171-188 |
| The field-isolating family digest node this module's invariant sibling mirrors. | "test_a_family_revision_digest_seals_its_predecessor_set" | mcp/tests/test_knowledge_family_revision.py:150-183 |
| The payloads that seal the predecessor set, one per revision kind. | `canonical_revision_payload`; `canonical_family_revision_payload` | mcp/src/agents_remember/models/knowledge/digest.py:30-52; mcp/src/agents_remember/models/knowledge/digest.py:71-90 |
| The read-path recomputation that turns a tampered edge into a storage defect. | `decode_revision_row`; `decode_family_revision_row` | mcp/src/agents_remember/memory/knowledge/records.py:153-189; mcp/src/agents_remember/memory/knowledge/records.py:327-356 |
| The unit-regression lane row this module is registered by. | "mcp/tests/test_knowledge_revision_seals.py" | mcp/tests/test-evidence-lanes.toml:81-81 |
|  The fixture contract that names this module as an exact consumer. | "contract:knowledge-identity-branching-fixture" | mcp/tests/evidence-lifecycle.toml:1031-1052  |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_knowledge_revision_seals.py" repointed to mcp/tests/test-evidence-lanes.toml:81-81. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "neither single-graph module owns the shared mechanism" repointed to mcp/tests/test_knowledge_revision_seals.py:5-5. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_revision_seals.py" repointed to mcp/tests/test-evidence-lanes.toml:78-78. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): created this one-to-one card for the fix-verification test module. It records that the module exists because round 1's mutation array could not kill the sealing field (sealed finding `260915-KS-L2-RV-1`), the field-isolating construction that makes the assertion reason-specific, and the four read nodes that extend the same isolation to the read path on both graphs in both directions. Verification metadata remains empty until closeout stamps the code commit.
