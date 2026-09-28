# dashboard/src/panels/review/ReviewRecordPanes.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewRecordPanes.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T21:46:34+02:00 |
| lastVerifiedCommitHash |  `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`|
| lastVerifiedCommitDate |  2026-09-28T22:11:57+02:00|
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

`ReviewTechnicalDetails({ payload, unanswered, paging })` is the only export. It always mounts one
`<details data-testid="review-details">`, so its open state survives a selection. When `payload` is
`null` — the subject on screen is still being read or could not be read — it renders one line instead of
the records: `review-details-pending` ("Reading the records of <label>…") or `review-details-unavailable`
("No records are shown: <label> could not be read."). Otherwise it renders a one-column grid
(`gridTemplateColumns: 'minmax(0, 1fr)'`) of `SubmissionBlock`, the surface's `paging` node, and the
`KnowledgePane`, `SourcePane` and `EvidencePane`.

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
| The pane helper's two load-bearing declarations. | `pane`; "minWidth: 0"; "overflowWrap"; `data-pane` | dashboard/src/panels/review/ReviewRecordPanes.tsx:25-33 |
| The attribution labels, displayed never computed. | `applicabilityNote`; `contextList`; `applicabilityCounts` | dashboard/src/panels/review/ReviewRecordPanes.tsx:46-61; dashboard/src/panels/review/ReviewRecordPanes.tsx:63-79; dashboard/src/panels/review/ReviewRecordPanes.tsx:81-92 |
| Absent vs recorded-empty field values. | `fieldValue`; "(absent)"; "(recorded empty)" | dashboard/src/panels/review/ReviewRecordPanes.tsx:109-110 |
| The knowledge pane delegates statements to `KnowledgeStatements`. | `KnowledgePane`; `KnowledgeStatements` | dashboard/src/panels/review/ReviewRecordPanes.tsx:215-240 |
| The source pane points at the explorer rather than listing a second inventory. | `SourcePane`; `review-source-explorer-pointer` | dashboard/src/panels/review/ReviewRecordPanes.tsx:242-297 |
| The evidence pane. | `EvidencePane` | dashboard/src/panels/review/ReviewRecordPanes.tsx:299-355 |
| The submission block: staleness, the unmeasured line, no control. | `SubmissionBlock`; `review-staleness-unmeasured` | dashboard/src/panels/review/ReviewRecordPanes.tsx:357-385 |
| **The disclosure: always mounted; records only for an answer, else one pending or unavailable line.** | `ReviewTechnicalDetails`; `review-details-pending`; `review-details-unavailable`; `gridTemplateColumns` | dashboard/src/panels/review/ReviewRecordPanes.tsx:387-434 |
| The surface hands it the answer alone. | `ReviewTechnicalDetails`; `unanswered` | dashboard/src/panels/review/ReviewSurface.tsx:346-354 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The panes render one repository namespace's
records.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T21:46:34+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **created this one-to-one card for the record panes extracted from `ReviewSurface.tsx` (L47-R1-F5).** The curator verified the move is byte-identical (old `ReviewSurface.tsx` lines 81-443 equal new lines 23-385). The pane-level contracts the surface card carried (display-only, absent vs recorded-empty, labels displayed not computed, narrow-width declarations, the explorer pointer, the unmeasured submission line) were carried here, not re-invented; the surface card keeps their dated history. New in L48: `ReviewTechnicalDetails` renders records only for a payload that answers the subject on screen and otherwise states pending/unavailable for the requested subject. The verification hash and date are blank because no commit contains this file yet; closeout owns the stamp.
