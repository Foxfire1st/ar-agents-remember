# dashboard/src/panels/review/MarkerTargetState.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The followed marker's unknown membership state (MIK-R34 rule 2).** The main reading area shows
`Attribution unknown` and its reason, distinct from confirmed `No recorded family`, while retaining
the review's own family context beside it. `ReviewContextNotes` mounts `InvariantTargetState` for a
selected invariant whose named family is absent from the composed context (or no family is named);
`MemberFamilyLabel` supplies the member center's matching label. The compact sidebar has no semantic
member note.

## Code Commentary

### Logic

- **Only an unknown membership.** `unknownTarget` passes the scope's followed `target` through only when its state is
  `membership_unknown`; every other target, and no target, shows nothing here.
- **The exact-member check (`useMemberTarget`).** It matches the followed `membership_unknown` target
  by family key and member revision key. `ChangeBadges` still uses this check for the membership fact
  displayed in the main reading area.
- **The retained export (`MemberTargetNote`).** It can render the exact target's tagged reason with an
  optional description id, but no production `FamilyTree.MemberNode` mounts it: `MemberNode` is removed.
  Its standalone test caller is not a current sidebar integration.
- **On the invariant view (`useInvariantTargetState`).** The target when the subject on screen is the target
  invariant and its membership has no row in this tree: no family is named, or the named family is not in the review's
  family context.
- **In the main page (`InvariantTargetState`).** A dashed focusable section headed `Attribution
  unknown` shows the reason, distinguishes unestablished membership from confirmed absence, and
  displays the review's family-context state/detail openly. `ReviewWorkspace.ReviewContextNotes`
  mounts it ahead of the selected review. The legacy test id `review-rail-target-state` does not
  make it a sidebar mount. Its heading and reason remain the accessible name/description, and
  `data-target-state-focus` retains the target-focus integration.
- **In the centre (`MemberFamilyLabel`).** The member review's family line: the review's own label
  (`memberContextLabel`, moved here from `FamilyReviewCenter.tsx`: `<family> · Member review`, `No recorded family` or
  `Family context unavailable`), or, for the target, a tagged `Attribution unknown`, the reason, and "The review's
  family context reads: <label>."

### Conventions

- `ATTRIBUTION_UNKNOWN` is the one spelling of the state. Test ids `review-member-target-state`,
  `review-rail-target-state` (with `data-family-state`), `review-center-target-state`, each with
  `data-member-state="membership_unknown"`.
- `FamilyTree` no longer imports or mounts the member note. The exported `useMemberTarget` remains
  a `ChangeBadges` dependency for main-page membership facts; `MemberTargetNote` remains testable as a retained export.

### Invariants And Boundaries

- **Candidate invariant (not ingested): unknown membership remains distinguishable from confirmed
  no-family.** The target carries state/reason; `occurrenceLabel`, `useMemberTarget`,
  `InvariantTargetState` and `MemberFamilyLabel` preserve that distinction. Current production
  target/context explanations are main-page facts, not member-button descriptions or a rail
  disclosure. The older MIK-L33/L34 row-description and mutation account is historical evidence for
  that earlier composition, not an assertion about the current compact tree. Current test-subject
  qualification belongs to the separately enumerated proof repairs; no run is claimed here.
- **Candidate invariant (not ingested): Back returns focus to the originating marker with its hunk in view, and never
  takes focus or scroll away from the reader.** Realized across modules: `intentMarkerScope` (`follow`, `back`,
  `returning`, `settle`), `markerNavigation.restore` (clears the tree's focus request), the pane-local reopen
  (`usePaneMarking`'s list and `ExpressionCards.ReadyCards` card Full file), and `markGutter` (`revealMark`,
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
- The retained exact-member note export; no current compact-tree mount. [3]
- The row check shared with the change badge (MIK-L33 merge round). [4]
- The invariant view's target: no row in this tree for the membership. [5]
- The main-page focusable target state, named by its heading and described by its reason, with open context. [6]
- The centre's family line, with the review's label moved here. [7]
- Current integrations: the main-page target state, main membership facts and the member-center family label; the standalone member note has no production tree mount. [8]
- Focus goes to the state before the tree's current node. [9]
- The real-data case: unknown membership in its own state, apart from no family. [10]
- The unit cases. [11]
- The note's `id`, by which a dataset row is described (review R3-1), and the space between tag and reason. [12]
- On a tree comparison the target is a tag on the change facts' membership line (MIK-L33). [13]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
- Unknown-attribution marker constant and row text [14]
- Unknown-target note on the member row [15]
- Invariant target state in the main page and member-center label [17]
