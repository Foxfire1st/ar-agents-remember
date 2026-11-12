# mcp/tests/test_worktree_sync.py

## Governing Overview

[overview](overview.md)

## Purpose

Checks supported worktree sync, parked-WIP restoration, real conflicts and continuation/cancellation on fixture repositories.

Exercise real code/external-memory sync, retained conflicts, cache independence, exact source/base publication, and journal quarantine.

## Code Commentary

SyncFixture drives the public transaction with an explicit code and memory pair. Cases check paired fast-forward and contract bases, code-conflict continuation, source-ref resolution, cache exclusions, cancelled restoration and memory-content conflict recovery. Memory conflicts are current knowledge-file/content conflicts; the canonical dataset reconciliation engine and its old helper vocabulary are retired. The transaction journal must describe its actual stop/continue state rather than infer completion from matching HEADs. No source or index operation is authorized by reading these tests, and no run is claimed.

### Logic

`SyncFixture` creates disposable code/memory worktrees and canonical contracts. Its default converted=True seeds knowledge/layout.json into the attributed base so ordinary scenarios reach converted judgment; converted=False is explicit legacy-format/refusal/crossing setup, not permission for ordinary legacy sync. Some setup deliberately retains or commits historical tracked memory.md states; these are inputs to prove cache independence, not cache commits created by the sync under test. `map_official_memory` writes attribution in a real memory-content commit. A `source_branch` argument (default `main`) names the official line: both repositories switch to it, the contract's code and memory plans and both worktrees start from it, and `move_official_code`/`map_official_memory` return its tip.

The scenario definitions cover two-sided fast-forward, a retained code conflict and continuation, stale/missing/malformed source caches, cache-independent start and memory-candidate identity, an already-current descendant with changed cache rows, native memory merge conflicts, and quarantine of a nonregular journal without following it.

The native memory case checks both cache-only success and a genuine README conflict. Real draft WIP is parked and returned while staged cache data is excluded. It asserts the exact merge parents, only one new reachable merge beyond its parents, a cache-free committed tree, an untracked materialized cache, and both source/work content. Its interrupted-merge branch adds an unstaged real edit after the merge was staged: resume must refuse with both repositories' refs unchanged, then complete after that edit is staged.

- **L37 (P2 task 1).** `test_cancel_after_a_memory_conflict_restores_the_branch_and_its_tracked_cache`
  (integration lane): with the fixture's tracked `memory.md`, a conflicted memory sync is cancelled; the state is
  `sync-cancelled`, the head is restored, there is no `MERGE_HEAD`, `git status` is empty, the cache is still
  tracked, and the next sync conflicts again.

### Conventions

The inventory describes current scenario definitions, not a production deployment or a certification receipt. The native merge scenario keeps its subcases inside one collected case. Quarantine assertions inspect the archived symlink itself and preserve its outside target.

### Invariants And Boundaries

- Missing attribution or a broken cache cannot become a sync admission refusal.
- Real content conflicts retain MERGE_HEAD and require the intended resolution.
- Memory-side cache data never enters recorded real WIP or a new merge tree.
- Post-admission tracked edits must be staged before resumed merge publication.
- Real source/base/ref and journal identity remain the operation evidence.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.


- `SyncFixture` owns the current boundary described above. [12]


- `WorktreeSyncTests` owns the current boundary described above. [13]



- Tracked, missing, staged and untracked caches do not prevent memory removal; real memory and code files remain protected. [14]

- The real Git fixture and attributed official memory update. [15]

- Fast-forward and retained code conflict behavior. [16]
- Cache-independent source admission, start, and candidate identity. [17]
- Nonregular journal quarantine preserves the outside target. [18]
- Cancel after a memory conflict restores the branch and its tracked cache. [19]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
