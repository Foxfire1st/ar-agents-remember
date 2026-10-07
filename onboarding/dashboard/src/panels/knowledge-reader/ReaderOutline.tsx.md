# dashboard/src/panels/knowledge-reader/ReaderOutline.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

"On this page" beside the document (MIK-R79 rule 10): the chapters of the text and the record
sections with their counts, one line each, the current chapter marked. It is navigation only: cited
code takes its place in the aside while it is open.

## Code Commentary

### Logic

- The outline reads the rendered document's headings (`h2..h6` with ids) and the record sections
  (`[data-page-section]`), building one row per chapter with its level. A scroll listener marks the
  last chapter whose top is above the document's reading line; `revealCurrentChapter` keeps the
  marked row visible inside the outline's own scroll.
- A row click scrolls the document to that chapter (`scrollIntoView`), never changing the reader's
  address.

### Conventions

- The outline derives its rows from the document DOM, so a view that draws no headings draws no
  outline rows; nothing is hard-coded.
- Rows are buttons with `aria-current="location"` on the current chapter.

### Invariants And Boundaries

- **Navigation only:** the outline never changes what the document shows and never fetches.
- **The current chapter is marked and kept visible**; the outline follows the document's scroll.
- **Repeated headings get a suffixed id per slug** (`step`, `step-1`), which keeps the usual repeated
  title distinct; the suffixing is per slug and makes no global collision-free guarantee.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rule 10); it lives outside the code and memory repositories, so it
is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The outline derives chapters from the document and marks the current one. [1]
- The marked row is kept visible inside the outline's scroll. [2]
- The text-derived heading ids with per-slug suffixes the outline navigates. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
