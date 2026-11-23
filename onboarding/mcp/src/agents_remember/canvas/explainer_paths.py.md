# mcp/src/agents_remember/canvas/explainer_paths.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Where one leaf's explainer environment lives: its folder outside every worktree and task folder, its generation counter, its one lock, its receipts, and the confinement every path below it passes.

## Code Commentary

- `guard_explainer_path` admits a target and every ancestor under the coordination or task root, and holds a symlinked component — reporting it — rather than following it.
- `ensure_leaf_workspace` admits the task and workspace, refuses symlinks, and creates `state/`, `instructions/`, `scratch/`, `drafts/`, `inputs/` and `stages/` under the same checks.
- `leaf_lock_resource` normalises a path that already ends in `.lock`, so every caller holds one file on disk and no doubled lock name is ever created.
- `remove_workspace` unregisters the bound checkouts, then clears the leaf workspace and its private stage files. A nested symlink holds workspace removal.
- `receipt_id_segment` admits a receipt id as one path segment, so a separator, a traversal, an absolute path or a hidden name is refused before any effect.
- `repository_path` refuses when the runtime names no such repository or holds no checkout for it, rather than resolving a relative path against the process's own working folder.

## Evidence



- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/explainer_paths.py:464-495 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.

- Workspace creation checks confinement and creates private input and stage directories alongside the drafts and scratch directories. [2]
- The path guard rejects a symlinked target or ancestor under the admitted root. [1]
- Leaf operations derive the same lock resource without duplicating its suffix. [3]
- Workspace removal unregisters its checkouts and removes the workspace after checking for nested links. [7]
- A receipt ID resolves to one admitted path segment. [5]
- Repository selection requires a registered checkout. [6]
