# mcp/tests/test_sprint_archive_enclosures.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Tests safe retirement of moving masters' enclosures through the real sprint-archive route, including interrupted and resumed archives.

## Code Commentary

Direct helper cases check named directory removal, a master without a contract and a staying master. Entry-route cases cover fresh execution, an interruption after folder moves and a partially moved prefix. They assert current-folder contract discovery, preserved dry-run snapshots, named removed paths and calls to the actual abandon routine with `force=False`.

The post-hook interruption case leaves only enclosure retirement pending. Its resumed preview lists each pending directory under `wouldChange`, keeps `state=would-clean-up`, and preserves task and worktree-group bytes. The real retry retires those directories; a completed preview then reports `archived`, an empty change list and unchanged bytes. A shared master another sprint commands keeps its live enclosure and never calls removal.

## Evidence

- The archive entry finds moving enclosures in fresh, fully moved and partial-move states. \[1] [1]
- A resumed post-hook dry run names pending retirement, leaves bytes unchanged, and completes only after real removal. \[2] [2]
- A master kept by another sprint retains its enclosure and removal is not called. \[3] [3]
- Direct helper retirement reports actual named directory removals. \[4] [4]
- Missing contracts are reported without guessing at an enclosure. \[5] [5]
- Staying masters are skipped by the helper. \[6] [6]
