# dashboard/src/data/reviewTrees.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewTrees.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:05:09+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

**The real leaf-wide `GET /api/review/trees` body of the MIK-L31 worker's converted scratch leaf `260928-MIK-L31`
(test evidence for `reviewTrees.test.ts`, `worklistGroups.test.ts` and `ReviewSurface.gitTrees.test.tsx`).**
Re-captured by MIK-L31 from L25's capture with this leaf's code (51,212 bytes); its receipt is the fourth entry of
`panels/review/gitTrees.capture-provenance.json` (route, parameters, status, seconds, sha256 and bytes).

## Code Commentary

### Logic

- `state: "trees"` with comparison number `1`, the code base committed at `8a2d4b47`, and both candidates pinned by
  `refs/ar/review/260928_maintained-invariant-knowledge/260928-MIK-L31/1` (the directory-name namespace).
- `code_sides: []` (a live comparison; review F4 fills it on reopen), per-side `currentness`, the
  `knowledge_diff` (3 knowledge files changed, including `knowledge/history/260928-MIK-L31.json`), both
  `knowledge_sides`, and a `worklist` with `source: "computed"`, `bound: true`, state `complete` and 7 items.
- **Every key is snake_case** (MIK-L25 review F9, settled by MIK-L31): the currentness documents carry `code_tree`
  and `stale_members`, and the history row carries `owner_kind`; the test asserts no camelCase key anywhere.
- **MIK-R11's marks and the planned effects (ruling 2026-09-29T21:56:18, carried from L11):** the scratch leaf
  declares two expected effects, so INV-2TQGXFAX is `planned` and FAM-2HBJREC2 `unplanned`, and two
  `planned_untouched` items name the effects no row delivered.
- The body carries no `entries`: the leaf-wide view never does (the cards read is `gitTrees.cards.captured.json`).

### Conventions

Keep the captured bytes and their receipt intact; only the test reads this file.

### Invariants And Boundaries

The body describes scratch copies under `/tmp/mik-l31-real`, not current project knowledge.

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
| Comparison 1, both candidates pinned under `refs/ar/review/260928_maintained-invariant-knowledge/260928-MIK-L31/1`. | "code_candidate"; "memory_candidate"; "\"number\": 1" | dashboard/src/data/reviewTrees.captured.json:9-25 |
| No camelCase key anywhere in this body, including the owners' own documents (the test asserts it). | "carries no camelCase key anywhere in the real body, including the owners own documents" | dashboard/src/data/reviewTrees.test.ts:121-135 |
| The two planned effects no row delivered, and the unplanned and planned marks. | "planned:family:FAM-BWQ4XYF9#strengthen"; "planned:invariant:INV-2TQGXFAX#clarify"; "\"planning\": \"unplanned\""; "\"planning\": \"planned\"" | dashboard/src/data/reviewTrees.captured.json:1813-1961 |
| The per-side currentness. | "currentness" | dashboard/src/data/reviewTrees.captured.json:30-30 |
| The memory diff, the knowledge sides, the state and the bound worklist. | "knowledge_diff"; "knowledge_sides"; "worklist" | dashboard/src/data/reviewTrees.captured.json:1533-1533; dashboard/src/data/reviewTrees.captured.json:1596-1596; dashboard/src/data/reviewTrees.captured.json:1616-1616 |
| The receipt row for this body, now a path relative to the dashboard. | "src/data/reviewTrees.captured.json" | dashboard/src/panels/review/gitTrees.capture-provenance.json:54-54 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update for the re-capture from MIK-L31's scratch leaf: comparison `1` of `260928-MIK-L31`, the snake_case keys (MIK-L25 review F9), the planned/unplanned marks and `planned_untouched` items (carried from L11), and no leaf-wide entries. **Claims re-anchored:** the pinned-ref row (the L25 ref no longer exists in the body) and the receipt row (the receipt now names the file relative to the dashboard); two rows added.
- 2026-09-30T07:50:05+00:00: Generated citation repair: "knowledge_diff"; "knowledge_sides"; "worklist" repointed to dashboard/src/data/reviewTrees.captured.json:1533-1533; dashboard/src/data/reviewTrees.captured.json:1596-1596; dashboard/src/data/reviewTrees.captured.json:1616-1616. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new captured fixture, recording ruling 02:32:42 (a) and review F4 as the body shows them. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
