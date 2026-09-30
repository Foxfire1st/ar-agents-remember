# dashboard/src/panels/review/hunkMarkers.classifier.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/hunkMarkers.classifier.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**Eleven real per-file classifications of MIK-L32's lane fixture world in six scenarios** (55,216 bytes; test evidence
for `hunkMarkers.test.ts` and `IntentMarkers.test.tsx`). Each body is `{ file_classification, texts }`: the served
response and, fixture-only, the exact side blob texts.

## Code Commentary

### Logic

- `precuration`: `lines.txt` (a replace linked to INV-BBBBBB with no family, a replace of attribution unknown on the
  after side, an unexplained deletion), `a.py` (a replace linked to INV-AAAAAA through the before side with its three
  occurrences, and an insertion of attribution unknown), `tests/test_a.py` (a proof link), `new.py` (bucket
  `unexplained`: the file-level mark) and `stale.py` (attribution unknown on both sides).
- `curated`: the same files after the scratch-authored realizations, `lines.txt` L2 linked to INV-AAAAAA (member,
  removed or reassigned in after, before-only) and INV-BBBBBB (confirmed no family), `a.py`'s insertion linked to
  INV-CCCCCC (confirmed no family).
- `before_unread` and `after_unread`: one memory side unavailable, so the readable side's links stay and the unread
  side's lines are unknown, or every family occurrence is `membership_unknown`; `both_unread`: bucket
  `attribution_unknown`, the file-level note; `partial`: an index read in part, INV-BBBBBB `membership_unknown`.

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

The bodies describe MIK-L32's test fixture world, not current project knowledge.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The first scenario's body: a linked hunk whose occurrences are all `membership_unknown` because the after side is unread. | "after_unread"; "\"state\": \"membership_unknown\"" | dashboard/src/panels/review/hunkMarkers.classifier.captured.json:2-178 |
| The unread-before scenario (the review R1 F1 excerpt case) and the file with no readable side. | "before_unread"; "both_unread" | dashboard/src/panels/review/hunkMarkers.classifier.captured.json:179-692 |
| The curated and partial scenarios. | "curated"; "partial" | dashboard/src/panels/review/hunkMarkers.classifier.captured.json:693-1322 |
| The pre-curation scenario, with the proof and the unregistered file. | "precuration"; "tests/test_a.py"; "pkg/new.py" | dashboard/src/panels/review/hunkMarkers.classifier.captured.json:1323-2093 |
| The receipt row for this body. | "src/panels/review/hunkMarkers.classifier.captured.json" | dashboard/src/panels/review/hunkMarkers.capture-provenance.json:38-38 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new captured classifier bodies (six scenarios). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
