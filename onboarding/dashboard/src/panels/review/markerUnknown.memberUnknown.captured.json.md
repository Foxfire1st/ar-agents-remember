# dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent` review of INV-Z66EMHMH on comparison 3 of the MIK-L34 scratch leaf** (102,922 bytes; test
evidence for `ReviewSurface.markers.test.tsx` and, since MIK-L33's merge round, `ReviewSurface.triageMarkers.test.tsx` and `MarkerTargetState.test.tsx`: the review a family-named unknown
target opens).

## Code Commentary

### Logic

- The review still composes FAM-4V4GSQCS's context (`recorded`, one family), so a family-named unknown target lands on
  that family's member row, which carries the `Attribution unknown` state; a family-less target of the same invariant
  shows the state above the tree (review R1 F3).
- The limitations name `review:trees:3` and `knowledge-index:after:partial`.
- **`change_kinds` (MIK-L33):** guarantee `unknown` and `members_total` absent, because the after side's
  FAM-4V4GSQCS record does not parse; every one of the five members has membership `unknown` with that record as its
  `membership_reasons`; INV-Z66EMHMH, INV-EJW15DXA and INV-ZJS1XY4R read `implementation` `+unknown` (the unknown mark
  is the membership), INV-QR24S1VH and INV-DA7D417G `unknown`. So on a tree comparison the followed member row states
  its unknown membership once, as the tagged membership line with the comparison's reason (MIK-L33 merge round).

- **Re-captured in MIK-L33's merge round** over the merged tree (MIK-L34 landed; the review route now carries `change_kinds`). Against MIK-L34's capture it differs only by scratch paths, the converted memory commit, timestamps and comparison digests, and it now carries FAM-4V4GSQCS's `change_kinds` (the reviewer's structural diff, review R3 point 5).

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

The body describes the scratch copies under `/tmp/mik-l33-merge`: MIK-L34's scenario, rebuilt by MIK-L33's merge round with MIK-L34's own scripts (code `59daf505` with the scratch leaf's edits and the same curated blobs `9019bea5` and `b6d07091`; memory `76f5e91e1` converted and committed as scratch `main` `31ab7016`), not current project knowledge; its line numbers, blobs and keys are the scratch tree's.

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
| The composed family context. | "family_context"; "Bounded notes listing with unchanged meaning" | dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json:116-116; dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json:622-622 |
| The comparison token and the partial after index. | "review:trees:3"; "knowledge-index:after:partial" | dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json:799-799; dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json:803-803 |
| The receipt row for this body. | "src/panels/review/markerUnknown.memberUnknown.captured.json" | dashboard/src/panels/review/markerUnknown.capture-provenance.json:74-74 |
| The family's change facts with every membership unknown (MIK-L33). | "\"change_kinds\": {"; "\"guarantee\": \"unknown\"," | dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json:508-620 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): **body updated for MIK-L33's merge round** (review R3-3): the body was re-captured over the merged tree from MIK-L34's scenario rebuilt under `/tmp/mik-l33-merge` (scratch `main` `31ab7016`); it now carries FAM-4V4GSQCS's `change_kinds`, summarized in Logic, with one row added; the byte count and the scratch sentence are updated, and the Purpose names the new consumer `ReviewSurface.triageMarkers.test.tsx`. Its sha256 and byte count match the updated receipt (checked by this curation). The rows' ranges were normalised by the installed fixer (its bullets kept).
- 2026-09-30T20:22:33+00:00: Generated citation repair: "family_context"; "Bounded notes listing with unchanged meaning" repointed to dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json:116-116; dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json:622-622. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T20:22:33+00:00: Generated citation repair: "review:trees:3"; "knowledge-index:after:partial" repointed to dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json:799-799; dashboard/src/panels/review/markerUnknown.memberUnknown.captured.json:803-803. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new captured family-named unknown review (comparison 3). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
