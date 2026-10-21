# dashboard/src/tray/AddToTray.test.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks quiet object controls in nested subject/block and file/hunk hosts.

## Code Commentary

### Logic

Replays top-level selector splitting and specificity to assert idle invisibility, own hover/focus exposure, sibling quietness and persistent in-tray checkmark.

A small CSS selector/cascade interpreter translates hover/focus-within to test attributes because jsdom does not implement the browser cascade.

### Invariants And Boundaries

Logic/selector evidence only; real browser hover and focus geometry require the separately supplied browser evidence.

## Evidence

- Checks quiet object controls in nested subject/block and file/hunk hosts. [1]
