# dashboard/src/panels/detail-panel/styles.ts

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The Panda CSS recipes of the DetailPanel, extracted from `DetailPanel.tsx` by the
260731-EFA-L8 split. Owns the detail container, step marks, breadcrumb, worktree spine and the remaining
change-set, grant and brief-state disclosure styles.
The fixed document pages and their rows now use pageStyles.ts; retired old-page recipe definitions
are not a second appearance owner.

## Code Commentary

### Logic

Static atoms are `css({...})`; `step` is a `cva` keyed on step state; `lane` is keyed on code/memory kind. All colours
go through `token(colors.*)`.

Since `260921-ICR-L47`, three classes style the brief-state disclosure the entry controls share
(`entryState.tsx`): `entryStateDetails` (inline, full-width when open), `entryStateSummary` (the bordered
`?` marker, native marker hidden) and `entryStateBody` (a bounded-width paragraph that wraps long codes).

- The three disclosure classes. [1]

### Conventions

Styles stay co-located with the panel; no animation in this domain.

### Invariants And Boundaries

The `sizing` flex rule preserves the panel's fill behavior.

### Todos

None recorded.

## Retired direct-grant action recipe

The earlier L94 page port retained `grantButton` and row-side text controls. D230 deliberately replaces that presentation: the old recipe and row hand-through are absent from current source, and the selected planning task uses the switch recipes below. That prior preservation claim remains historical in Git and the superseded L127 decision; it is not a current recipe or a current formatter/layout qualification.

## Direct execution look

The selected task uses directLine, directSwitch, directSwitchOff/directSwitchOn, directKnob, directGiven and directNote. Alignment gives the track its left/right position; the old grantButton recipe is gone. These styles present served UI state and do not decide permission or grant admission. Existing detail/lifecycle/change-set recipes keep their owners.

## Evidence

- The direct-execution line has one track, positional variants, knob and giver/notice text styles. [5]


### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The retained panel layout, step-mark and badge recipes. [2]

- The retained slice-container, breadcrumb and worktree-lane recipes. [3]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

- The current track-and-knob switch uses token styling; pending disables the button in the reader, not through a retained grantButton recipe. [4]

The obsolete stepper, taskHead, sliceMeta and sliceButton exports are removed; those names are not current appearance owners. Task-page-specific recipes remain in pageStyles.ts.
