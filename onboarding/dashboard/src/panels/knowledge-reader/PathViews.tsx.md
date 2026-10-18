# dashboard/src/panels/knowledge-reader/PathViews.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Renders path documents, directory summaries, subtree pages, the without-proof list and saved census reports. Path documents retain breadcrumb/title/facts, one prose body and nonempty invariant/family/record/reference sections in their existing order. Source code at a locator remains the separate ReaderCode owner.

## Code Commentary

`PathView` derives its title from the first level-one-heading regex match in the currently held prose, removes that match from the prose body, and renders document facts before prose and grouped sections after it. Facts name unavailable references rather than a measured zero; references are last, and a note sentence already present in the prose is not repeated by the reference renderer.

The added `usePathProse` starts with the bounded prose supplied by the path answer. “Load whole text” reads the same repository, memory selection and path through the prose operation. It admits replacement text only for a present answer whose selection treeKey and memoryRevision both equal the original answer. A different snapshot or failed/unavailable read leaves the existing text with a named failure and Reload whole view. The mounted hook has an in-flight gate and ignores inactive completions; it does not abort requests. Truncation and declared full byte size are stated explicitly rather than presenting the bounded prefix as the whole document.

Subtree continuation remains separately owned: one page in flight, returned rows accumulated, row states joined and a failed next page stated. This unchanged helper is not given the new prose hook’s liveness or identity guards. Without-proof counts are shown/total observations, not an execution or quality grade. Census fields are the delivered report’s measures, counts, route statuses and recorded history.

## Invariants And Boundaries

Conditional document sections suppress empty lists; the loaded prose remains one reading body. Whole-text loading adds an explicit read/state boundary, not a new memory selection, record acquisition or claim that all asynchronous reader helpers share one guard. Declared currentness/unverifiability and unavailable reference states remain named.

<details>
<summary>Historical prior account — retained, not the current contract</summary>

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

- The path view's title, facts, prose and fixed section order. (historical reference 11)
- The sections and their order after the text. (historical reference 12)
- The facts line where a zero is plain text and a count jumps to its section. (historical reference 13)
- The compact without-proof list. (historical reference 14)
- The census view with measures, counts and route histories. (historical reference 15)
- The paged subtree that reads one page at a time. (historical reference 16)
- The probe that reads a document's prose and references. (historical reference 17)

### Cross-Repo References

No cross-repo boundary is crossed by this file.

</details>

## Evidence

No Domain Documentation entries are configured; current repository bodies and caller boundaries supply the evidence below. The prior source-only accounts are preserved above, not promoted to a fresh execution result.

- The currently held prose supplies the path title/body and retains facts then grouped sections. [11]
- Only nonempty document groups render, in invariant/family/record/reference order. [12]
- Facts distinguish unavailable references from zero and link nonzero counts to their sections. [13]
- Without-proof rows show delivered shown/total counts, explicitly informational rather than a gate. [14]
- Census report problems, measures, counts and route histories are rendered from the supplied report. [15]
- The subtree’s separate in-flight gate accumulates returned pages and preserves a named next-page failure. [16]
- The prose/reference rendering owner handles citation navigation and suppresses a repeated prose sentence in reference notes; it is not the prose network reader. [17]
- Whole-text loading checks the original treeKey/memoryRevision and keeps old text on a failed or mismatched completion. [18]
- Truncation, byte size, in-flight loading and named failure/reload controls are explicit. [19]
