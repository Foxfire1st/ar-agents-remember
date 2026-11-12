# dashboard/src/tray/TrayChip.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Shows a pick with its identity, source, removable state, image preview and editable note.

## Code Commentary

### Logic

Quick intents reveal beside the active chip and write a note; fixed placement keeps them inside the viewport and clear of the neighboring chip. Note editing explicitly focuses its input and commits or leaves edit mode with keyboard/blur. Image object URLs are revoked.

### Invariants And Boundaries

Collection itself does not take focus; explicit note editing may. The chip does not resolve references or send.

## Evidence

- Shows a pick with its identity, source, removable state, image preview and editable note. [1]
- Shows a pick with its identity, source, removable state, image preview and editable note. [2]
- Shows a pick with its identity, source, removable state, image preview and editable note. [3]
