# dashboard/src/panels/review/ReviewKeys.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Reviewer key reference.

## Code Commentary

Render a visible Keys button and controlled react-aria Popover/Dialog. A document keydown listener opens help only for an unmodified, noncomposing question-mark key; an explicit other zone or keymap passthrough/text-editable target prevents it. The dialog lists only effective bindings whose zones include review and obtains labels from COMMANDS, so preference changes are reflected. Listener cleanup occurs on unmount; max-height scrolling keeps the reference bounded. This is help, not traversal command execution.

## Invariants And Boundaries

This is the inspected source contract, not an execution certificate. Parent and direct callers retain authority for identity, reads and state.

## Evidence

- Reviewer key reference: `isHelpKey` owns the described branch. [1]
- Reviewer key reference: `ReviewKeys` owns the described branch. [2]

