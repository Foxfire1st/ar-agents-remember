# mcp/tests/test_transaction_only_worktree_delivery.py

## Governing Overview

[overview](overview.md)

## Purpose

Holds the transaction-only closeout and integration regressions (CCR-R12): closeout and integration are Git
transactions that need no acceptance tool, the publication is bound to the branch and head that were admitted, a
moved branch refuses and a retry completes, and a refused memory publication gives back every preparation it made.

## Code Commentary

### Logic

The transaction cases remain in this module. Shared fixtures, executable hooks, branch-race helpers and attribution assertions live in `transaction_only_worktree_delivery_test_support.py`; the cache-refresh cases live in `test_transaction_only_worktree_delivery_cache.py`.

The cases drive the synchronous closeout and integration application entry points and worktree modules over a real repository pair. The support module constructs the requests from `application.worktree_tool_requests` and checks attribution through the memory cache and ledger readers.

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
  closeout to commit both sides with no selected profile or review rows and fail-if-called acceptance probes. The converted fixture supplies its required trace row. The test verifies that the failing hook attempt leaves both heads unchanged and that both hooks run for the successful publication.
  `test_public_integration_merges_prepared_pair_without_acceptance_tools` fast-forwards the prepared pair while the acceptance probes and fail-if-called hook conditions are present.
- **Recovery.** `test_closeout_recovery_attributes_the_memory_commit_it_still_owed` resumes an interrupted public
  closeout with only its memory commit owed.
- **Integration race.** `test_public_integration_ref_movement_refuses_before_pair_merge` keeps a source-tip race a
  refusal, so a torn pair is never published.
- **Recloseout.** `test_recloseout_after_a_sync_records_the_memory_head_as_content_commit` records the live memory
  head after a sync rather than the stale record.
- **Certification and hooks.** `test_l56_required_references_separate_requested_dagger_from_ordinary_closeout`
  keeps certification requested rather than an automatic gate, `test_l56_publication_code_pins_both_live_commit_hook_mechanisms`
  checks the Git source for commit-tree, reference-transaction and pre-commit and for absence of three retired phrases. The renderer test checks the surviving route and backfill prose, and the reader test rejects four obsolete descriptors.

### Conventions

The transaction cases build a code and memory Git pair and inspect refs, commit objects and content bytes. The documentation cases inspect source and prose.

### Invariants And Boundaries

- Closeout and integration are Git transactions; no acceptance tool is consulted.
- A moved branch or ref refuses rather than publishing a torn pair.

## Evidence



- The public apply is interrupted after the code commit. The recovery manager refuses a different code identity and completes the memory commit against the recorded one. The test verifies both commit counts and memory attribution. [3]



- Integration publishes accepted refs or refuses source movement before publication. [4]


- A recloseout after a sync records the actual memory head. [5]


- The public closeout fixture checks a code commit and a memory commit with no selected profile or review rows. Historical acceptance probes fail if called. The fixture provides the converted leaf’s trace row. The failing attempt leaves both heads unchanged, and both hooks log the successful attempt. [9]

- The refused converted-memory fixture restores open history, ignore-file presence and the index. The case compares status paths with its stated allowance, checks reachable commits and verifies the successful retry closes history. [10]

- The support module’s `_forbid_acceptance_tools` installs fail-if-called acceptance probes, and `_install_failing_pre_commit_hooks` exercises real Git hook refusals. [1]


- The main module’s public closeout case checks both content commits and cache exclusion. The support module supplies `_assert_memory_attribution`, `_converted_closeout_fixture`, `_seed_leaf_trace_row` and `_apply`. Its attribution assertion compares both trailer readers. [2]


- The cache module’s two refresh cases preserve refs, commit-object sets and worktree content. The support module owns `_ClosedCacheLeaf` and its repository pair. [6]

- The cache tests use the support module’s `_ClosedCacheLeaf` to compare HEADs, refs, commit-object identities, content bytes, an untracked cache and clean repository status. [7]

- The support module owns `_seed_leaf_trace_row`, which binds the fixture contract’s code snapshot and exact source path and blob. [8]
