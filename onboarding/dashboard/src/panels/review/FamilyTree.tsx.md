# dashboard/src/panels/review/FamilyTree.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Supply family/member selection types and the roster helpers used by the reading area's family context. Navigation rendering belongs to tree/ReviewTree.tsx.

## Code Commentary

`FamilySelection` identifies a family plus an optional member revision. `WalkedTree` carries retained entries, the last-read subject labels of kept families, a comparison-change notice and the selected subject's context state. These are supplied context, not a catalogue or a fetch.

`memberRows` unions before/after members by exact invariant revision. A revision on both sides keeps both side names and a same/differs/unknown wording result; recorded row content is preferred over an unrecorded copy. It does not merge distinct revisions or infer a canonical invariant from an unavailable row.

`RosterLine` distinguishes the read owner's cumulative returned/total/remaining item counts from the selected family revision's membership total and the actual loaded member array. A complete first page is the whole selection; a later complete page completes a walk whose loaded context may retain earlier pages. Unresolved-anchor counts are named as anchors not at their recorded blob. `emptyRosterSentence` separates no recorded family revision, measured zero memberships and a page that carried no members of a nonzero measured roster.

`RosterNext` offers one control per incomplete side only when the page published a cursor, labels it with that family, and passes the exact family/side/cursor to its caller. Pagination is explicit and the helper does not issue reads.

## Evidence

- FamilyTree.tsx current behavior at this source owner. [56]
- FamilyTree.tsx current behavior at this source owner. [57]
- FamilyTree.tsx current behavior at this source owner. [58]
- FamilyTree.tsx current behavior at this source owner. [59]
