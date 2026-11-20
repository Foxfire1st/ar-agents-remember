# dashboard/src/panels/knowledge-reader/KnowledgeTree.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The Knowledge reader's tree (MIK-R79 rules 3, 4 and 5), built on the dashboard's shared
`ExplorerTree` rather than a private one. It shows the path hierarchy by default (or every path with
"Show every path"), plus the two count rows and the Records branch. Families, decisions and other
records open by title. When supplied, revision state and the writer's role and model occupy a
wrapping second line beneath the title. Invariants are reached through files and families.

## Code Commentary

### Logic

- `rootRows` is the tree's root: the two count rows ("Invariants without proof", "Census"), the
  repository's path root, and the Records branch. `useRootCounts` reads the without-proof total and
  the census count independently and shows `reading…` until each answers.
- `useKnowledgeLoader` resolves rows per directory: root rows; the Records kinds (excluding
  invariants) and their records from the shared `loadRecords` answer; and `pathRows` for a path
  directory, which asks one `tree` read for that directory. `recordRows` uses
  `recordStandingText` for Records branch rows. `KnowledgeTree` passes that text to
  `ExplorerTree`, whose row detail wraps below the title. The family detail's member rows
  belong to `TruthView` and use `RecordLink`.
- `RowSuffix` shows a directory's `hasOverview` mark, a file's `onboarding` card mark, the entry
  count, and the directory's coverage (`cards/files`, or `coverage unavailable`). The optional
  `hasKnowledge`/`hasOverview` fields mean "unknown" when absent, so a row is never dropped or
  marked absent because a memory enumeration failed.
- `showPath` keeps a row when every-path is on, when it has knowledge, or when it is the current
  path or an ancestor of it; the revision prop makes the shared tree re-read loaded branches once
  when the switch flips.
- `ancestors` opens the path's ancestors (or the record's kind branch) so the selected row is
  visible, and `currentRow` marks it.

### Conventions

- Row identity is `path:<path>`, `kind:<kind>` or `record:<id>`; the address is what a row opens.
- The shared `ExplorerTree` owns row layout and navigation mechanics. This module adapts the
  Knowledge loader, filter, suffix and record detail to that component.
- `currentPath` keeps the open path visible even when a cited code file has no card.

### Invariants And Boundaries

- **The tree is built on the shared component** (rule 3); no second tree component exists for the
  Records branch or paths.
- **Invariants never appear as tree rows** (rule 5); they are reached through their files and
  families.
- **An unknown is not a false:** absent `hasKnowledge`/`hasOverview` must not be rendered as "no
  card"; an unavailable memory enumeration is named as unavailable coverage.
- **A records failure is the shared acquisition's failure:** the tree names it and keeps the path
  tree usable; it does not start a second request.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rules 3, 4, 5 and 6); it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The shared acquisition supplies the Records kinds and rows. A record row keeps its own address and optional standing detail. [8]

### Cross-Repo References

No cross-repo boundary is crossed by this file.

- The root rows, the Records branch and the two count rows. [7]
- The loader routes a directory to root, records or one tree read. [9]
- A row's marks, entry count and truthful coverage suffix. [10]
- The filter keeps the open path and knowledge rows visible. [11]
- The shared tree that owns loading and traversal. [12]
- The tree adapter hands record standing to the shared detail slot alongside the existing suffix. [13]
