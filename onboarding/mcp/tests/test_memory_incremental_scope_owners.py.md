# mcp/tests/test_memory_incremental_scope_owners.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_incremental_scope_owners.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:21:02+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Exercises the CCR-R06 dependency extractors and the actual citation-index observation boundary. Real code and memory Git repositories supply candidate tree deltas; a linked checkout demonstrates that exact candidate acquisition excludes checkout metadata and unrelated working files while retaining the selected source population.

## Code Commentary

### Logic

The five-extractor fixture commits its source and memory documents before constructing `_actual_candidate`. It supplies route-index/node facts, parses the real citation and entity documents, and asserts exactly the five edge classes, both governing-route levels and self-verifying edge payload digests.

`_linked_candidate` creates a detached linked worktree and real memory repository, selects the actual staged tree and leases the production source index. Empty-tree observation accepts despite the linked `.git` file and remains unchanged after adding an untracked source. The staged-change case composes `observe_git_tree_delta`, exact source acquisition and `observe_source_index`: additions, deletions and renames determine the indexed set; an ignored generated competitor and ordinary untracked source stay excluded, while force-added ignored source remains included.

Mutations after index acquisition cover dirty bytes, missing files, file symlinks and parent symlinks. Each produces `source-index-candidate-mismatch` and preserves readiness. An ordinary-policy lease or a lease for another exact tree also refuses, even with identical eligible source bytes. Wrong roots and malformed readiness remain distinct `source-index-stale` and `source-index-malformed` refusals.

### Conventions

- `_actual_candidate` uses real HEAD commits and staged trees through `observe_git_tree_delta`; it retains fixture contract/branch labels and task identity rather than invoking production pair admission.
- The five-extractor case supplies route-index and node fixtures. Its actual Git-backed citation extraction and digest assertions do not claim full lifecycle or contract-authority acceptance.

### Invariants And Boundaries

- The fixture's extracted class set and both governing-route pairs are exact; all returned edge payload digests self-verify.
- Candidate observation binds selection policy and exact tree identity separately from content snapshot identity, as well as roots and current tracked bytes.
- Unrelated untracked files do not invalidate exact candidate observation. Changed or unsafe tracked source does.
- Typed observation refusal does not replace the published readiness marker.

### Todos

None recorded.

## Docs References

No configured Domain Documentation applies; the extractor contracts are repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| The owner vocabularies have no external authority. | — | — |

## Repo-Internal References

The acceptance/refusal cases use the real index lease. The companion owner-edge suite retains dependency-authority composition coverage.

| Finding | Anchor | Source |
| --- | --- | --- |
| All five extractor classes and both route levels are asserted over a real Git candidate. | `test_all_five_owner_extractors_emit_exact_content_addressed_edges` | mcp/tests/test_memory_incremental_scope_owners.py:82-166 |
| Candidate deltas and linked-checkout setup come from actual Git objects. | `_actual_candidate`; `_linked_candidate` | mcp/tests/test_memory_incremental_scope_owners.py:188-212; mcp/tests/test_memory_incremental_scope_owners.py:215-239 |
| Empty and staged candidate observations exclude unrelated files while retaining selected ignored source. | `test_source_index_accepts_real_linked_empty_candidate_without_git_metadata`; `test_source_index_composes_exact_staged_git_members_with_real_candidate_observation` | mcp/tests/test_memory_incremental_scope_owners.py:242-252; mcp/tests/test_memory_incremental_scope_owners.py:255-279 |
| Post-acquisition source drift and wrong policy/tree leases refuse candidate observation. | `test_source_index_observer_revalidates_tracked_bytes_and_unsafe_nodes_after_acquisition`; `test_source_index_observer_refuses_wrong_policy_or_tree_with_identical_eligible_bytes` | mcp/tests/test_memory_incremental_scope_owners.py:283-306; mcp/tests/test_memory_incremental_scope_owners.py:310-333 |
| Wrong roots and malformed readiness retain distinct typed failures. | `test_source_index_refuses_malformed_or_wrong_root_generation` | mcp/tests/test_memory_incremental_scope_owners.py:337-352 |
| Production observation and citation extraction bind the selected candidate tree. | `observe_source_index`; `extract_citation_edges` | mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:100-152; mcp/src/agents_remember/memory_quality/incremental_scope/owners.py:219-247 |
| Companion coverage composes all existing dependency-owner outputs. | `test_dependency_authority_composes_all_existing_owner_outputs` | mcp/tests/test_memory_incremental_scope_owner_edges.py:96-150 |

## Cross-Repo References

The exercised owners and temporary fixtures belong to this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository implementation boundary is exercised. | — | — |

## Update History

- 2026-09-06T00:21:02+00:00 — CCR L30 candidate-index recovery: replaced obsolete fabricated-index acceptance narrative with actual Git/index/R06 observation and post-acquisition refusal boundaries.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 1ad9d51f743c5b17de51cc46d8b29e004736022d (CCR-R06@v2/L26): created the card for the new owner-extractor evidence suite of the R06v2 successor leaf; no prior sidecar existed.