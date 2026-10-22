# dashboard/src/panels/review/ReviewScopeHeader.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Supply the review's historical/reconstructed record label, the delivered-pair line and facts, and its task/comparison identity facts for Technical details.

## Code Commentary

`recordLabelOf` gives reconstructed recorded endpoints precedence over ordinary recorded history. It returns `Reconstructed from recorded endpoints` when that limitation is present, `Historical task comparison` for an ordinary recorded review and no label for a live review.

`DeliveredLine` states the one line a review shows when the comparison on screen is not the pair the leaf delivered. It renders nothing for a matching pair, and for `differs` it offers a control that asks for the delivered view. An `unavailable` delivery is stated on the line, while its detail appears in the technical details, and it offers no control, because no delivered view can be offered from a delivery that could not be established. The line reports which pair is shown; it never says an earlier record's own count or statement was wrong.

`DeliveredFacts` lists the delivered pair's exact code and memory trees and the number that holds them, or states that the delivered pair is unavailable, inside the page's existing technical details. `shortTree` is the page's short form of a tree id, or `not recorded` when the notice carries none.

`ScopeRecords` renders repository/master/leaf identity, comparison reference/policy, inventory count or unavailability, before/after code trees and inventory command. Partial inventory stays labelled partial; absent code-tree ids say `not recorded`.

Task-level inventory/tree values come from the supplied frame. A comparison identity is rendered only when `status` is null and the payload contains a comparison; all other cases display `Comparison identity not available`.

The enclosing reading/TechnicalDetails owner supplies disclosure placement.

## Invariants And Boundaries

Display only: no fetching, local read state, measurement, classification or submission authority. Pending/unavailable reads cannot print a previous subject's comparison identity through ScopeRecords. The delivered line and facts are statements about identities, never a review, acceptance or a verdict about another comparison.

## Evidence

- Reconstruction labels take precedence and a live review receives no record label. [9]
- Task inventory/trees and guarded comparison identity render without a self-owned disclosure. [10]
- Inventory partial/unavailable labels and internal comparison descriptions retain their distinct states. [11]
- Comparison fallback text is derived from supplied read status and comparison. [12]

- The mismatch line states the shown pair, offers the delivered control only where a pair was established, and states nothing for a matching pair. [13]
- The delivered identities are listed as facts, or named unavailable, in the existing technical details. [14]
