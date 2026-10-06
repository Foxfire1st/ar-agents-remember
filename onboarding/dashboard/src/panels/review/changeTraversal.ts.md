# dashboard/src/panels/review/changeTraversal.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Next and previous change in the family tree of the intent reviewer (requirements MIK-R33 and MIK-R39 rule 11). The stops are the tree's own rendered nodes, in displayed order, whose primary change kind is not `unchanged`. `j` and `k` are the keymap owner's `review.nextChange` and `review.previousChange` chords, bound on the reviewer's own zone.

## Code Commentary

### The walk over the rendered tree

- **Items (`itemsOf`).** Every `[data-tree-node]` and every roster continuation control (`review-family-roster-next`) under the family list, with its family, its occurrence (`data-occurrence`; the two revision rows of one revised member are one stop) and whether it stops. A node stops when its `data-change-primary` is set and is not `unchanged`, so `unknown` is visited. A continuation control stops when its family is marked `data-members-unreturned`.
- **Where the reader is (`positionOf`).** The focused tree control, else the node marked `aria-current`.
- **Forward (`forward`, `stopsForward`).** The next stop of another occurrence. Past the returned members of a family with unreturned members it is that family's continuation control; from one of a family's controls the walk moves on. A continuation control is only focused, never activated, so no page is loaded.
- **Backward (`backward`).** The previous stop of another occurrence, landing on that occurrence's first row. Continuation controls are not backward stops.
- **Messages (`outcomeMessage`).** At a continuation control: "Further members of … are not yet returned; continue its roster walk to reach them, or press next again to move on." At an end: "No later change in this tree; the selection stays." or "No earlier change in this tree; the selection stays."
- Because the stops are rendered nodes, a family hidden by the tree's filter is never visited.

### The hook

`useChangeTraversal(tree, enabled, rows)` returns `move` and `status`.

- **A move.** `move` computes the next stop from where the reader is. At an end it scrolls the selected node into view (`scrollIntoView({ block: 'center' })`), so the status in the sticky triage bar is read where the selection is. Otherwise it focuses the stop first and, for a tree node, clicks it. A key step, the visible previous and next controls and a click on the row are therefore one and the same selection, and the selection's answer returns focus to the node the reader moved to.
- **The status (`useStatusFor`).** `status` is the polite message of the last move; it is empty after a move that selected a node. `rows` is a string from the caller that names what the tree shows: its rows and their order. The status is stored together with the rows the committed tree showed when the move was made, and a render gives it out only while `rows` is that same string. In the commit that shows other rows a layout effect drops the stored status, so the message does not come back when the tree later shows the same rows again; a new move gets its own message. No state is updated while rendering, and saying the same status again for the same rows changes no state, so a key held at an end renders nothing. A held `j` can outrun the answer that brings the next family; "No later change in this tree" then does not stay beside the later change that answer shows. The same holds when a filter hides or shows a family, when the order control changes the order and when a roster continuation returns members, because each of these changes `rows`.
- **Binding.** When `enabled`, the effective keymap's binding of each traversal command is bound with tinykeys on the enclosing `[data-kbzone="review"]` element, which is the root of `ReviewSurface`. Each handler acts only when the target's zone is one of the binding's zones and the keymap owner's `routeKey` answers `handle`; then it prevents the default and moves. The keys therefore act only while focus is inside the reviewer and are inert where the owner's routing makes them so, in inputs, textareas and contenteditable regions. A rebinding in the keymap applies here.

### Conventions

Pure DOM helpers plus two hooks: the private `useStatusFor` and the exported `useChangeTraversal`. Exports: the types `TraversalDirection` and `TraversalOutcome`, `REVIEW_ZONE_SELECTOR`, `nextChange`, `outcomeMessage` and `useChangeTraversal`. The file is 192 lines.

### Boundaries

- The traversal walks rendered nodes only and never activates a continuation control, so it loads no page.
- It makes no request itself: a move is a focus and a click.

## Evidence

- The module's statement: stops, ends, the partial-family stop and the keymap binding. [11]
- Items, their occurrence and whether each stops. [12]
- Where the reader is. [13]
- The forward walk and its stop at a family's continuation control. [14]
- The backward walk, which lands on an occurrence's first row and skips continuation controls. [15]
- The next stop and the polite messages. [16]
- The status is kept with the rows it was said for, given out only beside those rows, and dropped in the commit that shows other rows. [17]
- A move (focus, then click; an end scrolls the selection into view) and the zone binding through the keymap owner. [18]
- The reviewer's zone on the surface root. [19]
- The tree passes the rows it shows: the order and each shown family with its member-row count. [20]
- The hook's own case: no render shows a status beside other rows, and it does not come back with the same rows. [21]
- The mounted cases of a status dropped when a held answer brings a later change, for one, three and five further presses. [22]
