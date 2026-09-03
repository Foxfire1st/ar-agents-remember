# mcp/tests/test_memory_incremental_scope_owners.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_incremental_scope_owners.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `1ad9d51f743c5b17de51cc46d8b29e004736022d` |
| lastVerifiedCommitDate | 2026-09-02T06:25:51+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Focused evidence for the CCR-R06@v2 dependency-owner extractors: proves that all five edge classes
are emitted as exact content-addressed edges from canonical route-index, citation, entity, and
Git facts, and that the citation source-index lease accepts an exact candidate while refusing stale
or malformed generations cit:([`test_all_five_owner_extractors_emit_exact_content_addressed_edges`, `test_source_index_accepts_exact_empty_candidate_and_refuses_stale_population`], mcp/tests/test_memory_incremental_scope_owners.py:85-163, 217-239).

## Code Commentary

### Logic

`test_all_five_owner_extractors_emit_exact_content_addressed_edges` plants a source file, a
citation-claiming onboarding document, an entity fingerprint table, and a two-level route-index
population, then asserts the extracted class set equals all five `EdgeClass` values, the
source-to-governing-route pairs cover both route levels, and every edge's `contentDigest`
self-verifies over its payload cit:([`test_all_five_owner_extractors_emit_exact_content_addressed_edges`], mcp/tests/test_memory_incremental_scope_owners.py:85-163).
`test_source_index_accepts_exact_empty_candidate_and_refuses_stale_population` builds a fake
ready/manifest generation and proves `observe_source_index` accepts an exact empty candidate, then
refuses `source-index-stale` when the code tree changes cit:([`test_source_index_accepts_exact_empty_candidate_and_refuses_stale_population`], mcp/tests/test_memory_incremental_scope_owners.py:217-239).
`test_source_index_refuses_malformed_or_wrong_root_generation` refuses a wrong-root generation and
unreadable readiness as `source-index-stale` / `source-index-malformed`
cit:([`test_source_index_refuses_malformed_or_wrong_root_generation`], mcp/tests/test_memory_incremental_scope_owners.py:242-262).

### Conventions

- Extraction inputs mirror the real owner outputs: route-index JSON shape, citation grammar,
  entity fingerprint rows, and `ReadyGeneration`/`Manifest` JSON.
- The suite builds its own `MemoryCandidatePairIdentity` fixtures so no production pair authority is
  required.

## Invariants And Boundaries

- All five dependency edge classes must be emitted together; class sets are asserted exactly.
- A stale, malformed, or wrong-root source-index generation fails closed; candidate-bound reuse is
  never accepted without the exact lease.
- Edge digests must self-verify; fabricated or mis-owned edges are impossible in the extracted set.

## Docs References

No configured Domain Documentation applies; the extractor contracts are repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| The owner vocabularies have no external authority. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Production extractors and source-index lease under test. | `extract_file_sidecar_edges`, `extract_governing_route_edges`, `extract_citation_edges`, `extract_entity_edges`, `extract_route_index_edges`, `observe_source_index` | mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:100-142, 174-275 |
| Fixture JSON shapes come from the citation source-index state module. | `ReadyGeneration`, `Manifest` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py |
| Companion edge suite for owner composition and refusal cases. | — | mcp/tests/test_memory_incremental_scope_owner_edges.py |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 1ad9d51f743c5b17de51cc46d8b29e004736022d (CCR-R06@v2/L26): created the card for the new owner-extractor evidence suite of the R06v2 successor leaf; no prior sidecar existed.