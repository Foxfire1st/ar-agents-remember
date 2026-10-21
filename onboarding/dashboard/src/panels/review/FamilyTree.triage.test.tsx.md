# dashboard/src/panels/review/FamilyTree.triage.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Review-tree controls cover one-line rows, explicit selection, grouped locations, pinned destinations and the single sort menu.

## Code Commentary

### Logic

- The synthetic outline enters with nothing selected. A click selects exactly that subject and its family occurrence without moving the tree; an external selection reveals its row using only the scroller. Arrow keys traverse tree and pinned rows, including wraparound.
- Changed and All views persist, with Changed as the storage-unavailable fallback. Priority interleaves the Without a family branch; a kept family survives in Changed. Filtering matches paths and reports no match; Escape restores the view.
- The captured L181 card data has 15 changed entries at 13 regions. The turn_ended.ts triple shares one tree row, and any one entry in that region selects it. The 31 unchanged and 28 not-comparable groups open in the reading column through a callback without expanding tree rows; an unchanged-path match in All keeps its subject and group visible.
- The Worklist row precedes the Code without invariant lane and its two file rows in the pinned block. The block is a direct child of the one scroller after the main list. The heading keeps one All changes action and compact invariant/file counts; old tree next/order controls are absent.
- The one Sort popup offers Priority, authored, currentness and four after-index memory sorts. It persists authored order, marks a memory sort unavailable with the exact reason, and reports Priority applying to a forced unavailable order. Popup row classes, radio semantics, separator, descriptions and one explanatory section match their supplied style constants.
- Location and lane-file line counts retain signs and numbers with mint/alarm classes; unknown attribution keeps its reason text. Code-fact count zero remains a polite screen-reader line, positive counts draw a status line, and Without a family is drawn only after another shown family.
- The All changes count is spoken rather than drawn twice, and Sort retains its accessible name when the responsive class hides its repeated word.

### Invariants And Boundaries

The suite uses a synthetic outline and lane plus captured L181 entries. Its reveal case mocks bounding rectangles; style checks compare declared classes and accessible markup. It was not executed here and does not prove real viewport geometry.

## Evidence

- Declared check and its fixture assertions. [14]
- Declared check and its fixture assertions. [15]
- Declared check and its fixture assertions. [16]
- Declared check and its fixture assertions. [17]
- Declared check and its fixture assertions. [18]
- Declared check and its fixture assertions. [19]
- Declared check and its fixture assertions. [20]
- Declared check and its fixture assertions. [21]
- Declared check and its fixture assertions. [22]
- Declared check and its fixture assertions. [23]
- Declared check and its fixture assertions. [24]
- Declared check and its fixture assertions. [25]
- Declared check and its fixture assertions. [26]
- Declared check and its fixture assertions. [27]
- Declared check and its fixture assertions. [28]
- Declared check and its fixture assertions. [29]
- Declared check and its fixture assertions. [30]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/FamilyTree.triage.test.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](overview.md)
>
> ## Purpose
>
> **Five focused R86 component cases over an explicit synthetic outline.** The mounted `FamilyTree` and `ReviewNavigation` receive two families and five invariants supplied by this test. The cases check compact DOM rows, persisted Changed/All views, initial-subject choice, kept rows, filtering, unknown-skipping `j`/`k`, catalogue-only unavailable outlines, summary states and the conditional polite reset message; they do not mount the predecessor captured sidebar/keymap/continuation harness.
>
> The synthetic outline supplies unchanged, unknown, joined, left, changed and added shapes; fixture coverage of those shapes is not an assertion that every branch, geometry or backend derivation is proved.
> ## Code Commentary
>
> ### Logic
>
> **Historical pre-R86 card account — superseded, not current assertion evidence.**
>
> > - **Change-kind badges (8):** every occurrence's delivered kind and marks and the family's guarantee badge; the shared
> >   member (`membership` where it joined, `unchanged` elsewhere); a reworded revision reads `intent` with the note beside
> >   a genuinely unchanged member (ruling 16:22:22 item 5); "why unknown" visible and in the node's description, never its
> >   name (R3-1); each fact once per node (the text note and the guarantee badge not repeated); an undescribed member reads
> >   `unknown` and says why (SYNTHETIC; mutation R-C2); an unknown guarantee says why (SYNTHETIC; mutation R-C10); a
> >   dataset review adds nothing (no badge, breakdown or controls; landed order).
> > - **Triage order (2):** changes first with unchanged siblings kept, the control switching to authored order and storing
> >   it; triage order when storage is unavailable (`readTreeOrder` over a throwing and an absent storage).
> > - **Next and previous change (5):** `j` from the top visits A, H, B, C, D, G and stays at the end with a polite "No
> >   later change…" and the selection scrolled into view; `k` walks back and lands on a revised member's first row; a
> >   filter showing only FAM-F00002 visits its guarantee row, then P, then F; past a partial family's returned members
> >   focus moves to the continuation control with the message, and the next `j` moves on; inert in the filter input, a
> >   textarea, contenteditable, the PTY zone, with ctrl, and outside the zone; registered with the keymap owner, listed for
> >   the `?` reference and rebindable to `N`.
> > - **One statement per fact on a member (3; merge round and R3-1, SYNTHETIC facts and scope over INV-GGGGGG):** the
> >   change kind, its reason, then the membership, each labelled; a followed marker's **Attribution unknown** on the
> >   membership line, drawn first, described after the kind, the name carrying no fact; MIK-L34's own note kept where no
> >   change facts are delivered (a dataset row), with the note as that row's description.
>
> ### Conventions
>
> Vitest and Testing Library mount the real components in a `data-kbzone=review` container. The current harness contains neither the predecessor textarea/contenteditable/PTY controls nor its keymap-registration and rebinding probes.
>
> ### Invariants And Boundaries
>
> The current assertions are the five synthetic-outline cases described here. No current assertion in this file establishes sidebar continuation focus, continuation loading, shortcut inertness in text editors or PTY zones, or registered/rebound keymap behavior.
>
> ### Todos
>
> No additional work is asserted by this card.
>
> - The synthetic outline contains two families and five invariants, with representative change and membership shapes.
> - The five cases assert the rendered row sets and text, both view states, first-real-change/named/no-change selection, kept tags and filtering, selected unknown-skipping `j`/`k` moves, unavailable-outline fallback and summary wording, and the conditional polite reset status.
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.
>
> No configured live documentation source was available for this pass.
>
> ### Repo-Internal References
>
> **Historical pre-R86 card account — superseded, not current assertion evidence.**
>
> > - The suite's statement: the real tree inside a reviewer zone over the store-authored bodies. (historical reference 1)
> > - The harness: the zone with a textarea, a contenteditable region and a terminal-zone control. (historical reference 2)
> > - Badges: kinds, marks, the shared member, the reworded revision, why unknown, one statement, undescribed members, the dataset review. (historical reference 3)
> > - Triage order and its control; triage when storage is unavailable. (historical reference 4)
> > - Traversal: displayed order, ends, filter, the partial-family stop, inertness, the keymap owner. (historical reference 5)
> > - One statement per fact on a member, with and without a followed marker, and L34's note on a dataset row. (historical reference 6)
>
> ### Cross-Repo References
>
> No cross-repo boundary is crossed by this file.
> - Mounted tree harness with kept-family support (historical reference 8)
> - Compact rows and persisted views (historical reference 9)
> - First-real-change opening and no-change selection (historical reference 10)
> - Kept families, filtering and unknown-skipping traversal (historical reference 11)
> - Catalogue-only listing and summary count states (historical reference 12)
> - Conditional polite comparison-reset status (historical reference 13)
>
> - Representative synthetic outline supplying unchanged, unknown, joined, left, changed and added shapes; not exhaustive badge-branch proof. (historical reference 7)
