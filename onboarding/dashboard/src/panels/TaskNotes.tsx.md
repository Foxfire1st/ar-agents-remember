# dashboard/src/panels/TaskNotes.tsx

## Governing Overview

[overview.md](overview.md)

## Purpose

`TaskNotes.tsx` is the compact **coordination-notes ENTRY SURFACE** inside the task reader (L9 friction
F-M, reshaped by L17). It lists the selected master's `tasks/<repo>/<master>/notes/**` tree — `reports/`
subfolders included — and resolves task-doc reference strings that name an existing notes file into openable
links. Both surfaces now **open the L17 Notes Reader** (`panels/notes-reader/NotesReaderViewer.tsx`) via the
`onOpenNotes` callback rather than expanding an inline pane. Rendered by `DetailPanel`'s `TaskReader` (with
the doc's references) and `MasterOverview` (list only); both thread `onOpenNotes` from `CockpitShell`.

## Code Commentary

### Logic

`TaskNotes({repo, master, references, onOpenNotes})` fetches `listNotes(repo, master)` on mount /
identity change (the `let live` cancellation idiom). An unreachable API — or a series whose notes folder is
missing (the server answers an empty list) — renders **no notes surface at all** and leaves every reference
plain text: the failure handler deliberately does not touch state.

- **References** (`references.length > 0`): each item runs through `resolveNoteReference(reference,
  notePaths)`; a hit renders the whole reference string as a link-styled `<button>` (`note-ref-<n>`) that
  calls `onOpenNotes({repo, master, path})`; a miss renders the usual `<Markdown inline>` bullet.
- **Series notes** (`notes.length > 0`): one row-button per note (`note-open-<n>`, path + byte size) that
  calls `onOpenNotes({repo, master, path})`; the server's `truncated` flag renders a muted "beyond the
  list cap" hint so the list never silently lies.
- `onOpenNotes` is **optional** — a context without the takeover (e.g. the master-overview list in a test)
  still renders the surface; the rows are then inert.

**Retired (L17):** the bespoke inline `NoteReader` (its own `noteBox`/`noteHead`/sticky-close chrome and the
markdown/text/binary rendering) was removed. Reading a note now happens in the full Notes Reader view, whose
content pane REUSES the File Viewer `DualPane`; the note-content rendering tests moved to that view's suite.


## 260831-CCR-L23 Requirement-Reference Routing

L23 split reference resolution by reserved root. Each reference is first checked for
a requirement address (`requirementAddressFromReference`); a hit resolves
against the provider's registered requirement listing and renders as a
`requirement-ref-<n>` button that opens a `kind: "requirements"` artifact
target through the link context, while non-requirement references keep the existing
notes resolution (`note-ref-<n>`). Series-note rows and note references now tag
their `onOpenNotes` payload with an explicit `kind: "notes"`. Both the
notes and requirement listings are read-only view state; opening stays delegated to
`onOpenNotes`.

### Conventions

Panda `css` local styles mirroring `DetailPanel`'s section/heading/row idioms; testids follow the house
position pattern (`note-open-1`, `note-ref-1`).

### Invariants And Boundaries

No mutation surface of any kind: the component only GETs the listing and holds it as view state. Links are
only ever created from the server's own listing (`resolveNoteReference` against fetched paths), so a link can
never point outside the series' notes tree — and opening is delegated to `onOpenNotes`, never a local
write.

## Evidence

### Cross-Repo References

No meaningful cross-repo references found.

A same-origin view over the local notes API; nothing crosses repositories.

### Repo-Internal References

- The data client + the pure reference resolver. [1]
- The surface passes a shared discriminated artifact target: notes carry a path, while requirements also carry the selected document. [2]
- TaskNotes imports the shared target under its existing local NotesReaderTarget name. [3]
- The shared markdown renderer (inline reference rendering). [4]


- The task reader + master overview that mount this component and thread `onOpenNotes`. [5]
- The serving endpoints behind the client. [6]
- The component test suite. [7]
