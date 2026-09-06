# mcp/tests/test_memory_citation_source_index_snapshot.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_memory_citation_source_index_snapshot.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-09-06T00:21:02+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Protects citation-index snapshot reuse and explicit Git-candidate acquisition. Ordinary filesystem indexing remains sensitive to source additions and byte changes. Exact candidate indexing uses the selected Git tree, including staged changes, while excluding linked-checkout metadata and unrelated generated or untracked source.

## Code Commentary

### Logic

`SnapshotReuseTests` distinguishes cold, warm, metadata-refreshed and frozen acquisition. Frozen reuse performs no source discovery, parsing, tokenization or database-integrity traversal; malformed, missing or replaced generations refuse. A memory-only edit preserves the code snapshot, a metadata-only touch rehashes without retokenizing, and a same-size edit with restored mtime still rebuilds. The fixer and its post-fix recheck share one leased index.

`CandidateSourceSnapshotTests` creates a real Git repository and detached linked checkout. Its selected tree can be the staged tree without advancing HEAD. Tracked ignored source and tracked source in ordinary traversal-skipped directories remain eligible; the linked `.git` file, untracked competitors, nested memory and actual Gitlink entries do not join the source population. Ordinary acquisition still discovers dirty/untracked working source.

Acquisition binds selection policy and the exact tree separately from the content snapshot hash. A frozen snapshot requested with another policy or tree refuses before a source walk or rebuild, including when eligible file content is identical. Dirty or missing tracked files, unsafe file/parent nodes, invalid tree selectors and a non-root Git checkout refuse. Direct resolution retains legitimate memory-only documents while rejecting untracked code and a memory symlink escaping into code.

The race fixture runs the actual Git hash command, then changes the source. Direct resolution detects the post-hash identity change; cached index acquisition reaches rebuilding, which refuses the now-dirty bytes. Separate transport-corruption fixtures keep actual Git output metadata but inject unsafe census rows or truncate hash output. They assert refusal and, where applicable, unchanged published readiness. The symlink-root case invokes the candidate owner directly. A population larger than one hash batch verifies late-member lookup and drift detection.

Capacity tests use an actual oversized tracked source and a dirty oversized source, plus lowered file-count and aggregate-byte limits. They forbid `hash-object` before asserting refusal; the per-file test exercises both acquisition and direct resolution. Rejected acquisition leaves the previous readiness bytes intact.

### Conventions

Temporary code, memory and cache roots come from `IndexCase`. Candidate cases invoke actual Git; transport and race fixtures alter only the explicitly described command result or post-command source state.

### Invariants And Boundaries

- A reusable snapshot cannot authorize a different candidate policy, tree or replaced database generation.
- Exact Git membership preserves ordinary filesystem discovery; each mode has explicit population assertions.
- Rejected candidate acquisition preserves published readiness. Source capacity is enforced before Git content hashing.
- These local Git, index and resolver tests do not constitute Gate-5 or lifecycle acceptance.

### Todos

None recorded.

## Docs References

No Domain Documentation entries are configured for this memory root. These test contracts are repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain authority is asserted. | — | — |

## Repo-Internal References

The source tests below are the behavioral evidence. Candidate transport corruption is deliberately injected after a real Git invocation; it is not presented as a Git-generated malformed tree.

| Finding | Anchor | Source |
| --- | --- | --- |
| Frozen reuse skips discovery and the fixer shares its lease with rechecking. | `test_expected_snapshot_opens_without_tree_or_integrity_traversal`; `test_warm_fix_and_post_fix_recheck_share_one_index_lease` | mcp/tests/test_memory_citation_source_index_snapshot.py:27-69; mcp/tests/test_memory_citation_source_index_snapshot.py:228-279 |
| Ordinary acquisition detects byte and membership changes. | `test_same_size_restored_mtime_content_change_rebuilds`; `test_add_delete_and_rename_each_rebuild_once` | mcp/tests/test_memory_citation_source_index_snapshot.py:196-211; mcp/tests/test_memory_citation_source_index_snapshot.py:213-226 |
| Exact linked-checkout membership excludes competitors and follows the staged tree. | `test_linked_candidate_excludes_generated_competitors_but_retains_tracked_ignored_files`; `test_staged_add_delete_and_rename_define_the_candidate_without_moving_head` | mcp/tests/test_memory_citation_source_index_snapshot.py:314-366; mcp/tests/test_memory_citation_source_index_snapshot.py:368-386 |
| Frozen leases bind policy and tree separately from content snapshot identity. | `test_frozen_acquisition_refuses_a_different_policy_with_identical_eligible_files`; `test_frozen_acquisition_binds_exact_tree_even_when_indexed_content_is_identical` | mcp/tests/test_memory_citation_source_index_snapshot.py:388-413; mcp/tests/test_memory_citation_source_index_snapshot.py:415-440 |
| Actual hash-race refusal reaches both index rebuilding and direct resolution. | `test_candidate_refuses_a_mutation_during_actual_git_hash_proof` | mcp/tests/test_memory_citation_source_index_snapshot.py:543-584 |
| Gitlinks stay excluded; malformed census and root nodes refuse. | `test_candidate_ignores_actual_gitlink_entries`; `test_candidate_refuses_unsafe_git_census_paths`; `test_candidate_refuses_a_symlink_root_before_member_hashing` | mcp/tests/test_memory_citation_source_index_snapshot.py:586-595; mcp/tests/test_memory_citation_source_index_snapshot.py:597-626; mcp/tests/test_memory_citation_source_index_snapshot.py:628-633 |
| Truncated actual hash output cannot replace readiness; memory-only resolution remains bounded. | `test_candidate_refuses_a_truncated_actual_hash_response_without_replacing_readiness`; `test_candidate_resolves_a_memory_only_file_without_admitting_code_competitors` | mcp/tests/test_memory_citation_source_index_snapshot.py:635-660; mcp/tests/test_memory_citation_source_index_snapshot.py:662-672 |
| Candidate capacity refuses before hashing and preserves readiness. | `test_candidate_size_cap_refuses_before_hashing_tracked_or_dirty_oversized_members`; `test_candidate_population_caps_refuse_before_hashing_and_preserve_prior_readiness` | mcp/tests/test_memory_citation_source_index_snapshot.py:688-722; mcp/tests/test_memory_citation_source_index_snapshot.py:724-751 |
| Shared source bounds are owned by the state layer. | `check_source_bounds` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:204-221 |

## Cross-Repo References

The exercised owners and temporary fixtures belong to this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository implementation boundary is exercised. | — | — |

## L23 SQLite Ownership

The metadata-corruption fixture now explicitly commits and closes its SQLite
connection before invoking the frozen-snapshot refusal. This removes implicit
context-manager connection lifetime from Python 3.14 cleanup behavior without
changing the snapshot contract under test.

## Update History

- 2026-09-06T00:21:02+00:00 — CCR L30 candidate-index recovery: documented real linked Git acquisition, policy/tree-bound reuse, hash/transport/unsafe-node refusal and capacity-before-hash proof; retained ordinary snapshot and L23 SQLite ownership history.
- 2026-08-12T20:10+02:00 — L23 curator: documented explicit commit/close ownership for the snapshot corruption fixture; verification remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
