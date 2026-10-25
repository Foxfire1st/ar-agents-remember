# mcp/src/agents_remember/worktrees/modules/startup/start_memory.py

## Governing Overview

[Nearest governing route overview](../overview.md)

## Purpose

Owns external-memory admission and preparation, and truthful named-ref facts, during worktree start.

## Code Commentary

`prepare_memory_for_start` settles external memory only. There is no disabled branch: `_memory_source_state` asserts the contract carries a memory repository and, when it is missing, returns `_missing_memory_repo_state`. That state refuses the removed `disabled-memory` recovery answer by name with the opt-out refusal (`_disabled_memory_choice`: the mode, the reason, and the action — never honored, no longer offered as a choice); any other missing repository blocks with the single `initialize-memory-repo` choice. A start without a memory repository fails before anything is created.

Otherwise the owner requires the exact task-derived protected source ref and creates no source branch: only an explicit dry run carrying an admitted unpublished, non-symlink parent may report the exact source ref `would-create`, and only when that named ref is actually absent. The planned base commit remains the owner's validated readable input; no fallback or guessed source is selected. `_memory_format_for_start` adds `memoryFormat: converted` or `legacy-format` with the first-conversion procedure. Start remains admitted on legacy memory; an absent official ref or unanswered marker probe omits the fact rather than guessing it. Ledger response metadata comes from `derive_memory_ledger` at that recorded base and remains informational; an unattributed history produces empty informational values, and a missing, stale, or malformed cached `memory.md` is not an admission condition.

The existing worktree/mTime preparation keeps its dry-run boundary: no worktree creation or mTime synchronization on dry runs. Mtime reuse skips `.git`, non-files, missing source files, and known divergent paths; files whose content diverges keep fresh checkout mtimes so the watcher re-embeds exactly the delta.

## Evidence


- External-only preparation, exact source ref, no fallback [12]

- Missing repository routes to the blocked state [13]
- Removed answer refused by name, never honored [14]
- One remaining recovery choice [15]
- Protected source ref required, never created [16]
