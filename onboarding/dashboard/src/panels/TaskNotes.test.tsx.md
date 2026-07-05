# dashboard/src/panels/TaskNotes.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/TaskNotes.test.tsx`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T02:20+02:00                           |
| lastVerifiedCommitHash | `7c63f64935f362c418e9852bf3820a769a437f45`       |
| lastVerifiedCommitDate | 2026-07-06T01:34:58+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[overview.md](overview.md)

## Purpose

`TaskNotes.test.tsx` is the component suite for the L9 notes view (`TaskNotes.tsx`): the
series-notes listing, the opened-note rendering modes, and reference-link resolution.

## Code Commentary

### Logic

Testing-library component tests in the `DetailPanel.test.tsx` idiom (render + fireEvent +
`findBy*`, cleanup/`vi.unstubAllGlobals` after each). `stubNotesApi(notes, contents,
truncated)` stubs `fetch` per URL — `/api/notes/list` answers the seeded listing,
`/api/notes/read` the seeded per-path content or a `404 not-found`, matching the serving
status idiom rather than an invented mock shape.

- **list + reader** — the listing renders `reports/` subfolder entries; opening a note
  renders formatted markdown (`**F-M**` becomes a real `<strong>`, the raw pipes/stars
  are gone) and the close button collapses it; a binary note degrades to the byte-count
  placeholder; a non-markdown text note renders inside `<pre>`; a `truncated: true`
  listing shows the depth-cap hint; an unreachable API renders no notes surface and the
  reference stays plain text.
- **reference resolution** — a reference naming an existing notes file renders as a
  `<button>` link (`note-ref-1`) that opens the note view with its fetched body; a
  code-path reference stays plain text with no link testid, asserted only after the
  listing has arrived so resolution is settled.

### Conventions

Fetch is stubbed per test (never a live server); assertions target testids
(`note-open-<n>`, `note-ref-<n>`, `note-view`, `note-close`) and rendered DOM tags,
never implementation internals.

### Invariants And Boundaries

The suite pins the no-mutation posture indirectly: every interaction is a GET-backed
render; there is nothing to submit.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| A stubbed-fetch component suite; nothing crosses repositories. | — | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The component under test. | [panels/TaskNotes.tsx](agents-remember/dashboard/src/panels/TaskNotes.tsx) |
| The data types the stubs shape. | [data/notes.ts](agents-remember/dashboard/src/data/notes.ts) |
| The sibling panel suite whose render/fireEvent idiom this mirrors. | [panels/DetailPanel.test.tsx](agents-remember/dashboard/src/panels/DetailPanel.test.tsx) |

## Update History

- 2026-07-06T02:20+02:00 — Created for agent-orchestration L9: 8 component tests over
  the notes list (subfolders, depth-cap hint), the note reader modes (formatted
  markdown, preformatted text, binary placeholder, close toggle), the unreachable-API
  degrade, and reference-link resolution (match opens the note; non-match stays plain).
  Verification metadata pinned until closeout stamps the L9 commit.
