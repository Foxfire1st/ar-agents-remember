# dashboard/src/panels/file-viewer/ — File Viewer Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/file-viewer/`              |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src/panels overview](../overview.md)

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
  language lazily imported by extension, the podracer theme). L4 reuses it via `@codemirror/merge`.
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The L1 read-only files API this view consumes. | `register_files_routes` | mcp/src/agents_remember/serving/files.py:296-325 |
| The same-origin client wrapping that API. | `fetchRepos` | dashboard/src/data/files.ts:108-111 |
| The shell that registers + keeps this view mounted. | `filesLayer` | dashboard/src/cockpit/Cockpit.tsx:332-332 |
| The markdown renderer the sidecar pane reuses. | `Markdown` | dashboard/src/grammar/Markdown.tsx:98-121 |

## Current L5I Route State

The mounted-hidden File Viewer does not fetch its repository catalog at dashboard boot. It waits for
its first selected view, retains that settled result across later visibility changes, and shares an
in-flight read during development effect replay.

## Update History

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 8 citation findings (4 rows); scoped recheck clean.

- 2026-07-24T13:17:17Z — Curator: documented first-visible catalog loading and settled keep-alive
  behavior. Verification metadata remains pre-commit.

- 2026-07-17T02:30+02:00 — No route impact: 260715-FEUI-L2's only touch under file-viewer/ is a
  reviewer-accepted one-line defensive guard in `FileViewer.tsx` (a `repos`-less catalog response
  degrades to `[]` instead of crash-looping `repos.find` — a latent robustness bug the leaf's
  test-timing shift surfaced). The route model (selectors, two trees, dual-pane, pairing) is
  unchanged; detail lives in the `FileViewer.tsx` sidecar. Verification metadata pinned to the
  leaf base until closeout stamps the L2 code commit.
- 2026-07-06T03:20+02:00 — No route impact: 260703-L9 reviewed `DualPane.tsx`/`FilePane.tsx` as the sidecar-markdown precedent for the new task-reader notes view (`panels/TaskNotes.tsx`); nothing under file-viewer/ changed.
- 2026-06-30T00:00:00+02:00 — operations-integration L5: the file-viewer now (a) renders an opened partnerless overview/onboarding doc as **markdown full-pane** (`openSidecar` carries the body; `DualPane` shows it in single and split mode) instead of an empty placeholder, and (b) fills the pane with a faint, effects-gated **siege-tank empty-state backdrop** (`/assets/sc2-siege-tank-boomerang.mp4`) until a file is selected, replacing the per-side "select a file" placeholders. `usePersistedFlag.ts` also gained `usePersistedNumber` (Cockpit rail widths). New `DualPane.test.tsx` covers the backdrop + overview rendering. Detail in the `DualPane.tsx` / `FileViewer.tsx` / `usePersistedFlag.ts` sidecars. Verification metadata pinned until closeout stamps the L5 code commit.
- 2026-06-29T17:00+02:00 — No route impact: the L4 follow-up only adjusted the shared `codemirrorTheme.ts` comment + operators/punctuation colours (readability — `--grid` → an `ink`/`bg` blend); the file-viewer route model (the selectors, the two trees, the dual-pane, the read-only CodeMirror) is unchanged. Detail in the `codemirrorTheme.ts` sidecar. Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T09:06+02:00 — Created for operations-integration L2: the File Viewer route — a full-bleed
  centre tab over the L1 files API with repo/scope selectors, a code tree + an onboarding tree (Headless
  Tree), a read-only CodeMirror dual-pane, and bidirectional code↔onboarding pairing; kept mounted across
  tab switches. Verification metadata pinned to the task base until closeout stamps the L2 code commit.
