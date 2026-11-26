# Managed-sync Git implementation

## Governing Overview

[Worktree lifecycle](../overview.md)

## What This Area Is

Exact Git reading, carrying, parking, reapply proof and cancellation support for resumable code and memory-content sync. The compatibility facade preserves the previous import surface; the qualified modules own implementation and evidence.

## Hot Path Summary

Both live converted-memory sync and scratch structural proof use the generated ignore resolver. It checks pinned stages and original Git conflict bytes, merges authored text, and restores the canonical briefs stanza only after a clean merge.


`_read` supplies exact refs, complete stash inventory and exact revision blobs; `_proof` constructs the native expected reapply; `_stash` parks/reapplies work; `_cancel` assesses ownership and preserves unattributable bytes before discard; `_merge` owns converted-memory carry/validation and staged memory commit settlement; `_code_merge_commit` owns shared conditional `Commit-Check-Pass` sync commit args, the bounded continued code-side commit and its mutation rollback; `_base` supplies shared result vocabulary.

## Operating Model

The driver journals authority and orders code before memory. These helpers prove actual Git state; a status label, sample, cached row or another merge algorithm cannot substitute for that proof. Converted memory merges are structurally planned and validated against both parents and paired code; incoming fast-forwards validate before refs move. Content, validator and repository-hook stops retain different recovery meanings.

The merge helper checks staged content against both verified parents for retained resolutions and automatic memory merges. It matches path, staged line and diagnosis so existing incoming whitespace survives. Failed Git comparisons retain their proof error.

The continued code-side commit runs through `commit_bounded_code_merge` in `_code_merge_commit.py`: `sync_merge_commit_args` stamps `Commit-Check-Pass` onto the comment-stripped `MERGE_MSG` via `git commit -m` only when a runnable pre-commit hook will run (falling back to unstamped `git commit --no-edit` when none is runnable), the commit executes under the shared commit-check bound, and a timed-out or mutating hook restores the pinned index tree and merge sequencer before the typed refusal. The same module proves a published head and clears a stale `index.lock` after a timeout kill. `_commit_staged_merge` in `_merge.py` uses `sync_merge_commit_args` for staged memory merges (stamping only when the memory repository has a runnable pre-commit hook and rewinding `HEAD`, index and sequencer files if a hook mutates the staged tree), while non-conflicting code merges in `start_side_merge` run plain `git merge --no-edit` with no stamp.

Restoration and cancellation ownership are distinct. Full parked inventory and native reapply equality establish restoration; exact index/stash or retained fingerprints establish attribution. Failed attribution never blesses owner work. Cancellation first saves later/unproved bytes with verified manifests and binary patches, then discards and rolls back. The original stash remains authority until terminal recovery. Only the memory root memory.md is disposable cache; a code file with that name remains ordinary content.

## Invariants And Boundaries

- Expected-value pins and typed side identity prevent destructive action on an unrelated ref or checkout.
- Native merge configuration and carried attributes govern expected content; merge-file or alternative-algorithm output is not a fallback.
- Diagnostic samples never establish complete restoration; renamed carried paths require explicit supported matching.
- Structural validation is not semantic approval, and a repository hook is not task acceptance.
- Saving unattributable bytes does not make them owned transaction output; failure to save retains recovery authority rather than authorizing loss.
- Dirty-path classification checks both index and HEAD before selecting an untracked mirror. Staged deletions remain in the staged patch, unstaged deletions in the unstaged patch, and genuine untracked bytes are mirrored separately; deletion absence is not a missing-file save failure.
- This package owns no task acceptance, final integration decision or Git closeout authority.

A structural content-conflict park on a master opens crossing history before recording the retained merge. Close recovery pairs the exact parents with disk and stage-zero ownership checks so a later crossing row survives a refused retry.

## Evidence

- Successful absence from both Git holders selects mirroring; native binary patches preserve staged and unstaged state before rollback. [6]




- Complete stash inventory is distinct from its display sample. [2]
- Native expected reapply has one configured merge owner. [3]
- Saved unproved state is written before destructive cancellation. [4]



- The shared staged comparison intersects path and diagnostic across the two pinned parents. [8]
- Compatibility exports preserve qualified implementation boundaries. [1]

- The continuation delegates the code-side commit to that owner. [10]

- Incoming memory fast-forwards validate before moving refs. [5]
- The continued code-side commit is bounded, stamps `Commit-Check-Pass` only for a runnable hook, and restores the pinned state on a hook mutation. [9]
- Staged sync merge commits stamp `Commit-Check-Pass` only when a runnable pre-commit hook will run, write no stamp when none is runnable, and rewind if a hook mutates the staged tree. [11]
