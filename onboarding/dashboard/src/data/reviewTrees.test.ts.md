# dashboard/src/data/reviewTrees.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewTrees.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:05:09+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

**The MIK-R25 adapter cases over the REAL route body of a converted leaf, and since MIK-L31 the wire convention
and the cards address (8 cases).** `reviewTrees.captured.json` is the measured body of `GET /api/review/trees`
served by `create_app(config, collaborators=serving_collaborators(config))` over the MIK-L31 worker's scratch copy
(the real memory repository converted with the worktree's own `knowledge-convert`; a leaf that edits `_not_listed`
in `review_source_admission.py`, re-anchors `RLZ-CXH58B4W` and declares two expected effects; re-captured by
MIK-L31 from L25's). Only `fetch` is stubbed, so the URL and the body travel the way the browser's do.

## Code Commentary

### Logic

- **The tree view of a converted leaf:** the four trees (code base `8a2d4b47`), the pinning refs (under
  `refs/ar/review/260928_maintained-invariant-knowledge/260928-MIK-L31/1`, the directory-name namespace of ruling
  02:32:42 (a)) and both knowledge sides; the currentness read through `code_tree.tree_id`; the memory diff grouped by record and by source path with currentness per
  side; the worklist items, their history rows without a currency mark, and the gate linkage.
- **One wire convention (MIK-L25 review F9, settled by MIK-L31):** no camelCase key anywhere in the real body,
  including the owners' own documents (`stale_members`, `owner_kind` present); `treeComparisonNumber` reads
  `review:trees:<n>` and nothing else, and `reviewTrees` sends `invariants=a,b` with `comparison=7`.
- **The answers that are not a tree view:** an unconverted leaf, a refusal and an unreadable body kept apart; a
  recorded comparison addressed by number and never by path; a side read from a partial index or lost to history
  is named.

### Conventions

- The expectations were updated when the fixture was recaptured under the directory-name refs (L25 worker round 5),
  and again when MIK-L31 re-captured it from its own scratch leaf (leaf, refs, code base and history file names).

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
| The tree view of a converted leaf. | "the tree view of a converted leaf" | dashboard/src/data/reviewTrees.test.ts:51-118 |
| One wire convention, and the comparison and selection a request names. | "one wire convention (MIK-L25 review F9)" | dashboard/src/data/reviewTrees.test.ts:120-145 |
| The answers that are not a tree view. | "the answers that are not a tree view" | dashboard/src/data/reviewTrees.test.ts:147-205 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Purpose and Logic record the re-captured body (leaf `260928-MIK-L31`, comparison 1) and the two new cases (no camelCase key, MIK-L25 review F9; `treeComparisonNumber` and the `invariants=` address, ruling 05:36:19 Q2); one row added.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new test MIK-R25 adds, recording ruling 02:32:42 (a) in the recaptured expectations. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
