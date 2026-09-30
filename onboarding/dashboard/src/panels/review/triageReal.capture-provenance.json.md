# dashboard/src/panels/review/triageReal.capture-provenance.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/triageReal.capture-provenance.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:21:58+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The receipt of the two real served bodies of the MIK-L33 worker's converted scratch leaf.** It names the capture
time (2026-09-30T19:15:33Z), the producer (`notes/reports/260928-MIK-L33-evidence/capture_real_bodies.py`) and its
command, the route, the source tree (the L33 worktree on base `d3a22213` with this leaf's changes), the scratch
(`/tmp/mik-l33-real`: `--shared` clones of the live repositories; memory `0b176f6b` converted and committed as scratch
`main` `0c3a0f83` with `Code-Commit` `904e804b`; leaf `260928-MIK-L33` whose code worktree holds this leaf's own change
and whose memory worktree holds SCRATCH-AUTHORED curator edits: INV-ZS9ZS878 revision 3→4, INV-2TQGXFAX joining
FAM-R6R095RW, FAM-2HBJREC2's guarantee revised, RLZ-6VEXGB6W re-anchored, INV-2E8MG43K reworded without a revision
bump; then the changed files' entries re-recorded at the candidate blob), the attempts, one row per body, and a
`merge_round` note (the scenario unchanged from the review R2 round).

## Code Commentary

### Logic

- Two rows: FAM-R6R095RW's family review (`triageReal.family`, 5.54 s) and the shared member INV-2TQGXFAX's review
  (`triageReal.shared`, 4.35 s).
- The worker's real-data runs (`run_kinds-pre.txt`, `run_kinds-post.txt`) and the scratch edits 6 and 7 (a stale entry
  repaired, a carried one) live in `notes/reports/260928-MIK-L33-evidence/`; this receipt records only the bodies.

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

These are scratch-copy captures, not current project knowledge or mounted-product acceptance. Both sha256 values and byte counts match the bodies (checked by this curation).

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| When, by what command and at which source tree the bodies were captured, and over which scratch leaf. | "captured_at"; "source_tree"; "SCRATCH-AUTHORED curator edits" | dashboard/src/panels/review/triageReal.capture-provenance.json:2-8 |
| One receipt row per body, and the merge-round note. | "\"fixtures\": ["; "merge_round" | dashboard/src/panels/review/triageReal.capture-provenance.json:9-41 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T22:21:58+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): created this card for the new capture receipt of the two real triage bodies. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
