# dashboard/src/panels/review/laneReview.trees.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/laneReview.trees.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real leaf-wide `GET /api/review/trees?comparison=2` body of the MIK-L32 scratch leaf** (86,687 bytes; test evidence
for `ReviewSurface.lane.test.tsx`, where it is the slower read that supplies the gate's worklist).

## Code Commentary

### Logic

- `state: "trees"` for comparison 2 with the currentness per side, the knowledge diff and the computed, complete
  worklist of 21 items, among them the gate's two `unexplained_file` items (the new binary and the mode-only
  `review_family_rosters.py`) and three `unexplained_hunk` items (`CONTRIBUTING.md`, the retention helper and the new
  module).
- The focused retention file shows its gate item through `UnexplainedGroups` from this worklist.

### Conventions

Keep the captured bytes and their receipt (`laneReview.capture-provenance.json`) intact; a recapture rewrites both.

### Invariants And Boundaries

The body describes the scratch copies under `/tmp/mik-l32-real` (code at `b54d1b03` with the scratch leaf's edits;
memory `58d016cb` converted), not current project knowledge; its line numbers and blobs are the scratch tree's.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The comparison it was read from. | "\"number\": 2" | dashboard/src/panels/review/laneReview.trees.captured.json:25-25 |
| The worklist and its computed, complete state. | "worklist"; "\"source\": \"computed\"" | dashboard/src/panels/review/laneReview.trees.captured.json:1867-3021 |
| The gate's two `unexplained_file` items: the new binary and the mode-only module. | "\"subject\": \"file:docs/scratch-lane.bin@c8b49c8cd518e58491924bfc364ff26e01a85009\""; "\"subject\": \"file:mcp/src/agents_remember/application/review_family_rosters.py@863986f5f429c7e0e5821471bcf7cd11a3543cbf\"" | dashboard/src/panels/review/laneReview.trees.captured.json:2870-2897 |
| The receipt row for this body. | "src/panels/review/laneReview.trees.captured.json" | dashboard/src/panels/review/laneReview.capture-provenance.json:38-38 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new captured leaf-wide tree view body. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
