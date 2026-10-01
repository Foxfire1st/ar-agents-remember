# dashboard/src/panels/review/hunkMarkers.classifier.captured.json

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

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The first scenario's body: a linked hunk whose occurrences are all `membership_unknown` because the after side is unread. [1]
- The unread-before scenario (the review R1 F1 excerpt case) and the file with no readable side. [2]
- The curated and partial scenarios. [3]
- The pre-curation scenario, with the proof and the unregistered file. [4]
- The receipt row for this body. [5]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
