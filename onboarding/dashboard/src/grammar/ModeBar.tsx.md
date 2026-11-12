# dashboard/src/grammar/ModeBar.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`ModeBar` is the viewport switcher (the bottom mode bar) — the first slice-5d React Aria primitive.
A generic single-select group `<ModeBar items value onChange label>` over a `{id,label}[]`. MIK-R79
narrows the product bar to Chats, Operations, Knowledge and File Viewer. At 40rem and narrower,
the local style now allows wrapping and sets minWidth zero while retaining the reduced spacing.

## Code Commentary

### Logic

Wraps React Aria `ToggleButtonGroup` (`selectionMode="single"`, `disallowEmptySelection`,
`selectedKeys={[value]}`) + a `ToggleButton` per item. `onSelectionChange` reads the single key from
the Set and calls `onChange`. The bar uses local Panda `css()`; its buttons import `viewTabButton`
from `viewTabLook.ts`, the one definition shared with launcher selectors, chips and buttons. The
shared class declares an amber selected look and an amber `_focusVisible` outline. The 40rem media
query adds flexWrap wrap and minWidth zero, retaining the reduced gap and button padding and zero
button letter-spacing. These source declarations do not establish a rendered fit or keyboard result.

### Conventions

Generic over `<T extends string>` so the view union flows through the props. The component configures
single selection, disallows empty selection and supplies an aria-label. The frozen application source
does not establish the dependency's emitted roles or keyboard-navigation behavior.

### Invariants And Boundaries

The component delegates selection behavior to the imported React Aria controls and supplies Panda
classes. It maps the items its caller passes: the product list is owned by `Cockpit`,
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

- The mode bar renders the caller's single-select item list using the imported shared tab class. [3]
### Cross-Repo References

No cross-repo boundary is crossed by this file.

- The local style preserves flex display, flexShrink zero, base gap, top border and padding. Its max-width 40rem rule newly sets flexWrap wrap and minWidth zero while retaining gap 0.2rem, button paddingInline 0.35rem and zero letterSpacing. No visual-fit result follows from these declarations. [4]

- Cockpit's VIEWS contains Chats, Operations, Knowledge and File Viewer in that order, and its ModeBar invocation passes that array. ModeBar itself maps caller-provided items and does not define the product list. [5]

- viewTabMetrics declares shared font, spacing, case, padding, border width and radius. viewTabButton, launcherButton, launcherSelect and launcherChip spread those metrics; the selector overrides textTransform. viewTabButton also declares the selected and focus-visible looks. This establishes shared style definitions, not identical rendered dimensions. [6]
