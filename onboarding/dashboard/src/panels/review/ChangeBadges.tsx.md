# dashboard/src/panels/review/ChangeBadges.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**Outline navigation badges, reading-area change facts, and triage controls.** Values rendered here are delivered facts or counts computed by `changeTriage.ts`; the module decides no fact. `FamilyTree.tsx` mounts `OutlineChangeBadge` from each outline row's badge, and that component renders nothing when no badge is supplied. It does not mount the full member/guarantee fact renderers. Those detailed reasons and followed-marker membership attribution belong to the reading area; their absence does not invent dataset change facts.

Render the family tree's change badges and its triage bar: one short badge per outline row saying what changed, the delivered per-member and guarantee facts with their reasons on the main page, and the order, traversal and status controls above the tree.
- `OutlineChangeBadge` draws the tree row's one badge; the member and guarantee badges below state the delivered facts in the main page only, never in the tree.
## Code Commentary

### Logic

- **`MemberChangeBadge`.** The primary badge (`pill` with the kind's token colour, and the word carrying the meaning
  without colour), the secondary `Marks` (`+impl`, `+membership`, `+test`, `+unknown`, and the note "same revision; text
  differs" for `text_differs`), then the reason lines. Its `title` holds the kind's meaning and every evidence and
  reason line. A returned member the facts do not describe reads `unknown` with "no change facts were delivered for this
  member" (`UNDESCRIBED_CHANGE`), never `unchanged`.
- **Reasons, labelled by what is unknown.** `UnknownReason` and `MembershipReason` expose every delivered
  reason joined in open reading content, also preserving title text. The guarantee fact names its own
  unknown reason; no closed disclosure or first-reason-only truncation substitutes for it.
- **One statement per fact on a named family's member (ruling 17:47:43's merge plan).** `useMemberChange` reads
  `MarkerTargetState.useMemberTarget` (the same check L34's `MemberTargetNote` uses, so the two cannot disagree on the
  target). When a followed marker's unknown-membership target is this row, the membership line carries the tagged
  **Attribution unknown** "opened from an intent marker ·" and is drawn first; L34's own note is not drawn. Should the
  comparison know a membership the marker could not confirm, the line names "the marker's classification: …" and the
  badge keeps the comparison's fact (`membershipLine`); on real data that case does not arise (review R3 point 2).
- **The accessible description (review R3-1).** `describedBy` always orders the badge, then the change-kind reason,
  then the membership, whatever the drawn order. Compact outline row names are title+badge; the removed
  `FamilyTree.useMemberNodeIds` integration is not a current sidebar contract.
- **`FamilyBreakdown`.** "Members by change: 1 intent · 2 impl · 0 membership · 1 unknown of 5", scoped as "… of N
  returned (T total)" or "(total unknown)" (`breakdownText`); never labelled as the `+N −N` intent count.
- **`TriageControls` in the sticky `triageBar`.** The order button ("Order: changes first" / "Order: authored"), "↑
  Previous" and "↓ Next" with the keymap owner's effective bindings in their titles and
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


### Invariants And Boundaries

- Delivered semantic facts are stated in the reading area, not duplicated as sidebar disclosures.
  A marker's unknown membership shares one membership reason line without replacing comparison facts.
- An unknown semantic badge is never unexplained, and an end status is announced where the reader is
  looking (the sticky bar; the live region stays).

### Todos

Review R3-2 (accepted as a note): at 390 px, as the tree section scrolls out, the sticky bar slides up under the sticky
Back for one step; Back stays on top and clickable.

- `OutlineChangeBadge` maps an `OutlineBadge` to a pill colour (`added`/`removed`/`changed` read as intent, `code changed` as implementation, `joined`/`left` as membership) and titles it with `OUTLINE_MEANING`; an aggregate `N changed` badge keeps the explanatory title instead.
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
- Row badge maps outline kinds to pill colours with meaning titles [12]
- Badge meanings for each outline kind [13]
- Marker target joined to delivered facts with ordered description [16]
- Membership line keeps both the marker reason and the comparison fact [17]
- Triage bar with order switch, traversal buttons and polite status [18]
