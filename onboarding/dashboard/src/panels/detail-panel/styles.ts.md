# dashboard/src/panels/detail-panel/styles.ts

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The Panda CSS recipes of the DetailPanel, extracted from `DetailPanel.tsx` by the
260731-EFA-L8 split. Owns sizing, the phase stepper, state badges, series/sub-task
slice list, cross-master button, breadcrumb, worktree spine lanes, and reader
typography.

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
