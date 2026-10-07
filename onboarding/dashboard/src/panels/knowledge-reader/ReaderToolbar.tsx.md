# dashboard/src/panels/knowledge-reader/ReaderToolbar.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The Knowledge reader's fixed single-line header and its truthful side reads (MIK-R79 rules 2 and 3):
the repository selector, the memory-tree selector, the record lookup and its open control, the
selection banner, the two count rows' counterparts in the tree, and the named failures of the reads
that feed them. The right side carries the selection's memory/code identifiers and the pin control;
"Browse" appears at phone widths to open the tree as a full screen of rows.

## Code Commentary

### Logic

- `useRead` is the one side-read primitive: it memoizes one promise per `view + selection`, publishes
  the answer only when its key still matches (an old selection's answer is hidden), and keeps a
  failure as a named value. `ReaderToolbar` calls it for the tree choices; the KnowledgeReader parent
  calls it for the record list and passes the same `load` to the tree, so the lookup and the Records
  branch share one acquisition.
- `CommitSelect` offers `published (default)`, the live leaves and the memory commits, disabling
  unconverted commits and still showing an older commit named by an opened URL. `SideFailures` names
  an unreadable tree-choices read, a non-listed commit list and an unreadable record list, beside the
  control each feeds.
- `SelectionBanner`/`SelectionNotes` name the selection kind, tree key, memory revision and code
  tree; a partial index names every file that could not be read; a clean published or leaf tree
  offers "pin" to its memory commit. `PinButton` switches the view to that commit.

### Conventions

- The toolbar is one flex line: it scrolls horizontally rather than wrapping, and labels lose their
  text at phone widths.
- Every read is a GET through `data/knowledgeReader.ts`; nothing here writes.

### Invariants And Boundaries

- **A failed side read is kept and named, never turned into an empty list.**
- **One promise per current selection:** a repo or commit change clears the old answer immediately,
  a late answer cannot be displayed, and a rerender, hide/show or Back does not add a request.
- **A pin is offered only where the tree can move** (`published` or a leaf) and only when the tree is
  clean.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rules 2 and 3) with its O1 ruling; it lives outside the code and
memory repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- One memoized promise per view and selection; late answers never published. [1]
- The failures of the toolbar's own reads are named beside it. [2]
- The memory-tree selector with live leaves and unconverted commits disabled. [3]
- The selection banner and its pin. [4]
- The partial index and code note lines. [5]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
