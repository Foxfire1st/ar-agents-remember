# dashboard/src/panels/review/ReviewSurface.wordDiff.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.wordDiff.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T13:18:53+02:00 |
| lastVerifiedCommitHash | `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`|
| lastVerifiedCommitDate | 2026-09-30T13:46:40+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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
  `/entries` with the entries body, `/source-content` with a refusal, and the review reads by `selectorId`.
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

- **Carried (ruling 2026-09-30T12:16:39):** whichever of L35 and L32 lands second reruns this file against L32's lane
  fetch. The stub answers every `/trees` read without `invariants` with the leaf-wide body, including L32's
  `/api/review/trees?…&lane=…` read; the reviewer expects the assertions to hold (the lane shows in the rail, not the
  centre) and suggests mirroring L32's `withoutLane` stub if they do not.

## Docs References

No domain documentation source is configured; the requirement packets `MIK-R35@v1` / `ICR-R35@v1` and the leaf's
rulings live outside the repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The five real bodies the surface is served. | "captured<ReviewResult>('gitTrees.family.captured.json')"; "captured<ReviewTreesResult>('gitTrees.cards.captured.json')" | dashboard/src/panels/review/ReviewSurface.wordDiff.test.tsx:15-25 |
| The successor revisions, including one guarantee revision whose text changes. | "function successor(result: ReviewResult, tree: boolean, sameRevision = false): ReviewResult {" | dashboard/src/panels/review/ReviewSurface.wordDiff.test.tsx:32-63 |
| The fetch stub; every `/trees` read without `invariants` gets the leaf-wide body (the carried L32 rerun). | "function serve(tree: boolean, sameRevision = false) {" | dashboard/src/panels/review/ReviewSurface.wordDiff.test.tsx:65-92 |
| The tree review's two passages, and the dataset review as landed. | "word-diffs a tree review's member statement and family guarantee in the center"; "keeps the landed statement and guarantee rendering for a dataset review" | dashboard/src/panels/review/ReviewSurface.wordDiff.test.tsx:108-150 |
| Review R1 F2 through the real surface. | "never calls one guarantee revision unchanged when its texts differ, anywhere on a tree review" | dashboard/src/panels/review/ReviewSurface.wordDiff.test.tsx:152-181 |
| The rail prop that makes the navigator compare bytes on a tree comparison. | "tree={treeComparisonNumber(payload.limitations) !== undefined}" | dashboard/src/panels/review/ReviewWorkspace.tsx:459-459 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T13:18:53+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): created this card for the new surface test module (3 cases), recording ruling Q3 (no word diff for datasets; 2026-09-30T11:53:13), review R1 F2 (the same-revision guarantee on every surface; 12:16:39), and the carried L32 rerun as a Todo. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
