# dashboard/src/panels/TaskNotes.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/TaskNotes.tsx`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T02:10+02:00                           |
| lastVerifiedCommitHash | `7c63f64935f362c418e9852bf3820a769a437f45`       |
| lastVerifiedCommitDate | 2026-07-06T01:34:58+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[overview.md](overview.md)

## Purpose

`TaskNotes.tsx` is the L9 **coordination-notes surface inside the task reader** (friction
F-M): it lists the selected master's `tasks/<repo>/<master>/notes/**` tree — `reports/`
subfolders included — and renders one opened note as formatted markdown via
`grammar/Markdown`, the same renderer the File Viewer's sidecar view uses. It also owns
the doc's **References** section so a reference string that names an existing notes file
becomes an openable link straight into the notes view (a non-matching reference stays
plain text). Rendered by `DetailPanel`'s `TaskReader` (with the doc's references) and
`MasterOverview` (list only).

## Code Commentary

### Logic

`TaskNotes({repo, master, references})` fetches `listNotes(repo, master)` on mount /
identity change (the `let live` cancellation idiom, mirroring `ChangeSetButton`), holding
`listing` + `openPath` as plain component state. An unreachable API — or a series whose
notes folder is missing (the server answers an empty list) — renders **no notes surface
at all** and leaves every reference plain text: the failure handler deliberately does not
touch state, so store-driven tests without a fetch stub stay quiet.

- **References** (`references.length > 0`): each item runs through
  `resolveNoteReference(reference, notePaths)`; a hit renders the whole reference string
  as a link-styled `<button>` (`note-ref-<n>`) that sets `openPath`; a miss renders the
  usual `<Markdown inline>` bullet.
- **Series notes** (`notes.length > 0`): one row-button per note (`note-open-<n>`,
  path + byte size), click-to-toggle; the server's `truncated` flag renders a muted
  "beyond the list cap" hint so the list never silently lies.
- **`NoteReader`** fetches `readNote` on demand and renders by `language`:
  `markdown` → `<Markdown>` inside a bounded scroll box (`note-view`, sticky head with a
  `note-close` button); other text → preformatted `<pre>`; `binary` → a
  "Binary file — N bytes (not shown)" placeholder; a failed read → "Could not load this
  note." — the download-or-skip posture, never raw bytes, never a crash. An oversize
  note shows the 2 MiB truncation banner (the DualPane wording).

### Conventions

Panda `css`/`cva` local styles mirroring `DetailPanel`'s section/heading/row idioms
(the notes row is the `sliceButton` treatment with an `open` variant); testids follow
the house position pattern (`note-open-1`, `note-ref-1`).

### Invariants And Boundaries

No mutation surface of any kind: the component only GETs and holds view state. Reference
links are only ever created from the server's own listing (`resolveNoteReference` against
fetched paths), so a link can never point outside the series' notes tree.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| A same-origin view over the local notes API; nothing crosses repositories. | — | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The data client + the pure reference resolver. | [data/notes.ts](agents-remember/dashboard/src/data/notes.ts) |
| The shared markdown renderer (the sidecar-view treatment). | [grammar/Markdown.tsx](agents-remember/dashboard/src/grammar/Markdown.tsx) |
| The task reader + master overview that mount this component. | [panels/DetailPanel.tsx](agents-remember/dashboard/src/panels/DetailPanel.tsx) |
| The serving endpoints behind the client. | [serving/notes.py](agents-remember/mcp/src/agents_remember/serving/notes.py) |
| The component test suite. | [panels/TaskNotes.test.tsx](agents-remember/dashboard/src/panels/TaskNotes.test.tsx) |

## Update History

- 2026-07-06T02:10+02:00 — Created for agent-orchestration L9 (friction F-M): the
  series-notes list + on-demand note reader (markdown formatted, text preformatted,
  binary placeholder, truncation banner) and the reference-link resolution over the
  fetched listing; unreachable API degrades to no surface with references staying plain
  text. Verification metadata pinned until closeout stamps the L9 commit.
