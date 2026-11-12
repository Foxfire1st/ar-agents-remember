# dashboard/src/panels/knowledge-reader/readerNavigation.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The Knowledge reader's place in the browser's own history (MIK-R79 rule 11): every navigation opens
the document at its top, Back returns to the place the reader left, and the shareable address keeps
working. Only the current visible position is kept locally; the browser history entry holds the place
left, so there is no finite path cache to evict Back visits.

## Code Commentary

### Logic

- `useReaderNavigation` owns the address state, follows `popstate`/`hashchange`, and exposes `go`,
  `save`, `remember`, `restore` and `restoreCurrent`. `go` writes a new history entry with
  `knowledgeScroll: 0` (a navigation opens at the top) and records the current position on the entry
  being left. A `go` to the current address only scrolls the pane to the top.
- `remember` records the pane's scroll position; `hiddenDocument` refuses the zero Chromium reports
  for a CSS-hidden panel, so a phone chooser or a hidden layer never overwrites the reader's place.
- `useRestoreReaderScroll` applies the remembered position in a layout effect once the address's
  answer is ready.

### Conventions

- The address type and its hash are owned by `data/knowledgeReader.ts`; this module owns only the
  history and the scroll place.
- The document pane's `onScroll` is wired to `remember`, which only updates the local visible
  position; the history entry is written by `save` at the explicit navigation points (`go`, `Browse`,
  a followed reference), so Back restores the place through `restore`.

### Invariants And Boundaries

- **A navigation opens at the top:** a new address never inherits the previous document's scroll.
- **Back returns to the place left**, including after the document was hidden and shown again.
- **A hidden pane's zero is not a place**: the reader never records a CSS-hidden panel's reported
  scroll as the reader's position.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rule 11); it lives outside the code and memory repositories, so it
is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The address, history entry and scroll place of the reader. [1]
- The place is restored when the document is ready and visible. [2]
- A CSS-hidden pane's reported zero is refused as the reader's place. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
