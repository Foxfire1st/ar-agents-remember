# dashboard/src/panels/file-viewer/usePersistedFlag.ts

| Field | Value |
| ---------------------- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/file-viewer/usePersistedFlag.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-29T09:06+02:00 |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a` |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview | `overview.md` |

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
storing/returning `NaN`. Both are SSR/jsdom safe: every `window` access is guarded, so the hooks no-op
without a DOM. Keys are caller-owned and global to the origin (e.g. `fileviewer.split`,
`cockpit.rail-left-w`); two callers sharing a key share persisted state.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `FileViewer` persists its split/single toggle through this hook. | L24, L157, L227 | [FileViewer.tsx](FileViewer.tsx) |
| `Cockpit` persists its left/right rail pixel widths via `usePersistedNumber`. | L33, L339-L340 | [../../cockpit/Cockpit.tsx](../../cockpit/Cockpit.tsx) |
| The calm-cockpit `localStorage` flag pattern this mirrors. | L344-L357 | [../../cockpit/Cockpit.tsx](../../cockpit/Cockpit.tsx) |

## Update History

- 2026-06-30T00:00:00+02:00 — operations-integration L5: added the exported `usePersistedNumber(key, fallback)` hook alongside `usePersistedFlag` — a `localStorage`-backed number that parses via `Number` and falls back on a non-finite value; the Cockpit resizable rails persist their pixel widths through it.
- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): the `localStorage`-backed
  boolean `useState` (the calm-cockpit pattern) that persists the File Viewer split/single view-mode
  across reloads and file switches. Verification metadata pinned to the task base until closeout stamps
  the L2 code commit.
