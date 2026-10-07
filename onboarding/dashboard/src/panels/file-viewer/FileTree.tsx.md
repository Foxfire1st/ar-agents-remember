# dashboard/src/panels/file-viewer/FileTree.tsx

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

`FileTree` is the File Viewer's adapter over the dashboard's shared async explorer (MIK-R79 rules 3
and 15). `FileViewer` mounts it once for the code side and once for the onboarding side; the shared
`ExplorerTree` owns loading, keyboard traversal, selection and expansion, and this module supplies
only the File API loader, the row identity and what a row opens. Before MIK-R79 this file carried its
own render loop and `useFilesTree`; both are gone, so the File Viewer and the Knowledge reader draw
one tree, not two.

## Code Commentary

### Logic

Props are `{ repo, scope, side, onOpen }`. The tree is keyed by `repo\0scope\0side`, so a repository,
scope or side change remounts with a fresh cache. `loadChildren` calls `listDir(repo, scope, path)`
and returns the listing's `code` or `onboarding` children for the requested side; an absent repository
returns no rows. `renderSuffix` marks a code row with `◖` when the entry has a sidecar (the
"has onboarding" marker) and says nothing for onboarding rows.

### Conventions

Rows are the shared `ExplorerRow` shape; `DirEntry`'s own fields ride along untouched. The test id
stays `tree-${side}`, so existing File Viewer tests keep their handle.

### Invariants And Boundaries

The side selection and the loader live here: `loadChildren` awaits `listDir(repo, scope, path)` and
returns the requested side's children, while caching, traversal and rendering belong to the shared
`ExplorerTree`. No second tree implementation may be added for the File Viewer. The sidecar marker is
code-side only; a failed load is the shared tree's visible alert.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rules 3 and 15); it lives outside the code and memory repositories,
so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The File Viewer's tree is the shared explorer with a File API loader. [5]
- The loader reads one directory listing and returns the requested side. [6]
- The shared explorer that owns loading, traversal and selection. [7]
- The page that mounts the tree twice (code and onboarding sides). [8]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
