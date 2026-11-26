# mcp/src/agents_remember/worktrees/sync_transaction_git/_merge.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Carry code and validated memory content through resumable Git merge steps.

## Code Commentary

Live converted-memory sync tries the shared generated briefs ignore settlement before reporting remaining conflicts. It prepares the root ignore on a fresh staged content merge before validating the memory tree and confirming its parents.

Converted memory is structurally planned before Git mutation: converted sides merge directly, crossings convert legacy sides, and only all-unconverted input takes plain Git. Reports retain conflicts, conversion and reference-alignment diagnostics, even for a clean merge when alignment matters. A converted staged memory merge is validated against both parents and settled paired code before commit. A precommit refusal leaves the staged tree and MERGE_HEAD for repair, so the merge parents are retained, and restores the checkpoint-owned history closure. Incoming converted fast-forwards validate before refs move and require source-line repair, not blessing a destination tree. Real content conflicts remain agent-owned. Hook failure after content merge is a retained commit stop with the actual repository-check reason. The continued code-side commit runs through `commit_bounded_code_merge` in `_code_merge_commit.py`, which builds conditional commit arguments through `sync_merge_commit_args` (stamping `Commit-Check-Pass` via `git commit -m` only when a runnable pre-commit hook will run, else unstamped `git commit --no-edit`), executes under the shared bounded runner, and restores the pinned index and merge sequencer when a hook changes tracked files. Staged memory merges commit through `_commit_staged_merge` using the same `sync_merge_commit_args`: when the memory repository has a runnable pre-commit hook it stamps `Commit-Check-Pass` with the memory hook and rewinds `HEAD`, index and sequencer files with `SyncMergeCommitError` if the hook mutates the staged tree; when no runnable hook exists or it is disabled it runs unstamped `git commit --no-edit`. Non-conflicting code merges in `start_side_merge` run plain `git merge --no-edit` and carry no `Commit-Check-Pass` stamp. Rollback strips only disposable memory cache before abort; it does not establish authority over owner work.

A master's structural merge opens crossing history and writes a report when it pauses for a content conflict, including a conflict outside knowledge records. Other reports select modeled conflicts, a converted side, renumbered references, kept evidence lines or skipped cards. Staged continuation supplies the settled paired-code commit, stages the cache ignore rule and validates the index against both pinned parents with the history staged closed. A refusal restores only checkpoint-owned history bytes and stage zero. The result must prove the exact two-parent ordering.

The shared staged check reads Git comparisons against the task and incoming parents. It uses the NUL-delimited destination paths from those comparisons to attribute each diagnostic. An ordinary finding requires the same staged line and diagnosis for the same path on both sides. An unattributable diagnostic is preserved in the refusal. The continuation and the automatic memory commit use this check, and a Git comparison error retains its proof diagnostic.

## Evidence

- `continue_side_merge` delegates a validated code-side merge to that bounded owner. [12]

- _knowledge_merge: qualified source contract. [2]
- _apply_knowledge_merge: qualified source contract. [3]

- commit_check_report: qualified source contract. [5]
- rollback_side: qualified source contract. [6]

- The shared merge comparison preserves diagnostics that match both sides and ambiguous framing evidence. [9]
- Retained code and memory continuation validate the staged snapshot before committing. [10]

- validate_memory_fast_forward: qualified source contract. [1]
- _finish_staged_memory_merge: qualified source contract. [4]
- The continued code-side commit runs through the bounded owner with conditional `Commit-Check-Pass` stamping and never `--no-verify`. [11]
- `_commit_staged_merge` stamps `Commit-Check-Pass` only when the memory repository has a runnable pre-commit hook (writing no stamp when absent or disabled) and rewinds `HEAD`, index and sequencer files if the hook mutates the staged tree. [13]
- Non-conflicting code merges in `start_side_merge` run plain `git merge --no-edit` without a `Commit-Check-Pass` stamp, while memory merges stop `--no-commit` for staged validation and settlement. [14]
