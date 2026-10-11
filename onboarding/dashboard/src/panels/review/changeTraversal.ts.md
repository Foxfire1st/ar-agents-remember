# dashboard/src/panels/review/changeTraversal.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Next and previous real change in the outline tree of the intent reviewer. Stops are the shown tree rows whose primary change is neither `unknown` nor `unchanged`. `j` and `k` remain the keymap owner's `review.nextChange` and `review.previousChange` chords, bound on the reviewer's own zone.

Move to the next and previous real change in the shown outline tree (MIK-R86). The stops are the tree's own rendered rows in displayed order; `unknown` and `unchanged` rows are not stops. At either end the selection stays and a polite message says so.
## Code Commentary

### The walk over the rendered tree

- **Items (`itemsOf`).** Every `[data-tree-node]` under the displayed family list, with its occurrence and stop flag. A row stops only when `data-change-primary` is defined and is neither `unknown` nor `unchanged`. No roster continuation is enumerated.
- **Where the reader is (`positionOf`).** The focused tree control, else the node marked `aria-current`.
- **Forward (`forward`).** The next real-change stop of another shown occurrence. The complete outline supplies navigation rows independently of roster paging, so traversal has no partial-family continuation outcome and loads no page.
- **Backward (`backward`).** The previous stop of another occurrence, landing on that occurrence's first row. Continuation controls are not backward stops.
- **Messages (`outcomeMessage`).** At an end: "No later change in this tree; the selection stays." or "No earlier change in this tree; the selection stays." There is no continuation message.
- Because the stops are rendered nodes, a family hidden by the tree's filter is never visited.

### The hook

`useChangeTraversal(tree, enabled, rows)` returns `move` and `status`.

- **A move.** `move` computes the next stop from where the reader is. At an end it scrolls the selected node into view (`scrollIntoView({ block: 'center' })`), so the status in the sticky triage bar is read where the selection is. Otherwise it focuses the stop first and, for a tree node, clicks it. A key step, the visible previous and next controls and a click on the row are therefore one and the same selection, and the selection's answer returns focus to the node the reader moved to.
- **The status (`useStatusFor`).** `status` is the polite message of the last move; it is empty after a move that selected a node. The caller's `rows` key contains order, view and the displayed family/selector/badge sequence, not returned roster-member counts. Status is exposed only beside that same committed key; a layout effect drops it when the key changes, so returning to the old rows does not resurrect a message. A new move can produce its own message. No state is updated during render, and repeating the same message for the same key changes no state. Filtering, order/view changes or an answer invalidate the message only when they change this displayed key; central roster pagination is not itself a traversal stop or an unconditional status reset.
- **Binding.** When `enabled`, the effective keymap's binding of each traversal command is bound with tinykeys on the enclosing `[data-kbzone="review"]` element, which is the root of `ReviewSurface`. Each handler acts only when the target's zone is one of the binding's zones and the keymap owner's `routeKey` answers `handle`; then it prevents the default and moves. The keys therefore act only while focus is inside the reviewer and are inert where the owner's routing makes them so, in inputs, textareas and contenteditable regions. A rebinding in the keymap applies here.

### Conventions

Pure DOM helpers plus two hooks: the private `useStatusFor` and the exported `useChangeTraversal`. Exports: the types `TraversalDirection` and `TraversalOutcome`, `REVIEW_ZONE_SELECTOR`, `nextChange`, `outcomeMessage` and `useChangeTraversal`.

### Boundaries

- The traversal walks rendered nodes only and never activates a continuation control, so it loads no page.
- It makes no request itself: a move is a focus and a click.

## Evidence

- The module enumerates shown real-change rows, excludes unknown/unchanged and retains end messages/keymap ownership without roster stops. [11]
- Items, their occurrence and whether each stops. [12]
- Where the reader is. [13]
- The forward walk selects the next shown real-change occurrence, or returns end; no continuation control is a traversal stop. [14]
- The backward walk, which lands on an occurrence's first row and skips continuation controls. [15]
- The next stop and the polite messages. [16]
- The status is kept with the rows it was said for, given out only beside those rows, and dropped in the commit that shows other rows. [17]
- A move (focus, then click; an end scrolls the selection into view) and the zone binding through the keymap owner. [18]
- The reviewer's zone on the surface root. [19]
- The tree keys traversal status by order, view and each shown row's family, selector and badge. [20]
- The hook's own case: no render shows a status beside other rows, and it does not come back with the same rows. [21]
- Historical pre-outline held-answer cases sampled one, three and five further presses; that removed block is not current compact-outline proof. Its original reference is preserved in the task repair custody.
- Rendered-row stops excluding unknown and unchanged [23]
- Forward and backward steps over occurrences [25]
- Stayed-selection messages at either end [26]
