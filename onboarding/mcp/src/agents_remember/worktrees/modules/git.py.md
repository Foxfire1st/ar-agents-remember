# mcp/src/agents_remember/worktrees/modules/git.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Provides shared repository/ref, candidate-tree, cleanliness, staging, committing, and changed-path
operations through the guarded kernel Git runner. Workflow admission remains with callers.

## Git evidence and conversion-rule boundary

Git hashes only files its recorded evidence cannot prove unchanged. A same-size rewrite in the second of an index write remains visible because the copy keeps that index's own time. The one-way HEAD merge drops ignored staged additions absent from HEAD and removes staged changes from the starting state; later working-file staging supplies actual content. Captures from a subdirectory clear flags over the entire worktree.

An unchanged stat-matching file is not reconverted solely because attributes, filters or autocrlf changed after the index recorded it; this follows what the real index stages. A changed file is read and converted. Objects remain in the addressed repository because review pins need them. All gate/preview/closeout/review callers use this same capture owner.


- One shared entry owns copied-index and existing full capture. [7]
- The copied index is normalized without changing real-index state. [8]
- Flag clearing uses the worktree top-level and one option per command. [9]

## Code Commentary

### Logic

`require_git` reports failed commands through transport-safe diagnostics while preserving the
runner's raw successful output. The removed local runner is not restored: repository-selector
scrubbing, standard-input ownership, encoding, and timeout policy stay in `kernel.git_command`.
Branch resolution uses explicit local refs, and repository identity uses Git's shared object store.

`worktree_candidate_tree(..., exclude_paths=())` uses a private temporary index per observation. It
seeds from HEAD, removes excluded entries before materialization, stages through an exclusion-aware
pathspec, writes the tree, and removes its scratch directory. The real index remains untouched.
The root cache uses `MEMORY_CACHE_EXCLUDE`; other explicit exclusions use their corresponding root
pathspecs. This avoids treating an ignored cache literal as an explicit add request.

`has_changes`, `worktree_dirty`, and `require_clean` accept the same explicit exclusions.
`contract_has_worktree_changes` excludes `memory.md` only on the memory side. Real content dirt
remains visible.

`stage_worktree_content` removes derived index entries and stages actual content without reading
those paths. `commit_if_dirty` creates an ordinary content commit when its filtered status is dirty.
`publish_tree_commit` publishes the admitted exact tree through `commit-tree` and an expected-old branch update. It settles the message before the per-worktree publication lock, refuses an unfinished Git action or a moved/detached admitted ref, stages the supplied tree, runs the supplied confirmation, then writes and publishes the object. A failure gives the index back only while it still holds this call's staged state. Assume-unchanged, skip-worktree and intent-to-add facts are preserved. This primitive runs no Git commit hook; the reference-transaction hook still runs and its refusal retains Git's diagnostic. Prepared closeout hook policies are separate and are not changed here.

Changed-path helpers retain their distinct semantics: existing-file worklists omit deletions, while
`changed_files_with_counts` reports additions/deletions, rename targets, counts, and binary-file
unknown counts for the serving change-set view.

`stage_tree(repo, tree)` makes the index exactly `tree` with `git read-tree` and reads nothing from the working
tree. The converted closeout stages its memory commit this way, from the tree its gate judged, so a file written to
the working tree after the tree was read is not committed and stays an uncommitted change (INV-49E649). The index
then keeps no stat data, so Git's next comparison with the working tree reads every file once.

### Conventions

Callers must supply exclusions for an owned derived artifact; this is not a blanket ignore rule for
all repositories. Candidate observations own separate scratch paths. Ordinary staging/committing and
verified-index committing remain deliberately separate APIs.

### Invariants And Boundaries

- All Git execution uses the guarded kernel runner and exact caller-selected repository.
- Cache-only dirt cannot trigger a memory-content commit when the caller supplies its exclusion.
- Real ref, ancestry, repository, and content checks are retained.
- Exact-tree publication does not pull in later working-tree changes. Its hook behavior is separate from prepared closeout policy.
- Exclusion never grants permission to move a protected ref or bypass workflow authority.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Evidence

### Repo-Internal References

- `worktree_candidate_tree` implements the retained boundary described above. [10]
- `stage_tree` implements the retained boundary described above. [11]
- `publish_tree_commit` implements the retained boundary described above. [12]
- `_move_admitted_ref` implements the retained boundary described above. [13]
