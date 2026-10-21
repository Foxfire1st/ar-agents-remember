# dashboard/src/panels/review/ReviewScopeHeader.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Supply the review’s historical/reconstructed record label and its task/comparison identity facts for Technical details.

## Code Commentary

`recordLabelOf` gives reconstructed recorded endpoints precedence over ordinary recorded history. It returns `Reconstructed from recorded endpoints` when that limitation is present, `Historical task comparison` for an ordinary recorded review and no label for a live review.

`ScopeRecords` renders repository/master/leaf identity, comparison reference/policy, inventory count or unavailability, before/after code trees and inventory command. Partial inventory stays labelled partial; absent code-tree ids say `not recorded`.

Task-level inventory/tree values come from the supplied frame. A comparison identity is rendered only when `status` is null and the payload contains a comparison; all other cases display `Comparison identity not available`. `comparisonOf` has pending/unavailable descriptions internally, but the current ScopeRecords rendering withholds them behind that guard.

The enclosing reading/TechnicalDetails owner supplies disclosure placement. This module no longer owns a combined scope header, family context renderer or movement block.

## Invariants And Boundaries

Display only: no fetching, local read state, measurement, classification or submission authority. Pending/unavailable reads cannot print a previous subject’s comparison identity through ScopeRecords. The caller owns the appropriate frame and selected-read status.

## Evidence

- Reconstruction labels take precedence and a live review receives no record label. [9]
- Task inventory/trees and guarded comparison identity render without a self-owned disclosure. [10]
- Inventory partial/unavailable labels and internal comparison descriptions retain their distinct states. [11]
- Comparison fallback text is derived from supplied read status and comparison. [12]
