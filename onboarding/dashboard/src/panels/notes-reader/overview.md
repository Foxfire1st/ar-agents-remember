# dashboard/src/panels/notes-reader/ — Notes Reader Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/notes-reader/`             |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-07T14:00+02:00                           |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`       |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src/panels overview](../overview.md)

## Purpose

`notes-reader/` is the **Notes Reader** (agent-orchestration L17): the L9 coordination-notes reading
experience rebuilt on the SAME full-view pattern the File Viewer / Change-Set Viewer use. It is a
task-scoped **takeover** — `CockpitShell` renders it full-bleed in place of the railed Operations body — and
it is the frontend consumer of the **unchanged** L9 read-only notes API (`GET /api/notes/{list,read}`,
served by `serving/notes.py`). It reuses the L2 File Viewer content primitive (`file-viewer/DualPane`, which
itself composes `FilePane` + `grammar/Markdown`) and the L4 Change-Set Viewer takeover chrome (sticky back
header + `react-resizable-panels` rail+pane). It **replaces** the retired inline `TaskNotes` reading pane;
the compact `TaskNotes` list + resolved references remain the ENTRY surfaces that open it.

## Route Model

- `NotesReaderViewer.tsx` — the screen. LEFT RAIL = the master's notes tree from `/api/notes/list`
  (`reports/` included), one clickable row per note (path + byte size) with the open note in an amber/cyan
  **active wash** (the Change-Set Viewer row idiom); the server's `truncated` flag surfaces a muted
  "beyond the list cap" hint. CONTENT PANE = the opened note (`/api/notes/read`) rendered by **reusing
  `DualPane`**: a markdown note takes DualPane's partnerless-markdown path (the File Viewer's route-overview
  treatment), a text note renders through DualPane's `CodeSide` (read-only CodeMirror), a binary note
  degrades to the byte-count placeholder; loading/failed show a local `note-status` placeholder. The view is
  **controlled** — the open `path` + rail `onSelectNote` are lifted to `CockpitShell`, so a rail click
  switches the pane in place and the selection survives back/forward (the reader stays mounted-hidden after
  Back, like the File Viewer). A sticky back link (`notes-reader-back`) restores the railed Operations body.

## Invariants And Boundaries

- Read-only over the **unchanged** L9 `/api/notes/*` server contract (allow-listing, confinement,
  binary/oversize all stay server-side); no store mutation — the screen owns its own listing/content fetch
  via `data/notes.ts`.
- **No second bespoke reader** — the content pane IS the File Viewer's `DualPane`; only the flat notes rail
  (the ChangeSetViewer column idiom) and the takeover chrome are local. Panda CSS owns looks; no CSS
  animation (GSAP/Motion only — master invariant).
- Opened as a Cockpit **takeover** (rails hidden, full-bleed), not a standing mode-bar tab; Back — or a
  mode-bar switch / a node `open()` — hides it. Unlike the Change-Set takeover, the reader is retained
  mounted-hidden (not discarded) so its listing + selection persist.

## Hot Path Summary

The Notes Reader: a `TaskNotes` list row or a resolved reference opens a full-bleed takeover — a notes-tree
rail (highlight-follows-selection, reports/ included) over the L9 `/api/notes/list` → a content pane that
reuses `DualPane` (markdown as a partnerless overview, text through CodeSide, binary placeholder) over
`/api/notes/read`; rail clicks switch the pane in place, and Back restores the railed Operations view with
the reader kept mounted-hidden so selection survives.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The unchanged L9 read-only notes API this screen consumes. | [serving/notes.py](agents-remember/mcp/src/agents_remember/serving/notes.py) |
| The same-origin notes client (`listNotes`/`readNote`/`resolveNoteReference`). | [data/notes.ts](agents-remember/dashboard/src/data/notes.ts) |
| The reused File Viewer content pane (markdown/code/placeholder). | [panels/file-viewer/DualPane.tsx](agents-remember/dashboard/src/panels/file-viewer/DualPane.tsx) |
| The shell that hosts the takeover + lifts its selection. | [cockpit/Cockpit.tsx](agents-remember/dashboard/src/cockpit/Cockpit.tsx) |
| The entry surface (compact list + references) that opens this reader. | [panels/TaskNotes.tsx](agents-remember/dashboard/src/panels/TaskNotes.tsx) |

## Update History

- 2026-07-07T18:40+02:00 — No route impact: 260703-L18 finding 2 renders the "Showing the first 2 MiB"
  truncation banner above the DualPane for a truncated markdown note (DualPane's banner lives only in
  CodeSide, which the markdown path never reaches); the Notes Reader takeover this overview describes is
  unchanged (detail in the file sidecar).
- 2026-07-07T14:00+02:00 — Created for agent-orchestration L17 (Notes reader v2): the Notes Reader child
  route — a task-scoped takeover over the unchanged L9 `/api/notes/*` API (a notes-tree rail with
  highlight-follows-selection + reports/, a content pane that REUSES `DualPane`), replacing the retired
  inline `TaskNotes` reading pane; the compact `TaskNotes` list + references stay as the entry surfaces.
  Verification metadata pinned until closeout stamps the L17 commit.
