# dashboard/src/panels/file-viewer/ — File Viewer Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/file-viewer/`              |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-09-30T20:36:31+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`       |
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview      | `../overview.md`                                 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The marks gutter a pane hosts: portals, placement, the gutter per editor and `drawn`. | `useMarkedPane` | dashboard/src/panels/file-viewer/markGutter.tsx:321-372 |
| The bounded, passive hold released by the reader's pointer, key or wheel. | `HOLD_RELEASES`; `holdRevealed` | dashboard/src/panels/file-viewer/markGutter.tsx:176-218 |
| The code pane's optional marks. | "marks?: PaneMarks;"; "drawn({ after: { view, first: firstLine } });" | dashboard/src/panels/file-viewer/FilePane.tsx:35-70 |

## 260928-MIK-L31 The Code Pane Can Show An Excerpt With Its File's Line Numbers

`MIK-R31` adds one module and two optional props to this route, for the reviewer's focused expression cards, all
inert for the File Viewer. [`lineNumbering.ts`](lineNumbering.ts.md) (new, carded, governed here) exports
`numberedFrom(first)`: the plain `lineNumbers()` for line 1, otherwise a gutter that prints the file's own line
numbers for an excerpt starting at `first`. [`FilePane.tsx`](FilePane.tsx.md) gains `firstLine` (default 1) and
`fit` (a content-sized host capped at `32rem`); `changeset/DiffPane.tsx` uses the same gutter per side. The File
Viewer passes neither prop and renders exactly as before.

| Finding | Anchor | Source |
| --- | --- | --- |
| The excerpt gutter. | `numberedFrom` | dashboard/src/panels/file-viewer/lineNumbering.ts:7-11 |
| The code pane's optional first line and content-sized host. | `fitHost`; "numberedFrom(firstLine)," | dashboard/src/panels/file-viewer/FilePane.tsx:23-23; dashboard/src/panels/file-viewer/FilePane.tsx:53-53 |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The L1 read-only files API this view consumes. | `register_files_routes` | mcp/src/agents_remember/serving/files.py:298-327 |
| The same-origin client wrapping that API. | `fetchRepos` | dashboard/src/data/files.ts:113-116 |
| The shell that registers + keeps this view mounted. | "const filesLayer = chatsLayer;" | dashboard/src/cockpit/Cockpit.tsx:340-343; dashboard/src/cockpit/Cockpit.tsx:780-782; dashboard/src/cockpit/Cockpit.tsx:344-344 |
| The markdown renderer the sidecar pane reuses. | `Markdown` | dashboard/src/grammar/Markdown.tsx:109-159 |

## Current L5I Route State

The mounted-hidden File Viewer does not fetch its repository catalog at dashboard boot. It waits for
its first selected view, retains that settled result across later visibility changes, and shares an
in-flight read during development effect replay.

## Update History
- 2026-09-30T20:36:31+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): **route body updated for MIK-R34.** Added the section "260928-MIK-L34 A Code Pane Can Carry Marks On Its File Lines": the new [`markGutter.tsx`](markGutter.tsx.md) and its test (both carded here) and the optional `marks` prop of [`FilePane.tsx`](FilePane.tsx.md), recording ruling 2026-09-30T16:19:34 Q4 and review R1 F2, R2-F1, R3-F1 and R3-F2; three rows. The MIK-L31 section's `FilePane` row was re-pointed by the exact line shift (`22` → `23`, `47` → `53`). The route's purpose is unchanged: the File Viewer passes no marks.
- 2026-09-30T12:15:39+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`): No content impact: this route's governed sources are unchanged. MIK-R29 grew `dashboard/src/cockpit/Cockpit.tsx` (two imports, the `knowledge` destination, the reader-hash initial view and the `ViewBody` case), so the citation rows into it that moved were re-pointed by the installed fixer's normalisation or by the exact base-to-staged line shift; every re-pointed row was checked to hold its anchors in the new range, and no claim was reworded. No verification stamp was advanced.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): **route body updated for MIK-R31.** Added the section "260928-MIK-L31 The Code Pane Can Show An Excerpt With Its File's Line Numbers" before Purpose (the new `lineNumbering.ts`, carded; `FilePane`'s optional `firstLine` and `fit`) and the Route Model entries. Two rows added.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `fetchRepos` repointed to dashboard/src/data/files.ts:113-116. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T18:22+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **this leaf's own code edit moved lines this route's body cites, so the carrier range was APPENDED to the row that cites them and this entry records that body change.** `dashboard/src/cockpit/Cockpit.tsx` gained the `ReviewSurface` import and the takeover's review branch, which shifted the cited declarations below the insertion; the row that names "const filesLayer = chatsLayer;" now also cites `dashboard/src/cockpit/Cockpit.tsx:339-339`, the line that actually carries it. **Every range the row already carried is kept** — the repair is a union, never a substitution and never a deletion — and no claim wording changed, because the claim's subject (the shell that registers and keeps this view mounted) is the same construct it always was. The verification stamp is **not** advanced: the code commit does not exist yet and closeout owns it.
- 2026-09-05T06:21+00:00 — Re-read the affected source declarations and repaired citation ranges shifted by CCR additions. Preserved the route contract and existing history; literal anchors identify the exact current construct where shared identifiers were ambiguous.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this route against the frontend-rail change set. No route impact: FileViewer.tsx changed only by behavior-preserving lint remediation.

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

## Update History
- 2026-09-28T17:15:39+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`dashboard/src/cockpit/Cockpit.tsx`) were re-pointed to where the same anchors now sit; each re-pointed row held its anchors at the base and holds them after the base-to-candidate line mapping. Claim wording unchanged. No stamp advanced.
