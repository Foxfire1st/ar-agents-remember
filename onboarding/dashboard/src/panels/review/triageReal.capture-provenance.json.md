# dashboard/src/panels/review/triageReal.capture-provenance.json

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

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- When, by what command and at which source tree the bodies were captured, and over which scratch leaf. [1]
- One receipt row per body, and the merge-round note. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
