# dashboard/src/data/reviewTrees.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewTrees.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:46:54+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

**The MIK-R25 adapter cases over the REAL route body of a converted leaf (6 cases).** `reviewTrees.captured.json`
is the measured body of `GET /api/review/trees` served by `create_app(config,
collaborators=serving_collaborators(config))` over the worker's scratch copy (the real memory repository converted
with the leaf's own `knowledge-convert`; a leaf that edits `_not_listed` in `review_source_admission.py` and
re-anchors `RLZ-CXH58B4W`). Only `fetch` is stubbed, so the URL and the body travel the way the browser's do.

## Code Commentary

### Logic

- **The tree view of a converted leaf:** the four trees, the pinning refs (under
  `refs/ar/review/260928_maintained-invariant-knowledge/260928-MIK-L25/2`, the directory-name namespace of ruling
  02:32:42 (a)) and both knowledge sides; the memory diff grouped by record and by source path with currentness per
  side; the worklist items, their history rows without a currency mark, and the gate linkage.
- **The answers that are not a tree view:** an unconverted leaf, a refusal and an unreadable body kept apart; a
  recorded comparison addressed by number and never by path; a side read from a partial index or lost to history
  is named.

### Conventions

- The expectations were updated when the fixture was recaptured under the directory-name refs (worker round 5).

### Invariants And Boundaries

- The body is test evidence from scratch copies, not current project knowledge.

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
| The real captured body. | "reviewTrees.captured.json" | dashboard/src/data/reviewTrees.test.ts:24-29 |
| The tree view of a converted leaf. | "the tree view of a converted leaf" | dashboard/src/data/reviewTrees.test.ts:49-116 |
| The answers that are not a tree view. | "the answers that are not a tree view" | dashboard/src/data/reviewTrees.test.ts:118-176 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new test MIK-R25 adds, recording ruling 02:32:42 (a) in the recaptured expectations. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
