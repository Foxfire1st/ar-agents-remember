# dashboard/src/panels/file-viewer/FileTree.tsx

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `dashboard/src/panels/file-viewer/FileTree.tsx`    |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-06-29T09:06+02:00                             |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`         |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The Headless Tree adapter it renders (async loading, selection, hotkeys). | `useFilesTree` | dashboard/src/panels/file-viewer/useFilesTree.ts:19-55 |
| The page that mounts it twice (code + onboarding sides) and supplies `onOpen`. | `FileViewerImpl` | dashboard/src/panels/file-viewer/FileViewer.tsx:151-273 |
| The `DirEntry`/`Scope` types it renders. | `DirEntry`; `Scope` | dashboard/src/data/files.ts:13-13; dashboard/src/data/files.ts:31-37 |
| The route overview that governs this component. | `# dashboard/src/panels/file-viewer/ — File Viewer Overview` | onboarding/dashboard/src/panels/file-viewer/overview.md:1-107 |

## Update History

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 4 repo-internal citation rows and preserved verification metadata.

- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): renders one Headless Tree (code or onboarding) as indented buttons with fully-controlled mouse click (select + folder toggle + file open, overriding the library's `onClick` so a folder never double-toggles) and a code-side `hasSidecar` marker. Verification metadata pinned to the task base until closeout stamps the L2 code commit.
