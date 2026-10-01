# dashboard/src/panels/file-viewer/lineNumbering.ts

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

**One CodeMirror gutter that keeps a file's own line numbers when the document is an excerpt (MIK-R31).** The
reviewer's focused expression cards show one region of a file, and its gutter must read the file's lines, not the
excerpt's. `numberedFrom(first)` returns the plain `lineNumbers()` extension for `first = 1` (exactly the gutter the
two panes used before) and otherwise a `lineNumbers` whose `formatNumber` adds `first - 1`.

## Code Commentary

### Logic

- `FilePane` passes its `firstLine` prop (default 1); `DiffPane` passes each side's own first line, so the before
  editor of a split diff numbers from the before range's start and the after editor from the after range's start.

### Conventions

- The default path is byte-for-byte the old extension, so every existing caller renders as before.

### Invariants And Boundaries

- Presentation only: it changes which number is printed beside a line, never the text.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; CodeMirror's `lineNumbers` option `formatNumber` is the only external
API used, and its behaviour is exercised by the mounted card cases.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The gutter: plain for line 1, offset otherwise. [1]
- The file pane's use, through its optional first line. [2]
- The diff pane's use, one first line per side. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
