# dashboard/src/panels/review/ReviewRecordPanes.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Render one admitted review payload's open main-page facts separately from compact technical identities. `ReviewMainFacts` owns the visible changed non-authored fields, detection signals, unresolved references, attribution counts, staleness and submission reason. `ReviewTechnicalDetails` keeps only record/provenance identities in its Technical details disclosure. Neither export computes a review, fetches, publishes or selects a subject.

## Code Commentary

### Logic

- `RecordFacts` excludes statement, applicability, conditions, exclusions, essential_conditions and joint_guarantee from its non-authored field-change list. `fieldValue` distinguishes undefined `(absent)` from a present empty string `(recorded empty)`; neither is printed as a blank. Other recorded text is passed through unchanged. These field rows are main-page facts, not content moved back into Technical details. It renders detection signals and combines knowledge/source/evidence/link unresolved references, with reason content explicitly marked in the open page.
- `ReviewMainFacts({ payload, laneRead, onAllChanges })` consumes the optional lane read for attribution count wording, otherwise displays the payload's landed counts. It prints non-current staleness, the assessment submission state/reason and next action. Its optional All changes button invokes the supplied callback; it does not fetch or own comparison selection. There is no SourceExplorer pointer or LaneAttributionLists renderer here.
- `ReviewTechnicalDetails({ payload, unanswered, paging })` renders a pending/unavailable paragraph outside the disclosure when payload is null, then the supplied paging node and always-mounted provenance `<details>`. With a payload it prints comparison/policy, retained revision groups, source expansion reference/command, evidence/observation/assessment IDs and the dispositions accepted by the existing authority. Those dispositions are not publication approval.
- The TechnicalDetails type still permits an optional laneRead compatibility prop, but this export does not destructure or use it; current lane attribution is in ReviewMainFacts. No old KnowledgePane, SourcePane, EvidencePane, SubmissionBlock or KnowledgeStatements delegation survives in this module.

### Invariants And Boundaries

The parent owns admitted payload/subject binding. A pending or unavailable subject receives no old payload's identities in TechnicalDetails. Authored content, non-authored changes and reasons must not be described as hidden behind Technical details: current main-page renderers own them. The supplied paging node is outside that disclosure. This card describes source composition, not a new browser run, narrow-width proof or whole-CODE verdict.

## Evidence

- Undefined and recorded-empty field values have distinct explicit labels while other text passes through. [15]

### Repo-Internal References



- The open record facts filter authored fields and display detection signals and combined unresolved references. [12]

- Main-page facts render lane/landed counts, staleness, submission reason and optional All changes callback. [13]

- Compact provenance identities remain in the technical disclosure, with pending state and paging outside it. [14]

## Historical pre-R86 account — preserved, superseded, not current assertions

<details>
<summary>Original renderer corpus, evidence identities and historical source/test custody</summary>

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

The renderers are unchanged from the surface. `KnowledgePane` mounts `KnowledgeFacts`,
`DetectionSignals` and delegates its statements to `KnowledgeStatements`. The authored-effects
collection left with the retired envelope tables: no `authored-effects` list renders here, only the
detection signals (facts, not findings). `SourcePane` carries a
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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module's own statement of why it exists and that the disclosure stays mounted while another subject is pending or unavailable.** [1]
- The pane helper's two load-bearing declarations. [2]
- The attribution labels, displayed never computed. [3]
- Absent vs recorded-empty field values. [4]
- The knowledge pane delegates statements to `KnowledgeStatements`. [5]
- The landed count text, and the lane's two lists or its pending or unknown line (MIK-L32). [6]
- The source pane points at the explorer rather than listing a second inventory; on a tree comparison its attribution counts and lists come from the lane (review F1). [7]
- The evidence pane. [8]
- The submission block: staleness, the unmeasured line, no control. [9]
- **The disclosure: always mounted; records only for an answer, else one pending or unavailable line; the lane read passed to the source pane.** [10]
- The surface hands it the answer alone, and the one lane read. [11]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The panes render one repository namespace's
records.

No meaningful cross-repo references found.

</details>
