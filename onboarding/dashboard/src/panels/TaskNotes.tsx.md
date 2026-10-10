# dashboard/src/panels/TaskNotes.tsx

## Governing Overview

[overview.md](overview.md)

## Purpose

`TaskNotes.tsx` is the compact **notes ENTRY surface** inside the task reader (L9 friction
F-M, reshaped by L17, re-scoped by 260928-MIK-L126). A task page lists **no notes tree**.
Where the master has a notes folder, the page shows one `Notes` line naming the top-folder
entry count with a link opening the reader at the notes root; no total over the tree is
computed for a page. Beside the link, a task's page shows its references (each a link where
it names an existing note) and the reports of the role agents the product started for this
task — newest first, at most twenty, with a link to their folder in the explorer where there
are more. The page of a master shows its own references and the link. Rendered by
`DetailPanel`'s `TaskReader` (with the doc's references) and `MasterOverview`; both thread
`onOpenNotes` from `CockpitShell`.

## Code Commentary

### Logic

`TaskNotes({repo, master, references, onOpenNotes})` fetches the root folder with
`listFolder(repo, master, "")` on mount / identity change (the `let live` cancellation
idiom). An unreachable API renders the notes failure state — but a missing folder
answer (`exists: false`) still applies the resolved references: the effect sets
the resolution map regardless of folder existence and resets all three pieces of
state on every selection. Requirement links come from their separate
`useTaskRequirementLinks` context and render even on notes failure. Only a
rejected request pair leaves references unresolved.

- **Notes line**: one line under `Notes` naming the root folder's entry count with a link
  opening the reader at the notes root. No total over the tree is computed.
- **References** (`references.length > 0`): resolved by the one `resolveNoteReferences`
  request; each item renders the whole reference string as a link-styled `<button>`
  (`note-ref-<n>`) that calls `onOpenNotes({repo, master, path})` where it names an
  existing note; a miss renders the usual `<Markdown inline>` bullet.
- **Reports**: the recorded starts for this task via `listTaskReports` (newest first, at
  most twenty rows, `task-reports-explorer-link` to the reports folder where more exist);
  zero recorded reports render `task-reports-empty` while keeping the Notes link; an
  unreadable reports record renders `task-reports-failed`.
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
notes resolution (`note-ref-<n>`). Note references and requirement references tag
their `onOpenNotes` payload with an explicit `kind` (`"notes"` / `"requirements"`).
(The L9 series-note rows that once carried note payloads are retired with the list
endpoint.) Both the
notes and requirement listings are read-only view state; opening stays delegated to
`onOpenNotes`.

### Conventions

Panda `css` local styles mirroring `DetailPanel`'s section/heading/row idioms; testids follow the house
position pattern (`notes-root-count`, `notes-root-link`, `note-ref-1`, `task-reports-empty`, `task-reports-failed`, `task-reports-explorer-link`). No `note-open-*` testid exists in the carried source.

### Invariants And Boundaries

No mutation surface of any kind: the component only GETs one folder and POSTs one reference
request, and holds them as view state. Links are
only ever created from the server's own answers (resolved references, recorded report rows),
so a link can never point outside the series' notes tree — and opening is delegated to `onOpenNotes`, never a local
write. No request grows with the tree: one root-folder read, one bounded reference request,
one bounded reports request.

## Evidence

### Cross-Repo References

No meaningful cross-repo references found.

A same-origin view over the local notes API; nothing crosses repositories.

### Repo-Internal References


- The data client with the folder and reference resolvers. [1]


- The surface passes a shared discriminated artifact target. [2]


- The task reader mounts this component and threads `onOpenNotes`. [5]


- The folder, resolve and read endpoints behind the client. [6]


- The component test suite. [7]

- TaskNotes imports the shared target under its existing local NotesReaderTarget name. [3]
- The shared markdown renderer (inline reference rendering). [4]


- The page shows one Notes line with the root count and no tree. [8]


- References resolve through one request; reports read newest-first capped at twenty. [9]
