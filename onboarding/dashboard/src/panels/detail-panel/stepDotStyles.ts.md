# dashboard/src/panels/detail-panel/stepDotStyles.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Style pointer-only cached step details separately from clipped task row cells.

## Code Commentary

The tooltip is fixed-position, has a viewport-relative maximum width and a high stacking layer, and sets pointerEvents to none. Its head and nested-state rows use local flex/grid layout.

The component owns portal creation, timing and placement; CSS does not. Markdown links inside this pointer-inert tooltip are not independent clickable controls. No keyboard-tooltip, scroll tracking or browser acceptance follows from these declarations.

MIK-R175 rule 3: `stepTipStyles` stops the box breaking words anywhere (`overflowWrap: normal`, `wordBreak: normal`); `tipPartStyles` keeps the id and status word whole (`flexShrink: 0`, `whiteSpace: nowrap`) and `tipTitleStyles` is the one part that shrinks and wraps. The style objects themselves are exported beside their `css()` results, so the contract can be measured rather than inferred from a rendered width.

## Evidence

- The tooltip's box breaks no word, and the parts that must stay whole say so themselves. [2]


- Pointer-inert fixed tooltip styles and ordered nested-row layout remain separate from interaction/data ownership. [1]
