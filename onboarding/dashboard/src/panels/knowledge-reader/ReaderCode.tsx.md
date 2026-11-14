# dashboard/src/panels/knowledge-reader/ReaderCode.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The Knowledge reader's cited-code view (MIK-R79 rule 9): a code file opened at the citation's lines,
Text uses the File Viewer's existing code pane; recognized media uses the shared MediaView rather than a private renderer. Where a
citation has one code or test target it opens beside the text; several targets are listed first and
one is chosen; an unresolved locator is named rather than guessed.

## Code Commentary

### Logic

CodeView first dispatches a media answer with mediaType to MediaCodeView. Other non-present answers show path, state and detail. A present text answer renders the path link, blob prefix and any resolved range, then FilePane with highlightedLines.
- An `unresolved` locator adds a named line saying the locator does not resolve here, while the file
  still renders.

### Conventions

- Text uses the shared `FilePane`; recognized media uses the shared `MediaView`. This module supplies the header and appropriate rendering props.
- The path is a reader navigation through `PathLink`.

### Invariants And Boundaries

- Text citations use the File Viewer's `FilePane`, and media citations use the shared `MediaView`; this module builds no private CodeMirror editor or highlighter.
- **A citation that cannot open says so in the pane** where it would have opened; the text stays in
  place.
- **The read stays bound to its memory selection**: the answer comes from the address's selected
  tree, and the blob named in the header is the one the lines were resolved in.

### Todos

No additional work is asserted by this card.

A recognized media answer with a selection uses knowledgeMediaUrl with that selection's repository and memory commit, retains CodeHeader and supplies the measured size to MediaView. Cited Markdown that arrives as present text remains source in FilePane.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rules 9 and 15); it lives outside the code and memory repositories,
so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References



- The Knowledge reader's text-code view renders FilePane and passes the resolved cited line range as highlightedLines. Media citations use the separate media view. [1]


- The shared pane that marks the cited lines. [2]



- The unresolved locator is named, not guessed. Anchor: `CodeHeader` [3]


### Cross-Repo References

No cross-repo boundary is crossed by this file.
