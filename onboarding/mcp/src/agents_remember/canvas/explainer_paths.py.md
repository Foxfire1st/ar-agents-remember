# mcp/src/agents_remember/canvas/explainer_paths.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Where one leaf's explainer environment lives: its folder outside every worktree and task folder, its generation counter, its one lock, its receipts, and the confinement every path below it passes.

## Code Commentary

- `guard_explainer_path` admits a target and every ancestor under the coordination or task root, and holds a symlinked component — reporting it — rather than following it.
- `ensure_leaf_workspace` admits the task folder before and after creating it, refuses a workspace that is a symlink, and creates `instructions/`, `scratch/` and `drafts/` under the same admission.
- `leaf_lock_resource` normalises a path that already ends in `.lock`, so every caller holds one file on disk and no doubled lock name is ever created.
- `remove_workspace_contents` keeps the retired marker and holds a symlink, or a directory containing one, instead of removing anything behind it.
- `receipt_id_segment` admits a receipt id as one path segment, so a separator, a traversal, an absolute path or a hidden name is refused before any effect.
- `repository_path` refuses when the runtime names no such repository or holds no checkout for it, rather than resolving a relative path against the process's own working folder.

## Evidence

- A target and every ancestor below the coordination or task root are admitted, and a symlinked component is held rather than followed [1]
- The leaf's workspace and its three writable folders are created only after the landing folder is admitted, and a symlinked workspace is refused [2]
- Every caller of the leaf lock names one file on disk, with no doubled suffix [3]
- Clearing a workspace keeps its retired marker and removes nothing behind a symlink
- A receipt id is one path segment, so it cannot leave the leaf's receipt folder [5]
- A repository the runtime does not name, or one with no checkout, is refused rather than resolved relative to the process [6]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/explainer_paths.py:464-495 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
