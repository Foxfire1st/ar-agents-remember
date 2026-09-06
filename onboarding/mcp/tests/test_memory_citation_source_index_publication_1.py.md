# mcp/tests/test_memory_citation_source_index_publication_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_memory_citation_source_index_publication_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-09-06T00:21:02+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Exercises citation-index publication, bounded cache ownership and legacy-generation reclamation. The tests protect publication identity and resource limits across repository collisions, concurrent publishers and live legacy readers.

## Code Commentary

### Logic

Corrupt databases and obsolete manifests rebuild without changing a content-equivalent snapshot. A forced slot collision must revalidate repository identity before reuse. The per-file limit is patched on its canonical owner, `source_index_state.MAX_SOURCE_FILE_BYTES`; an oversized source leaves database, manifest and readiness unpublished.

The cache-population fixture checks two slot/repository sizes and removes its isolated legacy fixture roots. A separate fixture launches four real Python publishers against a shared temporary cache and checks that reclamation leaves stable bounded slots. Shared locks on legacy slots prevent deletion; releasing only one slot does not restart the common wait budget. Additional cases reject anchor-key collisions and reclaim stale builder temporary files.

### Conventions

The tests use temporary repositories and caches, real process/thread coordination, and explicit fault injection for capacity and collisions. Reclamation is exercised only against isolated fixture roots.

### Invariants And Boundaries

- Citation caches stay outside code and memory roots and within the configured slot and publication-size limits exercised by these fixtures.
- A failed per-file bound check publishes no generation; changing the policy owner preserves that assertion.
- Live legacy readers retain their locked generation until release, subject to one bounded reclamation wait.

### Todos

None recorded.

## Docs References

No Domain Documentation entries are configured for this memory root. These test contracts are repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain authority is asserted. | — | — |

## Repo-Internal References

These cases exercise publication through the real index owner, with explicit fault injection for limits and collisions.

| Finding | Anchor | Source |
| --- | --- | --- |
| Corrupt/obsolete generations rebuild; per-file capacity publishes nothing. | `test_corrupt_database_and_obsolete_manifest_rebuild`; `test_cache_is_external_fixed_slot_and_per_file_cap_fails_closed` | mcp/tests/test_memory_citation_source_index_publication_1.py:22-35; mcp/tests/test_memory_citation_source_index_publication_1.py:37-50 |
| Repository collisions revalidate identity and tested cache populations remain bounded. | `test_repository_slot_collision_revalidates_identity`; `test_cache_lifecycle_is_bounded_at_two_slot_and_repository_sizes` | mcp/tests/test_memory_citation_source_index_publication_1.py:52-66; mcp/tests/test_memory_citation_source_index_publication_1.py:68-112 |
| Concurrent publishers and locked legacy readers retain reclamation boundaries. | `test_concurrent_legacy_reclamation_publishes_only_stable_slots`; `test_live_legacy_slots_are_not_deleted_and_share_one_bounded_wait` | mcp/tests/test_memory_citation_source_index_publication_1.py:114-171; mcp/tests/test_memory_citation_source_index_publication_1.py:173-208 |
| Digest collisions refuse and stale builder temporaries are reclaimed. | `test_anchor_digest_collision_is_rejected`; `test_stale_builder_temp_is_reclaimed_by_next_publisher` | mcp/tests/test_memory_citation_source_index_publication_1.py:210-216; mcp/tests/test_memory_citation_source_index_publication_1.py:218-228 |

## Cross-Repo References

The exercised owners and temporary fixtures belong to this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository implementation boundary is exercised. | — | — |

## Update History

- 2026-09-06T00:21:02+00:00 — CCR L30 candidate-index recovery: documented existing bounded publication/reclamation responsibility and canonical state-layer per-file bound ownership.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
