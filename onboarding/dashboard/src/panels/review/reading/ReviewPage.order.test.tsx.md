# dashboard/src/panels/review/reading/ReviewPage.order.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Keep the page's tree, reading order and traversal on the same grouped change-set model.

## Code Commentary

### Logic

Injects leaf-wide currentness facts and checks an unrealized subject without entries precedes current entries in both tree and column. In the captured shared region, a URL naming RLZ-ZA95M4 selects the one grouped row/card containing all three entries; j advances through that region once. In All view, k from a subject with no changed blocks selects the last block above its place.

### Invariants And Boundaries

The currentness map is synthetic, and the alias-URL case exercises one specific nonrepresentative entry rather than enumerating every alias. These tests assert DOM order and selection, not browser geometry.

## Evidence

- Synthetic currentness drives identical tree and column order. [4]
- One tested alias selects the three-entry region and traversal counts it once. [5]
- Backward traversal starts from the empty subject's displayed place. [6]
