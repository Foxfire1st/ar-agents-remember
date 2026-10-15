# dashboard/src/panels/notes-reader/NotesReaderViewer.tsx

## Governing Overview

[overview.md](overview.md)

## Purpose

`NotesReaderViewer.tsx` is the **Notes Reader** screen (agent-orchestration L17): the L9 coordination-notes
reading experience rebuilt on the SAME full-view pattern the Change-Set / File Viewer use. It is a
task-scoped **takeover** whose LEFT RAIL is the shared `ExplorerTree` (the File viewer's tree, no
second tree written) fed one folder at a time by rule 2, with the open note highlighted, and whose
content pane renders fetched notes by **reusing the
File Viewer's `DualPane` primitive**. It replaces the retired inline `TaskNotes` reading pane; the compact
`TaskNotes` line + resolved references stay as the ENTRY surfaces that open this reader. The wider artifact target also includes a whole decision log: that branch uses the shared task-page DecisionList rather than DualPane.


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
  authored decisions newest-first, with product records in a separate counted end disclosure).
- `kind === "role-report"` / supplied report content: the recorded body in the
  shared pane with no rail.

The rail header, open-path label, and failure copy are kind-aware (`notes` vs
`requirements`), the screen root carries `data-artifact-kind`, and
`CockpitShell` keys the takeover marker on the kind. Rendering still reuses
`DualPane` for fetched notes, requirements and reports; the whole decision log reuses DecisionList in a dedicated DecisionsPane instead of DualPane.

The whole-log page counts and numbers authored decisions only. It shows every authored entry newest-first with its recorded time, Markdown decision text and rationale already expanded; whole rows have no more/less control. The reading area uses the shared centered 100ch recipe. Product-written records are retained after the authored list in a muted native details disclosure with its own count, time, text and rationale, but no decision number. Opening the disclosure is not a new fetch.

## Code Commentary

### Logic

`NotesReaderViewer({repo, master, path, onSelectNote, onBack})` is a **controlled** component — the open
`path` and rail `onSelectNote` are lifted to `CockpitShell` (like the File Viewer's persisted state) so a
selection survives back/forward.

- `NotesTree` wires the shared ExplorerTree to `useNotesFolderCache`, which owns stable folder paging, fill-to-note, vanish recovery and refresh invalidation. The repo/master-keyed tree lifetime owns the cache; content reads remain in the viewer.
- Fetches the open note with `readNote(repo, master, path)` on `(repo, master, path)` change — `null` while
  loading, `failed` on a read error. Changing `path` (a rail click or a fresh entry) re-fetches → the
  "switch the pane in place" behavior.
- **Rail** — the shared `ExplorerTree`: folders start closed; opening on a note opens the
  folders on the way to it and marks the note, loading beyond the first part as needed
  (L126-CODE-03); a folder answered in parts shows a row loading the next part; a vanished
  folder shows empty with the server's reason while the rest stays usable (L126-CODE-04).
  The extracted cache targets 32 folders with LRU eviction that protects the inserted directory and the open note chain. If no unprotected victim exists, it stops above the target; this is not an unconditional ceiling.
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
all stay server-side; the whole-tree list route is gone). No store mutation. Fetched note, requirement and report bodies use the File Viewer’s DualPane through NotePane. DecisionsPane is a separate branch within the same takeover chrome, reusing shared DecisionList and the already supplied decision array rather than fetching a log.

For the fetched-content path, the existing test accommodation remains recorded here: the only file-viewer leaf stubbed in tests is `FilePane` (the CodeMirror editor), the same jsdom accommodation the Change-Set Viewer tests make for `ChangeSetPane`. This pass does not reverify that test claim or use it as acceptance evidence for whole-log layout.

## Role-report kind

The viewer also accepts a **role report** as one more artifact kind (`kind: "role-report"` with a
`RoleReportContent`): the header shows `Report` and the recorded path, the pane reuses `DualPane`
through the same `noteAsFileContent` mapping, and no rail is rendered. `RoleChatsPane` opens it from
Result through `readRoleReport`, so the launcher needs no second viewer (MIK-R75 rule 4).

## Current L5I Maintenance

The controlled Notes Reader is memoized as a persistent cockpit view. Shell view switches with
unchanged route props no longer reconstruct its reader subtree, while its own selected-note state
and data reads remain unchanged.

## Evidence

### Cross-Repo References

No meaningful cross-repo references found.

A same-origin view over the local notes API; nothing crosses repositories.

### Repo-Internal References



- NotePane maps fetched content to DualPane, adds the Markdown truncation banner and keeps local status placeholders; this is viewer integration, not proof of DualPane internals. [1]



- The `FileContent` type the text path maps a note into. [2]

- Cockpit owns the artifact target and open flag, preserves the target on Back, updates note paths and hosts the controlled viewer takeover. [4]



- TaskNotes composes resolved references and the Notes line; its data callbacks open exact notes, folders and report targets through the supplied artifact callback. [5]




- The component test suite covers the tree, open path, parts and depth. [7]



- The notes client with folder, resolve and read helpers. [3]



- The folder, resolve and read endpoints behind the client. [6]


- The extracted folder cache owns paging, fill, vanish recovery and the protected LRU target. [8]



- The whole-log pane shows authored decisions newest-first with expanded shared rows; retained product records are unnumbered in a separate counted native disclosure. [9]




- The notes-target reader retains the same note and keyed tree lifetime. [10]
