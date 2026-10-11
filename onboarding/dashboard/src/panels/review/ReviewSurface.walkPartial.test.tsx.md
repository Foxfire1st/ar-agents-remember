# dashboard/src/panels/review/ReviewSurface.walkPartial.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

A kept family whose members are not all returned, on a real partial answer (requirement MIK-R39 rules 8 and 11). The real route was asked for the shared member INV-2TQGXFAX with its own `pageSize=2`, so both of its families return two members per side (`walkReal.INV-2TQGXFAX-page2`, and the continued page `walkReal.FAM-R6R095RW-continued`; the receipt's `partial_round` note). `ReviewSurface` is the real component and only `fetch` is stubbed. 2 cases.

Partial reads in the walked tree: outline rows stay complete while family continuation lives in the main page, and the No earlier change message drops when the order control lists another family before the selection.
## Code Commentary

### Serving

The file uses the real-data world of `walk.test-utils.tsx` (`installWorld`) and, before each test, replaces its answer: a review request with a `continuation` parameter gets the continued page, and the shared member's review is the paged body.

### Case 1: complete outline rows with main-page continuation

- The synthetic outline retains all 24 distinct member subjects of the kept first family while the immutable review facts are paged. No tree roster-next control is mounted.
- Selecting that family opens its centre; clicking the centre's continuation sends one family review request with the exact published cursor. The outline still has 24 subjects, and the other family becomes kept.
- No current assertion sends J to a sidebar continuation stop or focuses a tree continuation control.

### Case 2: the order control changes the rows a message was said for

- The filter first shows only the second family; K reports No earlier change with no request.
- Clearing that filter and switching to authored order restores both complete outline families, clears the old message and lets K select a row of the first family.

The paged fixture serves a continued family with its cursor, asserting complete outline rows, member occurrences and the kept mark beside the main-page continuation control with its cursor. The order case flips to authored order after filtering, asserting the end message clears and k reaches the earlier member.
## Evidence

- The file's statement of its data. [5]
- The paged body and the continued page replace the world's answers. [6]
- "No earlier change" is dropped when the order control lists the other family before the selection. [8]
- The receipt of the two partial bodies. [9]
- Continued-page fixture for the partial family [10]
- Held previous world for the partial journey [11]
- Main-page continuation control with its cursor [12]
- Continuation request carrying family and cursor [13]

- A partial family keeps all 24 synthetic-outline rows; continuation is a main-page control that sends the unchanged family cursor in one review read. [7]
