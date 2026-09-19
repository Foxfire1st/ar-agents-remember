# dashboard/src/panels/changeset/ — Change-Set Viewer Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/changeset/`                |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-09-18T18:10+02:00                           |
| lastVerifiedCommitHash | `c5a74a85af20a8fb48cc44f59de7e926d589d3fc`       |
| lastVerifiedCommitDate | 2026-09-18T18:30:35+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l22` uncommitted source; base `2dcacb27446ecbaba01b69ee32e2ac40a1713b09` |
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src/panels overview](../overview.md)

## Purpose

`changeset/` is the **Change-Set Viewer** (operations-integration slice L4): a task-scoped screen that
shows what a task — or a series master (the NET diff since the series base) — changed, as an up-to-3-column diff. It is the
frontend consumer of the L3 read-only change-set API (`GET /api/changeset/{task,file-diff,master}`,
served by `serving/changeset.py`) and reuses the L2 File Viewer primitives (`FilePane`, `codemirrorTheme`,
`langByExtension`, `usePersistedFlag`, `grammar/Markdown`). It is opened as a **takeover** from a
`DetailPanel` change-set button: `CockpitShell` renders it full-bleed in place of the railed Operations
body, and the screen's back link restores the rails.

The viewer renders an explicit loading placeholder until its first change-set
response and preserves request errors. Working leaf refreshes run the list and
active-file requests together, then schedule the next cycle only after both
settle; series requests omit the unused per-leaf summary.

## Route Model

- `ChangeSetViewer.tsx` — the screen. Column 1 splits into two rows — **changed code files** /
  **changed onboarding files** (path + git status + `+ins/−del`, from `taskChangeset` or
  `masterChangeset`); the active/hover row now wears the File-Viewer-tree **amber wash**
  (`color-mix(in oklab, var(--amber) 20%/12%, transparent)`) so the selected file actually looks
  selected (the old `background: bg` was invisible against the panel). Column 2 is the selected file's
  diff (`ChangeSetPane`, always visible once a row is picked) — until then it shows a faint **siege-tank
  empty-state backdrop** (`EmptyStateBackdrop`, `/assets/sc2-siege-tank-boomerang.mp4` at `opacity 0.18`)
  behind the "Select a changed file" prompt; column 3 is the code↔sidecar partner, opened from a per-row
  split affordance. A `scope`
  (one active enclosure) drives the full per-file diff via `/api/changeset/file-diff`; a `master` drives
  the **NET** series diff (`git diff <master-base> <tip>`) via the same endpoint's `master` param, so its
  rows are equally inspectable (the per-leaf counter breakdown rides alongside). **L4a** adds the `leaf`
  target (`+ mode`): a leaf's `committed` (landed) or `working` (uncommitted) change-set via the `leaf` +
  `mode` selector on the same routes — equally per-file inspectable — with the header labelling the view
  (`committed · <leaf>` / `working · <leaf> · uncommitted`). A counters header + a back link sit above the
  `react-resizable-panels` columns.
- `ChangeSetPane.tsx` — one diff column with a toolbar of persisted toggles (`usePersistedFlag`,
  per-column `keyPrefix`): the task doc's three states map onto two flags — **change-set** (collapsed
  diff) / **full-file + highlight** (uncollapsed diff) / **full-file + highlight-off** (the plain L2
  `FilePane` on the after-content) — plus a split⇄inline flip for whichever diff shows. For **markdown**
  files it also offers a **"rendered"** toggle (`changeset-rendered-toggle`) that swaps the raw diff for
  a formatted `<Markdown>` view (in an `mdScroll` container), so a changed onboarding doc reads as nicely
  here as in the file reader.
- `DiffPane.tsx` — the one genuinely new CodeMirror primitive: a read-only `@codemirror/merge` pane.
  `split` = `MergeView` (a=before, b=after, side by side); `inline` = `unifiedMergeView` over a single
  `EditorView` (doc=after). It reuses `FilePane`'s exact read-only extension set (`lineNumbers` +
  `EditorState.readOnly` + `EditorView.editable.of(false)` + `lineWrapping` + `codeTheme` + the lazy
  `langExtension`) so tokens match across the plain and diff views; both are read-only (no revert/merge
  controls). Built imperatively in an effect with a `disposed` guard against a late async language
  resolve. Its `host` css also renders `.cm-changedText` as a full-height highlight **rectangle** (dark
  muted green for additions, red for deletions) rather than `@codemirror/merge`'s default thin underline
  (L4a) — dark fills, not the bright `--mint`/`--amber` tokens, so the light diff text stays legible.

## Invariants And Boundaries

- Read-only over the L3/L4a change-set API; no store mutation — the screen owns its own component state,
  fed by the `data/changeset.ts` client. An enclosure `scope` diffs base→worktree; a `master` the NET
  series range (`master_base → tip`); a `leaf` (`+ mode`) its `committed` (`base → code_commit`) or
  `working` (`HEAD → worktree`) range — all equally per-file inspectable, and a `leaf`/`master` view needs
  no live enclosure (it resolves off the contract), which is what lets the doc reader show it.
- Panda CSS owns looks, React Aria owns behaviour (the toggles are React Aria `ToggleButton`); no CSS
  animation (GSAP/Motion only — master invariant).
- Opened as a Cockpit **takeover** (rails hidden, full-bleed), not a standing mode-bar tab; the back link
  (or a mode-bar switch / a node `open()`) clears it and restores Operations. View-mode toggles persist
  across file switches via `usePersistedFlag`.

## Hot Path Summary

The Change-Set Viewer: a DetailPanel change-set button opens a full-bleed takeover — column 1 changed
code/onboarding rows (active row in an amber wash) over the L3 change-set API → column 2/3 a read-only
CodeMirror `@codemirror/merge` diff (split/inline/full-file/highlight-off, persisted) reusing the L2
FilePane, with a **rendered-markdown** toggle for `.md` files and a faint siege-tank empty-state backdrop
until a file is picked; the back link restores the railed Operations view.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The L3 read-only change-set API this screen consumes. | `task_changeset` | mcp/src/agents_remember/serving/changeset.py:78-97 |
| The same-origin client wrapping that API. | `taskChangeset` | dashboard/src/data/changeset.ts:56-57 |
| The shell that hosts the takeover + restores the rails. | `CockpitShell` | dashboard/src/cockpit/Cockpit.tsx:385-666; dashboard/src/cockpit/Cockpit.tsx:850-850 |
| The detail panel button + counters that open this screen. | `ChangeSetButton` | dashboard/src/panels/detail-panel/changeSetBar.tsx:20-62 |
| The reused read-only CodeMirror pane + theme + lang map. | `FilePane` | dashboard/src/panels/file-viewer/FilePane.tsx:20-50 |
| The markdown renderer the sidecar column + rendered-markdown toggle reuse. | `Markdown` | dashboard/src/grammar/Markdown.tsx:98-121 |
| The siege-tank empty-state backdrop shown until a file is picked. | `EmptyStateBackdrop` | dashboard/src/panels/EmptyStateBackdrop.tsx:52-97 |

## 260915-KS-L22 The Review Variant Beside The Change-Set Actions

This route gained the reviewer's target variant and the entry that produces it, and nothing else on
it changed. `ChangeSetTarget` now carries an optional `review?: { selectorKind; selectorId }` — the
reviewed subject's recorded identity — and the variant is a *dispatch* field rather than a fifth
change-set mode: the change-set viewer is never mounted for a target that carries it, so the three
ranges this screen already owns (`scope`, `master`, and `leaf` with its `mode`) keep their meaning
exactly and no request this route makes is ever issued from a review. The declaration says as much
in its own comment, which is where a reader arriving at the type will look first.

`changeSetBar.tsx` renders the reviewer entry **beside** the working and committed actions and never
in their place: a third `ChangeSetButton` labelled "Intent review" appears only when the bar's target
is a live admitted curator candidate and a selector id was supplied (`live && selectorId`). That is
the same liveness the working change-set action is gated on, so the two appear together, and the new
props are optional and defaulted (`selectorKind` falls back to `invariant`), so every existing caller
that supplies neither renders exactly what it rendered before this leaf.

What the entry carries is an identity, not a path. `{ repo, master, leaf, review: { selectorKind,
selectorId } }` names the task context and the recorded subject; the browser never chooses the
candidate dataset, because the resolution behind the route does that from the same task context. The
screen that displays a review belongs to the `panels/review/` child route; this route owns the target
variant and the entry that sets it, which is the boundary the two cards divide.

| Finding | Anchor | Source |
| --- | --- | --- |
| The target variant this route's type gained. | "review?: { selectorKind: ReviewSelectorKind; selectorId: string };" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:41-41 |
| The declaration's own statement that no change-set request comes from a review. | "never mounted for one, so no change-set request is made from a review" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:40-40 |
| The reviewer entry, added beside the working/committed actions. | "{live && selectorId ? (" | dashboard/src/panels/detail-panel/changeSetBar.tsx:119-119 |
| The entry's label. | "Intent review" | dashboard/src/panels/detail-panel/changeSetBar.tsx:126-126 |
| The identity the entry carries instead of a filesystem path. | "target={{ repo, master, leaf, review: { selectorKind, selectorId } }}" | dashboard/src/panels/detail-panel/changeSetBar.tsx:125-125 |
| The optional props, defaulted so existing callers are unchanged. | "selectorKind?: ReviewSelectorKind;" | dashboard/src/panels/detail-panel/changeSetBar.tsx:84-85 |

## Update History
- 2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **added the L22 section** — the `review` variant `ChangeSetTarget` gained and why it is a dispatch field rather than a fifth change-set mode, plus the "Intent review" entry `changeSetBar.tsx` adds beside the working/committed actions for a live candidate that names a selector. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns that stamp.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this route against the frontend-rail change set. No route impact: changeset files changed only by behavior-preserving lint remediation and import-path updates.

- 2026-08-04T18:05+02:00 — 260731-EFA-L6 S18-B17 curator: re-anchored the detail-panel row from the
  `DetailPanel` memo export (cited range was a bare `);`) to the operative `ChangeSetButton`
  function (counters, fetches, and the `open-changeset` button) at its exact frozen-source extent.
  Claim wording unchanged.
- 2026-08-02T20:43+02:00 — W2-B08: anchored 7 change-set viewer citation claims and supplied exact source paths; ranges remain generated by the scoped fixer. Verification metadata stays pinned until closeout.

- 2026-07-12T12:55+02:00 — 260712-TRH-L2 route impact: the existing Change-Set Viewer now makes series net requests without unused per-leaf summaries, exposes loading before the first response, preserves errors, and refreshes working data only after the prior cycle settles. Verification metadata pinned until closeout stamps the L2 code commit.

- 2026-06-30T00:00:00+02:00 — L5 (diff-viewer polish): three viewer refinements — (1) `ChangeSetPane` gains a
  **rendered-markdown** toggle (`changeset-rendered-toggle`) that, for `.md` diffs, swaps the raw merge
  diff for a formatted `<Markdown>` view (persisted per column); (2) the changed-file **row highlight**
  is fixed to the File-Viewer amber wash (`color-mix(in oklab, var(--amber) 20%/12%, transparent)`),
  replacing the invisible `background: bg`; (3) the no-file column-2 placeholder becomes a faint
  **siege-tank `EmptyStateBackdrop`** (`/assets/sc2-siege-tank-boomerang.mp4`, `opacity 0.18`) behind
  the "Select a changed file" prompt. Updated the `ChangeSetPane`/`ChangeSetViewer` Route Model bullets,
  the Hot Path Summary, and the references (added `EmptyStateBackdrop`). A new `ChangeSetPane.test.tsx`
  sidecar covers the rendered toggle. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-29T23:00+02:00 — L4a: the screen learns the **leaf views** — `ChangeSetViewer` takes a `leaf` +
  `mode` target (committed/working, precedence `leaf > master > scope`), labels the header, and is per-file
  inspectable via `leafFileDiff`; the **working** view auto-refreshes its file list and the
  currently-open file's diff on a 2.5s interval (a live delta, not a frozen snapshot — committed/series/scope
  never poll); and `DiffPane`'s `host` css turns
  `.cm-changedText` into a full-height highlight **rectangle** (dark muted green/red fills, `!important`
  over the library theme) instead of the default underline. Updated the `ChangeSetViewer`/`DiffPane` Route
  Model bullets + the Invariants. (The takeover's back-to-origin behaviour is a `cockpit/Cockpit.tsx`
  change — see its sidecar.) Verification metadata pinned until closeout stamps the L4a commit.
- 2026-06-29T17:00+02:00 — L4 follow-up: the **series/master view is now inspectable** — `master` drives the
  NET `git diff <master-base> <tip>` (via the file-diff `master` param) so its rows open per-file diffs like a
  leaf's (per-leaf counters kept alongside); and the `DiffPane` host makes `.cm-mergeView` the bounded scroll
  container so a long split diff scrolls. Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T16:40+02:00 — Created for operations-integration L4: the Change-Set Viewer route — a
  task-scoped takeover screen over the L3 `/api/changeset/*` API (column-1 changed code/onboarding rows,
  column-2/3 a read-only `@codemirror/merge` diff with split/inline/full-file/highlight-off toggles,
  code↔sidecar partner column), reusing the L2 File Viewer primitives; master scope is accumulated-only.
  Verification metadata pinned to the task base until closeout stamps the L4 code commit.
