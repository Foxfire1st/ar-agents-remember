# dashboard/src/panels/detail-panel/styles.ts

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The Panda CSS recipes of the DetailPanel, extracted from `DetailPanel.tsx` by the
260731-EFA-L8 split. Owns the detail container, lifecycle phase/identity chrome, breadcrumb,
master-less slice fallback, worktree spine and change-set/brief-state disclosure styles.
The fixed document pages and their rows now use pageStyles.ts; retired old-page recipe definitions
are not a second appearance owner.

## Code Commentary

### Logic

Static atoms are `css({...})`; `step` and `lane` are `cva` keyed on state. All colours
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

## Retained direct-grant action recipe

`grantButton` is the landed L94 inline action recipe, retained byte-for-byte through the page port. The control stays beside, never nested within, the drill-in link; pending requests use its disabled styling. Fixed page appearance still belongs to pageStyles.ts. The preserved double-quoted block carries the disclosed Prettier debt; this card claims source preservation, not a new layout capture or formatter pass.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The panel layout/stepper/badge recipes. [2]
- The slice/cross/spine recipes. [3]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

- The landed inline grant action recipe retains its pending-disabled treatment. [4]
