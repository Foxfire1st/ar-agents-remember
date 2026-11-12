# dashboard/src/panels/review/focusedCards.ts

## Governing Overview

[review route overview](overview.md)

## Purpose

Provide the source block's recorded voice, line/range labels, non-current entry marks and highlighting language to the shared card renderer.

## Code Commentary

`ExpressionCard` carries kind/path/change, both supplied sides and every drawn entry. `cardVoice` chooses the recorded after side, otherwise before, retaining its authored role/rationale or proof facet. An absent realization rationale stays missing. When both sides record the entry and the after-side authored value differs, revised holds the earlier value.

`firstLines` retains each excerpt's file numbering with one only when unrecorded. `drawnText` removes one terminal newline so the range's last line creates no extra blank row. `rangeLabel` reports the supplied range or state. `notCurrent` returns every recorded non-current entry/side plus its optional supplied reason. `languageOfPath` maps known suffixes to the existing language identifiers and otherwise uses text. No range is resolved or searched here.

## Evidence

- focusedCards.ts current behavior at this source owner. [14]
- focusedCards.ts current behavior at this source owner. [15]
