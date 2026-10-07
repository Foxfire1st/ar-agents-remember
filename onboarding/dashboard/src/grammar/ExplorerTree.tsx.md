# dashboard/src/grammar/ExplorerTree.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

One shared async tree for the File Viewer and the Knowledge reader (MIK-R79 rules 3 and 15). The
headless tree owns loading, selection, expansion and keyboard traversal; the caller owns what a row
opens, what its suffix says and which row marks the current address. The File Viewer and the
Knowledge reader each pass their own row type, loader and open behavior, so no page keeps a second
tree implementation.

## Code Commentary

### Logic

- `ExplorerTree` renders the library's `getItems()` as indented buttons, spreads `item.getProps()`
  for keyboard and ARIA behavior, and keeps the click fully controlled: select, toggle a folder, then
  call `onOpen` when the caller says a folder opens on click (`openFolders`).
- `useExplorerTree` caches loaded rows by path in a ref, loads children through `loadChildren`, and
  records a failed load as a visible `role="alert"` line with the loader's error text instead of an
  empty result; the line does not guarantee the directory's own name, and a later successful reload
  clears it and replaces it with real rows.
- `revision` invalidates the children of every already loaded parent when the caller's filter changes
  (the Knowledge reader's "Show every path"), so a changed filter re-reads each loaded branch once.
- `useRevealItem` re-reads one loaded parent when the current address names a row the cache does not
  hold — a filter switch can otherwise hide the selected row — and only once per changed address;
  ordinary renders and Back to a known row keep the cache.
- The viewport effect scrolls the selected row into view once per `current` value.

### Conventions

- A row is `{path, name, kind: 'dir' | 'file'}`; `kind` is a rendering and expansion fact.
- A caller's own fields ride on its row subtype; `rowAttributes` maps them to DOM attributes for
  tests.
- Styling is Panda CSS in this module; the tree fetches nothing itself.

### Invariants And Boundaries

- Reads are lazy on expansion and on a selection whose row is not yet in the cache; a changed
  `revision` invalidates every already loaded parent, and `useRevealItem` re-reads one loaded ancestor
  once for a changed address. Ordinary renders and Back to a known row keep the loaded cache.
- A failed load is a visible alert carrying the loader's error text and renders no rows for that
  directory; no directory identity is guaranteed, and a later successful reload replaces the alert
  with real rows.
- Keyboard navigation, selection and expansion stay the shared library's; a caller must not override
  the primary action behavior it does not own.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rules 3 and 15); it lives outside the code and memory repositories,
so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The shared tree composes the headless library with one caller-supplied loader and open behavior. [1]
- A failed load is shown as an alert with the loader's error text instead of an empty result; no directory name is guaranteed and a successful reload clears it. [2]
- A new address can re-read one loaded parent, once, when the filter had hidden the row. [3]
- The File Viewer consumes the shared tree through its own row adapter. [4]
- The Knowledge reader consumes the same tree for paths and the Records branch. [5]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
