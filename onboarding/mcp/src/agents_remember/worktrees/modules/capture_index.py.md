# mcp/src/agents_remember/worktrees/modules/capture_index.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Own private-index discovery and trust-flag clearing for disposable worktree captures. This module's `_tree_from_index_copy` calls `kernel.git_command.copy_git_index`, which reads bytes and mtime from one open. `git.py` calls this owner directly for the private-copy capture and retains orchestration. Clear flags only on the private copy; the caller retains the full-capture fallback on unusable copies. The real index and user work stay untouched.

## Code Commentary

Own private-index discovery and trust-flag clearing for disposable worktree captures. This module's `_tree_from_index_copy` calls `kernel.git_command.copy_git_index`, which reads bytes and mtime from one open. `git.py` calls this owner directly for the private-copy capture and retains orchestration. Clear flags only on the private copy; the caller retains the full-capture fallback on unusable copies. The real index and user work stay untouched.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence


- Private capture copies the real index with its time, restores HEAD, clears trust flags only on the copy, applies explicit exclusions and stages working files. Unusable-copy recovery remains with the caller; unchanged stat-matching files are not reconverted merely because conversion rules changed. [1]

## 260928-MIK-L177 The Index Census The Proof Reads

`_index_entries` reads a version-2 or version-3 index in process and returns, per entry, the path, the
mode, the size and the recorded mtime and ctime — the census of every path the capture read, `HEAD`'s
entries plus every eligible addition `git add` made, and no ignored path because the capture never
read one. Any shape it cannot read (version 4's path compression, a truncation, an unreadable file)
answers `None`, so a caller re-derives instead of trusting a partial reading.

`_tree_from_index_copy` accepts a `captured` callback and hands it the private index before the
temporary directory holding it is removed; `git.py` passes that callback through from
`worktree_candidate_tree`, which is how `capture_baseline` obtains the census.
