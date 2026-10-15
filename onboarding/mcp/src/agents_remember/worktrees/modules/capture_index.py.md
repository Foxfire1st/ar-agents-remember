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

