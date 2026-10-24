# mcp/tests/test_transaction_only_worktree_delivery.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds the transaction-only closeout and integration regressions (CCR-R12): closeout and integration are Git
transactions that need no acceptance tool, the publication is bound to the branch and head that were admitted, a
moved branch refuses and a retry completes, and a refused memory publication gives back every preparation it made.

## Code Commentary

### Logic

The transaction cases remain in this module. Shared fixtures, executable hooks, branch-race helpers and attribution assertions live in `transaction_only_worktree_delivery_test_support.py`; the cache-refresh cases live in `test_transaction_only_worktree_delivery_cache.py`. Their extraction changes the source owners, not the transaction, restoration or hook guarantees described here.

The cases drive `worktree_closeout_apply`, the integration lifecycle and the worktree modules over a real
repository pair, with `applications.worktree_tool_requests`, `memory_cache` and `memory_ledger` supplying the
request and the cache witness.

- **Code commit.** `test_ordinary_code_commit_is_the_admitted_tree_and_keeps_a_later_edit` proves a file edited
  while the commit object is written is not committed.
- **Refusals.** `test_a_moved_code_branch_refuses_the_closeout_and_a_retry_completes_it` and
  `test_a_moved_memory_branch_leaves_the_pair_to_the_recovery_a_retry_runs` keep a moved branch a concrete
  refusal with nothing of the memory side published, and a retry completing it.
- **Preparation.** `test_a_refused_converted_memory_publication_gives_back_every_preparation` gives back
  everything a refused converted-memory publication prepared, and
  `test_the_publication_is_bound_to_the_branch_and_the_head_the_closeout_admitted` keeps the publication bound to
  the admitted branch and head.
- **No acceptance tool.** `test_public_closeout_commits_code_and_memory_without_acceptance_tools` requires the
  closeout to commit both sides with no quality or review authority present, and
  `test_public_integration_merges_prepared_pair_without_acceptance_tools` merges a prepared pair the same way.
- **Recovery.** `test_closeout_recovery_attributes_the_memory_commit_it_still_owed` resumes an interrupted public
  closeout with only its memory commit owed.
- **Integration race.** `test_public_integration_ref_movement_refuses_before_pair_merge` keeps a source-tip race a
  refusal, so a torn pair is never published.
- **Recloseout.** `test_recloseout_after_a_sync_records_the_memory_head_as_content_commit` records the live memory
  head after a sync rather than the stale record.
- **Certification and hooks.** `test_l56_required_references_separate_requested_dagger_from_ordinary_closeout`
  keeps certification requested rather than an automatic gate, `test_l56_publication_code_pins_both_live_commit_hook_mechanisms`
  and `test_l56_closeout_skill_names_the_live_hook_guarantee_without_prepared_policy` remove the retired policy
  claims without weakening the live hook guarantee, and the renderer and reader prose cases name only surviving
  routes and analytics.

### Conventions

A case builds a real code and memory repository pair and asserts on refs, commit objects and content bytes, so a
publication that wrote a plausible record over the wrong tree fails.

### Invariants And Boundaries

- Closeout and integration are Git transactions; no acceptance tool is consulted.
- A moved branch or ref refuses rather than publishing a torn pair.

## Evidence

- An interrupted public closeout resumes only its exact accepted code identity. [3]

- Integration publishes accepted refs or refuses source movement before publication. [4]


- A recloseout after a sync records the actual memory head. [5]


- Closeout commits code and memory as one transaction without any acceptance tool. [9]
- A refused converted-memory publication gives back every preparation it made. [10]

- Named acceptance-tool prohibition and real failing-hook probes — `_forbid_acceptance_tools`, `_install_failing_pre_commit_hooks` in mcp/tests/test_transaction_only_worktree_delivery.py. [1]

- One code/memory commit, cache absence from the committed tree, and both trailer readers — `_assert_memory_attribution`, `test_public_closeout_commits_code_and_memory_without_acceptance_tools`, `_converted_closeout_fixture`, `_seed_leaf_trace_row`, `_apply` in mcp/tests/test_transaction_only_worktree_delivery.py. [2]

- Cache materialization preserves both repositories' refs/commit objects and real content — `test_cache_refresh_preserves_current_bytes_and_materializes_a_missing_cache`, `test_cache_refresh_repairs_malformed_forged_and_reordered_data_from_git`, `_ClosedCacheLeaf` in mcp/tests/test_transaction_only_worktree_delivery.py. [6]

- Cache witnesses compare HEADs, refs and all commit-object identities, then check content bytes, untracked cache and clean repository status — `test_cache_refresh_preserves_current_bytes_and_materializes_a_missing_cache`, `test_cache_refresh_repairs_malformed_forged_and_reordered_data_from_git`, `_ClosedCacheLeaf` in mcp/tests/test_transaction_only_worktree_delivery.py. [7]

- The open trace fixture binds its actual contract code snapshot and source path/blob — `_seed_leaf_trace_row` in mcp/tests/test_transaction_only_worktree_delivery.py. [8]
