# dashboard/src/panels/review/LeafKnowledgeChanges.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The panel "Knowledge changes in this leaf" of the reviewer's centre, for a tree comparison. It renders
the leaf-wide tree read: the Git diff of the two memory trees, the currentness of each side, and the
worklist with the history rows about its items. While that read has no tree answer, the same place shows
a notice instead: that the view is being computed, or that it is unavailable and why.

## Code Commentary

### The notice (`LeafKnowledgeNotice`)

- It renders a visible `<section>` with the panel's own title and a status paragraph; there is no
  collapsed disclosure.
- For the read phase `loading` the status paragraph reads "Computing the knowledge changes of this leaf.
  The first read of a large leaf takes several seconds; the review stays usable." The paragraph has
  `role="status"` and the test ID `review-leaf-knowledge-computing`; the container has the test ID
  `review-leaf-knowledge-pending`.
- For the phase `unavailable` the status paragraph reads "The knowledge changes of this leaf are
  unavailable: <detail>"; a separately rendered paragraph follows with "Next: <next action>." when the
  failure names one. The container has the test ID `review-leaf-knowledge-unavailable`.
- For every other phase it renders nothing. A dataset review (`not-converted`) therefore shows no panel.
- The notice exists so that the place of the panel is never empty while a tree read is expected: an absent
  panel would read as "this leaf changed no knowledge".

### The panel (`LeafKnowledgeChanges`)

- **Status line.** The number of changed knowledge files, or "knowledge diff unavailable"; then the
  worklist's state, item count and source, with "not bound to this comparison" when the worklist is not
  bound; "no worklist applies" when the worklist's source is `absent`; "no worklist" when the answer
  carries none. When the read answered for another comparison than the review shows, the line names both
  comparison numbers.
- **Degraded sides.** One line for each knowledge side that is not available or was read from a partial
  index (`degradedKnowledgeSides`).
- **Diff** (`KnowledgeDiff`). By record, with the entries a sidecar change touched; by source path; then
  history and other knowledge files. Each file is a disclosure with its patch, and a truncated patch says
  so.
- **Currentness** (`Currentness`). One disclosure per side, "before at the code base" and "after at the
  code candidate". Its summary gives the counts of current, stale, unverifiable and unrealized invariants,
  or the reason the side is unverifiable, or "not read"; its list gives every invariant that is not
  current with those of its entries that are not current and their reasons.
- **Worklist** (`Worklist`). Knowledge items with their planning mark, the planned effects no row
  delivered, the other kinds grouped by kind, the unexplained items (`UnexplainedGroups`: one disclosure
  per file, split by coverage state), and the gate linkage of each changed file: how many of its hunks
  are linked. Each item shows its subject, kind, planning mark and "answered" when a row satisfies it,
  the history rows about it by owner, disposition and identity, or "no history row about it", and its
  facts in a nested disclosure.
- The panel offers no disposition of an item. The grouping (`worklistGroups`) and the linkage counts
  (`hunkLinkage`) come from `worklistGroups.ts`; this file renders them.

## Evidence

- The module comment: what the panel shows, and that history rows answer the unexplained changes. [11]
- The panel: status line, degraded sides, diff, currentness, worklist. [12]
- The notice for a loading and for an unavailable read; nothing for any other phase. [13]
- The worklist's status text. [14]
- The diff by record, by source path, and history and other files. [15]
- Currentness per side. [16]
- The unexplained groups by file and coverage state. [17]
- Knowledge items, planned effects, other kinds, unexplained groups and the gate linkage. [18]
- The notice says that it is computing, as a status region. [19]
- The notice names the failure and its action. [20]
- The notice draws nothing for a dataset review. [21]
