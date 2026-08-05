# dashboard/src/panels/TaskNotes.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/TaskNotes.tsx`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-07T14:00+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

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

### Conventions

Panda `css` local styles mirroring `DetailPanel`'s section/heading/row idioms; testids follow the house
position pattern (`note-open-1`, `note-ref-1`).

### Invariants And Boundaries

No mutation surface of any kind: the component only GETs the listing and holds it as view state. Links are
only ever created from the server's own listing (`resolveNoteReference` against fetched paths), so a link can
never point outside the series' notes tree — and opening is delegated to `onOpenNotes`, never a local
write.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| A same-origin view over the local notes API; nothing crosses repositories. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The data client + the pure reference resolver. | `listNotes`, `resolveNoteReference` | dashboard/src/data/notes.ts:32-33; dashboard/src/data/notes.ts:52-65 |
| The L17 reader this surface opens (and the `NotesReaderTarget` type it passes). | `NotesReaderTarget` | dashboard/src/panels/notes-reader/NotesReaderViewer.tsx:22-26 |
| The shared markdown renderer (inline reference rendering). | `Markdown` | dashboard/src/grammar/Markdown.tsx:98-121 |
| The task reader + master overview that mount this component and thread `onOpenNotes`. | `MasterOverview`, `TaskReader` | dashboard/src/panels/DetailPanel.tsx:1029-1097; dashboard/src/panels/DetailPanel.tsx:1296-1381 |
| The serving endpoints behind the client. | `register_notes_routes` | mcp/src/agents_remember/serving/notes.py:168-177 |
| The component test suite. | "TaskNotes entry surface" | dashboard/src/panels/TaskNotes.test.tsx:38-76 |

## Update History

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 5 repository-internal references for the notes client, renderer, mounting surfaces, serving routes, and component tests; final scoped result 0 (checker-clean).

- 2026-07-07T14:00+02:00 — agent-orchestration L17: TaskNotes became the compact ENTRY SURFACE only. The
  inline `NoteReader` pane was RETIRED; the list rows and resolved references now call the new `onOpenNotes`
  callback to open the L17 Notes Reader takeover (with the whole notes tree in its rail). The note-content
  rendering tests (markdown/text/binary/truncation) moved to `notes-reader/NotesReaderViewer.test.tsx`;
  `TaskNotes.test.tsx` now asserts the entry callbacks. Verification metadata pinned until closeout stamps
  the L17 commit.
- 2026-07-06T02:10+02:00 — Created for agent-orchestration L9 (friction F-M): the
  series-notes list + on-demand note reader (markdown formatted, text preformatted,
  binary placeholder, truncation banner) and the reference-link resolution over the
  fetched listing; unreachable API degrades to no surface with references staying plain
  text. Verification metadata pinned until closeout stamps the L9 commit.
