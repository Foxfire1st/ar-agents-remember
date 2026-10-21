# dashboard/src/panels/review/ExpressionCards.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Render a change-set model location as one selectable source block with every entry that shares its region, authored introductions, side facts, source excerpts and intent markers.

## Code Commentary

`ReviewBlockCard` draws only locations whose model node has drawn entries. `BlockCard` carries a comparison-bound block stop, highlights a selection of any entry the node draws, and renders one heading plus all entry voices before the excerpt. The heading names symbol, path, range, role and signed added/removed line counts; unchanged and not-comparable cards retain those labels. A single-entry card exposes its tray action in the heading; shared cards expose one for each voice, retaining each entry's own side-bound identity and alias stop.

`cardVoice` supplies the recorded after-side rationale or proof facet, else the before side. A voice names its entry, invariant, role/facet and planning mark; an absent authored value is an explicit gap. Added, retired and revised introductions have visible state badges, and a revised entry keeps its earlier wording on its own Before line. `OneLine` shows an ellipsis with whole text in its title and expands that one line by click, Enter or Space. A click ending a text selection leaves the line unchanged.

An unchanged excerpt draws the after text once. A changed excerpt draws the actual before/after diff, with an absent file represented by its named empty operand; missing resolved text produces its reason instead. Not-comparable sides draw each available resolved excerpt separately and claim no comparison. File line numbers are retained, `drawnText` removes only the range's terminal newline, and every pane fits its content. Both resolved side lines remain available to assistive reading while the excerpt gutters show their ranges; a non-region side keeps its reason visible. Truncation points to the tree's All changes action. Layout and Changes only collapse arrive from the reading column.

`useExcerptMarking` receives the sides actually drawn and whether the block is in view. Its returned note, pane marks and marker panel stay with the excerpt. `CardCurrentness` separately renders each recorded non-current entry's exact entry/state/side mark and its supplied reason outside disclosures. Neither presentation replaces the source owner's classification or currentness state.

`HeldPane` measures nonzero drawings and holds the last height during editor replacement. A mutation observer restores a removed drawing as an inert, aria-hidden snapshot, undoing same-batch internal changes except React-owned mark portals, until a fresh drawing arrives. `HeldExcerpt` independently holds the whole excerpt's previous height when mark placement changes, releasing it when a pane draws the new marks. These are local drawing and size mechanisms.

## Evidence

- ExpressionCards.tsx current behavior at this source owner. [31]
- ExpressionCards.tsx current behavior at this source owner. [32]
- ExpressionCards.tsx current behavior at this source owner. [33]
- ExpressionCards.tsx current behavior at this source owner. [34]
- ExpressionCards.tsx current behavior at this source owner. [35]
- ExpressionCards.tsx current behavior at this source owner. [36]
- ExpressionCards.tsx current behavior at this source owner. [37]
