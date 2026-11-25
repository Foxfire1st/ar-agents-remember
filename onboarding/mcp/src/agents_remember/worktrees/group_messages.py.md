# mcp/src/agents_remember/worktrees/group_messages.py

## Governing Overview

[Worktree overview](overview.md)

## Purpose

Preserves regular files from a real `<worktree_group>/messages` directory into the contract's canonical group messages directory before terminal folder removal, without following symlinks or overwriting differing content.

## Code Commentary

- `collect_group_messages` returns immediately unless `lstat` confirms `contract.worktree_group / MESSAGES_LINK` is a real directory (ignoring symlinks and absent paths), verifies canonical destination ancestry, and wraps `OSError` and `ValueError` into `GroupMessageCollectionError`.
- `_message_files` traverses subdirectories via `os.scandir` with `follow_symlinks=False`, yielding only real regular files; `_open_regular` checks `S_ISREG` via `lstat` and confirms `os.path.samestat` after opening to defeat concurrent file swaps.
- `_message_destinations` tries the exact relative path first, then deterministic collision-safe `recovered-<sha256(relative)[:16]>-<sha256(content)>[-N]<suffix[:16]>` names so retries remain idempotent and colliding basenames from different subfolders stay distinct.
- `_preserve_message` skips already-identical files (`_same_message`), verifies write/exec permissions on the nearest existing parent directory (including in `dry_run=True`), and on live runs calls `_place_message`, which copies into an fsynced temp file, re-verifies its SHA-256 digest, links via non-overwriting `os.link`, and fsyncs the target directory.

## Relationships

- Consumed by `worktrees/modules/terminal_group.py` during terminal move-out and preview, and by `worktrees/role_reports.py`.
- Reuses `MESSAGES_LINK` and `canonical_group_messages` from `worktrees/role_reports.py`.

## Evidence

- `collect_group_messages` no-ops unless `<worktree_group>/messages` is a real directory, checks canonical ancestry, preserves regular files, and wraps failures in `GroupMessageCollectionError`. [1]
- `_open_regular` validates parent directories, checks `S_ISREG` via `lstat`, and compares `os.path.samestat` against `fstat` to reject concurrent replacements. [2]
- `_message_destinations` yields the preferred relative path first and then deterministic `recovered-<pathhash16>-<digest>[-N]<ext>` fallback paths. [3]
- `_place_message` copies into an fsynced temp file, re-verifies SHA-256, publishes via non-overwriting `os.link`, and fsyncs the target directory. [4]
