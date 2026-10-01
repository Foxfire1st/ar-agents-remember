# dashboard/src/panels/review/SourceExplorer.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

List the complete measured source-change population independently of family or invariant selection, with every textual or byte-named path retained.

## Code Commentary

### Logic

InventoryRows renders all entries and unrepresentable byte names. Each textual entry carries the backend-derived mapped, unmapped or unknown attribution label. With showContent=false the workspace rail owns navigation while ReviewExpressions opens the actual diff in the center; otherwise SourceContent can expand the row at the listing bound trees. Layout and full-file preferences are caller-owned. Inventory details retain the owner explanation, reproducing command and exact tree IDs.

### Conventions

Styles come from `../../../styled-system/css` as module-level constants (`shell`, `bar`, `sectionLabel`,
`muted`, `rows`, `rowButton`), matching the cockpit panels' idiom. Types come as type-only imports from
`../../data/review` (`ReviewChangedFile`, `ReviewSourceInventory`, `ReviewUnrepresentablePath`), and the
entry renderer comes from `./SourceContent`. Everything else is a plain function: `inventoryEntry`,
`byteNamedEntry`, `DisplayControls` and `InventoryRows` take the values they render and hold no state —
`SourceExplorer` is the only component in the file, and it holds no state either, because `open`,
`layout` and `fullFile` are all caller-owned. `DiffLayout = "split" | "inline"` is exported from here and
imported by the workspace and the centre. Every list item carries a `key` derived from the record's own
identity (`entry.path`, `entry.path_bytes`). Test ids are the contract (`review-source-explorer`,
`review-display-controls`, `review-diff-layout`, `review-full-file`, `review-inventory`,
`review-population-scope`, `review-inventory-entry`, `review-inventory-open`, `review-inventory-byte-path`,
`review-byte-path-not-addressable`, `review-inventory-unclassified`, `review-inventory-command`), and the
machine-readable facts ride data attributes (`data-inventory-state`, `data-status`, `data-path`,
`data-diff-layout`, `data-full-file`, `aria-expanded`, `aria-pressed`). No `useEffect`, no fetch and no
request construction appear in this file: the expansion is a child component's read.

### Invariants And Boundaries

Unavailable inventory is not a measured zero. Partial and unclassified entries remain visible. Byte-named paths remain listed even when the request vocabulary cannot address them for expansion. Semantic selection never narrows this population.

### Todos

None recorded. The byte-form rows stay identification-only until this vocabulary can carry a path as bytes,
and no control in this file writes or re-measures anything: the two display preferences are the reader's,
and the inventory is the server's.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no entries).
The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The current ownership and boundaries above are grounded in these source declarations.

- `SourceExplorer` owns the behavior described above. [1]
- `InventoryRows` owns the behavior described above. [2]
- `inventoryEntry` owns the behavior described above. [3]
- `byteNamedEntry` owns the behavior described above. [4]
- `InventoryDetails` owns the behavior described above. [5]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The explorer lists one repository namespace's
changed paths and carries no identity that ranges beyond it.

No meaningful cross-repo references found.
