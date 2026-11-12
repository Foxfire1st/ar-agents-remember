# dashboard/src/panels/review/changeSetOrder.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Build the pure ordered change-set model shared by the review tree and reading column.

## Code Commentary

### Logic

The model combines supplied outline/catalogue facts, leaf-wide code/currentness and card entries. Subjects are invariants nested under family headings; a multi-family invariant renders its locations only at its first displayed occurrence. Without an outline the applied view is All.

Priority orders by recorded effect, change kind, changed-entry count and span, then id. Authored preserves outline order; currentness ranks the least current supplied subject/entry state; memory sorts rank the highest entry value and retain the requested sort while unavailable values apply Priority with a reason.

Location nodes use exact block identities, role order, resolved span and excerpt line counts. Complete excerpts get bounded line-diff counts; unavailable/truncated text retains a range/state. Changed entries sharing kind and resolved regions on both sides share one drawn row/card/keyboard stop while retaining entry identities and entry-based counts.

Changed keeps real changes and explicitly selected/walked context. filterTree matches family/id/title/effect or path/symbol/role only in the tree; folded-location matches retain their subject/group row. Lane rows match their path or Code without invariant.

### Invariants And Boundaries

This module has no fetch or React state and creates no intent judgment. Counts remain undefined until card reads answer; shared drawing does not merge entry identity or turn missing text into an empty side.

## Evidence

- Exact locations, shared-region drawing and deterministic ranking [1]
- One model/view/order for both consumers [2]
- Tree-only matching and reachable folded groups

The pure model now consumes published explainer categories and grades as inputs. A judgment sort orders each subject's drawn changed blocks by the category's declared scale with the pre-existing Priority order breaking ties, places ungraded blocks last under Ungraded (n), and preserves follower/shared-entry identity. Chips carry explicit presenter-inference hover text with the active category first; carried grades retain all reasons and stale flags. Deterministic sorts remain available, while category sorts are enabled only when their category data exists. The model still authors no judgment: it only renders supplied judgments.

- The pure model now consumes published explainer categories and grades as inputs. A judgment sort orders each subject's drawn changed blocks by the category's declared scale with the pre-existing Priority order breaking ties, places ungraded blocks last under Ungraded (n), and preserves follower/shared-entry identity. Chips carry explicit presenter-inference hover text with the active category first; carried grades retain all reasons and stale flags. Deterministic sorts remain available, while category sorts are enabled only when their category data exists. The model still authors no judgment: it only renders supplied judgments. [4]

- Retired at the fifth freeze d59c3493: dashboard/src/panels/review/changeSetOrder.ts:1177-1210 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 10e466b17feee2530c06b2670fef496c6c9e755f. Retired means the anchor no longer stands, not that the cited subject was deleted.
