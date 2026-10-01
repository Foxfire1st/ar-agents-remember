# dashboard/src/panels/file-viewer/ — File Viewer Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/file-viewer/`              |

## Governing Overview

[dashboard/src/panels overview](../overview.md)

## 260928-MIK-L34 A Code Pane Can Carry Marks On Its File Lines

`MIK-R34` adds one module and one optional prop to this route, for the reviewer's per-hunk intent markers, all inert
for the File Viewer. [`markGutter.tsx`](markGutter.tsx.md) (new, carded, governed here, with its test
[`markGutter.test.tsx`](markGutter.test.tsx.md), 15 cases) is a CodeMirror gutter whose markers are React content
portalled into hosts the pane owns, placed on the pane's own file line numbers: `useMarkedPane(marks)` gives a pane
the gutter per editor, the portals, `placement` (rebuild only when a mark moves) and `drawn`, which exposes the marks
to assistive technology, expands a collapsed run of unchanged lines that holds a mark (ruling 2026-09-30T16:19:34 Q4),
and reveals a returned-to mark with focus on it. The reveal's hold keeps the mark focused and in view while CodeMirror
settles and ends at the reader's first pointer, key or wheel, at focus moved elsewhere, at teardown, or after 45
frames (review R2-F1, R3-F1, R3-F2). Below 40rem the gutter is sized to each mark's compact text (review R1 F2).
[`FilePane.tsx`](FilePane.tsx.md) gains `marks` (the `"all"` gutter first in its extensions, `drawn` after the build
and at teardown, the portals after its host); `changeset/DiffPane.tsx` takes the same prop per editor. Which line a
mark sits on is always the caller's decision. The File Viewer passes no marks and renders exactly as before.

- The marks gutter a pane hosts: portals, placement, the gutter per editor and `drawn`. [1]
- The bounded, passive hold released by the reader's pointer, key or wheel. [2]
- The code pane's optional marks. [3]

## 260928-MIK-L31 The Code Pane Can Show An Excerpt With Its File's Line Numbers

`MIK-R31` adds one module and two optional props to this route, for the reviewer's focused expression cards, all
inert for the File Viewer. [`lineNumbering.ts`](lineNumbering.ts.md) (new, carded, governed here) exports
`numberedFrom(first)`: the plain `lineNumbers()` for line 1, otherwise a gutter that prints the file's own line
numbers for an excerpt starting at `first`. [`FilePane.tsx`](FilePane.tsx.md) gains `firstLine` (default 1) and
`fit` (a content-sized host capped at `32rem`); `changeset/DiffPane.tsx` uses the same gutter per side. The File
Viewer passes neither prop and renders exactly as before.

- The excerpt gutter. [4]
- The code pane's optional first line and content-sized host. [5]

## Purpose

`file-viewer/` is the **File Viewer** centre tab (operations-integration slice L2): a general-purpose,
read-only browser for code + paired onboarding across repositories and worktree enclosures. It is the
first consumer of the L1 read-only files API (`GET /api/files/{repos,list,read,onboarding}`, served by
`serving/files.py`) and the home of the reusable dual-pane the Change-Set Viewer (L4) will reuse. It is a
full-bleed view that is **kept mounted** across tab switches (the Chats pattern), so its repo/scope
selection, open file, and expanded tree state survive a switch instead of resetting.

## Route Model

- `FileViewer.tsx` — the page. A repository selector + a mainline/enclosure scope selector (React Aria
  `Select`, fed by `/api/files/repos`) drive two Headless Tree explorers — a **code** tree and an
  **onboarding** tree — over the files API; the right side is the reusable `DualPane`. Pairing is
  **bidirectional**: opening a code file derives its sidecar (forward `/api/files/onboarding`), opening a
  sidecar opens its partner code file (reverse) or — for a partnerless overview/onboarding doc — renders
  that doc's **own markdown full-pane** so the prose is readable (falling back to an overview placeholder
  only when its body is unreadable). View-mode (split/single) persists across file switches via
  `usePersistedFlag`.
- `FileTree.tsx` — renders one Headless Tree (code or onboarding) as indented buttons. The library owns
  async loading, keyboard nav, and selection; the click handler selects, toggles folders, and opens files
  (its own `onClick` overrides the library's so a folder never double-toggles).
- `useFilesTree.ts` — the `@headless-tree/react` `asyncDataLoaderFeature` adapter: one tree per side,
  rooted at `{repo, scope}` (changing `rootItemId` re-roots it). `getChildren` calls `/api/files/list`
  (one call returns both `code[]` and `onboarding[]`) and caches each entry for `getItem`. Features:
  `asyncDataLoaderFeature` + `selectionFeature` + `hotkeysCoreFeature`.
- `DualPane.tsx` — single | split (code **left**, sidecar **right**) via `react-resizable-panels`
  (persisted sizes). The markdown sidecar reuses `grammar/Markdown`. Before anything is opened it fills the
  whole pane with a faint, effects-gated **siege-tank boomerang backdrop** (`EmptyStateBackdrop`,
  `/assets/sc2-siege-tank-boomerang.mp4`, `opacity 0.18`) instead of per-side placeholders; a **partnerless
  overview** (markdown, no code) renders its markdown **full-pane**. A missing partner / binary /
  overview-without-body still renders a **stable-size** placeholder (no flip-flop).
- `FilePane.tsx` — the reusable read-only CodeMirror 6 pane (read-only + non-editable, line numbers,
  language lazily imported by extension, the podracer theme). L4 reuses it via `@codemirror/merge`. Since MIK-L31
  it takes an optional `firstLine` and `fit` for an excerpt (the reviewer's cards).
- `lineNumbering.ts` — `numberedFrom(first)`, the gutter `FilePane` and `changeset/DiffPane` share, so an excerpt
  keeps its file's line numbers (MIK-L31).
- `codemirrorTheme.ts` — maps the podracer OKLCH tokens (`styles/tokens.css` vars) onto CodeMirror via
  `EditorView.theme` + a `HighlightStyle`.
- `langByExtension.ts` — lazily maps the L1 `language` id to a `@codemirror/lang-*` extension
  (js/ts/jsx/tsx/python/json/css/html/markdown); unknown/binary → plain text.
- `usePersistedFlag.ts` — a `localStorage`-backed boolean `useState` (the `calm-cockpit` pattern) for
  view-mode persistence; also exports its numeric sibling `usePersistedNumber` (used by the Cockpit
  resizable rails to persist their pixel widths).

## Invariants And Boundaries

- Read-only over the L1 files API; no new serving endpoints. No store mutation — the File Viewer owns its
  own component state, fed by the `data/files.ts` client.
- Panda CSS owns looks, React Aria owns behaviour (the selectors are React Aria `Select`); no CSS
  animation (GSAP/Motion only — master invariant).
- Kept mounted (hidden) across tab switches so state survives; full-bleed (drops the rails) like the
  Engine Room / Topology / Chats views.

## Hot Path Summary

The File Viewer tab: repo/scope selectors → two Headless Tree explorers (code + onboarding) over the L1
files API → a read-only CodeMirror dual-pane with bidirectional code↔onboarding pairing — opened
overview/onboarding docs render as markdown full-pane, and a faint siege-tank backdrop fills the pane until
a file is selected; kept mounted so state survives a tab switch.

## Evidence

### Repo-Internal References

- The L1 read-only files API this view consumes. [6]
- The same-origin client wrapping that API. [7]
- The shell that registers + keeps this view mounted. [8]
- The markdown renderer the sidecar pane reuses. [9]

## Current L5I Route State

The mounted-hidden File Viewer does not fetch its repository catalog at dashboard boot. It waits for
its first selected view, retains that settled result across later visibility changes, and shares an
in-flight read during development effect replay.
