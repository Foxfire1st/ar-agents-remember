# dashboard/src/panels/file-viewer/FileTree.tsx

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `dashboard/src/panels/file-viewer/FileTree.tsx`    |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-06-29T09:06+02:00                             |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`         |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

`FileTree` renders **one** Headless Tree (from `useFilesTree`) as indented buttons. `FileViewer` mounts it
twice — once for the **code** side and once for the **onboarding** side. The library owns async loading,
keyboard navigation, and selection state; this component is purely the renderer: it maps `getItems()` to
buttons and fully controls the mouse click (select + folder toggle + file open). A code file that has a
paired sidecar shows a marker so a reader can see at a glance which files are documented.

## Code Commentary

### Logic

Props are `{ repo, scope, side, onOpen }`; it calls `useFilesTree(repo, scope, side, onOpen)` and renders
into a container built from **`tree.getContainerProps()`** (the library's a11y/keyboard wiring). Each row
spreads **`item.getProps()`** for accessibility, then layers on its own behaviour: `cx` merges the Panda
`itemBtn({ selected })` with the library's `className`, and `paddingLeft` indents by
`level * 0.85 + 0.3` rem. The explicit **`onClick` overrides the library's spread `onClick`**: it
single-selects (`setSelectedItems([id])`), then for a folder toggles `expand()`/`collapse()`, and for a
file calls `onOpen(data)`. The leading glyph is `▾`/`▸` for an open/closed folder (blank for a file); a
`◖` dot (cyan, `title="has onboarding"`) renders **only** when `side === "code"` and `data?.hasSidecar`.

### Conventions

Panda `css`/`cva`/`cx` from `../../../styled-system/css` (relative import). Rows are mono-font buttons;
`data-testid="tree-${side}"`. The library's `getContainerProps`/`getProps` are spread first for a11y and
keyboard, with the local class and click handler applied on top.

### Invariants And Boundaries

Presentational over the Headless Tree state — **no data fetching here** (`useFilesTree` owns loading and
caching). The explicit `onClick` is load-bearing: it must override the spread library `onClick`, otherwise
a folder click would **double-toggle**. Mouse click is the single source of truth for select + toggle +
open; keyboard **Enter** opens a file via `useFilesTree`'s `onPrimaryAction`, not here. Selection is
single-select. The sidecar marker is code-side only (onboarding entries carry no `hasSidecar`).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Headless Tree adapter it renders (async loading, selection, hotkeys). | L19-L55 | [useFilesTree.ts](useFilesTree.ts) |
| The page that mounts it twice (code + onboarding sides) and supplies `onOpen`. | L236-L249 | [FileViewer.tsx](FileViewer.tsx) |
| The `DirEntry`/`Scope` types it renders. | L10-L34 | [files.ts](agents-remember/dashboard/src/data/files.ts) |
| The route overview that governs this component. | — | [overview.md](overview.md) |

## Update History

- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): renders one Headless Tree (code or onboarding) as indented buttons with fully-controlled mouse click (select + folder toggle + file open, overriding the library's `onClick` so a folder never double-toggles) and a code-side `hasSidecar` marker. Verification metadata pinned to the task base until closeout stamps the L2 code commit.
