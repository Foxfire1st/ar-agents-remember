# dashboard/src/panels/review/ReviewKeys.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Expose the reviewer's effective key bindings and its two fixed sidebar keys in a keyboard-operable help popover.

## Code Commentary

The Keys control uses the existing dialog/popover components. Its list reads effective bindings admitted to the review zone and labels them through COMMANDS, then adds the fixed Tree sidebar `[` and Chat sidebar `]` keys. Those two keys are outside the rebindable keymap.

The document listener opens help for `?` without Ctrl, Alt or Meta and outside composition. It ignores another keyboard zone and the key-routing owner's passthrough/text-entry cases. The close control changes only this popover's local state; the listener is disposed on unmount.

## Evidence

- ReviewKeys.tsx current behavior at this source owner. [5]
- ReviewKeys.tsx current behavior at this source owner. [6]
