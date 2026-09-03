# mcp/tests/test_memory_incremental_scope_owner_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_incremental_scope_owner_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `1ad9d51f743c5b17de51cc46d8b29e004736022d` |
| lastVerifiedCommitDate | 2026-09-02T06:25:51+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Edge coverage for the CCR-R06@v2 dependency owners: authority composition, exact Git blob node
observation, citation/entity/route extractor refusal behavior, route-index population drift, the
trailing-NUL tree parser repair, source-index census and candidate-blob matching, and citation
root-confinement cit:([`test_dependency_authority_composes_all_existing_owner_outputs`, `test_git_node_owner_reads_candidate_and_deleted_base_blobs`], mcp/tests/test_memory_incremental_scope_owner_edges.py:96-183).

## Code Commentary

### Logic

`test_dependency_authority_composes_all_existing_owner_outputs` proves the direct function and the
`ContractDependencyAuthority` adapter emit identical snapshots and that root pre-checks run
cit:([`test_dependency_authority_composes_all_existing_owner_outputs`], mcp/tests/test_memory_incremental_scope_owner_edges.py:96-150).
`test_git_node_owner_reads_candidate_and_deleted_base_blobs` and
`test_citation_extractor_skips_unowned_documents_and_unresolved_sources` cover node emission from
both trees and the skip-not-refuse behavior for unresolved citation sources
cit:([`test_git_node_owner_reads_candidate_and_deleted_base_blobs`, `test_citation_extractor_skips_unowned_documents_and_unresolved_sources`], mcp/tests/test_memory_incremental_scope_owner_edges.py:153-211).
`test_absent_entity_catalog_and_malformed_child_routes_fail_closed`,
`test_current_route_indexes_accept_exact_population_and_parse_documents`, and
`test_current_route_indexes_refuse_owner_and_document_drift` prove the route-index population
contract refuses stale, extra/missing, non-JSON, and non-object documents
cit:([`test_current_route_indexes_accept_exact_population_and_parse_documents`], mcp/tests/test_memory_incremental_scope_owner_edges.py:213-287).
`test_tree_entries_keeps_only_recursive_blob_records` pins the `ls-tree -r -z` parsing repair: the
canonical trailing NUL is removed and only blob records are kept
cit:([`test_tree_entries_keeps_only_recursive_blob_records`], mcp/tests/test_memory_incremental_scope_owner_edges.py:290-304).
`test_owner_extractors_cover_repeated_source_route_and_child_populations` counts sidecar, governing
route, and route-index edges over repeated and child populations
cit:([`test_owner_extractors_cover_repeated_source_route_and_child_populations`], mcp/tests/test_memory_incremental_scope_owner_edges.py:307-343).
`test_index_member_census_and_exact_git_blob_match` and
`test_index_member_refuses_unavailable_or_mismatched_candidate` prove the source-index census and
per-member candidate blob/content matching, and
`test_citation_resolution_handles_missing_memory_code_and_escape_roots` proves citation root
confinement with `citation-source-escape` refusal
cit:([`test_index_member_*`, `test_citation_resolution_handles_missing_memory_code_and_escape_roots`], mcp/tests/test_memory_incremental_scope_owner_edges.py:357-455).
`test_route_strings_and_dependency_roots_fail_closed` covers malformed index string arrays and the
`dependency-root-mismatch` refusal cit:([`test_route_strings_and_dependency_roots_fail_closed`], mcp/tests/test_memory_incremental_scope_owner_edges.py:458-472).

### Conventions

- Refusals are asserted by exact `failure.code`; extraction helpers are monkeypatched so each case
  is attributable to one owner.
- Fixture route indexes follow the real `overview.index.json` shape.

## Invariants And Boundaries

- Route-index population must exactly equal the generator's expected set; `stale`/`population`/
  `json`/`root` drift all fail closed.
- A deleted path must still resolve a blob from the base tree; otherwise `git-node-missing`.
- Citation sources escaping the exact code/memory roots fail `citation-source-escape` — never
  silently included.
- The source-index manifest must exactly match the candidate tree census and per-member digests.

## Docs References

No configured Domain Documentation applies; the assertions follow the CCR-R06@v2 packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| The owner edge semantics are repository-owned. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Production owner internals under test. | `_tree_entries`, `_current_route_indexes`, `_require_index_matches_candidate`, `_citation_node`, `_require_roots`, `observe_git_nodes`, `extract_*` | mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:145-464 |
| Companion primary suite for extractor/lease behavior. | `test_source_index_accepts_exact_empty_candidate_and_refuses_stale_population` | mcp/tests/test_memory_incremental_scope_owners.py:217-241 |
| Fixture JSON shapes follow the citation source-index state module. | `Identity`, `SourceFile`, `Manifest` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:137-258 |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 1ad9d51f743c5b17de51cc46d8b29e004736022d (CCR-R06@v2/L26): created the card for the new owner edge suite of the R06v2 successor leaf; no prior sidecar existed.