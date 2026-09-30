# dashboard/src/panels/review/gitTrees.entries.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/gitTrees.entries.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:05:09+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent/entries` body over the MIK-L31 worker's converted scratch leaf `260928-MIK-L31`
(test evidence for `ReviewSurface.gitTrees.test.tsx`).** Its receipt is in `gitTrees.capture-provenance.json` (route, status, sha256 and bytes).

## Code Commentary

### Logic

- The entry list of the converted leaf: 108 subjects (94 invariants and 14 families) with their presence, as the review navigation reads it.
- **Re-captured by MIK-L31** from its own scratch leaf: against L25's capture only `leaf_id` changed (`260928-MIK-L25` → `260928-MIK-L31`). (L25's own recapture history is in this card's Update History.)

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
| The subject total: 94 invariants and 14 families. | "total_subjects" | dashboard/src/panels/review/gitTrees.entries.captured.json:659-659 |
| The receipt row for this body, now with its request parameters. | "gitTrees.entries.captured.json" | dashboard/src/panels/review/gitTrees.capture-provenance.json:11-11 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update for the MIK-L31 re-capture (only the leaf id changed in the body). **Claim reworded:** the receipt row (this pass's generated bullet removed).

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new captured fixture. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
