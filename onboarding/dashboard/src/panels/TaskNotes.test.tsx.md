# dashboard/src/panels/TaskNotes.test.tsx

## Governing Overview

[overview.md](overview.md)

## Purpose

`TaskNotes.test.tsx` is the component suite for the notes ENTRY surface (`TaskNotes.tsx`
after L17): the series-notes listing and reference-link resolution, plus the contract that
opening a note delegates to the notes-reader takeover via the `onOpenNotes` callback — the
inline reading pane is retired, and note-content rendering is covered by
`notes-reader/NotesReaderViewer.test.tsx`.

## Code Commentary

### Logic

Testing-library component tests in the `DetailPanel.test.tsx` idiom (render + fireEvent +
`findBy*`, cleanup/`vi.unstubAllGlobals` after each). `stubNotesApi(notes, truncated)`
stubs `fetch` for `/api/notes/list` only — the entry surface never fetches note content
(`/api/notes/read` belongs to the reader since L17); every other URL answers a `404
not-found` in the serving status idiom.

- **entry surface** — the listing renders `reports/` subfolder entries; clicking a list
  row fires `onOpenNotes` with `{repo, master, path}` (the notes-reader takeover) instead
  of rendering anything inline; a `truncated: true` listing shows the depth-cap hint; an
  unreachable API renders no notes surface and the reference stays plain text.
- **reference resolution** — a reference naming an existing notes file renders as a
  `<button>` link (`note-ref-1`) whose click fires `onOpenNotes` with the resolved path; a
  code-path reference stays plain text with no link testid, asserted only after the
  listing has arrived so resolution is settled.


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

The suite pins the no-mutation posture indirectly: every interaction is a GET-backed
render or a callback dispatch; there is nothing to submit, and nothing here reads
`/api/notes/read`.

## Evidence

### Cross-Repo References

No meaningful cross-repo references found.

A stubbed-fetch component suite; nothing crosses repositories.

### Repo-Internal References

- The component under test. [1]
- The listing entry type shaped by the suite's stub payload. [2]
- The component suite's `stubNotesApi` returns the directly evidenced listing payload. [3]
- The moved note-content suite (markdown, text fallback, binary placeholder, truncation) covering the reader this surface opens. [4]
