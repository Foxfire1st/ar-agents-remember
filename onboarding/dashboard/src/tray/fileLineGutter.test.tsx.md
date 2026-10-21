# dashboard/src/tray/fileLineGutter.test.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks scoped line/range picking through the File Viewer gutter.

## Code Commentary

### Logic

Single clicks add a line, Shift replaces the anchored range, existing lines/ranges deduplicate; one named keyboard tab stop supports Enter/Space/arrows/Home/End without focus loss; only the actual viewer pane has the gutter.

Uses real DualPane/FilePane and CodeMirror with a bounded five-line fixture plus direct takeFileLine transitions.

### Invariants And Boundaries

Does not prove browser pixel hover appearance; ordinary code excerpts deliberately lack tray gutters.

## Evidence

- Checks scoped line/range picking through the File Viewer gutter. [1]
- Checks scoped line/range picking through the File Viewer gutter. [2]
- Checks scoped line/range picking through the File Viewer gutter. [3]
