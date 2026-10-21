# dashboard/src/data/keymap/chords.ts

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

The review traversal chord table is data, not an installer: `REVIEW_CHORDS` contains `J`/`K` with labels `j`/`k`, command IDs `review.nextChange`/`review.previousChange`, and `review` zones only. No CHROME_CHORDS, COMPOSER_CHORDS, palette, session navigation, focus-cycle or interrupt chord is exported here.

## Code Commentary

### Logic

`ZoneChord` has tinykeys `chord`, a human label beside the control, `commandId` and readonly `zones`. Membership determines where a binding can handle an event; other zones pass it through. The reviewer reads effective preferences and installs traversal on its own review container. Preferences use this table as their sole defaults.

### Invariants And Boundaries

Printable bindings never consume plain typing in editable targets: `routeKey` implements that generic rule, not a per-chord printable flag. Browser-forbidden chords cannot be accepted as overrides. Review traversal is handled by its own zone binding rather than requiring new command-registry entries. This module does not install a binding or prove a browser effect; no removed keyboard-reference or PTY consumer is implied.

### Historical MIK-L33 observation

This retained observation predates the baseline: `commands.ts` already registers both IDs on both sides of this leaf. Its suggested registry work is not current work.

> - **MIK-L33 observation for the keymap owner:** the two review chords are dispatched outside the command registry
  (see the invariant above). If the rule that every chord's id is a registered command should hold without
  exception, the reviewer's traversal needs registry entries; nothing asserts it today.

The review page now interprets these stable j/k command IDs as next/previous reading-column blocks by block identity. This module still supplies data only; traversal and editable-target guards remain with their owners. [5]

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The reviewer binds them itself on its zone from the effective keymap. [6]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

- ZoneChord carries chord/label/commandId/zones, and REVIEW_CHORDS supplies only review j/k traversal. [1]
- The reviewer's `j`/`k` table, `review` zone only (MIK-L33). [5]
