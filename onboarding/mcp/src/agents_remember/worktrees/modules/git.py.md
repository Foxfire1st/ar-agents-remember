# mcp/src/agents_remember/worktrees/modules/git.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Provides shared repository/ref, candidate-tree, cleanliness, staging, committing, and changed-path
operations through the guarded kernel Git runner. Workflow admission remains with callers.

## Git evidence and conversion-rule boundary

Git hashes only files its recorded evidence cannot prove unchanged. A same-size rewrite in the second of an index write remains visible because the copy keeps that index's own time. The one-way HEAD merge drops ignored staged additions absent from HEAD and removes staged changes from the starting state; later working-file staging supplies actual content. Captures from a subdirectory clear flags over the entire worktree.

An unchanged stat-matching file is not reconverted solely because attributes, filters or autocrlf changed after the index recorded it; this follows what the real index stages. A changed file is read and converted. Objects remain in the addressed repository because review pins need them. All gate/preview/closeout/review callers use this same capture owner.



## Code Commentary

### Logic

`require_git` reports failed commands through transport-safe diagnostics while preserving the
runner's raw successful output. The removed local runner is not restored: repository-selector
scrubbing, standard-input ownership, encoding, and timeout policy stay in `kernel.git_command`.
Branch resolution uses explicit local refs, and repository identity uses Git's shared object store. Landing callers use `require_readable_commit` and `require_ancestor`: only ancestry return codes 0/1 mean true/false; a failed object or ancestry read refuses with the caller's input name rather than acting absent.

`worktree_candidate_tree(..., exclude_paths=())` uses a private temporary index per observation. It
seeds from HEAD, removes excluded entries before materialization, stages through an exclusion-aware
pathspec, writes the tree, and removes its scratch directory. The real index remains untouched.
The root cache uses `MEMORY_CACHE_EXCLUDE`; other explicit exclusions use their corresponding root
pathspecs. This avoids treating an ignored cache literal as an explicit add request.

`has_changes`, `worktree_dirty`, and `require_clean` accept the same explicit exclusions.
`contract_has_worktree_changes` excludes `memory.md` only on the memory side. Real content dirt
remains visible.

`stage_worktree_content(repo, *, exclude_paths=(), index_path=None)` removes derived index entries
and stages actual content without reading those paths. With `index_path` every step runs through
`_require_git_with_index` against a private index file instead of the worktree's own index — this is
the staging half of the converted baseline adoption's private interval; without it the worktree's own
index is staged. `_require_git_with_index` runs one Git command against the private file and keeps the
failure's name. `commit_if_dirty` creates an ordinary content commit when its filtered status is dirty.
The generic two-sentence form of this contract (derived-entry removal without reading; ordinary commit when dirty) now stands above in signature-specific form with the private-index interval.
`publish_tree_commit` publishes the admitted exact tree through `commit-tree` and an expected-old branch update. It settles the message before the per-worktree publication lock, refuses an unfinished Git action or a moved/detached admitted ref, stages the supplied tree, runs the supplied confirmation, then writes and publishes the object. A failure gives the index back only while it still holds this call's staged state. Assume-unchanged, skip-worktree and intent-to-add facts are preserved. Runs pre-commit before commit-tree, refuses tracked/index mutation with index restore, and stamps Commit-Check-Pass.

Existing-file worklist helpers remain here and omit deletions. Native change-set count/status
parsing now lives in the sibling `worktrees/modules/git_changes.py`: its
`changed_files_with_counts` keeps deletions, rename destinations and unknown binary counts with
NUL-delimited path identity. `serving/changeset_reads.py` is the cached serving wrapper over that
implementation, not the parser's owner. This mutation/capture module no longer defines that reader.

The two read domains keep different Git refresh behavior. The landing-chain/worklist `_nul_git` here passes its arguments to the guarded runner without adding `diff.autoRefreshIndex=false`; `changed_worktree_paths` therefore retains ordinary Git refresh behavior for its NUL-delimited worklist. Only the sibling change-set `_nul_git` adds that override, preserving the real index generation for its content/count reads. A stat-only identical-byte replacement is not a content change for the landing worklist; the existing regression stages the native exact tree after such a rewrite and then asserts an empty changed-path list. This distinction does not override the shared kernel's `GIT_OPTIONAL_LOCKS=0` policy or authorize a new index write.

`stage_tree(repo, tree)` retargets only differing index entries using cached diff-index and update-index, reading no working files. Unchanged entries retain stat data and flags; replaced entries have assume-unchanged/skip-worktree flags restored, and absent-tree intent-to-add entries remain. The resulting write-tree is exactly the judged tree; later working writes remain uncommitted (INV-49E649). It does not run read-tree or discard every entry's stat data.

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

## Branch-holding checkout

checkout_holding_branch reads git worktree list --porcelain and selects the first non-detached, non-bare checkout holding the exact refs/heads branch, returning None if unavailable. Series direct-code mutation binds intent and proof to this actual checkout while the contract anchors the repository. This reader neither commits code nor grants permission.

`capture_index.py` owns `_tree_from_index_copy`, `_add_all_args` and `_excluded_pathspec`; this module calls that owner directly. The shared capture entry, full-capture recovery and publication policy remain here. The extraction preserves the copied-index timestamp, HEAD normalization, trust-flag clearing and conversion-rule boundary described above.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.


### Repo-Internal References

- Native NUL-delimited statuses/counts live in `git_changes`; the serving wrapper caches that one implementation. [27]

- Only the change-set wrapper adds diff.autoRefreshIndex=false; the native landing worklist keeps ordinary Git refresh behavior, and the existing identical-byte/native-stage regression asserts an empty worklist. [28]

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.



- The exact cache pathspec is defined beside the consumer filename. [21]


### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.

- One shared entry owns copied-index and existing full capture. [7]
- The copied index is normalized without changing real-index state. [8]
- Flag clearing uses the worktree top-level and one option per command. [9]
- `worktree_candidate_tree` implements the retained boundary described above. [10]
- `stage_tree` implements the retained boundary described above. [11]
- `publish_tree_commit` implements the retained boundary described above. [12]
- `_move_admitted_ref` implements the retained boundary described above. [13]
- One Git command runs against a private index file; a failure keeps its name. [14]
- Staging writes a private index file when asked; otherwise the worktree's own index. [15]
- Ref/repository identity and transport-safe errors have shared implementations. [19]
- Candidate trees use private indices and exact derived-path exclusions. [20]
> Historical reference 22 records the former local change-set reader. Its current serving owner is named in the operative account and current source evidence, not re-advertised as a local function.
- `stage_tree` makes the index exactly one tree and reads nothing from the working tree. [23]
- checkout_holding_branch reads git worktree list --porcelain and selects the first non-detached, non-bare checkout holding the exact refs/heads branch, returning None if unavailable. [24]

- Capture orchestration delegates private-copy materialization and exclusion pathspecs to their actual owner. [25]

- The serving count reader retains deletion/rename/binary path facts outside this mutation module. [26]
