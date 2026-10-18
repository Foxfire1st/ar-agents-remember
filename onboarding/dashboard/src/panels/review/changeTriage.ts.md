# dashboard/src/panels/review/changeTriage.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

These helpers hold navigation grouping, ordering, primary badge precedence, counts and member change facts as pure projections of the delivered outline and kept family context. Existing semantic roster ordering is separate from compact sidebar ordering. Recorded meaning is transported as the own row’s typed state/labels, never a new CHANGE_KIND, sorting weight, count or computed overall effect. An older catalogue-only listing without an admitted outline remains unbadged.

## Code Commentary

### Pure projection of delivered outline facts

`outlineGroups` also accepts an optional invariant-ID map of `ReviewCodeChange`. When that argument is undefined, `outlineMember` uses the walked member fact; a supplied map or null replaces that fact source, including when the map lacks the ID. A real outline change or an `unknown` outline badge is preserved first. Otherwise established implementation yields `code changed`, joined/left membership follows, then unknown implementation (or a walked primary of unknown) yields `unknown`; otherwise the outline badge remains. Recorded meaning still comes from the member's own family occurrence or invariant entry, independently of this badge.

`orderFamilies` copies authored order and otherwise sorts by descending family weight, using zero for an entry without triage facts and original index for ties. `orderMemberRows` now always applies its occurrence-grouping sort; missing facts supply unknown occurrence kind and no authored position. The historical missing-facts bypass is no longer a current contract. `outlineCounts` and `firstOutlineChange` do not pass the optional code map.

OutlineRow also carries the delivered meaning state and ordered labels. memberMeaning takes the exact member’s answer from its family outline occurrence, falling back to the invariant outline entry; it never assigns the family’s labels to a member. This transports recorded judgments beside existing primary change/ordering facts and neither reclassifies change kinds nor computes a net effect.


<details>
<summary>Historical prior account (not the current contract)</summary>


## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The family tree's triage rules as pure functions over the delivered change facts (MIK-R33, ICR-R32@v1 rules 2 to 5).**
Weights, labels and meanings; a family's counts, returned and total, partial and scoped state and weight; the breakdown
text; family and member order; and the union of two deliveries across an admitted roster walk. Nothing here decides a
fact; an entry without `change_kinds` (a dataset review) is left exactly as the landed tree shows it.

Hold the family tree's triage rules as pure functions over the delivered facts: the outline the tree draws, with its badges, order, counts and opening row, plus the per-member change facts the main page states. Nothing here decides a fact; an entry without `change_kinds` (a dataset review) is left exactly as the landed tree shows it.
## Code Commentary

### Recorded reviewer judgments

OutlineRow also carries the delivered meaning state and ordered labels. memberMeaning takes the exact member’s answer from its family outline occurrence, falling back to the invariant outline entry; it never assigns the family’s labels to a member. This transports recorded judgments beside existing primary change/ordering facts and neither reclassifies change kinds nor computes a net effect.

- OutlineRow also carries the delivered meaning state and ordered labels. [16]

### Logic

- **Weights and words.** `CHANGE_WEIGHT` (intent 4 > implementation 3 > membership 2 > unknown 1 > unchanged 0),
  `CHANGE_LABEL` (`impl`; "same revision; text differs"), `CHANGE_MEANING` (each kind's accessible meaning).
- **`occurrenceKind`.** A returned member the facts do not describe reads `unknown`, never `unchanged`.
- **`familyTriage`.** Counts the distinct returned occurrences by primary kind. `partial` (members unreturned) is
  `returned < members_total`; only without a total does an incomplete page count as unreturned members, because a
  roster page can be incomplete with every member returned (ruling 16:22:22 item 8). `scoped` is `partial` or no total
  (review R1 F2): the breakdown then covers only the returned members, and the family weighs at least `unknown`. The
  weight is the highest of the guarantee's, the members' and that floor (ruling 16:22:22 item 3; rule 5).
- **`breakdownText`.** "`a` intent · `b` impl · `c` membership · `d` unknown of T", or "… of N returned (T total)",
  or "… of N returned (total unknown)" (review R1 F2).
- **`orderFamilies`.** By weight, then the context's order; `authored` or no facts keeps the landed order.
- **`orderMemberRows`.** By weight (triage order only), then `authored_position` (the family record's `members` list), then landed row order; an occurrence's revision rows stay together and no sibling is removed. `FamilyReviewCenter` uses it for its semantic member list. Compact sidebar ordering instead comes from `outlineGroups` over outline rows and badges; it does not consume `orderMemberRows`.
- **`mergeChangeKinds`.** Every occurrence either delivery described is kept; the newer family-level facts apply.

### Conventions

Pure, typed functions exported for the tree, the badges, the centre and the walk merge; 200 lines.

### Invariants And Boundaries

- **Returned-member triage scope.** `orderFamilies` and `orderMemberRows` reorder the delivered population without removing its unchanged siblings; `familyTriage` scopes counts to returned members. Current `changeTriage.test.ts` asserts returned occurrence counts, partial/unknown totals, sibling-preserving order and delivery unions. Compact outline navigation is a different population: `changeTraversal.ts` walks rendered eligible tree nodes and does not stop at a removed partial-family continuation control. The prior FamilyTree continuation-stop and mutation account is historical, not current proof; no fresh execution is claimed.
- A total the server could not read never lets the returned members pass for the whole family (`scoped`).

### Todos

No additional work is asserted by this card.

- `OutlineBadge` is what a tree row shows: the outline's own change, `code changed` (walked implementation facts under an unchanged outline row), `joined`/`left` membership, or an aggregate `N changed` family count. `realChange` is true for every badge except `unknown`, `unchanged` and none.
- `outlineGroups` builds the drawn groups: outline families with their members in triage order (by `badgeWeight`: intent-class changes first, then implementation, then membership), unlisted invariants in their own group, and a catalogue-only listing without badges when no outline is admitted. `memberBadge` overlays walked member facts and membership onto the outline row with intent-then-membership precedence; an unchanged family with changed members aggregates to `N changed`.
- `firstOutlineChange` opens the reviewer on the first real change (an added, removed or changed family, else the first changed member); `outlineCounts` counts changed families and changed invariants for the navigation summary.
## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's statement: pure functions over the delivered facts; a dataset entry is left as landed. [1]
- Precedence and sort weight, the labels and the accessible meanings. [2]
- An undescribed returned member reads unknown. [3]
- A family's counts, partial and scoped state and weight (item 8; review R1 F2). [4]
- The breakdown text, never the intent count. [5]
- Families and member rows ordered, siblings kept, one occurrence's rows together. [6]
- The union of two deliveries across a roster walk. [7]
- The centre retains `orderMemberRows` for its semantic roster; compact sidebar rows use `outlineGroups`. [8]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
- Row badge vocabulary with aggregate counts [9]
- Real-change predicate excluding unknown and unchanged [10]
- Drawn groups from outline, walked facts and catalogue [11]
- Walked-fact and membership overlay with precedence [12]
- Triage sort weights for outline badges [13]
- Opening row on the first real change [14]
- Summary counts of changed families and invariants [15]

</details>

- The module projects delivered facts. Missing member facts read unknown through occurrenceKind; familyTriage still returns undefined without change_kinds. The former missing-facts early returns in orderFamilies and orderMemberRows are removed; this is not a blanket guarantee that dataset rows retain their original order. [18]
- outlineGroups builds family/member groups from an admitted outline, tracks listed invariants, appends unlisted invariants, applies authored or badge-weight order and aggregates real member changes under unchanged families. Without an outlined state it returns identity-only catalogue groups. Its optional code map is passed to both family members and unlisted invariant rows; undefined retains walked facts, whereas a map or null replaces that source. [19]
- memberBadge preserves a real outline change or an unknown outline badge first; otherwise established implementation yields code changed, then joined/left membership wins, then unknownImplementation yields unknown, otherwise the original badge remains. unknownImplementation recognizes implementation unknown and, on facts carrying primary, primary unknown. This accepts walked-member or code-change facts and does not infer recorded meaning. [20]
- These pure helpers project outline grouping, ordering, primary badges, counts and member facts. outlineGroups optionally accepts an invariant-ID code-change map; undefined uses walked facts, while a supplied map or null replaces that fact source. memberBadge preserves real or unknown outline changes, then considers established implementation, membership and unknown implementation in that order. Semantic roster ordering remains separate from compact sidebar ordering. OutlineRow carries recorded meaning state and labels separately from its badge. memberMeaning selects the exact member's family occurrence meaning when defined, otherwise the invariant entry's meaning, never the family's labels. Meaning adds no change kind, sorting weight, count or computed net effect. A catalogue-only listing remains unbadged; outlineCounts and firstOutlineChange do not pass the optional code map. [17]
