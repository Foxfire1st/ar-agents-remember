# dashboard/src/panels/session-cockpit/sessions-view/shell.test.tsx

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The shell/scaffold suite split from `SessionsView.test.tsx` by the 260731-EFA-L8
test split (47-name set reconciled item-for-item). Pins the scaffold structure, the
~80-col floor chip re-measure, the ~280px rail calibration, command palette, and
keyboard zones over the legacy-raw PTY.

## Code Commentary

### Logic

Uses `test-utils.tsx` seeds and a local `setClientWidth` helper to simulate panel
layout changes; asserts the floor-chip and rail calibration behavior plus palette and
keyboard-zone registration. **Since MIK-L33** the `?` keyboard-reference case also asserts the "Intent reviewer —
while focus is inside it" group with `review.nextChange` and `review.previousChange`, and that `j` pressed in the
sessions view is not handled (`fireEvent.keyDown` returns `true`: nothing prevented it), so the reviewer's chords
are inert outside the reviewer (MIK-R33 rule 7).

### Invariants And Boundaries

Assertions preserved from the monolithic suite.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The shell suite. [1]
- The `?` page lists the reviewer's chords, and `j` is unhandled in the sessions view (MIK-L33). [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
