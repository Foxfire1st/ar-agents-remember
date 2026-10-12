# dashboard/src/panels/TaskNotes.test.tsx

## Governing Overview

[overview.md](overview.md)

## Purpose

`TaskNotes.test.tsx` is the component suite for the notes ENTRY surface (`TaskNotes.tsx`
after L17): the Notes line, reference-link resolution and recorded reports, plus the contract that
opening a note delegates to the notes-reader takeover via the `onOpenNotes` callback — the
inline reading pane is retired, and note-content rendering is covered by
`notes-reader/NotesReaderViewer.test.tsx`.

## Code Commentary

### Logic

Testing-library component tests in the `DetailPanel.test.tsx` idiom (render + fireEvent +
`findBy*`, cleanup/`vi.unstubAllGlobals` after each). `stubNotesApi(entries, resolutions,
reports)` stubs `fetch` for `/api/notes/folder` (the seeded top folder), `/api/notes/resolve`
and the reports route — the entry surface never fetches note content
(`/api/notes/read` belongs to the reader since L17); every other URL answers a `404
not-found` in the serving status idiom.

- **entry surface** — the Notes line names the top-folder count with a link opening the
  reader at the notes root; no note rows are drawn and no tree total is computed. An
  unreachable API renders no notes surface and the reference stays plain text.
- **reference resolution** — a reference naming an existing notes file renders as a
  `<button>` link (`note-ref-1`) whose click fires `onOpenNotes` with the resolved path; a
  code-path reference stays plain text with no link testid, asserted only after the
  resolve answer has arrived so resolution is settled.
- **request-key stability** — equal-content array rerenders do not send another resolution POST;
  changing the joined content sends the current list. The F9 regression separately pins the historical
  joined-key collision: `[]` and `[""]` share a key, so the new empty-text row appears without a second
  resolution request. The earlier different-content-to-empty-text case does send a request; it is not
  the same transition.
- **recorded reports** — the task's recorded starts render newest-first capped at twenty
  with the explorer link; an unreadable record keeps the Notes link.


## 260831-CCR-L23 Kind-Tagged Open Payloads

L23 advanced the suite's `onOpenNotes` expectations to the discriminated
artifact target: note rows and resolved note references now fire
`{ kind: "notes", repo, master, path }` (the `kind` tag was added to every
asserted payload).

### Conventions

Fetch is stubbed per test (never a live server); assertions target testids
(`note-open-<n>`, `note-ref-<n>`) and the `onOpenNotes` callback payload, never
implementation internals — the `note-view`/`note-close` testids left with the inline
reader.

### Invariants And Boundaries

The suite pins a read-only view: folder/report reads and the reference-resolution POST obtain
view data, while clicks dispatch callbacks. The POST resolves references; it is not document
mutation. Nothing here reads `/api/notes/read`, which belongs to the reader.

## Evidence

### Cross-Repo References

No meaningful cross-repo references found.

A stubbed-fetch component suite; nothing crosses repositories.

### Repo-Internal References

- The component under test. [1]
- The folder entry type shaped by the suite's stub payload. [2]
- The component suite's `stubNotesApi` returns the directly evidenced folder payload. [3]
- The moved note-content suite covering the reader this surface opens. [4]

- Equal content does not repeat resolution; changing content posts the current list, while the empty-list to one-empty-text regression retains the historical joined-key equivalence. \[5] [5]
