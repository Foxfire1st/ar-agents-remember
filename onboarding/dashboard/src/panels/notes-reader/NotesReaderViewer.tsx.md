# dashboard/src/panels/notes-reader/NotesReaderViewer.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/notes-reader/NotesReaderViewer.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-07T14:00+02:00                           |
| lastVerifiedCommitHash | `5160dbbbb06695742fea9aed9bd8e9efc78f29bc`       |
| lastVerifiedCommitDate | 2026-07-06T23:12:58+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[overview.md](overview.md)

## Purpose

`NotesReaderViewer.tsx` is the **Notes Reader** screen (agent-orchestration L17): the L9 coordination-notes
reading experience rebuilt on the SAME full-view pattern the Change-Set / File Viewer use. It is a
task-scoped **takeover** whose LEFT RAIL is the master's notes tree (from `/api/notes/list`, `reports/`
included) with the open note highlighted, and whose content pane renders the opened note by **reusing the
File Viewer's `DualPane` primitive**. It replaces the retired inline `TaskNotes` reading pane; the compact
`TaskNotes` list + resolved references stay as the ENTRY surfaces that open this reader.

## Code Commentary

### Logic

`NotesReaderViewer({repo, master, path, onSelectNote, onBack})` is a **controlled** component — the open
`path` and rail `onSelectNote` are lifted to `CockpitShell` (like the File Viewer's persisted state) so a
selection survives back/forward.

- Fetches the rail listing with `listNotes(repo, master)` on `(repo, master)` change (the `let live`
  cancellation idiom; an unreachable API leaves an empty rail, never a crash).
- Fetches the open note with `readNote(repo, master, path)` on `(repo, master, path)` change — `null` while
  loading, `failed` on a read error. Changing `path` (a rail click or a fresh entry) re-fetches → the
  "switch the pane in place" behavior.
- **Rail** — the ChangeSetViewer changed-files column idiom: a sticky `notes (n)` head + one `<button>` per
  note (`note-rail-<n>`, path + byte size), `data-active` on the row whose path is open (the amber/cyan
  wash), a click calls `onSelectNote(entry.path)`, and the server's `truncated` flag renders a muted
  "beyond the list cap" hint.
- **Content pane** reuses `DualPane` via `dualPaneProps(note)`: a **markdown** note takes DualPane's
  partnerless-markdown path (`code=null`, `sidecar={state:"markdown"}`) — the exact treatment the File
  Viewer gives a partnerless route overview; a **text** note becomes a synthetic `FileContent`
  (`noteAsFileContent`) rendered through DualPane's `CodeSide` (read-only CodeMirror); a **binary** note
  degrades to DualPane's byte-count placeholder. Loading/failed render a local `note-status` placeholder
  (a distinct testid from DualPane's `pane-placeholder` so a binary note's placeholder is unambiguous).

### Conventions

Panda `css` local styles mirroring the `ChangeSetViewer` takeover chrome (screen · sticky back header ·
`react-resizable-panels` rail+pane). Testids: `notes-reader-viewer` (screen), `notes-reader-back`,
`notes-reader-open` (the open path in the header), `notes-rail`, `note-rail-<n>`, `note-status`.

### Invariants And Boundaries

GET-only over the unchanged L9 `/api/notes/*` server contract (allow-listing, confinement, binary/oversize
all stay server-side). No store mutation. There is **no second bespoke reader** — the content pane is the
File Viewer's `DualPane`, and the only file-viewer leaf stubbed in tests is `FilePane` (the CodeMirror
editor), the same jsdom accommodation the Change-Set Viewer tests make for `ChangeSetPane`.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| A same-origin view over the local notes API; nothing crosses repositories. | — | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The reused File Viewer content pane (markdown/code/placeholder). | [file-viewer/DualPane.tsx](agents-remember/dashboard/src/panels/file-viewer/DualPane.tsx) |
| The `FileContent` type the text path maps a note into. | [data/files.ts](agents-remember/dashboard/src/data/files.ts) |
| The L9 notes client (`listNotes`/`readNote`) this view consumes. | [data/notes.ts](agents-remember/dashboard/src/data/notes.ts) |
| The shell that hosts the takeover + lifts its selection. | [cockpit/Cockpit.tsx](agents-remember/dashboard/src/cockpit/Cockpit.tsx) |
| The entry surface (compact list + references) that opens this reader. | [panels/TaskNotes.tsx](agents-remember/dashboard/src/panels/TaskNotes.tsx) |
| The unchanged L9 serving endpoints behind the client. | [serving/notes.py](agents-remember/mcp/src/agents_remember/serving/notes.py) |
| The component test suite. | [panels/notes-reader/NotesReaderViewer.test.tsx](agents-remember/dashboard/src/panels/notes-reader/NotesReaderViewer.test.tsx) |

## Update History

- 2026-07-07T14:00+02:00 — Created for agent-orchestration L17: the Notes Reader takeover on the file-viewer
  chrome — a notes-tree rail (highlight-follows-selection, reports/ included) + a content pane that REUSES
  `DualPane` (markdown as a partnerless overview, text through CodeSide, binary placeholder). Controlled by
  `CockpitShell` (selection lifted so it survives back/forward). Server contract unchanged. Verification
  metadata pinned until closeout stamps the L17 commit.
