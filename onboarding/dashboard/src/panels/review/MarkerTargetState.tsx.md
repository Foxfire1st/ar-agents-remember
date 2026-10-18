# dashboard/src/panels/review/MarkerTargetState.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Show a followed intent marker's unknown membership distinctly from confirmed no-family, while keeping
the review's independently composed family context visible. Production target explanations are main
reading-area and member-center facts, not semantic disclosures added to compact navigation rows.

## Code Commentary

unknownTarget admits only membership_unknown. useMemberTarget matches exact family and member-revision
keys for the retained row-note export and main-page change facts. That local row-prop match does not
establish that the current family roster actually returned such a row.

The updated invariant fallback uses hasTargetMember: a returned family must match the target family
key and either returned side must contain its exact invariant-revision key. Merely seeing the named
family is insufficient when its roster is unreadable. useInvariantTargetState first requires that the
selected invariant matches the marker target; only an actually returned exact member suppresses the
fallback. No confirmed membership or absence is inferred from a family-only context.

InvariantTargetState is an open focusable section with state/reason labels and the review context
state/detail beside it. MemberFamilyLabel keeps the marker's unknown and the context's own label
separate. MemberTargetNote remains an exact-row-props export, not a current compact-tree mount.

Stored tests distinguish captured unreadable-roster behavior from a deliberately synthetic healthy
roster positive branch. The synthetic mixed component inputs prove a renderer branch, not a newly
produced same-comparison membership fact or fresh browser run.

## Invariants And Boundaries

Unknown membership is not confirmed no-family. Legacy rail test IDs do not determine actual mount
location. This module neither reclassifies a marker nor owns Back/scroll restoration; those owners'
old execution observations below retain their historical scope.

## Historical source-epoch account — superseded where different

Original explanatory detail and producer/test observations are preserved below. Removed dataset or
evidence branches, old mount/population/state rules and earlier execution grades are historical only.
The current account and renewed source evidence govern; prose reference markers below are inert.

> ## Purpose
>
> **The followed marker's unknown membership state (MIK-R34 rule 2).** The main reading area shows
> `Attribution unknown` and its reason, distinct from confirmed `No recorded family`, while retaining
> the review's own family context beside it. `ReviewContextNotes` mounts `InvariantTargetState` for a
> selected invariant whose named family is absent from the composed context (or no family is named);
> `MemberFamilyLabel` supplies the member center's matching label. The compact sidebar has no semantic
> member note.
>
> ## Code Commentary
>
> ### Logic
>
> - **Only an unknown membership.** `unknownTarget` passes the scope's followed `target` through only when its state is
>   `membership_unknown`; every other target, and no target, shows nothing here.
> - **The exact-member check (`useMemberTarget`).** It matches the followed `membership_unknown` target
>   by family key and member revision key. `ChangeBadges` still uses this check for the membership fact
>   displayed in the main reading area.
> - **The retained export (`MemberTargetNote`).** It can render the exact target's tagged reason with an
>   optional description id, but no production `FamilyTree.MemberNode` mounts it: `MemberNode` is removed.
>   Its standalone test caller is not a current sidebar integration.
> - **On the invariant view (`useInvariantTargetState`).** The target when the subject on screen is the target
>   invariant and its membership has no row in this tree: no family is named, or the named family is not in the review's
>   family context.
> - **In the main page (`InvariantTargetState`).** A dashed focusable section headed `Attribution
>   unknown` shows the reason, distinguishes unestablished membership from confirmed absence, and
>   displays the review's family-context state/detail openly. `ReviewWorkspace.ReviewContextNotes`
>   mounts it ahead of the selected review. The legacy test id `review-rail-target-state` does not
>   make it a sidebar mount. Its heading and reason remain the accessible name/description, and
>   `data-target-state-focus` retains the target-focus integration.
> - **In the centre (`MemberFamilyLabel`).** The member review's family line: the review's own label
>   (`memberContextLabel`, moved here from `FamilyReviewCenter.tsx`: `<family> · Member review`, `No recorded family` or
>   `Family context unavailable`), or, for the target, a tagged `Attribution unknown`, the reason, and "The review's
>   family context reads: <label>."
>
> ### Conventions
>
> - `ATTRIBUTION_UNKNOWN` is the one spelling of the state. Test ids `review-member-target-state`,
>   `review-rail-target-state` (with `data-family-state`), `review-center-target-state`, each with
>   `data-member-state="membership_unknown"`.
> - `FamilyTree` no longer imports or mounts the member note. The exported `useMemberTarget` remains
>   a `ChangeBadges` dependency for main-page membership facts; `MemberTargetNote` remains testable as a retained export.
>
> ### Invariants And Boundaries
>
> - **Candidate invariant (not ingested): unknown membership remains distinguishable from confirmed
>   no-family.** The target carries state/reason; `occurrenceLabel`, `useMemberTarget`,
>   `InvariantTargetState` and `MemberFamilyLabel` preserve that distinction. Current production
>   target/context explanations are main-page facts, not member-button descriptions or a rail
>   disclosure. The older MIK-L33/L34 row-description and mutation account is historical evidence for
>   that earlier composition, not an assertion about the current compact tree. Current test-subject
>   qualification belongs to the separately enumerated proof repairs; no run is claimed here.
> - **Candidate invariant (not ingested): Back returns focus to the originating marker with its hunk in view, and never
>   takes focus or scroll away from the reader.** Realized across modules: `intentMarkerScope` (`follow`, `back`,
>   `returning`, `settle`), `markerNavigation.restore` (clears the tree's focus request), the pane-local reopen
>   (`usePaneMarking`'s list and `ExpressionCards.ReadyCards` card Full file), and `markGutter` (`revealMark`,
>   the bounded, passive `holdRevealed` that ends at the reader's pointer, key or wheel, and the redraw carry that acts
>   only while focus is on the body). Proved by `ReviewSurface.markers.test.tsx` case 2 (layout restored, list open,
>   host scrolled into view, focus on the marker), `IntentMarkers.test.tsx`'s return cases, `markGutter.test.tsx`'s
>   redraw and hold cases, and the R2 and R3 browser matrices at 390 and 1600 px (hunks A, C and D; wheel, click and
>   Tab during the hold).
> - A followed target's state stays until Back (review R1 N3, accepted).
>
> ### Todos
>
> - **Resolved by MIK-L33's merge round (rulings 2026-09-30T17:39:21 and 17:47:43; accepted 21:41:02; R3-1 at
>   21:55:02).** Built as ruled: both elements are kept in the member button (the change badge with facts, this note
>   without), the change-kind fact comes first in the description, and the reasons read "change kind unknown" and
>   "membership unknown". On a named family's member the comparison's membership line is the standing line and this
>   module's state is its `Attribution unknown` tag; this note stays for dataset reviews, and `InvariantTargetState` and
>   `MemberFamilyLabel` stay for the invariant view and the rail. The row check is shared as `useMemberTarget`, and the
>   note gained an optional `id` so the row is described by it.

## Evidence

### Docs References

No configured domain-documentation source was available. Current implementation claims use direct
source; requirement/provenance names are not fresh runtime evidence.

### Repo-Internal References

- The followed unknown-membership state stays distinct from confirmed no-family while the review context remains separately visible. [1]
- The stored captured-fixture marker case checks the partial roster fallback, delivered reason, center label and focus; this is not a fresh real-data run. [10]
- Stored unit cases distinguish synthetic exact row props, an unreadable native roster and an explicitly synthetic healthy-roster positive branch. [11]
- The retained note accepts an optional accessible-description ID and separates its tag/reason; it is not a current dataset-row integration. [12]
- On a tree comparison the target is a tag on the change facts' membership line (MIK-L33). [13]
- Unknown-attribution marker constant and row text [14]
- The retained exact-row note renders only the matched followed target, independently of whether production navigation mounts it. [15]
- Main-page target context and the member-center label retain both marker unknown and the review context. [17]
- Only a `membership_unknown` target shows anything. [2]
- The member row's note, only on the exact family and revision. [3]
- The row check shared with the change badge (MIK-L33 merge round). [4]
- The invariant target fallback is suppressed only when the exact family/member revision actually occurs on a returned side, not merely when the family ID exists. [5]
- The focusable main-page state exposes its heading, reason and separate context openly; its legacy rail test ID does not make it a sidebar mount. [6]
- The centre's family line, with the review's label moved here. [7]
- Current integrations are main-page invariant context, the member-center label and main-page change facts; the old member-button mount is removed. [8]
- The current workspace selection-focus chooser retains the explicit target-state destination before its ordinary tree focus path. [9]
- A family-only or unreadable roster cannot suppress the invariant fallback: hasTargetMember requires both the exact family key and a matching invariant revision on either returned side. [18]

### Cross-Repo References

No new cross-repository boundary is introduced by these presentation helpers.
