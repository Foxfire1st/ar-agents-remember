# dashboard/src/panels/notes-reader/NotesReaderViewer.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/notes-reader/NotesReaderViewer.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T01:14+02:00                           |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`       |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[overview.md](overview.md)

## Purpose

Vitest + Testing Library coverage for the L17 Notes Reader. It covers the two leaf-required axes plus the
content pane and the cockpit takeover wiring, and it absorbs the note-CONTENT rendering cases (markdown /
text fallback / binary placeholder) that used to live in `TaskNotes.test.tsx` before the inline reader was
retired.

## Code Commentary

### 260707-HFX2-L13 Fetch-Fixture Compatibility

The notes-reader fetch stub now serves `/api/task-document` before its notes list/read branches. The
notes viewer embeds task-reader flows whose `DetailPanel` dependency fetches full task bodies on
demand, so this branch preserves the suite's isolation while leaving notes API assertions unchanged.

### Logic

- **Rail** — lists the master's notes (reports/ included) with the open note highlighted; the highlight
  follows the controlled `path` prop (rerender moves `data-active`); a rail click calls `onSelectNote`.
- **Content pane** — a markdown note renders formatted through the reused `DualPane` sidecar (`sidecar-pane`);
  a text note renders through the shared file pane (`file-pane`); a binary note degrades to DualPane's
  `pane-placeholder`. The CodeMirror leaf `../file-viewer/FilePane` is `vi.mock`ed to a `<pre>` — the house
  jsdom accommodation (mirrors `ChangeSetViewer.test` mocking `ChangeSetPane`). Since 260703-L18
  (finding 2, the L17R-2 remedy): a `truncated: true` MARKDOWN note renders the "Showing the first
  2 MiB" banner above the DualPane, and the negative case pins that a non-truncated markdown note
  renders no banner.
- **Back** — `notes-reader-back` calls `onBack`.
- **Cockpit takeover** — renders `CockpitShell`, asserts the reader is absent initially (rails intact), then
  drives select-master → open-note → **Back** → re-open and asserts the reader node is the SAME element
  (hidden-not-unmounted → selection survives back/forward, the File Viewer property).

### Invariants And Boundaries

Fetch is stubbed per-URL (`/api/notes/list`, `/api/notes/read`; a `{repos:[]}` fallback keeps the hidden
File Viewer layer happy). No real network, no store mutation beyond the seeded projection.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| A frontend component test; nothing crosses repositories. | — | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The component under test. | [notes-reader/NotesReaderViewer.tsx](agents-remember/dashboard/src/panels/notes-reader/NotesReaderViewer.tsx) |
| The shell driven by the takeover-wiring test. | [cockpit/Cockpit.tsx](agents-remember/dashboard/src/cockpit/Cockpit.tsx) |

## Update History

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13: extended the notes-reader fetch fixture for the
  on-demand task-document body endpoint used by the embedded detail reader. Verification metadata
  remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-07T20:50+02:00 — agent-orchestration L18 (finding 2 / L17R-2 remedy): added the
  truncated-markdown banner cases — `truncated: true` markdown renders the first-2-MiB banner above
  the DualPane; the negative case pins no banner on non-truncated markdown. Verification metadata
  pinned until closeout stamps the L18 commit.
- 2026-07-07T14:00+02:00 — Created for agent-orchestration L17: rail listing + highlight-follows-selection,
  rail-click switch, markdown/text/binary content rendering (FilePane mocked), back, and the CockpitShell
  takeover open→back→reopen survival test. Verification metadata pinned until closeout stamps the L17 commit.
