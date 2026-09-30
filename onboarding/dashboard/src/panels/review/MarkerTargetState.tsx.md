# dashboard/src/panels/review/MarkerTargetState.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/MarkerTargetState.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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
- **On the member's row (`MemberTargetNote`).** Rendered by `FamilyTree.MemberNode` inside the member button, after the
  side tag: for the exact family and member revision of the target, a tagged `Attribution unknown` and the target's
  reason. Inside the button, it is part of the selected node's accessible name.
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
- The `FamilyTree.tsx` hook is an import and one element, kept small because MIK-L33 changes that file.

### Invariants And Boundaries

- **Candidate invariant (not ingested): unknown membership is always distinguishable from confirmed no-family.**
  Realized by the target carrying its `state` and `reason` (`hunkMarkers.addOccurrence`, `unknownReason`),
  `occurrenceLabel` (`Attribution unknown` versus `No recorded family`), and this module, which shows the unknown state
  at the member row, in the rail and in the centre while a confirmed-no-family target keeps the landed
  `No recorded family`. Proved by `ReviewSurface.markers.test.tsx` case 3 on real comparison 3 (the four occurrences;
  the member row named "Attribution unknown"; the confirmed target with the heading and no unknown state; the
  family-less target focused and announced with its reason, with and without a composed tree),
  `MarkerTargetState.test.tsx`, and mutations Q3-1 to Q3-6, F3a and F3b, all caught.
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

- **MIK-L33's sync (ruling 2026-09-30T17:39:21).** L33 adds a change-kind badge beside `MemberTargetNote` in the same
  member button: keep both, the change-kind fact first, and move both reasons to `aria-describedby` with wording that
  tells "change kind unknown" from "membership unknown".

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement: the state at the target, never `No recorded family`, and the review's context kept beside it. | "The review's own family context is kept beside it, never replaced silently" | dashboard/src/panels/review/MarkerTargetState.tsx:1-7 |
| Only a `membership_unknown` target shows anything. | `ATTRIBUTION_UNKNOWN`; `unknownTarget` | dashboard/src/panels/review/MarkerTargetState.tsx:19-54 |
| The member row's note, only on the exact family and revision. | `MemberTargetNote` | dashboard/src/panels/review/MarkerTargetState.tsx:56-81 |
| The invariant view's target: no row in this tree for the membership. | `useInvariantTargetState` | dashboard/src/panels/review/MarkerTargetState.tsx:83-96 |
| The rail's focusable state, named by its heading and described by its reason (review R1 F3). | `InvariantTargetState`; "data-target-state-focus" | dashboard/src/panels/review/MarkerTargetState.tsx:98-145 |
| The centre's family line, with the review's label moved here. | `memberContextLabel`; `MemberFamilyLabel` | dashboard/src/panels/review/MarkerTargetState.tsx:147-182 |
| Its three mounts: the member button, the rail and the centre. | "<MemberTargetNote"; "const unknown = useInvariantTargetState(subject, context);"; "<MemberFamilyLabel subject={subject} payload={payload} entry={entry} />" | dashboard/src/panels/review/FamilyTree.tsx:453-456; dashboard/src/panels/review/ReviewWorkspace.tsx:576-576; dashboard/src/panels/review/FamilyReviewCenter.tsx:796-796 |
| Focus goes to the state before the tree's current node. | `selectionNode` | dashboard/src/panels/review/ReviewWorkspace.tsx:640-649 |
| The real-data case: unknown membership in its own state, apart from no family. | "opens an unknown membership in its own Attribution unknown state, apart from no family" | dashboard/src/panels/review/ReviewSurface.markers.test.tsx:279-365 |
| The unit cases. | "marks the member's row when the named family is in the tree, and only that row"; "shows the state on the invariant view when the named family is not in the review" | dashboard/src/panels/review/MarkerTargetState.test.tsx:55-93 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new target-state module MIK-R34 adds, recording rulings 2026-09-30T16:19:34 Q3 and 2026-09-30T17:39:21 (review R1 F3; N3 accepted; the L33 merge order), and two candidate invariants. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
