# dashboard/src/panels/TaskNotes.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/TaskNotes.test.tsx`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-07T14:00+02:00                           |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`       |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
| governingOverview      | `overview.md`                                    |

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

### Conventions

Fetch is stubbed per test (never a live server); assertions target testids
(`note-open-<n>`, `note-ref-<n>`) and the `onOpenNotes` callback payload, never
implementation internals — the `note-view`/`note-close` testids left with the inline
reader.

### Invariants And Boundaries

The suite pins the no-mutation posture indirectly: every interaction is a GET-backed
render or a callback dispatch; there is nothing to submit, and nothing here reads
`/api/notes/read`.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| A stubbed-fetch component suite; nothing crosses repositories. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component under test. | `TaskNotes` | dashboard/src/panels/TaskNotes.tsx:73-161 |
| The listing entry type shaped by the suite's stub payload. | `NoteEntry` | dashboard/src/panels/TaskNotes.test.tsx:13-15; dashboard/src/data/notes.ts:10-15 |
| The component suite's `stubNotesApi` returns the directly evidenced listing payload. | `stubNotesApi` | dashboard/src/panels/TaskNotes.test.tsx:18-30 |
| The moved note-content suite (markdown, text fallback, binary placeholder, truncation) covering the reader this surface opens. | "NotesReaderViewer content pane (reuses the File Viewer DualPane)" | dashboard/src/panels/notes-reader/NotesReaderViewer.test.tsx:110-179 |

## Update History

- 2026-08-04T16:40:00+02:00 — 260731-EFA-L6 S18-B12 curator correction (reviewer-BLOCK repair): narrowed the stub-shape claim to `NoteEntry` (bound to the suite's `entry()` use and the type definition) and the directly evidenced listing payload; `NoteContent` removed from this test's claim; moved note-reader ownership retained; the scoped fixer confirmed the final ranges with no writes.
- 2026-07-07T14:00+02:00 — agent-orchestration L17: rewritten to the entry-surface contract — the list +
  resolved references now assert the `onOpenNotes` callback (with `{repo, master, path}`) instead of an
  inline `note-view`. The note-CONTENT tests (formatted markdown, preformatted text, binary placeholder,
  truncation, close) were MOVED to `notes-reader/NotesReaderViewer.test.tsx` with the retired inline reader.
  Verification metadata pinned until closeout stamps the L17 commit.
- 2026-07-06T02:20+02:00 — Created for agent-orchestration L9: 8 component tests over
  the notes list (subfolders, depth-cap hint), the note reader modes (formatted
  markdown, preformatted text, binary placeholder, close toggle), the unreachable-API
  degrade, and reference-link resolution (match opens the note; non-match stays plain).
  Verification metadata pinned until closeout stamps the L9 commit.
