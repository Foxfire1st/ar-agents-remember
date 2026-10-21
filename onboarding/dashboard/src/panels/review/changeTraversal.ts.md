# dashboard/src/panels/review/changeTraversal.ts

## Governing Overview

[review route overview](overview.md)

## Purpose

Choose next and previous comparison-bound reading blocks in the shared displayed order, and bind the effective review traversal keys to that selection.

## Code Commentary

`blockStops` places each family/subject heading around its drawn changed blocks; shared-region aliases name one stop, and later subject occurrences have selection places without duplicate blocks. Closed unchanged/not-comparable groups provide places but no block stops. `laneStops` appends the lane and its files/hunks in supplied display order, retaining a place for an unread file.

`nextStop` resolves the selection at its exact block/alias or shown place. A lane hunk/file without its own place falls immediately before that file's first hunk, or at the lane if none is read; an otherwise unshown selection sits before the column's stops. With nothing selected either direction selects the first block. At an end it leaves selection unchanged and returns the explicit no-earlier/later-block message.

`useStatusFor` stores status with the shown block-key sequence, hides it immediately for another sequence and clears it at commit so it cannot reappear when old stops return. Repeating the same status for the same key is a no-op. `useBlockTraversal` uses the keymap owner's effective next/previous commands, handling only the review zone or an unfocused body/document and respecting routeKey text/modifier guards. It calls only onSelect for a selected block; URL changes and scrolling remain page owners. Disabled traversal binds no keys.

## Evidence

- changeTraversal.ts current behavior at this source owner. [32]
- changeTraversal.ts current behavior at this source owner. [33]
- changeTraversal.ts current behavior at this source owner. [34]
- changeTraversal.ts current behavior at this source owner. [35]
