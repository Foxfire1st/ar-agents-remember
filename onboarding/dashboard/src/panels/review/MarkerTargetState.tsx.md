# dashboard/src/panels/review/MarkerTargetState.tsx

## Governing Overview

[Review route overview](overview.md)

## Purpose

Show a followed marker's unknown membership distinctly from confirmed no-family, keeping the review's independently composed family context beside it. These are target and selected-member explanations, with their mount locations established by the reading-area callers.

## Code Commentary

`unknownTarget` accepts only `membership_unknown`. `useMemberTarget` matches exact family and member-revision keys; `MemberTargetNote` draws that matched target's tag and reason with an optional accessible-description ID. Supplied matching row props do not establish that a current family roster actually contains that row, and the retained export alone establishes no production navigation mount.

`hasTargetMember` requires both the exact target family and its invariant-revision key on either returned side. A family ID without a readable matching member cannot suppress the fallback. `useInvariantTargetState` also requires the selected subject to be the target invariant. Neither a confirmed membership nor a confirmed absence is inferred from a family-only context.

`InvariantTargetState` is an open focusable section, labelled by its state and described by its reason. It retains the separate review context's detail and now translates that context's state through `familyStateWords(context.state)` rather than printing the machine state directly. Its legacy rail test ID does not determine its actual mount. `SelectedSlot` mounts the target note before the selected center; the workspace focus chooser prefers this explicit target-state destination before the ordinary current tree row.

`MemberFamilyLabel` keeps the target's unknown reason distinct from the context's own member/family label. `FamilyReviewCenter.MemberTargetLine` mounts it before the invariant content only when the marker fallback applies. Main-page member change facts also read the exact family/revision target and add its unknown tag to the membership reason, without replacing the comparison's separate facts.

Stored mounted tests check a named unknown target over a partial roster, matching reason/center state and focus. Stored component cases distinguish supplied row props, native unreadable context and explicitly synthetic alternate renderer inputs. The healthy-roster positive branch combines component inputs for that branch; it is not a newly produced same-comparison membership fact or a fresh browser result.

## Invariants And Boundaries

Unknown membership is not confirmed no-family. This module neither reclassifies the marker nor owns Back, editor scrolling or restoration. Its retained note export and synthetic renderer controls must not be read as proof of a current sidebar integration.

## Evidence

- The followed marker unknown-membership state remains distinct from confirmed no-family while the review context is kept separately. [1]
- Only a membership_unknown target is admitted by unknownTarget. [2]
- MemberTargetNote renders its tagged reason only for matching exact family/revision row props. [3]
- useMemberTarget matches the followed unknown target by family key and invariant-revision key. [4]
- An invariant fallback is suppressed only when its exact target member actually occurs in the returned family roster. [5]
- The focusable target section shows state and reason and translates the separate review-context state through familyStateWords. [6]
- The member label preserves the review context label and qualifies it when marker membership is unknown. [7]
- The retained note takes an optional accessible-description ID; its existence does not prove that a production navigation row mounts it. [12]
- The one unknown-attribution label is explicitly named. [14]
- The retained row-note export uses only the exact matched target and its reason. [15]
- The focusable target and center label retain marker unknown separately from their supplied review context. [17]
- The fallback member check requires exact family and revision identity on either returned side. [18]
- The answered SelectedSlot mounts MarkerTargetNote before the selected center content. [8]
- The selection-focus chooser prefers the explicit target-state destination before a current tree row. [9]
- A stored mounted test follows the named unknown occurrence and checks its native reason, partial family-state label, matching center reason and target focus. [10]
- Stored component tests distinguish exact supplied row props, an unreadable roster and an explicitly synthetic healthy-roster positive branch; these are not new producer facts. [11]
- The main-page membership-reason renderer adds the marker unknown tag while keeping the independently composed change reason. [13]
- MemberTargetLine mounts the unknown marker family label before the invariant statement, steps and judgment. [19]
- Main-page member change facts call useMemberChange with exact family and revision keys before drawing MemberChangeBadge. [20]

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
