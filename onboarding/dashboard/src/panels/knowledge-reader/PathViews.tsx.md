# dashboard/src/panels/knowledge-reader/PathViews.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The reader's path-side views (MIK-R29 rules 2 and 3, relaid out by MIK-R79 rules 7 and 14): a file's
path view, a directory's bounded summary and its paged subtree, the without-proof list and the census
view. The code file opened at its locator is `ReaderCode.tsx`'s `CodeView`. A document reads from its title through its text
without interruption; the record sections and references follow the text, empty sections are not
drawn, and lists use one line per row.

## Code Commentary

### Logic

- `PathView` takes the file's own first heading as the title, renders the sticky breadcrumb line, the
  facts line (invariants, families, records, references counts, each a jump to its section and a zero
  as plain text), the prose through `ProseWithReferences`, and then `DocumentSections` in the fixed
  order: invariants, families, records, references last. A references section that could not be read
  says so instead of showing zero; the block "Knowledge below this directory" is gone.
- `WithoutProofView` and `CensusView` keep the compact one-line rows; the census names its problems
  and each report's measures, counts, route statuses and history.
- `SubtreeView` reads pages on request through `useSubtreePages`: one page in flight at a time, the
  accumulated row states shown, and a refused or failed next page named in place.
- `PathView` computes the title from the first `#` heading and removes it from the rendered body so
  the title is not repeated.

### Conventions

- Sections come from `Section`, entries from `EntryRow`, decisions from `DecisionCard`; all links are
  reader navigations.
- A record group links to the record's own page; a family shows its guarantee, route and other
  locations.

### Invariants And Boundaries

- **Order is fixed** (rule 7): invariants, families, decisions and other records, references last; a
  record's meaning leads its page.
- **No empty section is drawn**; a zero count is plain text with no section anchor.
- **A failed or unavailable read is named**, never rendered as an empty list or zero.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rules 7, 12 and 14); it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The path view's title, facts, prose and fixed section order. [11]
- The sections and their order after the text. [12]
- The facts line where a zero is plain text and a count jumps to its section. [13]
- The compact without-proof list. [14]
- The census view with measures, counts and route histories. [15]
- The paged subtree that reads one page at a time. [16]
- The probe that reads a document's prose and references. [17]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
