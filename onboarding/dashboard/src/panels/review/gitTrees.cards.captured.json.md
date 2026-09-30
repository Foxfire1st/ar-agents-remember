# dashboard/src/panels/review/gitTrees.cards.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/gitTrees.cards.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:36:31+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/trees?comparison=1&invariants=<7 identities>` body over the MIK-L31 worker's converted
scratch leaf `260928-MIK-L31`: the focused cards read for the family `FAM-2HBJREC2` (test evidence for
`ExpressionCards.test.tsx`, `ReviewSurface.gitTrees.test.tsx`, since MIK-L35 `ReviewSurface.wordDiff.test.tsx`, and since
MIK-L34 `IntentMarkers.test.tsx`, whose card cases take its two `review_source_admission.py` entries RLZ-CXH58B4W and
RLZ-D43E5CF2, two cards of one path, to check that a return reopens the exact card).** 38,264 bytes; its receipt is in
`gitTrees.capture-provenance.json` (route, the seven invariant identities, status, sha256 and bytes).

## Code Commentary

### Logic

- `state: "trees"` for comparison `1` of leaf `260928-MIK-L31`, with the knowledge and code sides, and **11
  entries** (10 realizations, 1 proof): exactly one `changed` entry, `RLZ-CXH58B4W` (`review_source_admission.py`,
  the scratch edit of `_not_listed`, resolved at `194–213` on both sides), and 10 `unchanged` entries.
- In `review_source_admission.py` there are exactly four entries, the packet's conforming example: RLZ-CXH58B4W
  (changed), RLZ-D43E5CF2, RLZ-9EC7B6PN and RLZ-NM6160PK (unchanged), each with its own role and rationale.
- The proof is `PRF-7Q3M5K` (a scratch-authored proof of INV-2TQGXFAX on
  `test_knowledge_review_attributed_source_content.py`), added in this leaf (`recorded` false before, true after),
  carrying its facet and no role or rationale (the boundary example).
- Every entry is `resolved` on both sides and MIK-R03 `current`. The server orders proofs before realizations
  within an invariant; the client reorders them (`focusedCards.orderedEntries`).

### Conventions

Keep the captured bytes and their receipt intact; only the tests read this file.

### Invariants And Boundaries

The body describes the scratch copies under `/tmp/mik-l31-real` (code at `8a2d4b47` with the scratch edit), not
current project knowledge. Its line ranges are the scratch tree's.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R31@v1` and its rulings live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The proof entry, added in this leaf, with its facet. | "PRF-7Q3M5K" | dashboard/src/panels/review/gitTrees.cards.captured.json:67-67 |
| The one changed entry. | "\"change\": \"changed\""; "RLZ-CXH58B4W" | dashboard/src/panels/review/gitTrees.cards.captured.json:101-102 |
| The comparison it was read from. | "\"number\": 1" | dashboard/src/panels/review/gitTrees.cards.captured.json:36-36 |
| The receipt row for this body, with the invariants it names. | "gitTrees.cards.captured.json" | dashboard/src/panels/review/gitTrees.capture-provenance.json:67-67 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:36:31+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): Body updated: MIK-L34's `IntentMarkers.test.tsx` now also reads this body (its two `review_source_admission.py` cards, for the exact-card return), so Purpose names it. Bytes unchanged. No stamp advanced.
- 2026-09-30T13:23:08+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): body update, bytes unchanged. Purpose names its MIK-L35 consumer (`ReviewSurface.wordDiff.test.tsx`).
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new captured fixture (MIK-R31 rule 6: a captured fixture whose member entries have resolved, non-empty ranges). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
