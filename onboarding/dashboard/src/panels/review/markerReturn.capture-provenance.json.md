# dashboard/src/panels/review/markerReturn.capture-provenance.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The receipt of five of the six real served bodies of the MIK-L34 worker's converted scratch leaf, comparison 2,
as re-captured in MIK-L33's merge round.** It names the capture time (2026-09-30T19:11:44Z; MIK-L34's own capture was
13:48:07Z), the producer (MIK-L34's `capture_ui_fixtures.py` re-run by the MIK-L33 worker from
`notes/reports/260928-MIK-L33-evidence/merge-round/l34-scenario/`) and its command, the route
(`create_app(config, collaborators=serving_collaborators(config))` over a FastAPI `TestClient`), the source tree (the
L33 worktree on base `d3a22213`, MIK-L34 landed, with MIK-L33's changes: the review route now carries
`change_kinds`), the scratch (`/tmp/mik-l33-merge`: MIK-L34's `setup_scratch.sh` re-run, `--shared` clones of the live
repositories; memory `76f5e91e1` converted and committed as scratch `main` with `Code-Commit` `59daf505`; the leaf's
edits and `curate`), comparison `2`, the
attempts (one capture per body, each the first answer), and one row per body with route, parameters, status,
seconds, sha256 and bytes. The sixth comparison-2 body, `markerReturn.cards.captured.json`, was captured in the
rulings round and is receipted in `markerUnknown.capture-provenance.json`. A closing `merge_round` note says what
changed: the invariant review now carries its family's `change_kinds`; the other bodies differ only by scratch paths,
the memory commit, timestamps and comparison digests.

## Code Commentary

### Logic

- Five rows: the task-context review (`GET /api/review/intent`, 6.09 s), the lane (`lane=files`, 0.08 s), `notes.py`'s
  classification (`file=`, 0.05 s), `notes.py`'s source content (`GET /api/review/intent/source-content` at trees
  `59daf505` → `db68db54`, 2.55 s) and INV-Z66EMHMH's review (`selectorKind=invariant`, 4.09 s).
- The scratch leaf: `serving/notes.py` edited inside `_confined_stat` (two recorded ranges) and `list_notes`'s
  docstring line deleted (three recorded ranges); `review_comparison_retention.py` edited inside `_side_binding`
  with a helper appended; a new module with no entry; a test body edited with a scratch-authored proof `PRF-7Q3M5K`;
  INV-ZJS1XY4R reassigned out of FAM-4V4GSQCS on the after side; the `notes.py` and retention entries re-recorded at
  the candidate blob.

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

These are scratch-copy captures, not current project knowledge or mounted-product acceptance. All five sha256 values match the fixtures (checked by this curation).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- When, by what command and at which source tree the bodies were captured, and over which scratch leaf. [1]
- One receipt row per captured body, and the merge-round note (MIK-L33). [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
