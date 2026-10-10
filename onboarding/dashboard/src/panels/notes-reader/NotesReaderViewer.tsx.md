# dashboard/src/panels/notes-reader/NotesReaderViewer.tsx

## Governing Overview

[overview.md](overview.md)

## Purpose

`NotesReaderViewer.tsx` is the **Notes Reader** screen (agent-orchestration L17): the L9 coordination-notes
reading experience rebuilt on the SAME full-view pattern the Change-Set / File Viewer use. It is a
task-scoped **takeover** whose LEFT RAIL is the shared `ExplorerTree` (the File viewer's tree, no
second tree written) fed one folder at a time by rule 2, with the open note highlighted, and whose
content pane renders the opened note by **reusing the
File Viewer's `DualPane` primitive**. It replaces the retired inline `TaskNotes` reading pane; the compact
`TaskNotes` line + resolved references stay as the ENTRY surfaces that open this reader.


## 260831-CCR-L23 Task-Artifact Reader (notes + requirements)

L23 widened the reader from notes-only to a discriminated task-artifact reader. The
local `NotesReaderTarget` interface was deleted and re-exported as the shared
`TaskArtifactReaderTarget` (`dashboard/src/data/taskArtifacts.ts`); the
view now takes a `kind` member plus an optional `document` (requirements
only). Listing/content hooks branch on the kind:

- `kind === "notes"` (no document): the folder/read path (`listFolder` with
  offsets for next parts / `readNote`);
- `kind === "requirements"`: `listRequirements` /
  `readRequirement` with the task-document reference, mapping each packet row
  into the notes rail shape (`language: "markdown"`, `truncated: false`).
- `kind === "task-report"`: one recorded report by its exact recorded identity.
- `kind === "decisions"`: the whole log on its own page (`DecisionsPane`,
  newest-first, product records muted).
- `kind === "role-report"` / supplied report content: the recorded body in the
  shared pane with no rail.

The rail header, open-path label, and failure copy are kind-aware (`notes` vs
`requirements`), the screen root carries `data-artifact-kind`, and
`CockpitShell` keys the takeover marker on the kind. Rendering still reuses
`DualPane`; no second bespoke reader exists.

## Code Commentary

### Logic

`NotesReaderViewer({repo, master, path, onSelectNote, onBack})` is a **controlled** component — the open
`path` and rail `onSelectNote` are lifted to `CockpitShell` (like the File Viewer's persisted state) so a
selection survives back/forward.

- Fetches the rail one folder at a time with `listFolder(repo, master, path, offset)` on
  `(repo, master)` change (the `let live`
  cancellation idiom; an unreachable API leaves an empty rail, never a crash).
- Fetches the open note with `readNote(repo, master, path)` on `(repo, master, path)` change — `null` while
  loading, `failed` on a read error. Changing `path` (a rail click or a fresh entry) re-fetches → the
  "switch the pane in place" behavior.
- **Rail** — the shared `ExplorerTree`: folders start closed; opening on a note opens the
  folders on the way to it and marks the note, loading beyond the first part as needed
  (L126-CODE-03); a folder answered in parts shows a row loading the next part; a vanished
  folder shows empty with the server's reason while the rest stays usable (L126-CODE-04).
  The adapter holds at most 32 folders with LRU eviction that never touches the open note
  chain (`MAX_CACHED_FOLDERS`, L126-CODE-11).
- **Content pane** reuses `DualPane` via `dualPaneProps(note)`: a **markdown** note takes DualPane's
  partnerless-markdown path (`code=null`, `sidecar={state:"markdown"}`) — the exact treatment the File
  Viewer gives a partnerless route overview; a **text** note becomes a synthetic `FileContent`
  (`noteAsFileContent`) rendered through DualPane's `CodeSide` (read-only CodeMirror); a **binary** note
  degrades to DualPane's byte-count placeholder. Loading/failed render a local `note-status` placeholder
  (a distinct testid from DualPane's `pane-placeholder` so a binary note's placeholder is unambiguous).
- **Truncation banner** (260703-L18 finding 2): DualPane's "Showing the first 2 MiB" banner lives only in
  `CodeSide`, which the markdown path never reaches — so a truncated MARKDOWN note (the dominant note type)
  would silently drop the truncation contract. When `note.truncated && note.language === "markdown"` the
  view renders the same banner (`notes-trunc-banner`, matching CodeSide's wording/style) ABOVE the DualPane;
  text notes keep CodeSide's own banner.

### Conventions

Panda `css` local styles mirroring the `ChangeSetViewer` takeover chrome (screen · sticky back header ·
`react-resizable-panels` rail+pane). Testids: `notes-reader-viewer` (screen), `notes-reader-back`,
`notes-reader-open` (the open path in the header), `note-rail-<n>`, `note-status`. No `notes-rail` testid exists in the carried source.

### Invariants And Boundaries

Folder/read transport over the L126 `/api/notes/*` server contract (allow-listing, confinement, binary/oversize
all stay server-side; the whole-tree list route is gone). No store mutation. There is **no second bespoke reader** — the content pane is the
File Viewer's `DualPane`, and the only file-viewer leaf stubbed in tests is `FilePane` (the CodeMirror
editor), the same jsdom accommodation the Change-Set Viewer tests make for `ChangeSetPane`. The whole-log
`DecisionsPane`, task-report and role-report readers render their kinds in the same pane.

## Role-report kind

The viewer also accepts a **role report** as one more artifact kind (`kind: "role-report"` with a
`RoleReportContent`): the header shows `Report` and the recorded path, the pane reuses `DualPane`
through the same `noteAsFileContent` mapping, and no rail is rendered. `RoleChatsPane` opens it from
Result through `readRoleReport`, so the launcher needs no second viewer (MIK-R75 rule 4).

## Evidence

### Cross-Repo References

No meaningful cross-repo references found.

A same-origin view over the local notes API; nothing crosses repositories.

### Repo-Internal References


- The reused File Viewer content pane (markdown/code/placeholder). [1]

- The `FileContent` type the text path maps a note into. [2]
- The shell that hosts the takeover + lifts its selection. [4]
- The entry surface (Notes line + references) that opens this reader. [5]


- The component test suite covers the tree, open path, parts and depth. [7]



- The notes client with folder, resolve and read helpers. [3]



- The folder, resolve and read endpoints behind the client. [6]


- The folder-fed tree adapter with fill, vanish recovery and the folder cap. [8]


- The whole-log pane renders newest-first with product records muted. [9]


- Old reader addresses open the same note through the new tree. [10]


## Current L5I Maintenance

The controlled Notes Reader is memoized as a persistent cockpit view. Shell view switches with
unchanged route props no longer reconstruct its reader subtree, while its own selected-note state
and data reads remain unchanged.
