# dashboard/src/panels/notes-reader/ — Notes Reader Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/notes-reader/`             |

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

260707-HFX2-L13 changes only `NotesReaderViewer.test.tsx` in this child route. Its shared `fetch`
fixture now recognizes `/api/task-document` because the surrounding detail/task-reader composition
loads the visible task body on demand before or alongside notes requests. The production Notes Reader
component, its `/api/notes/{list,read}` transport, takeover state, and `DualPane` rendering are
unchanged; the fixture branch prevents the parent reader's new request from leaking into or
invalidating the notes-specific assertions.

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

`NotesReaderViewer.tsx` is the shared task-artifact takeover: `kind: notes` uses `/api/notes/{list,read}`, while `kind: requirements` uses the canonical task-document-selected `/api/requirements/{list,read}` endpoints. The tree rail and `DualPane` are shared; kind-aware labels prevent requirement packets from being presented as ordinary notes.

## Evidence

### Repo-Internal References

- The read-only notes routes. [1]
- The same-origin notes client (`listNotes`/`readNote`/`resolveNoteReference`). [2]
- The reused File Viewer content pane maps both notes and requirement packets to markdown/code/placeholder rendering. [3]
- Cockpit defines the note-opening callback. [4]
- Cockpit defines the note-selection callback. [5]
- Cockpit renders NotesReaderViewer. [6]
- TaskNotes resolves registered requirement references first; a requirement address never falls through to a note target. [7]

## Current L5I Route State

The current source-backed Notes Reader integration is recorded by the repository-local references
above.

## 260831-CCR-L23 Task-Artifact Reader (notes + requirements)

L23 widened this child route from a notes-only reader to a discriminated
task-artifact reader. `NotesReaderViewer.tsx` now takes the shared
`TaskArtifactReaderTarget` (`data/taskArtifacts.ts`) with a `kind`
member: `notes` keeps the unchanged `/api/notes/{list,read}` transport,
and the new `requirements` kind reads the task-local packet root over
`/api/requirements/{list,read}` (listing/content hooks branch on the kind and
map packets into the existing rail/pane). Rail headers, the open-path label, failure
copy, and the screen root (`data-artifact-kind`) are kind-aware; rendering still
reuses the File Viewer `DualPane`. Entry surfaces (task prose via
`Markdown`, `TaskNotes` references, the `DetailPanel` reader) open
registered requirement packets through the same takeover.
