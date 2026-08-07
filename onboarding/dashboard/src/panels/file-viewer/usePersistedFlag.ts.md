# dashboard/src/panels/file-viewer/usePersistedFlag.ts

| Field | Value |
| ---------------------- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/file-viewer/usePersistedFlag.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-29T09:06+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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
storing/returning `NaN`. Both are SSR/jsdom safe: without `window`, their lazy initializers return the
fallback and their setters still update React state while skipping only the `localStorage` write. Keys
are caller-owned and global to the origin (e.g. `fileviewer.split`,
`cockpit.rail-left-w`); two callers sharing a key share persisted state.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `FileViewer` persists its split/single toggle through this hook. | "fileviewer.split"; "className={toggle({ on: split })} aria-pressed={split} onClick={() => setSplit(!split)}> {split ? \"▣ Split\" : \"▢ Single\"} </button>" | dashboard/src/panels/file-viewer/FileViewer.tsx:211-211; dashboard/src/panels/file-viewer/FileViewer.tsx:269-271 |
| `Cockpit` persists its left/right rail pixel widths via `usePersistedNumber`. | "cockpit.rail-left-w", "cockpit.rail-right-w" | dashboard/src/cockpit/Cockpit.tsx:431-432 |
| The calm-cockpit `localStorage` flag pattern this mirrors. | `EffectsToggle` | dashboard/src/cockpit/Cockpit.tsx:1089-1116 |

## Update History

- 2026-08-04T03:21:00+02:00 — S18-SR3-B05 curator: regenerated the assigned whole-claim bindings with the locked scoped fixer and inspected the generated extents against the approved claim; no approved semantic claim changes.
- 2026-08-04T03:03:32+02:00 — S18-SR3-B05 worker: added the split-button toggle wiring anchor and returned the whole consumer binding to provisional fixer input; approved semantics are unchanged.
- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: corrected the no-DOM boundary: setters still update React state and only storage access is skipped; rebound the FileViewer consumer claim provisionally for the aggregate fixer.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-30T00:00:00+02:00 — operations-integration L5: added the exported `usePersistedNumber(key, fallback)` hook alongside `usePersistedFlag` — a `localStorage`-backed number that parses via `Number` and falls back on a non-finite value; the Cockpit resizable rails persist their pixel widths through it.
- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): the `localStorage`-backed
  boolean `useState` (the calm-cockpit pattern) that persists the File Viewer split/single view-mode
  across reloads and file switches. Verification metadata pinned to the task base until closeout stamps
  the L2 code commit.
