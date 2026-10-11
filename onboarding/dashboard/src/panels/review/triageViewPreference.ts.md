# dashboard/src/panels/review/triageViewPreference.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Persist the reviewer's outline view choice (MIK-R86): changed rows by default, the whole catalogue on demand. The preference is browser-local and read defensively, so a denied store still shows the changed view.

## Code Commentary

- `TreeView` is `changed` or `all`; `TREE_VIEW_KEY` (`review.tree-view.v1`) is its storage key.
- `readTreeView` returns `all` only when the store says exactly that, else `changed`, including for a missing or throwing store.
- `treeViewStore` persists through `setView` (a private-mode failure keeps the control working without persisting); `useTreeView` subscribes components to the current view.

## Evidence

- Changed-first view vocabulary [1]
- Storage key for the persisted view [2]
- Defensive read defaulting to changed [3]
- Persisted store tolerating denied storage [4]
- Component subscription to the view [5]
