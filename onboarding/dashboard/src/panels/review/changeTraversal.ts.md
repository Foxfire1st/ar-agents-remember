# dashboard/src/panels/review/changeTraversal.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**Next and previous change in the family tree (MIK-R33, ICR-R32@v1 rules 6 and 7).** The stops are the tree's own
rendered nodes in displayed order whose primary badge is not `unchanged` (so `unknown` is visited, and a filter's hidden
families are never visited); `j`/`k` are the keymap owner's `review.nextChange`/`review.previousChange` chords, bound on
the reviewer's own zone.

## Code Commentary

### Logic

- **Items (`itemsOf`).** Every `[data-tree-node]` and every roster continuation control (`review-family-roster-next`)
  under the family list, with its family, its occurrence (`data-occurrence`: a revised member's two rows are one stop)
  and whether it stops: a node with a `data-change-primary` other than `unchanged`, or a continuation control of a
  family with `data-members-unreturned`.
- **Where the reader is (`positionOf`).** The focused tree control, else the selected (`aria-current`) node.
- **Forward (`forward`, `stopsForward`).** The next stop of another occurrence; past the returned members of a partial
  family it stops at that family's continuation control (focus moves there, the message says further members are not
  yet returned), and the next `j` moves on. It never activates the continuation, so no page is loaded.
- **Backward (`backward`).** The previous stop of another occurrence, landing on that occurrence's first row
  (review R1 mutation R-C5); continuation controls are not backward stops.
- **Ends (`outcomeMessage`).** "No later change in this tree; the selection stays." / "No earlier change…". At an end
  the selection is scrolled into view (`scrollIntoView({block: 'center'})`), so the sticky bar's status and the
  selection are on screen together (ruling 16:22:22 item 9).
- **A move (`useChangeTraversal`).** Focus first, then `click()` the node, so the selection's answer returns focus to
  the node moved to, keeping family context, focus and the mounted workspace (ICR-R24@v3). On the narrow route the
  selection reveals the centre through the workspace's existing `revealCenter`, exactly as a tap does (ruling
  2026-09-30T21:41:02: kept, no change here).
- **Binding.** For each traversal command the effective keymap's binding is bound with tinykeys on the enclosing
  `[data-kbzone="review"]` element (`ReviewSurface`'s root); each handler checks the target's zone is one of the
  binding's zones and `routeKey` says `handle`, so the keys are inert in inputs, textareas, selects, contenteditable
  regions and the PTY zone, and act only while focus is inside the reviewer. A rebinding applies here and in the
  labels. The zone handler also acts from a returned marker outside the tree; L34's hold ends on a document-capture
  `keydown` first (the merge round).

### Conventions

Pure DOM helpers plus one hook; `REVIEW_ZONE_SELECTOR` is exported; 164 lines.

### Invariants And Boundaries

- Traversal never forces unreturned pages to load: it walks rendered nodes only and stops at, never activates, a
  continuation control (part of the candidate invariant recorded on `changeTriage.ts.md`).
- `j`/`k` never act outside the reviewer or in text fields and the terminal zone (rule 7), through the keymap owner's
  own routing contract.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's statement: stops, ends, the partial-family stop and the keymap binding. [1]
- Items, their occurrence and whether each stops. [2]
- Where the reader is, and the forward and backward walks. [3]
- The next stop and the polite messages. [4]
- A move (focus, then select; an end scrolls the selection into view) and the zone binding through the keymap owner. [5]
- The reviewer's zone on the surface root. [6]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
