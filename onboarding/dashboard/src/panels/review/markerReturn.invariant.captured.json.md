# dashboard/src/panels/review/markerReturn.invariant.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/markerReturn.invariant.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**A real `GET /api/review/intent` review of INV-Z66EMHMH (selector `c7c5be49…`) on comparison 2 of the MIK-L34 scratch
leaf** (139,987 bytes; test evidence for `ReviewSurface.markers.test.tsx`: the target a followed marker reads).

## Code Commentary

### Logic

- Family context `recorded`: one family, FAM-4V4GSQCS ("Bounded notes listing with unchanged meaning", family id
  `8519c70b…`), with its before and after revisions and member rosters, so the member row of INV-Z66EMHMH's revision
  becomes current when the marker is followed.
- The limitations name `review:trees:2` and both indexes complete.
- **`change_kinds` (MIK-L33):** guarantee `unchanged`, `members_total` 5; INV-ZJS1XY4R `implementation` `+membership`
  (reassigned out of the family on the after side; the L210 deletion meets its entry), INV-Z66EMHMH and INV-EJW15DXA
  `implementation` (the two hunks), INV-QR24S1VH and INV-DA7D417G `unchanged`.

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
| The recorded family context with its one family and rosters. | "family_context"; "Bounded notes listing with unchanged meaning" | dashboard/src/panels/review/markerReturn.invariant.captured.json:116-116; dashboard/src/panels/review/markerReturn.invariant.captured.json:925-925 |
| The comparison token. | "review:trees:2" | dashboard/src/panels/review/markerReturn.invariant.captured.json:1128-1128 |
| The receipt row for this body. | "src/panels/review/markerReturn.invariant.captured.json" | dashboard/src/panels/review/markerReturn.capture-provenance.json:71-71 |
| The family's change facts (MIK-L33). | "\"change_kinds\": {"; "\"guarantee\": \"unchanged\"," | dashboard/src/panels/review/markerReturn.invariant.captured.json:823-923 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): **body updated for MIK-L33's merge round** (review R3-3): the body was re-captured over the merged tree from MIK-L34's scenario rebuilt under `/tmp/mik-l33-merge` (scratch `main` `31ab7016`); it now carries FAM-4V4GSQCS's `change_kinds`, summarized in Logic, with one row added; the byte count and the scratch sentence are updated. Its sha256 and byte count match the updated receipt (checked by this curation). The rows' ranges were normalised by the installed fixer (its bullets kept).
- 2026-09-30T20:22:24+00:00: Generated citation repair: "family_context"; "Bounded notes listing with unchanged meaning" repointed to dashboard/src/panels/review/markerReturn.invariant.captured.json:116-116; dashboard/src/panels/review/markerReturn.invariant.captured.json:925-925. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T20:22:24+00:00: Generated citation repair: "review:trees:2" repointed to dashboard/src/panels/review/markerReturn.invariant.captured.json:1128-1128. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new captured invariant review (comparison 2). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
