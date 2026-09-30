# dashboard/src/panels/review/ReviewSurface.gitTrees.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.gitTrees.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:46:54+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**MIK-R25 rule 6 on real data: the landed review workspace over a converted leaf's Git trees (1 case).** The three
bodies (`gitTrees.family`, `gitTrees.invariant`, `gitTrees.entries`) are the real served answers of the reviewer
routes for the worker's scratch copy after conversion; each memory side was read through the derived index of its
tree, never a dataset copy. `ReviewSurface` is the real component and only `fetch` is stubbed: the workspace and its
navigation behave exactly as over datasets.

## Code Commentary

### Logic

- The family payload declares `review:trees:2`; the family centre renders; the complete source inventory holds
  the one changed file (`review_source_admission.py`); the family `Comparison-bound unchanged realization context`
  renders its whole 7-member roster from the memory trees' indexes; opening the touched member reads its own review
  and shows its statement, still under the same family.

### Conventions

- The 124 existing review-panel cases were rerun unchanged (worker and reviewer, rounds 1–6).

### Invariants And Boundaries

- This case is the Expected Evidence "UI test on real data after conversion".

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` and its rulings
(`25_reviewer-on-git-trees.json`) live outside the code and memory repositories, so they are named here and not
cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three real bodies. | "gitTrees.family.captured.json"; "gitTrees.invariant.captured.json"; "gitTrees.entries.captured.json" | dashboard/src/panels/review/ReviewSurface.gitTrees.test.tsx:20-22 |
| The one case: the family review from trees, then the touched member. | "renders a converted leaf family review from its trees and opens the touched member" | dashboard/src/panels/review/ReviewSurface.gitTrees.test.tsx:59-100 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new UI test MIK-R25 adds (rule 6 on real data). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
