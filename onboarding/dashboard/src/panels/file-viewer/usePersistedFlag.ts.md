# dashboard/src/panels/file-viewer/usePersistedFlag.ts

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

A boolean `useState` backed by `localStorage` — the same calm-cockpit pattern `Cockpit.tsx` uses — so a
view-mode choice (split/single) survives both a page reload and a file switch, because the value lives
outside the file-scoped component state. Exports `usePersistedFlag` and its numeric sibling
`usePersistedNumber` (used by the Cockpit resizable rails to persist their pixel widths).

## Code Commentary

### Logic

`usePersistedFlag(key, fallback)` returns `[boolean, (next: boolean) => void]`. The lazy `useState`
initializer reads `window.localStorage.getItem(key)`: it is SSR-safe (`typeof window === "undefined"` →
`fallback`), values are stored as `"1"`/`"0"`, and an unset (null) key falls back. The memoized `set`
callback (keyed on `key`) updates React state and writes `"1"`/`"0"` back to `localStorage`, behind the
same `window` guard.

`usePersistedNumber(key, fallback)` returns `[number, (next: number) => void]` — the numeric sibling. Its
lazy initializer is SSR-safe the same way, parses the stored string via `Number`, and falls back when the
result is non-finite (`!Number.isFinite`) so a corrupt key never poisons the layout with `NaN`. The
memoized `set` writes `String(next)` back to `localStorage` behind the `window` guard. The cockpit's
resizable rails persist their pixel widths through this (keys `cockpit.rail-left-w` / `cockpit.rail-right-w`).

### Invariants And Boundaries

`usePersistedFlag` is boolean only — values serialize as exactly `"1"`/`"0"`, and any other stored string
reads as `false`. `usePersistedNumber` is finite-number only — a non-finite parse falls back rather than
storing/returning `NaN`. Both are SSR/jsdom safe: without `window`, their lazy initializers return the
fallback and their setters still update React state while skipping only the `localStorage` write. Keys
are caller-owned and global to the origin (e.g. `fileviewer.split`,
`cockpit.rail-left-w`); two callers sharing a key share persisted state.

## Evidence

### Repo-Internal References

- `FileViewer` persists its split/single toggle through this hook. [1]
- `Cockpit` persists its left/right rail pixel widths via `usePersistedNumber`. [2]
- The calm-cockpit `localStorage` flag pattern this mirrors. [3]
