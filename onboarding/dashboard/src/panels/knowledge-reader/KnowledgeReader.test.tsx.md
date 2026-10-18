# dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The Knowledge reader's suite: real served answers with `fetch` stubbed and controlled test inputs — a
`matchMedia` stub, synthesized tree presence/coverage values and constructed hidden-pane zero
conditions. It renders no real browser and claims none. It pins the MIK-R29
views (path, root summary, subtree paging, test proofs, truth views, census, without-proof, code)
and, since MIK-R79, the document order, top/Back navigation, the citation pane, the phone layout and
the O1 shared records acquisition.

## Code Commentary

### Logic

- The MIK-R29 cases open a file/directory/root/test file/invariant/family/decision/incident/census,
  check the shareable hash, the partial index and unavailable states, the `[n]` marker rendering,
  the located code lines, the history rows and the side-read failures.
- The MIK-R79 additions prove: prose before records and references with empty sections skipped and a
  record leading with its meaning; a followed link opening at the top and Back restoring the visit;
  a wide citation opening beside unchanged prose and a phone citation as its own page with Browse;
  a hidden pane's zero not overwriting the place; an unreadable reference list named instead of zero;
  unsupported links kept as text, external links separate and mapped cards navigating; an Anchor note
  preserved; the leaf code note and empty record lists named; paths and Records usable when a side
  count is unavailable; a newly filtered branch refreshed once; and the O1 acquisition cases — one
  shared list through delay, branches, rerenders and Back, a failed list named without retry or
  gating, and old answers cleared on commit/repository change with late selections ignored.

### Conventions

- Vitest + Testing Library; the served answers are scratch-authored. `fetch` is stubbed, and the suite also sets a `matchMedia` stub, synthesized tree presence/coverage values and constructed hidden-pane zero conditions; it renders no real browser.
- Cases select by test id and by the reader's own address/hash.

### Invariants And Boundaries

The suite binds the reader's document order, navigation and truthful failure display; it does not
claim a browser rendering or test the File Viewer.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packets `MIK-R29@v1` and `MIK-R79@v1`; they live outside the code and memory
repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References






### Cross-Repo References

No cross-repo boundary is crossed by this file.


### Clock And Settlement Evidence

- The document-order, top/Back and wide/phone citation cases remain in this suite. [8]
- Held record replies, branch navigation, rerenders and Back precede the single-acquisition assertion; the following case names a failed shared list without retry. [9]
- Commit and repository changes clear prior record answers; delivered late selections cannot replace the current selection. [10]
- captured is imported from readerTestSupport, then used to serve record bodies here; it is not a declaration in this file. [11]
- Imported heldTree replies and locally held record replies are delivered in async act before negative stale-answer and duplicate-acquisition assertions. [12]
