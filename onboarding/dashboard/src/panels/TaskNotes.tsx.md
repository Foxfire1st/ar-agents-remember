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

The read-only hooks separate three bounded requests: useResolvedNotes makes one content-keyed
reference resolution. Its key remains `references.join('\0')`, not JSON serialization:
`[]` and one empty reference share that key. `useEffectEvent` supplies the list current when the
keyed effect runs, without adding array identity as a request trigger. useTaskReports lists recorded starts for a task-root-relative document path;
useNotesFolderTotal reads the root folder count, never walks descendants. Each drops late answers
on identity change. useTaskNotesData preserves the joint wrapper; the task page uses two disjoint
islands so references/reports can precede Further notes while the one Notes line stays last, without
duplicating requests. An unavailable report list is stated, not converted into an empty result.

- **Notes line:** only the actual root-folder total, with the notes-root artifact target; no tree
  rows, note content or whole-tree count is fetched for the page.
- **References:** one References and reports heading on a task. The first eight rows have an
  all-link when needed; whole views reuse the same resolved affordance. A whole Markdown link draws
  its label as the link and its destination beside it. Reserved requirement addresses resolve through
  the requirement-link provider; ordinary note links require the server's resolution. Unresolved
  values remain plain/inline text, never an invented internal target.
- **Reports:** product-recorded starts, newest first and capped at twenty by their API, with available
  role/request targets and a folder link for the complete list. A report not yet written is disabled;
  an unreadable record is distinct from no reports.
- The optional onOpenNotes callback carries the shared kind-tagged artifact target. Without a
  takeover callback the surface remains visible but opens nothing. Requirement navigation retains
  its own provider rather than being tied to the notes-folder result.

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

Shared pageParts/pageStyles block and row primitives, rather than a second private notes-heading/list style; testids follow the house
position pattern (`notes-root-count`, `notes-root-link`, `note-ref-1`, `task-reports-empty`, `task-reports-failed`, `task-reports-explorer-link`). No `note-open-*` testid exists in the carried source.

### Invariants And Boundaries

No mutation surface: the page makes one root-folder read, one reference-resolution request and,
for a task, one recorded-report list request, holding them as view state. Links are
only ever created from the server's own answers (resolved references, recorded report rows).
Resolved note references remain notes-tree targets; reserved requirement links use their separate
provider and recorded-report targets retain their role/request identity. Opening is delegated to
`onOpenNotes`, never a local
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

- Reference resolution keeps the old joined-text key and reads the current list through useEffectEvent, without treating array identity as another trigger. \[11] [10]
