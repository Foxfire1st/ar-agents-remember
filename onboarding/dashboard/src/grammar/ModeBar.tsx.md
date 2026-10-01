# dashboard/src/grammar/ModeBar.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`ModeBar` is the viewport switcher (the bottom mode bar) — the first slice-5d React Aria primitive.
A generic single-select group `<ModeBar items value onChange label>` over a `{id,label}[]`.

## Code Commentary

### Logic

Wraps React Aria `ToggleButtonGroup` (`selectionMode="single"`, `disallowEmptySelection`,
`selectedKeys={[value]}`) + a `ToggleButton` per item. `onSelectionChange` reads the single key from
the Set and calls `onChange`. The bar + buttons are Panda `css()`; the active look comes from the
`_selected` condition (matches React Aria's `data-selected`) and `_focusVisible` gives a keyboard-only
amber ring — visually identical to the old `.modebar button.is-active`.

### Conventions

Generic over `<T extends string>` so the view union flows through. React Aria renders single-select
toggle groups as `role="radiogroup"` + `role="radio"` (correct "pick one view" semantics).

### Invariants And Boundaries

Behavior + a11y are React Aria's; the look is Panda's. Keyboard arrow-nav + roving focus come for
free. (A full `Tabs`/`TabPanel` wiring with `aria-controls` to the viewport is a later option.)

## Evidence

### Repo-Internal References

- The cockpit shell consumes `ModeBar` for the view switcher. [1]
- The React Aria condition reconciliation it relies on. [2]
