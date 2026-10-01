# dashboard/src/panels/review/ChangeBadges.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The family tree's change-kind badges, family breakdown and triage controls (MIK-R33, adopting ICR-R32@v1 rules 2, 3,
6 and 9's status placement).** Every value it renders is the server's fact or a count of them (`changeTriage.ts`); it
decides no fact. `FamilyTree.tsx` mounts it only when the context carries change facts (a tree comparison); a dataset
review renders none of it. It is also where a followed intent marker's unknown membership (MIK-L34) is stated once on a
tree comparison's member row, as a tag on the membership line.

## Code Commentary

### Logic

- **`MemberChangeBadge`.** The primary badge (`pill` with the kind's token colour, and the word carrying the meaning
  without colour), the secondary `Marks` (`+impl`, `+membership`, `+test`, `+unknown`, and the note "same revision; text
  differs" for `text_differs`), then the reason lines. Its `title` holds the kind's meaning and every evidence and
  reason line. A returned member the facts do not describe reads `unknown` with "no change facts were delivered for this
  member" (`UNDESCRIBED_CHANGE`), never `unchanged`.
- **Reasons, labelled by what is unknown (merge round).** `UnknownReason` draws "change kind unknown: <first reason>
  (and N more)" and `MembershipReason` draws "membership unknown: …", each in view beside the badge with every reason in
  its `title` (ruling 16:22:22 items 4 and 9). The family row's `GuaranteeChangeBadge` draws "guarantee unknown: …".
- **One statement per fact on a named family's member (ruling 17:47:43's merge plan).** `useMemberChange` reads
  `MarkerTargetState.useMemberTarget` (the same check L34's `MemberTargetNote` uses, so the two cannot disagree on the
  target). When a followed marker's unknown-membership target is this row, the membership line carries the tagged
  **Attribution unknown** "opened from an intent marker ·" and is drawn first; L34's own note is not drawn. Should the
  comparison know a membership the marker could not confirm, the line names "the marker's classification: …" and the
  badge keeps the comparison's fact (`membershipLine`); on real data that case does not arise (review R3 point 2).
- **The accessible description (review R3-1).** `describedBy` always orders the badge, then the change-kind reason,
  then the membership, whatever the drawn order; `FamilyTree.useMemberNodeIds` puts it in `aria-describedby` while the
  node's name stays its subject.
- **`FamilyBreakdown`.** "Members by change: 1 intent · 2 impl · 0 membership · 1 unknown of 5", scoped as "… of N
  returned (T total)" or "(total unknown)" (`breakdownText`); never labelled as the `+N −N` intent count.
- **`TriageControls` in the sticky `triageBar`.** The order button ("Order: changes first" / "Order: authored"), "↑
  Previous change (k)" and "↓ Next change (j)" with the keymap owner's effective bindings in their labels and
  `aria-keyshortcuts`, and the polite `role="status"` line. The bar sticks at `top: var(--review-sticky-top, 0)`, below
  L34's sticky `Back to <file>` while it is open in the stacked layout (`ReviewWorkspace` sets the variable; the merge
  round's shared offset), and its panel-coloured top shadow covers the scroll container's padding strip when stuck.

### Conventions

- `styled-system/css` with existing tokens only (`alarm`, `cyan`, `purple`, `gold`, `muted`, `grid`, `bgPanel`); an
  unknown badge is dashed. Test ids: `review-change-badge` (`data-change-kind`, `data-change-marks`),
  `review-change-mark` (`data-mark`), `review-change-why`, `review-change-membership-why` (`data-member-state`),
  `review-member-target-tag`, `review-guarantee-change`, `review-family-breakdown` (`data-partial`),
  `review-triage-bar`, `review-triage-controls`, `review-tree-order` (`data-order`), `review-previous-change`,
  `review-next-change`, `review-change-status`.
- 359 lines.

### Invariants And Boundaries

- **Candidate invariant (not ingested; no speculative ingestion): each fact is stated once per node, both visually and
  to assistive technology.** Realized by `MemberChangeBadge` (one badge, one change-kind reason line, one membership
  line; the marker's state as a tag on that line, L34's note not drawn), the `text_differs` note replacing the side
  tag's "· same revision · text differs" and the family badge replacing the guarantee block's "· unchanged"
  (`FamilyTree.tsx`), and `describedBy` with `FamilyTree.useMemberNodeIds` (name = subject, description = facts, ruled
  order). Proved by `FamilyTree.triage.test.tsx` ("states each fact once per node…", "says why an unknown is unknown…",
  the three "one statement per fact on a member" cases), `ReviewSurface.triageMarkers.test.tsx` case 1 and L34's
  adjusted `ReviewSurface.markers.test.tsx` step (name and description on real data), the merge-round mutations (tag
  dropped; L34's note beside the badge; description with membership first; the marker's reason preferred) and the R3
  mutations (no `aria-labelledby`; facts in the name; a dataset row not described; the side tag left out of the name),
  all caught, and the worker's and the reviewer's CDP reads at 390 px.
- An unknown badge is never unexplained, and the status of an end or a partial family is announced where the reader is
  looking (the sticky bar; the live region stays).

### Todos

Review R3-2 (accepted as a note): at 390 px, as the tree section scrolls out, the sticky bar slides up under the sticky
Back for one step; Back stays on top and clickable.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's statement: every value is the server's fact or a count of them. [1]
- The kind styles on existing tokens; an unknown is dashed. [2]
- The sticky triage bar below the workspace's sticky way back. [3]
- The marks and the labelled reason line. [4]
- A returned member without facts reads unknown and says why. [5]
- The row's change state: the marker's target from L34's own check, and the description in the ruled order. [6]
- The membership line and the followed marker's tag on it. [7]
- The member badge: the tagged membership line drawn first under a followed marker. [8]
- The family's guarantee badge and the breakdown line. [9]
- The order, previous and next controls and the polite status. [10]
- Its mounts in the tree. [11]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
