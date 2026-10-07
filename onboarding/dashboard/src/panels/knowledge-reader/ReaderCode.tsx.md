# dashboard/src/panels/knowledge-reader/ReaderCode.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The Knowledge reader's cited-code view (MIK-R79 rule 9): a code file opened at the citation's lines,
rendered by the File Viewer's existing code pane rather than a private code view (rule 15). Where a
citation has one code or test target it opens beside the text; several targets are listed first and
one is chosen; an unresolved locator is named rather than guessed.

## Code Commentary

### Logic

- `CodeView` renders a non-`present` answer as a named line (`path: state — detail`). A `present`
  answer renders a header with the path link, the blob prefix and the cited range, then `FilePane`
  with `highlightedLines` when the locator resolved, so the cited lines are marked and scrolled to.
- An `unresolved` locator adds a named line saying the locator does not resolve here, while the file
  still renders.

### Conventions

- The pane is the shared `FilePane`; this module supplies only the header and the range.
- The path is a reader navigation through `PathLink`.

### Invariants And Boundaries

- **One code view exists**: the File Viewer's pane; no reader-private CodeMirror or highlighter.
- **A citation that cannot open says so in the pane** where it would have opened; the text stays in
  place.
- **The read stays bound to its memory selection**: the answer comes from the address's selected
  tree, and the blob named in the header is the one the lines were resolved in.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rules 9 and 15); it lives outside the code and memory repositories,
so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The cited code opens in the File Viewer's code pane at its lines. [1]
- The shared pane that marks the cited lines. [2]
- The unresolved locator is named, not guessed. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
