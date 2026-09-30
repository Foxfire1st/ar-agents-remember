# dashboard/src/panels/review/hunkMarkers.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/hunkMarkers.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The pure model of MIK-R34's per-hunk intent markers: what each hunk of a changed text file names, and where its
mark sits in a drawn diff.** Nothing here classifies. Every hunk, class, link and family occurrence is MIK-R32's one
per-file classification (`data/reviewLane.ts`, served by the tree view route); these functions only group what it
names and place each hunk's mark on the side line numbers it names. The mark's line never comes from the renderer's
own change regions, from context lines, or from any name or text in the file, so two owner hunks drawn in one
displayed region keep two marks (ICR-R34 rule 1).

## Code Commentary

### Logic

- **One file, one kind of marking (`fileMarks`).** A confirmed-unregistered file (bucket `unexplained`) carries one
  file-level `unexplained` mark with the owner's reason, and so does a file neither side of which has readable
  knowledge (`attribution_unknown`, each side's detail); ICR-R34 rule 4 and the Failure rule. Otherwise every owner
  hunk gets its own `HunkMark` (`hunkMark`).
- **What a hunk names (`hunkMark`, `markEntries`).** Realization links and proof links are grouped apart, one
  `MarkEntry` per kind and invariant key in the owner's order, with its facets, entry ids and revisions: proofs are
  listed as tests and never counted with realizations (the MIK-R34 substitution). Each entry's family occurrences
  (`addOccurrence`) are keyed by membership state, family key and revision key and merged across the sides that
  record the same revision in the same state (`sides`).
- **The target an occurrence opens (`MarkTarget`).** The invariant (display id and key), and, when a family records
  it, the family key with the member revision key; its membership `state`; and for `membership_unknown` a `reason`.
  A family is reached only through a member occurrence, never on its own (ICR-R34 rule 2).
- **Why a membership is unknown (`unknownReason`; ruling 2026-09-30T16:19:34 Q3, review R1 N1).** Built only from the
  owner's facts: a named family is unknown for a before-side occurrence whose after side could not be read whole ("not
  every family record of the after knowledge could be read, so whether FAM-… still lists INV-… there is not
  established"); a family-less one because not every family record of its own side was read; an unread side adds its
  detail. The comment names L32's `_membership` and `_occurrences` in `application/review_unexplained_lane.py` as the
  rule's owner: the response carries no per-occurrence reason, so this sentence restates that rule and must change
  with it.
- **Unknown lines on a linked hunk (`unreadChangedSides`; ruling Q2).** The owner links a hunk through its readable
  side and names the unread side's availability on the file, not on the hunk; a linked hunk that changes lines on an
  unread side lists them as attribution unknown. This is the one fact derived on the client, and it is the owner's
  own side availability applied to the owner's own spans, not intersection arithmetic.
- **Labels.** `markLabel`: `unexplained` or `attribution unknown` for those classes; one entry's short label
  (`INV-9BH2BNCT`, `INV-2TQGXFAX · test`); otherwise a compact count (`2 intents`, `1 intent · 1 test`,
  `1 intent · unknown`). `compactLabel` (review R1 F2): `2`, `1+1t`, `1t`, `1?`, `!` for unexplained, `?` for
  attribution unknown. `occurrenceLabel`: `No recorded family` only for `confirmed_no_family`, `Attribution unknown`
  for a family-less unknown occurrence, else `FAM-… rN · member`, `before-only`, `removed or reassigned in after` or
  `membership unknown`. `sidesLabel`, `hunkKey` (`before.start:before.count:after.start:after.count`).
- **Placement (`markAnchor`).** On the first changed after line the pane draws; for a hunk that changes no drawn
  after line, on its first drawn removed line: in a side-by-side diff on the before side, inline on the after line
  just below the removed lines (the owner names the line they follow), clamped to the drawn after window; `null` when
  the pane draws none of the hunk's changed lines. `firstDrawn` intersects a changed span only with the lines the
  pane draws (`PaneWindow`, `SideWindow`; `wholeSide` for a whole text), which is placement, not attribution.

### Conventions

- Pure functions over the served types of `data/reviewLane.ts`; no React, no fetch, no state.
- Every label a reader sees for a hunk or an occurrence is composed here, so the gutter, the list and the tests read
  one vocabulary.

### Invariants And Boundaries

- **Candidate invariant (not ingested): every intent marker comes from L32's per-file classification response, and
  the client never intersects recorded ranges itself.** Realized by `fileMarks`, `hunkMark`, `markEntries` and
  `addOccurrence`, which only group and label the owner's hunks, links and occurrences, and by `markAnchor`, which
  places on the owner's side lines and intersects only with the lines a pane draws; the one client-derived fact
  (ruling Q2) applies the owner's side availability. Proved by `hunkMarkers.test.ts` over six real captured scenarios
  of L32's lane fixture world (`hunkMarkers.classifier.captured.json`) and the mutations M1–M7 and N1 of the worker's
  sets, all caught; the reviewer confirmed there is no second classifier (review R1, rule 5).
- **Part of the candidate invariant "unknown membership is always distinguishable from confirmed no-family"**
  (recorded on `MarkerTargetState.tsx.md`): a target carries its `state` and `reason`, and `occurrenceLabel` never
  reads an unknown membership as `No recorded family`.
- Proof and realization entries are never merged into one count.

### Todos

- The unknown-membership reason restates L32's server rule (review R1 N1). If MIK-R32's response later carries a
  per-occurrence reason, this function should read it instead.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement: nothing here classifies; marks sit on the owner's side lines only. | "Nothing here classifies."; "owner hunks drawn in one displayed region keep two marks." | dashboard/src/panels/review/hunkMarkers.ts:1-8 |
| The target an occurrence opens, carrying its membership state and reason. | `MarkTarget` | dashboard/src/panels/review/hunkMarkers.ts:20-33 |
| An occurrence, an entry (realization or proof), an unknown line, a hunk's mark with its label and compact text, and a file's marks. | `MarkOccurrence`; `MarkEntry`; `HunkMark`; `FileMarks` | dashboard/src/panels/review/hunkMarkers.ts:35-85 |
| One file-level mark for a confirmed-unregistered or wholly unreadable file; otherwise one mark per owner hunk. | `hunkKey`; `fileMarks` | dashboard/src/panels/review/hunkMarkers.ts:87-102 |
| A hunk's realizations and proofs apart, and its unknown lines, including a linked hunk's unread side (ruling Q2). | `hunkMark`; `unreadChangedSides` | dashboard/src/panels/review/hunkMarkers.ts:104-140 |
| One entry per kind and invariant; occurrences merged across sides; each with its target. | `markEntries`; `addOccurrence` | dashboard/src/panels/review/hunkMarkers.ts:142-201 |
| The unknown-membership reason from the owner's facts, naming L32's rule as its owner (ruling Q3, review N1). | `unknownReason`; "The rule's owner is MIK-L32's server" | dashboard/src/panels/review/hunkMarkers.ts:203-227 |
| The gutter label, the compact phone label (review R1 F2) and the occurrence label. | `markLabel`; `compactLabel`; `occurrenceLabel` | dashboard/src/panels/review/hunkMarkers.ts:229-284 |
| Placement on the owner's side lines within the drawn window; an inline deletion below its removed lines. | `firstDrawn`; `markAnchor`; `wholeSide` | dashboard/src/panels/review/hunkMarkers.ts:290-347 |
| The owner's response these functions read. | `ReviewFileClassification`; `ReviewLaneLink` | dashboard/src/data/reviewLane.ts:123-134; dashboard/src/data/reviewLane.ts:61-73 |
| The cases over the six real scenarios. | "names every intersecting invariant of a replace hunk, with each family occurrence"; "marks every hunk a window draws, a neighbour shown as context too" | dashboard/src/panels/review/hunkMarkers.test.ts:34-227 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new pure marker model MIK-R34 adds, recording rulings 2026-09-30T16:19:34 Q2 (per-side availability on a linked hunk) and Q3 (the membership reason), review R1 F2 (compact labels) and N1 (the reason's owner), and one candidate invariant. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
