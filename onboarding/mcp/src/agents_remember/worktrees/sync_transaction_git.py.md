# mcp/src/agents_remember/worktrees/sync_transaction_git.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Exact Git mutations and proofs for resumable code and memory-content sync.

## Code Commentary

### Logic

WIP is parked/restored under recorded ownership; only memory-side root memory.md is disposable cache. Code files with that name retain ordinary semantics.

Before Git mutates a divergent memory merge, _knowledge_merge plans structural knowledge/onboarding merge for any converted side: all-converted trees merge directly, crossings convert legacy sides first, and only all-unconverted sides use plain Git. _apply_knowledge_merge installs clean/conflicted items and writes a report when the merge leaves something for the curator: conflicts, a converted side, or — since MIK-R66 — alignment diagnostics (renumbered references, kept evidence lines, skipped cards), even on a clean merge.

Remaining real conflicts go to the agent. Staged continuation closes crossing history and validates the exact staged tree against both parents/paired code before the admitted ordinary merge commit. Refusal leaves the merge staged; no dataset stage or row-decision route remains. Rollback retains exact ownership and restores tracked cache before abort.


Ref reads distinguish invalid names, absent refs, and inspection errors. Pinned refs use expected-value creation/deletion, and worktree identity includes the recorded repository and branch. A completed side must be the admitted fast-forward or an exact two-parent merge in pre-sync/source order.

Dirty-path and WIP helpers take the typed side record. Only the memory domain excludes root memory.md. Before a native operation, only that disposable path is restored/cleaned so its local edits cannot obstruct Git or enter a stash; substantive WIP is still parked with untracked files and later restored and proved.

**Since MIK-R22, the memory merge is validated before it is committed.** `start_side_merge` and `continue_side_merge` take an optional keyword `paired_code` (a `worktrees.knowledge_validation.PairedCode`: the code side's settled result commit) and thread it through `_existing_side_merge` and `_continue_memory_merge` to `_finish_staged_memory_merge`. After the cache ignore rule is staged, that function writes the staged index as a tree (`git write-tree`) and calls `memory_commit_refusal` with the tree, both parents (`preSyncHead`, `sourceCommit`) and `paired_code`, before `git commit --no-edit`. A refusal raises `SyncKnowledgeValidationError`, a subclass of `SyncGitProofError`, and the merge stays staged: nothing is committed, and `HEAD` and `MERGE_HEAD` are unchanged. Unconverted memory, where neither the candidate nor a parent holds `knowledge/layout.json`, gets `None` from the helper and commits exactly as before. Code-side merges and memory plans that are not a merge (fast-forward, skip, already-current) are not validated here.

The cache is refreshed as a disposable view after applicable memory results. A narrow cache-only stash conflict recovery additionally requires a clean content prestate and the existing restored-WIP proof. Other Git failures remain errors. Rollback and temporary removal retain exact side/ref identity and refuse later substantive work.

Restoration compares each substantive parked entry with the computed reapply onto the carried head, rather than dirty-path presence or whole-file equality. `stashed_parked_paths` enumerates tracked changes and the untracked third parent completely; a capped journal sample is diagnostic only and unreadable inventory cannot pass. Already-held edits beside unrelated landed changes therefore restore successfully. Non-computable content fails the restoration proof; exact stash-owned raw content can still establish cancellation ownership where supported.

Cancellation ownership is separate from restoration proof. `assess_stash_tree` compares worktree and index content against live recorded holders; `assess_retained_tree` checks operation-created worktree-plus-full-index fingerprints. Unknown attribution is not later-work attribution. Resumed merges and crash reapplies earn fingerprints through exact scratch reproduction of dirty/untracked sets and per-path content/index state; converted-memory replay includes structural crossing, paired code and owner. Where that proof fails, cancellation refuses without adopting owner bytes. Only explicitly proven owned untracked paths may be removed during rollback.

### Conventions

All commands use the shared runner. `SyncGitProofError` exposes an unproven Git transition; its subclass `SyncKnowledgeValidationError` is the validator's refusal, which the driver catches first so it is reported as `sync-knowledge-validation-refused`. Cache stripping is domain- and path-specific; it is not an ours/theirs policy for other files.


### Invariants And Boundaries

- Only exact admitted fast-forward/two-parent output is accepted.
- Structural validity is not semantic approval.
- Every converted memory merge is validated before commit.

- Memory cache state cannot block dirty/WIP, native merge, resolution preview, or admitted continuation.
- Real unresolved content is retained with its stash or MERGE_HEAD evidence.
- Code-side memory.md keeps normal Git conflict semantics.
- Only the pinned fast-forward or exact admitted two-parent merge is accepted.
- No cache-only commit or cached-row authority is introduced.
- **A converted memory merge is never committed without a passing validator run (MIK-R22 rule 8).** The staged tree is validated against both parents and the paired code commit before `git commit`; a refusal, an unbound validator, an unknown paired code commit, or an unreadable tree leaves the merge staged. There is no parameter that skips the validation.
- **Cancel after a memory conflict restores a tracked cache first (L37).** The memory merge removes a tracked
  `memory.md` from the index, which leaves it on disk as an untracked file; `git merge --abort` then refuses to
  overwrite it. `rollback_side` therefore calls `discard_memory_cache_changes(side)` before the abort: a tracked
  cache is restored from `HEAD`, an untracked one is removed, and the code side is untouched. An abort that still
  does not restore the head raises `_abort_failure`, which names Git's own stderr. A line that
  untracks the cache could already cancel.

## Evidence

### Docs References

No external Domain Documentation entries are configured. Source and test assertions are distinguished from execution and acceptance evidence.

### Repo-Internal References

- Pinned refs/checkouts. [1]

- Exact staged validator before commit. [12]

- Attributable rollback. [14]

- Current public content-conflict scenario. [15]

- The report gate keeps conflicts, conversions, and every nonzero alignment population. [16]

- The merge installs the structural plan and persists the report through that gate. [17]

- Exact WIP park/restore proof. [2]

- Exact refs, worktree identity, and authority-safe cleanup. [30]

- Typed dirty/WIP and restore proof exclude only the memory cache. [31]

- Content-domain conflicts and narrowly scoped cache state handling. [32]

- Native merge, exact continuation, and cache-free merge output; both entry points carry the paired code commit to the final memory merge, which first closes any master-line crossing history file the merge adds. [33]

- The crossing helpers this module drives. [34]

- The managed sync crosses an unconverted leaf into a converted line, and leaves overlapping edits to the curator. [35]

- The staged memory tree is validated against both parents before the commit; a refusal raises and leaves the merge staged. [36]

- The managed sync refuses a merge with duplicate IDs, keeps it staged, and syncs after the repair. [37]

- Rollback and created-head proof retain exact operation ownership. [38]

- The rollback restores the cache before the merge abort. [39]

- A failed abort names Git's reason. [40]

- Cancel after a memory conflict restores the branch and its tracked cache. [41]

- The proof enumerates tracked and untracked parked paths with no sample acceptance. [42]

- Reapply expectations compare parked, pre-sync and carried content. [43]

- Interrupted converted-memory output is attributed only by exact merge-plus-crossing replay. [44]

- Cancellation compares live stash holders with worktree and independent index content. [45]

- Retained fingerprints distinguish provable operation output from later and unknown bytes. [46]

- Supported staged continuation. [8]

### Cross-Repo References

No additional configured cross-repository contract is asserted.
