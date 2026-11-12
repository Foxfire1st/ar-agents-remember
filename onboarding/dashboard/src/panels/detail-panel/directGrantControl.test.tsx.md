# dashboard/src/panels/detail-panel/directGrantControl.test.tsx

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

Pins the one planning-task switch and the absence of grant controls and marks from master rows.

## Contract

The tests distinguish off/on planning switches, giver words, granted non-planning bare words and grantless absence; reject master-row controls and marks; assert the existing give route body, pending-position retention and refusal notice; retain the actual grant after a refused revoke; and exercise live projection changes. The selected-task isolation case now establishes a granted leaf and its refusal notice, selects a different planning leaf, and checks that the second switch is off with no first-leaf giver or notice. It witnesses document-transition reset; this case does not itself defer a reply across the transition. Mocked responses are UI witnesses, not store mutations or live-host qualification.

## Evidence


- The mounted suite asserts switch state, row absence, canonical route and refusal/pending behavior. [1]
