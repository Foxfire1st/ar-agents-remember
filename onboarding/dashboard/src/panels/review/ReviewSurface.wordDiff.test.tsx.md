# dashboard/src/panels/review/ReviewSurface.wordDiff.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-R35 wired into the real review surface (3 cases).** The real `ReviewSurface` renders the real served bodies
of the converted scratch leaf (`gitTrees.family`, `gitTrees.invariant`, `gitTrees.entries`, `gitTrees.cards` and the
leaf-wide `data/reviewTrees.captured.json`; a tree comparison `review:trees:1`), with only `fetch` stubbed. The
family guarantee and the touched member's statement are given a successor revision. The same bodies without the
tree comparison's token stand for a dataset review, which keeps the landed rendering.

## Code Commentary

### Logic

- `successor(result, tree, sameRevision)` adds a clause to the after guarantee ("…is refused by name, and the
  refusal says what each snapshot answered.") and, for the member review, gives the selected member a successor
  revision (`r3`, "is refused" → "is rejected and reported"). `sameRevision` keeps the guarantee's one revision while
  its text changes (MIK-R21 allows it). Without `tree`, the `review:*` limitations are dropped.
- `serve` answers `/trees` with the cards body when `invariants` is present and the leaf-wide body otherwise,
  `/entries` with the entries body, `/source-content` with a refusal, and the review reads by `selectorId`. Since
  MIK-L32 the surface also makes one `lane=files` read for the tree review; the stub answers it with the leaf-wide
  body, which carries no `lane`, so the lane's destinations read `unavailable` (never a zero) and no assertion here
  depends on them.
- **Case 1, the tree review:** the member centre holds exactly two passages, `guarantee` and `statement`; the label
  is "Changed statement · revision r2 → r3"; the statement reads "…is removed: refused added: rejected and reported
  with…"; the guarantee is `review-center-guarantee-changed` with `data-word-diff="true"` and "Changed guarantee ·
  revision r2 → r3"; no code editor draws the prose. The family review word-diffs its guarantee too.
- **Case 2, the dataset review (ruling Q3):** no passage, and the guarantee keeps its `DiffPane`.
- **Case 3, review R1 F2 (same-revision guarantee):** on the tree review the centre reads "Changed guarantee ·
  revision r2 → r2 · the same revision on both sides; its text differs", the rail reads "Joint guarantee · before ·
  same revision, text differs" and "… after · same revision, text differs", and the details fact is
  `guarantee: same_revision_text_changed`; the dataset form keeps "Joint guarantee · unchanged".

### Conventions

- Like `ReviewSurface.gitTrees.test.tsx`, only `fetch` is stubbed and every body is a captured one; the successor
  revisions are the derivation's own fixed identities (`NEXT_MEMBER`, `NEXT_FAMILY`).

### Invariants And Boundaries

- Proves, through the real surface, two candidate invariants recorded on `IntentWordDiff.tsx.md`: no tree-comparison
  surface calls a changed text unchanged (the centre, the rail and the details), and dataset reviews get no word
  diff. The mutation G8 (the rail not told it reads a tree comparison) fails case 3.

### Todos

- **Resolved by MIK-L32, which landed second (ruling 2026-09-30T12:16:39):** the architect's sync note records that this
  file was rerun on the L35-synced tree and passes; L32's review R1 F6 had also run it on a merged scratch copy (6
  files, 60 tests). The stub answers the lane read with the leaf-wide body, so no `withoutLane` mirror was needed (F6
  accepted: the stub needs no change).

## Evidence

### Docs References

No domain documentation source is configured; the requirement packets `MIK-R35@v1` / `ICR-R35@v1` and the leaf's
rulings live outside the repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The five real bodies the surface is served. [1]
- The successor revisions, including one guarantee revision whose text changes. [2]
- The fetch stub; every `/trees` read without `invariants` gets the leaf-wide body, L32's lane read included (it reads unavailable). [3]
- The tree review's two passages, and the dataset review as landed. [4]
- Review R1 F2 through the real surface. [5]
- The rail prop that makes the navigator compare bytes on a tree comparison. [6]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
