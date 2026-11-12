# dashboard/src/tray/selectionOffer.test.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks that dashboard highlight offers and explicit clicks collect while selection/copy survive.

## Code Commentary

### Logic

Mouseup shows offer without adding; mousedown prevents selection loss; click retains panel provenance; preference gates copy; editable text is excluded; opening tray preserves highlight; static scan rejects production removeAllRanges callers.

Native jsdom Selection plus mocked execCommand and empty seat-list fetch.

### Invariants And Boundaries

No real clipboard or layout; test setup intentionally clears selections and is excluded from the production-source scan.

## Evidence

- Checks that dashboard highlight offers and explicit clicks collect while selection/copy survive. [1]
- Checks that dashboard highlight offers and explicit clicks collect while selection/copy survive. [2]
- Checks that dashboard highlight offers and explicit clicks collect while selection/copy survive. [3]
- Checks that dashboard highlight offers and explicit clicks collect while selection/copy survive. [4]
