# dashboard/src/grammar/ModeBar.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`ModeBar` is the viewport switcher (the bottom mode bar) — the first slice-5d React Aria primitive.
A generic single-select group `<ModeBar items value onChange label>` over a `{id,label}[]`. MIK-R79
narrows the product bar to Chats, Operations, Knowledge and File Viewer and adds the phone-width
spacing so all four still fit at 40rem and narrower.

## Code Commentary

### Logic

Wraps React Aria `ToggleButtonGroup` (`selectionMode="single"`, `disallowEmptySelection`,
`selectedKeys={[value]}`) + a `ToggleButton` per item. `onSelectionChange` reads the single key from
the Set and calls `onChange`. The bar + buttons are Panda `css()`; the active look comes from the
`_selected` condition (matches React Aria's `data-selected`) and `_focusVisible` gives a keyboard-only
amber ring. The 40rem media query reduces the bar gap and button padding and drops button
letter-spacing, so the four product entries fit the phone width.

### Conventions

Generic over `<T extends string>` so the view union flows through. React Aria renders single-select
toggle groups as `role="radiogroup"` + `role="radio"` (correct "pick one view" semantics).

### Invariants And Boundaries

Behavior and a11y are React Aria's; the look is Panda's. Keyboard arrow-nav and roving focus come for
free. The bar renders exactly the items its caller passes: the product list is owned by `Cockpit`,
not by this component, so a view outside the bar is not rendered here at all.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rule 16); it lives outside the code and memory repositories, so it
is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The mode bar renders the caller's single-select item list. [3]
- The phone widths keep the four product entries fitting. [4]
- The cockpit supplies the four product entries and the opening view. [5]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
