# dashboard/src/panels/review/ReviewSurface.triage.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

`j` in the mounted reviewer (requirement MIK-R33), over the served bodies of the store-authored comparison (`triage.family`, `triage.memberA`, `triage.memberH` and `triage.entries`; receipt `triage.capture-provenance.json`). `ReviewSurface` is the real component and only `fetch` is stubbed. 1 case.

## Code Commentary

### The case

- The reviewer opens on the family. The center's member list follows the tree's displayed order, in triage order and, after one click on the order control, in authored order; a second click returns to triage order.
- The family's row is focused and `j` is pressed. The member review of the next change is read, as a click would read it; its row is marked `aria-current` and has focus; the workspace is the same DOM node; and the family's breakdown is still on screen.
- A second `j` selects the following change, again with the mark and focus on its row and the same workspace node.

### How the case stays stable on a loaded machine

- Async conditions use the shared Testing Library guard; the Vitest configuration owns the test and hook hang guards. The case still waits for the displayed order and selection conditions rather than elapsed time.
- After each click on the order control the case waits until the control's `data-order` shows that click's order (`authored`, then `triage`), because the control computes the next order from the one it shows.
- The first `j` is pressed again until the selection moves, because the keymap's binding is a passive effect and a press made before it has run is ignored, as in a browser.

### Conventions

Vitest with Testing Library. Requests for the tree view and for source content get a typed refusal, because they are outside this check; a review request for a subject without a body throws.

## Evidence

- The suite's statement, its bounds and its stubbed reads. [3]
- The one case: the center's order in both orders with a wait after each click on the order control, the two moves, and the kept context, focus and workspace. [4]
