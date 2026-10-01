# dashboard/src/panels/knowledge-reader/PathViews.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The knowledge reader's path-side views (MIK-R29 rule 2): a file's path view, a directory's bounded summary
and its paged subtree, the without-proof list, the census view, and a code file opened at its locator.**

## Code Commentary

### Logic

- **The path view.** `PathView` heads the view "File", "Test file", "Directory" or "Repository summary" (the
  root). A directory leads with its knowledge summary. Then: the onboarding prose with its `[n]` references
  (`ProseWithReferences`); the invariants realized or proved here (for a test file, "Proofs by invariant"), each
  with its state and entries (`InvariantsSection`, which names unverifiable states and their reason); the
  families, each saying whether it contains an invariant here or is routed over the path, `via` which route, its
  stale-member count and its locations elsewhere (`FamilyItem`); and the linked records, a decision in full
  (`LinkedRecordItem` with `DecisionCard`).
- **The bounded directory (ruling 2026-09-30T09:42:58, F2).** `DirectorySummary` lists the children holding
  knowledge with their entry counts and offers "list all N entries under …", a navigation to the `subtree` view.
- **The subtree, page by page.** `SubtreeView` shows every entry row with its invariant and state, and "more (N
  remaining)" while a continuation remains. `useSubtreePages` asks the next page with the last page's
  continuation and appends it; **one page is in flight at a time** (a ref guard plus the button disabled while
  loading, the R2 note, ruling 10:44:14), so a double click asks once. A refused first page shows its code and
  detail (`SubtreeRefused`); a failed next page is named (`SubtreeNextPageFailure`).
- **Without proof.** `WithoutProofView` shows how many of the live invariants no proof names are shown, with
  their realization paths, as information, not a gate.
- **Census.** `CensusView` shows each census's inventory, measures with their counts, counts per class, route
  statuses and each route's status history, and names census file problems; with no census it shows the
  answer's detail.
- **Code.** `CodeView` names a non-present answer (`absent`, `binary`, `too-large`, `unavailable`) with its
  detail; otherwise it shows the file at its blob, names an unresolved locator, and `CodeLines` marks the
  resolved lines (`data-located`) with three lines of context (80 lines when no span).

### Conventions

- Every path and record is a navigation link from `readerParts.tsx`; nothing is local view state.
- Empty lists say what is absent in words ("No family contains these invariants or routes over this path.").

### Invariants And Boundaries

- **A failed source is shown as partial or unavailable, never as empty:** unverifiable states, refused or
  failed subtree pages and non-text code are each named.
- Proved by `KnowledgeReader.test.tsx`: the directory case follows "list all" into the subtree; the root-summary
  case follows "more" and a double click sends one continuation request; the census, without-proof and code case;
  the located-lines case (193 to 213 marked).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The component's own statement of the path-side views. [1]
- Invariants with their states; unverifiable states named. [2]
- A family here or routed over the path, with its locations elsewhere; a linked record, a decision in full. [3]
- A directory's children and the way to its subtree (F2). [4]
- The path view. [5]
- The without-proof list and the census view. [6]
- The located lines marked; a code answer that is not text named. [7]
- The pages read so far, one next page in flight at a time. [8]
- The subtree view, its refusal and a failed next page named. [9]
- The directory, root-summary and double-click cases. [10]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
