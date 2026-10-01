# dashboard/src/panels/review/MarkerTargetState.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The selection a followed intent marker opened when its membership is unknown (MIK-R34 rule 2, with ICR-R24@v3's
per-member `Attribution unknown` state; ruling 2026-09-30T16:19:34 Q3).** It shows `Attribution unknown` and its reason
at the target: on the member's row when the family is named and in the tree, otherwise on the invariant view, in the
rail and the centre. It never shows the `No recorded family` a confirmed absence reads, and it keeps the review's own
family context beside it rather than replacing it silently: where the review states a measured zero that the
marker's classification could not confirm, both are named.

## Code Commentary

### Logic

- **Only an unknown membership.** `unknownTarget` passes the scope's followed `target` through only when its state is
  `membership_unknown`; every other target, and no target, shows nothing here.
- **The row check (`useMemberTarget`, MIK-L33 merge round).** L34's check, lifted verbatim out of `MemberTargetNote`:
  the scope's followed target when it is `membership_unknown` and its `familyKey` and `memberRevisionKey` are this
  row's, else `null`. `MemberTargetNote` and MIK-L33's `ChangeBadges.useMemberChange` both call it, so the note and the
  change badge cannot disagree about which row is the target.
- **On the member's row (`MemberTargetNote`).** Rendered by `FamilyTree.MemberNode` inside the member button, after the
  side tag, **only on a row without change facts** (a dataset review) since MIK-L33: for the exact family and member
  revision of the target, a tagged `Attribution unknown`, a space, and the target's reason. It takes an optional `id`,
  and the row names that id in its `aria-describedby`, so the state is the row's accessible description while its name
  stays its subject (MIK-L33 review R3-1; the space keeps the tag and the reason apart when read). **On a tree
  comparison's row** the change badge states the target once instead: the change facts' membership line carries a
  tagged `Attribution unknown` "opened from an intent marker ·", drawn first, with the comparison's own membership
  reason, and L34's note is not drawn (`ChangeBadges.MembershipReason`, ruling 2026-09-30T17:47:43).
- **On the invariant view (`useInvariantTargetState`).** The target when the subject on screen is the target
  invariant and its membership has no row in this tree: no family is named, or the named family is not in the review's
  family context.
- **In the rail (`InvariantTargetState`; review R1 F3).** A dashed section headed `Attribution unknown`, with the
  reason (`<invariant> in <family>: <reason>.`), a sentence that this membership is not established and is not a
  confirmed absence of a family, and the review's own context (`state: detail`) in a disclosure. It is focusable
  (`tabIndex=-1`, `data-target-state-focus`), its accessible name is its heading (`aria-labelledby`) and its
  description the reason (`aria-describedby`), so a follow lands on an element that announces the state:
  `ReviewWorkspace.selectionNode` focuses it in preference to the tree's auto-selected row. `FamilyRailContext` renders
  it in place of the review's statement when no tree is composed, and above the composed tree otherwise.
- **In the centre (`MemberFamilyLabel`).** The member review's family line: the review's own label
  (`memberContextLabel`, moved here from `FamilyReviewCenter.tsx`: `<family> · Member review`, `No recorded family` or
  `Family context unavailable`), or, for the target, a tagged `Attribution unknown`, the reason, and "The review's
  family context reads: <label>."

### Conventions

- `ATTRIBUTION_UNKNOWN` is the one spelling of the state. Test ids `review-member-target-state`,
  `review-rail-target-state` (with `data-family-state`), `review-center-target-state`, each with
  `data-member-state="membership_unknown"`.
- The `FamilyTree.tsx` hook was an import and one element, kept small for MIK-L33's merge; MIK-L33 kept it for rows
  without change facts and imports `useMemberTarget` for its badge (`ChangeBadges.tsx`).

### Invariants And Boundaries

- **Candidate invariant (not ingested): unknown membership is always distinguishable from confirmed no-family.**
  Realized by the target carrying its `state` and `reason` (`hunkMarkers.addOccurrence`, `unknownReason`),
  `occurrenceLabel` (`Attribution unknown` versus `No recorded family`), and this module, which shows the unknown state
  at the member row, in the rail and in the centre while a confirmed-no-family target keeps the landed
  `No recorded family`. Proved by `ReviewSurface.markers.test.tsx` case 3 on real comparison 3 (the four occurrences;
  the member row carrying "Attribution unknown", since MIK-L33 in its description with the comparison's reason; the
  confirmed target with the heading and no unknown state; the family-less target focused and announced with its
  reason, with and without a composed tree), `MarkerTargetState.test.tsx`, and mutations Q3-1 to Q3-6, F3a and F3b,
  all caught. **Since MIK-L33** the state is stated once on a tree comparison's row, as the tag on the change facts'
  membership line, and on a dataset row by this note as the row's description: proved by
  `ReviewSurface.triageMarkers.test.tsx` case 1 on real data, `FamilyTree.triage.test.tsx`'s "one statement per fact
  on a member" cases (with and without the tag; the dataset row), and the merge-round and R3 mutations (tag dropped;
  L34's note beside the badge; a dataset row not described), all caught.
- **Candidate invariant (not ingested): Back returns focus to the originating marker with its hunk in view, and never
  takes focus or scroll away from the reader.** Realized across modules: `intentMarkerScope` (`follow`, `back`,
  `returning`, `settle`), `markerNavigation.restore` (clears the tree's focus request), the pane-local reopen
  (`usePaneMarking`'s list, `LaneFileFocus.FullFile`, `ExpressionCards.ReadyCards`), and `markGutter` (`revealMark`,
  the bounded, passive `holdRevealed` that ends at the reader's pointer, key or wheel, and the redraw carry that acts
  only while focus is on the body). Proved by `ReviewSurface.markers.test.tsx` case 2 (layout restored, list open,
  host scrolled into view, focus on the marker), `IntentMarkers.test.tsx`'s return cases, `markGutter.test.tsx`'s
  redraw and hold cases, and the R2 and R3 browser matrices at 390 and 1600 px (hunks A, C and D; wheel, click and
  Tab during the hold).
- A followed target's state stays until Back (review R1 N3, accepted).

### Todos

- **Resolved by MIK-L33's merge round (rulings 2026-09-30T17:39:21 and 17:47:43; accepted 21:41:02; R3-1 at
  21:55:02).** Built as ruled: both elements are kept in the member button (the change badge with facts, this note
  without), the change-kind fact comes first in the description, and the reasons read "change kind unknown" and
  "membership unknown". On a named family's member the comparison's membership line is the standing line and this
  module's state is its `Attribution unknown` tag; this note stays for dataset reviews, and `InvariantTargetState` and
  `MemberFamilyLabel` stay for the invariant view and the rail. The row check is shared as `useMemberTarget`, and the
  note gained an optional `id` so the row is described by it.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement: the state at the target, never `No recorded family`, and the review's context kept beside it. [1]
- Only a `membership_unknown` target shows anything. [2]
- The member row's note, only on the exact family and revision. [3]
- The row check shared with the change badge (MIK-L33 merge round). [4]
- The invariant view's target: no row in this tree for the membership. [5]
- The rail's focusable state, named by its heading and described by its reason (review R1 F3). [6]
- The centre's family line, with the review's label moved here. [7]
- Its three mounts: the member button, the rail and the centre. [8]
- Focus goes to the state before the tree's current node. [9]
- The real-data case: unknown membership in its own state, apart from no family. [10]
- The unit cases. [11]
- The note's `id`, by which a dataset row is described (review R3-1), and the space between tag and reason. [12]
- On a tree comparison the target is a tag on the change facts' membership line (MIK-L33). [13]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
