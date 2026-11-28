# dashboard/src/panels/review/focusedCards.ts

## Governing Overview

[review route overview](overview.md)

## Purpose

Provide the source block's recorded voice, line/range labels, non-current entry marks and highlighting language to the shared card renderer.

## Code Commentary

`ExpressionCard` carries kind/path/change, both supplied sides and every drawn entry. `cardVoice` chooses the recorded after side, otherwise before, retaining its authored role/rationale or proof facet. An absent realization rationale stays missing. When both sides record the entry and the after-side authored value differs, revised holds the earlier value.

`firstLines` retains each excerpt's file numbering with one only when unrecorded. `drawnText` removes one terminal newline so the range's last line creates no extra blank row. `rangeLabel` reports the supplied range or state. `notCurrent` returns every recorded non-current entry/side plus its optional supplied reason. Language and syntax highlights are now supplied directly by the backend on `ReviewTreeEntrySide` rather than inferred by a client suffix map (`languageOfPath` was removed). No range is resolved or searched here.

## Evidence

- Declares `ExpressionCard`, `CardVoice`, and `cardVoice` choosing recorded side rationale/facet and revisions. [14]
- Exports `firstLines`, `drawnText`, `rangeLabel`, and `notCurrent` for excerpt numbering and non-current entry marks. [15]
