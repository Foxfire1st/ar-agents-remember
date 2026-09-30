# dashboard/src/panels/review/gitTrees.family.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/gitTrees.family.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T13:23:08+02:00 |
| lastVerifiedCommitHash | `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`|
| lastVerifiedCommitDate | 2026-09-30T13:46:40+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent` body over the MIK-L31 worker's converted scratch leaf `260928-MIK-L31` (test
evidence for `ReviewSurface.gitTrees.test.tsx`, `ExpressionCards.test.tsx`, and since MIK-L35
`IntentWordDiff.test.tsx` and `ReviewSurface.wordDiff.test.tsx`).** The MIK-L35 cases derive a successor guarantee
from its `FAM-2HBJREC2` guarantee, including one revision whose text changes. Its receipt is in `gitTrees.capture-provenance.json` (route, status, sha256 and bytes).

## Code Commentary

### Logic

- The family-selected review of `FAM-2HBJREC2` ("Comparison-bound unchanged realization context"): the source inventory, the family context with its 7-member roster, and the limitations `review:trees:1`, `history:intent:<side>:available` and `knowledge-index:<side>:complete`.
- **MIK-R31 rule 6:** its member sources carry resolved, non-empty ranges (`resolved_ranges`, for example `194–213` for `_not_listed`), and its seven member identities are the ones the cards read names.
- **Re-captured by MIK-L31** from its own scratch leaf `260928-MIK-L31` with this leaf's code (review F7: the bodies are byte-identical to the capture at the L10-synced tree; only the receipt changed). Against L25's capture the deltas are the leaf, the code trees (`8a2d4b47` → the scratch candidate), the curator-authority name and `review:trees:2` → `review:trees:1`. (L25's own recapture history, ruling 02:32:42 (a), is in this card's Update History.)

### Conventions

Keep the captured bytes and their receipt intact; only the tests read this file.

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
| The tree comparison it was read from (comparison 1 of the MIK-L31 scratch leaf). | "review:trees:1" | dashboard/src/panels/review/gitTrees.family.captured.json:1346-1346 |
| The receipt row for this body, now with its request parameters. | "gitTrees.family.captured.json" | dashboard/src/panels/review/gitTrees.capture-provenance.json:24-24 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T13:23:08+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): body update, bytes unchanged. Purpose names its MIK-L35 consumers (`IntentWordDiff.test.tsx`, `ReviewSurface.wordDiff.test.tsx`), which derive a successor guarantee from it; Conventions says tests, plural.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update for the MIK-L31 re-capture: leaf `260928-MIK-L31`, `review:trees:1`, member sources with resolved ranges (MIK-R31 rule 6). **Claims re-anchored:** the comparison row (`review:trees:2` no longer exists in the body) and the receipt row (reworded; this pass's generated bullet removed).

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new captured fixture. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
