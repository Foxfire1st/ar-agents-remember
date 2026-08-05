# dashboard/src/grammar/ModeBar.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/ModeBar.tsx`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-15T17:00                                 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The cockpit shell consumes `ModeBar` for the view switcher. | "Views" | dashboard/src/cockpit/Cockpit.tsx:654-654 |
| The React Aria condition reconciliation it relies on. | `_selected` | dashboard/panda.config.ts:18-18 |

## Update History

- 2026-08-03T02:32:19+02:00 — Curator W3-B02: anchored 2 Repo-Internal citation rows with exact
  current React/Panda source anchors and repository-relative paths; verification metadata unchanged.

- 2026-06-15T17:00 — Created for slice 5d: React Aria `ToggleButtonGroup` mode bar styled by Panda.
  Verification metadata pinned until closeout stamps the 5d code commit.
