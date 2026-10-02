# mcp/tests/test_worktree_sync.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.
## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Exercise real code/external-memory sync, retained conflicts, cache independence, exact source/base publication, and journal quarantine.

## Code Commentary

The terminal-removal case uses the real Git fixture for tracked, missing, staged and untracked cache states. It verifies cache-free terminal preflight and actual non-forced memory-worktree removal. A neighboring `memory.md.other` file and a code-side `memory.md` remain protected. This adds one collected integration case using the existing fixture; no new test support or budget change is needed.

### Logic

`SyncFixture` creates disposable code/memory worktrees and canonical contracts. Some setup deliberately retains or commits historical tracked memory.md states; these are inputs to prove cache independence, not cache commits created by the sync under test. `map_official_memory` writes attribution in a real memory-content commit.

The scenario definitions cover two-sided fast-forward, a retained code conflict and continuation, stale/missing/malformed source caches, cache-independent start and memory-candidate identity, an already-current descendant with changed cache rows, native memory merge conflicts, and quarantine of a nonregular journal without following it.

The native memory case checks both cache-only success and a genuine README conflict. Real draft WIP is parked and returned while staged cache data is excluded. It asserts the exact merge parents, only one new reachable merge beyond its parents, a cache-free committed tree, an untracked materialized cache, and both source/work content. Its interrupted-merge branch adds an unstaged real edit after the merge was staged: resume must refuse with both repositories' refs unchanged, then complete after that edit is staged.

**CYCLE-02 gave the same case a second conflict shape, and it is the one Git cannot decide.** `_assert_knowledge_database_conflict_settles` builds a real three-commit branching scenario over a knowledge database with disjoint valid edits on both sides, commits those datasets into the memory worktree and the memory repository, and then syncs: the ordinary Git merge must stop on the binary file, the transaction must route the three-way merge through the shipped adapter, and the sync must **complete** with `state == "synced"`. What it asserts is exactly what the review asked for — both sides survive in the merged dataset, the merged identity differs from either side's, the three input datasets are byte-identical afterwards, and the merge commit's two parents are the two sides' own commits. The caller invokes no merge function: the test never calls `resolve_knowledge_merge_base` or `merge_resolved_knowledge_datasets`, which is the property that distinguishes a wired seam from a callable one. Both shapes share one collected case rather than taking one each, because the integration lane sits at its declared ceiling of 400 and a further collected case would breach it — above the ceiling conftest raises and the lane then runs zero tests, which is worse than either outcome it would report. The shipped content scenarios were moved intact into `_assert_memory_content_conflict_scenarios` and their body is unchanged.

The module also became a consumer of the shared `merge_case_test_support` fixture for that case, which is why the lifecycle catalog's byte pin moved at this tip without any registered artifact or contract being added.

**CYCLE-02's residue is closed here by making the other orientation's advertised route real.** `_shape_delete_reference_reversed` builds the same row-less `delete_reference_conflict` from the opposite side — the retained (left) side keeps a realization claim while the arriving (right) side deletes the anchor that claim cites, so the arriving delta carries only the DELETE — and `_assert_unretractable_delete_reference_advertises_its_real_route` drives that dataset through `SyncFixture.sync()` and asserts the whole corrected surface: the diagnosis is still the engine's (same code, same `engine_reported_without_row`, still no row, and now `precondition == "no_arriving_insertion"`), `decisions` is empty, `nextOperation` is `continue_sync_resolution` with no `knowledge_resolution` anywhere in `nextArgs`, the summary names the conflict and says what the caller must do instead of promising a continuation, `cancelArgs` is still carried beside the call, and **driving exactly what the response advertised changes the state** to `sync-resolution-incomplete` rather than repeating the response — with HEAD and all three input datasets byte-identical afterwards. That last assertion is the acceptance the round-2 verifier applied and a round-3 verifier will apply again, so it is written as "the advertised call changed something" rather than as "the second response is one of these states". Like the other three scenarios it runs from the existing retained-conflict case through a module-level helper, so no collected case was added to a lane already at its exact ceiling. One item is left **open rather than settled** in this population: `cancelArgs`, which every `sync-resolution-required` response carries, returns `sync-operation-refused` / `SyncGitProofError` in **both** orientations — including the INSERTED-row orientation round 2 verified as working — so the cancel half of the manual continuation could not be proven to settle in this fixture (most likely its missing canonical enclosure locator chain, already recorded as unresolved for the live route); it is named for the round-3 reviewer and is not widened into this leaf. Both captures are kept in the leaf's evidence: the verifier's own BEFORE at `notes/reports/2026-09-21-cycle-fix-verification/evidence/cycle02-orientation/summary-driven.json` and the AFTER at `…/evidence/cycle02-orientation-fixed/`.

- **L37 (P2 task 1).** `test_cancel_after_a_memory_conflict_restores_the_branch_and_its_tracked_cache`
  (integration lane): with the fixture's tracked `memory.md`, a conflicted memory sync is cancelled; the state is
  `sync-cancelled`, the head is restored, there is no `MERGE_HEAD`, `git status` is empty, the cache is still
  tracked, and the next sync conflicts again. Before the fix in `sync_transaction_git.rollback_side` this case
  returned `sync-operation-refused`.
- **L37.** `test_the_merge_stage_copies_are_removed_on_every_way_out`: a settlement's three stage copies live in
  one temporary directory (`STAGE_DIRECTORY_PREFIX`). The directory is gone when the merge refused, when it
  raised, and when a stage could not be written.

### Conventions

The inventory describes current scenario definitions, not a production deployment or a certification receipt. The native merge scenario keeps its subcases inside one collected case. Quarantine assertions inspect the archived symlink itself and preserve its outside target.

### Invariants And Boundaries

- Missing attribution or a broken cache cannot become a sync admission refusal.
- Real content conflicts retain MERGE_HEAD and require the intended resolution.
- Memory-side cache data never enters recorded real WIP or a new merge tree.
- Post-admission tracked edits must be staged before resumed merge publication.
- Real source/base/ref and journal identity remain the operation evidence.
- **An advertised call that provably cannot change the state is a failure of the response, not of the caller.** Where no arriving insertion can be retracted the response advertises only operations that exist, and the case asserts that the advertised call moves the state rather than tolerating a byte-identical repeat.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Tracked, missing, staged and untracked caches do not prevent memory removal; real memory and code files remain protected. [1]
- The real Git fixture and attributed official memory update. [2]
- Fast-forward and retained code conflict behavior. [3]
- Cache-independent source admission, start, and candidate identity. [4]
- Native cache-only success, real conflict continuation, resumed staged-content validation, and the four knowledge-conflict scenarios this leaf's line added. [5]
- **The CYCLE-02 knowledge-dataset case: the sync completes, both sides survive, and the caller invokes no merge entry point.** [6]
- **The CYCLE-02 residue case: the reversed orientation, whose arriving side removed the row the retained side cites, and the assertion that the call the response advertises actually moves the state.** [7]
- **The shared merge-case fixture this module began consuming for that case, and the two imports it takes from it.** [8]
- Nonregular journal quarantine preserves the outside target. [9]

- Cancel after a memory conflict restores the branch and its tracked cache. [10]

- The merge stage copies are removed on every way out. [11]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
