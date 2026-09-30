# dashboard/src/panels/review/ReviewRecordPanes.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewRecordPanes.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:18:54+02:00 |
| lastVerifiedCommitHash |  `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate |  2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The review's record panes: the knowledge, source, evidence and submission records of **one admitted
payload**, behind the workspace's "Technical details" disclosure. Extracted verbatim from
`ReviewSurface.tsx` in `260921-ICR-L48` (the L47-R1-F5 file budget: that file went 931 → 585 lines),
plus one new rule in the disclosure itself: the records are rendered only for a payload that answers the
subject on screen. The accumulated history of these renderers (L2, L6, L10, L22, L23, L25 round 3, L26)
is recorded on [ReviewSurface.tsx](ReviewSurface.tsx.md), where they lived until this move.

## Code Commentary

### Logic

`ReviewTechnicalDetails({ payload, unanswered, paging, laneRead })` is the only export (`laneRead`, optional and
`null` by default, since MIK-L32). It always mounts one
`<details data-testid="review-details">`, so its open state survives a selection. When `payload` is
`null` — the subject on screen is still being read or could not be read — it renders one line instead of
the records: `review-details-pending` ("Reading the records of <label>…") or `review-details-unavailable`
("No records are shown: <label> could not be read."). Otherwise it renders a one-column grid
(`gridTemplateColumns: 'minmax(0, 1fr)'`) of `SubmissionBlock`, the surface's `paging` node, and the
`KnowledgePane`, `SourcePane` (handed `laneRead`) and `EvidencePane`.

**The source pane's attribution on a tree comparison follows the lane (MIK-L32; review R1 F1, ruling
2026-09-30T13:07:38).** The surface makes the one lane read and hands it here as `laneRead`. With a lane read,
`SourcePane` takes `laneAttributionFacts(laneRead)` (`laneFocus.ts`): the remaining counts
`unattributed_changed_paths` and `unknown_attribution_changed_paths` are written by `laneCountText` (the lane's
unexplained and unknown counts, marked `(partial)` on a partial lane, or `Attribution pending` / `Attribution unknown
(the lane could not be read)`), every other count keeps the landed text (`landedCountText`), and
`LaneAttributionLists` replaces the landed list: "changed paths no recorded entry explains: …" and "changed paths of
unknown attribution: …", or one pending/unknown line (`data-attribution-state`). `review-remaining` carries
`data-attribution-source="lane"`. A dataset review (no `laneRead`) keeps the landed counts and the landed "changed paths
with no registered attribution" list (`data-attribution-source="landed"`); the reviewer rendered it with the base and
the candidate and found the details' text byte-identical.

The renderers are unchanged from the surface. `KnowledgePane` mounts `KnowledgeFacts`, `AuthoredRecords`
and delegates its statements to `KnowledgeStatements`. `SourcePane` carries a
`review-source-explorer-pointer` (the inventory itself is `SourceExplorer.tsx`'s) and the attribution side
of the same records. `EvidencePane` lists evidence links and observations. `SubmissionBlock` prints the
server's staleness and submission boundary, including the `not-measured` line
(`review-staleness-unmeasured`), and offers no control. The small helpers keep the bodies readable:
`pane` (a grid item that may shrink and wrap), `muted`, `attribution` (prints an unresolved author rather
than an anonymous one), `applicabilityNote`/`contextList`/`applicabilityCounts` (the L26 attribution
labels, displayed never computed), `unresolvedList`, and `fieldValue` (`(absent)` vs `(recorded empty)`).

### Conventions

Pure display of one payload's fields: no state, no read, no selection, no paging logic. Inline `style`
objects and `data-testid`/`data-pane` attributes, as in the surface; every list item carries a stable
`key` from the record's own identifiers. `TAKEOVER` (`changeset-viewer`) is the class the grid carries.

### Invariants And Boundaries

- **Records only for the answer on screen (L48, `ICR-R26` isolation).** The surface hands `payload` only
  when it answers the subject on screen; while another subject is pending or unavailable, no previous
  subject's statements, assessments or evidence are shown under the new subject.
- **Display-only.** No POST, no form, no submit handler; the submission block prints the authority's path
  and state rather than offering a control.
- **A label is displayed, never computed** (L26): the applicability renderers print the server's fields
  and mount nothing when the payload carries no label.
- **Narrow-width declarations** (L25 round 3): `pane` keeps `minWidth: 0` and `overflowWrap: 'anywhere'`,
  and the grid track is `minmax(0, 1fr)`; none of them works alone. `ReviewSurface.narrow.test.tsx` pins
  them on the rendered surface.
- **On a tree comparison the details never contradict the lane** (review R1 F1): part of the candidate invariant
  "the explorer and the technical details take their attribution from the lane" recorded on
  `review_unexplained_lane.py.md`. Proved by `ReviewSurface.lane.test.tsx` (the lane's counts and lists; pending
  while the lane is held) and the gitTrees cases (unknown without a lane; the dataset review's landed text word for
  word); forcing the lane facts off fails 3 cases.
- **Boundary.** Which payload is shown, paging and the outcome states are `ReviewSurface.tsx`'s and
  `ReviewOutcome.tsx`'s; the statement diff is `KnowledgeStatements.tsx`'s.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of why it exists and that the disclosure stays mounted while another subject is pending or unavailable.** | "WHY THIS IS ITS OWN MODULE" | dashboard/src/panels/review/ReviewRecordPanes.tsx:1-9 |
| The pane helper's two load-bearing declarations. | `pane`; "minWidth: 0"; "overflowWrap"; `data-pane` | dashboard/src/panels/review/ReviewRecordPanes.tsx:33-41 |
| The attribution labels, displayed never computed. | `applicabilityNote`; `contextList`; `applicabilityCounts` | dashboard/src/panels/review/ReviewRecordPanes.tsx:54-69; dashboard/src/panels/review/ReviewRecordPanes.tsx:71-87; dashboard/src/panels/review/ReviewRecordPanes.tsx:89-100 |
| Absent vs recorded-empty field values. | `fieldValue`; "(absent)"; "(recorded empty)" | dashboard/src/panels/review/ReviewRecordPanes.tsx:117-118 |
| The knowledge pane delegates statements to `KnowledgeStatements`. | `KnowledgePane`; `KnowledgeStatements` | dashboard/src/panels/review/ReviewRecordPanes.tsx:223-248 |
| The landed count text, and the lane's two lists or its pending or unknown line (MIK-L32). | `landedCountText`; `LaneAttributionLists` | dashboard/src/panels/review/ReviewRecordPanes.tsx:250-290 |
| The source pane points at the explorer rather than listing a second inventory; on a tree comparison its attribution counts and lists come from the lane (review F1). | "function SourcePane({"; `review-source-explorer-pointer`; "const lane = laneRead ? laneAttributionFacts(laneRead) : null;" | dashboard/src/panels/review/ReviewRecordPanes.tsx:292-357 |
| The evidence pane. | `EvidencePane` | dashboard/src/panels/review/ReviewRecordPanes.tsx:359-415 |
| The submission block: staleness, the unmeasured line, no control. | `SubmissionBlock`; `review-staleness-unmeasured` | dashboard/src/panels/review/ReviewRecordPanes.tsx:417-445 |
| **The disclosure: always mounted; records only for an answer, else one pending or unavailable line; the lane read passed to the source pane.** | "export function ReviewTechnicalDetails({"; `review-details-pending`; `review-details-unavailable`; `gridTemplateColumns`; "<SourcePane payload={payload} laneRead={laneRead} />" | dashboard/src/panels/review/ReviewRecordPanes.tsx:446-497 |
| The surface hands it the answer alone, and the one lane read. | "<ReviewTechnicalDetails"; `unanswered` | dashboard/src/panels/review/ReviewSurface.tsx:358-367 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The panes render one repository namespace's
records.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): **body update for MIK-R32 (review R1 F1, ruling 2026-09-30T13:07:38).** Logic records `laneRead` and the source pane's lane-derived counts and lists (`laneAttributionFacts`, `laneCountText`, `LaneAttributionLists`, `landedCountText`, `data-attribution-source`), with the dataset review's landed text unchanged; an Invariants bullet records the candidate-invariant part. **Reopened claim reworded and re-anchored:** the `ReviewTechnicalDetails` row (the construct changed) now names the lane read and is anchored on line-exact quotes ("export function ReviewTechnicalDetails({", "<SourcePane payload={payload} laneRead={laneRead} />"), re-measured to `446-497`; this pass's generated bullet for it was removed. The source-pane and surface rows are reworded and re-anchored on quotes the same way; one row added. The fixer's other bullets are kept. No verification stamp was advanced.
- 2026-09-30T12:06:06+00:00: Generated citation repair: `pane`; "minWidth: 0"; "overflowWrap" repointed to dashboard/src/panels/review/ReviewRecordPanes.tsx:33-41; dashboard/src/panels/review/ReviewRecordPanes.tsx:35-35; dashboard/src/panels/review/ReviewRecordPanes.tsx:35-35. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T12:06:06+00:00: Generated citation repair: `fieldValue`; "(absent)"; "(recorded empty)" repointed to dashboard/src/panels/review/ReviewRecordPanes.tsx:117-118; dashboard/src/panels/review/ReviewRecordPanes.tsx:118-118; dashboard/src/panels/review/ReviewRecordPanes.tsx:118-118. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T12:06:06+00:00: Generated citation repair: `EvidencePane` repointed to dashboard/src/panels/review/ReviewRecordPanes.tsx:359-415. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T12:06:06+00:00: Generated citation repair: `SubmissionBlock` repointed to dashboard/src/panels/review/ReviewRecordPanes.tsx:417-445. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-28T21:46:34+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **created this one-to-one card for the record panes extracted from `ReviewSurface.tsx` (L47-R1-F5).** The curator verified the move is byte-identical (old `ReviewSurface.tsx` lines 81-443 equal new lines 23-385). The pane-level contracts the surface card carried (display-only, absent vs recorded-empty, labels displayed not computed, narrow-width declarations, the explorer pointer, the unmeasured submission line) were carried here, not re-invented; the surface card keeps their dated history. New in L48: `ReviewTechnicalDetails` renders records only for a payload that answers the subject on screen and otherwise states pending/unavailable for the requested subject. The verification hash and date are blank because no commit contains this file yet; closeout owns the stamp.
