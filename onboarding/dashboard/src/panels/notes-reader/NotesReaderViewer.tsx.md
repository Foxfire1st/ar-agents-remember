# dashboard/src/panels/notes-reader/NotesReaderViewer.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/notes-reader/NotesReaderViewer.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[overview.md](overview.md)

## Purpose

`NotesReaderViewer.tsx` is the **Notes Reader** screen (agent-orchestration L17): the L9 coordination-notes
reading experience rebuilt on the SAME full-view pattern the Change-Set / File Viewer use. It is a
task-scoped **takeover** whose LEFT RAIL is the master's notes tree (from `/api/notes/list`, `reports/`
included) with the open note highlighted, and whose content pane renders the opened note by **reusing the
File Viewer's `DualPane` primitive**. It replaces the retired inline `TaskNotes` reading pane; the compact
`TaskNotes` list + resolved references stay as the ENTRY surfaces that open this reader.

## Code Commentary

### Logic

`NotesReaderViewer({repo, master, path, onSelectNote, onBack})` is a **controlled** component — the open
`path` and rail `onSelectNote` are lifted to `CockpitShell` (like the File Viewer's persisted state) so a
selection survives back/forward.

- Fetches the rail listing with `listNotes(repo, master)` on `(repo, master)` change (the `let live`
  cancellation idiom; an unreachable API leaves an empty rail, never a crash).
- Fetches the open note with `readNote(repo, master, path)` on `(repo, master, path)` change — `null` while
  loading, `failed` on a read error. Changing `path` (a rail click or a fresh entry) re-fetches → the
  "switch the pane in place" behavior.
- **Rail** — the ChangeSetViewer changed-files column idiom: a sticky `notes (n)` head + one `<button>` per
  note (`note-rail-<n>`, path + byte size), `data-active` on the row whose path is open (the amber/cyan
  wash), a click calls `onSelectNote(entry.path)`, and the server's `truncated` flag renders a muted
  "beyond the list cap" hint.
- **Content pane** reuses `DualPane` via `dualPaneProps(note)`: a **markdown** note takes DualPane's
  partnerless-markdown path (`code=null`, `sidecar={state:"markdown"}`) — the exact treatment the File
  Viewer gives a partnerless route overview; a **text** note becomes a synthetic `FileContent`
  (`noteAsFileContent`) rendered through DualPane's `CodeSide` (read-only CodeMirror); a **binary** note
  degrades to DualPane's byte-count placeholder. Loading/failed render a local `note-status` placeholder
  (a distinct testid from DualPane's `pane-placeholder` so a binary note's placeholder is unambiguous).
- **Truncation banner** (260703-L18 finding 2): DualPane's "Showing the first 2 MiB" banner lives only in
  `CodeSide`, which the markdown path never reaches — so a truncated MARKDOWN note (the dominant note type)
  would silently drop the truncation contract. When `note.truncated && note.language === "markdown"` the
  view renders the same banner (`notes-trunc-banner`, matching CodeSide's wording/style) ABOVE the DualPane;
  text notes keep CodeSide's own banner.

### Conventions

Panda `css` local styles mirroring the `ChangeSetViewer` takeover chrome (screen · sticky back header ·
`react-resizable-panels` rail+pane). Testids: `notes-reader-viewer` (screen), `notes-reader-back`,
`notes-reader-open` (the open path in the header), `notes-rail`, `note-rail-<n>`, `note-status`.

### Invariants And Boundaries

GET-only over the unchanged L9 `/api/notes/*` server contract (allow-listing, confinement, binary/oversize
all stay server-side). No store mutation. There is **no second bespoke reader** — the content pane is the
File Viewer's `DualPane`, and the only file-viewer leaf stubbed in tests is `FilePane` (the CodeMirror
editor), the same jsdom accommodation the Change-Set Viewer tests make for `ChangeSetPane`.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| A same-origin view over the local notes API; nothing crosses repositories. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The reused File Viewer content pane (markdown/code/placeholder). | "export type SidecarView" | dashboard/src/panels/file-viewer/DualPane.tsx:14-14 |
| The `FileContent` type the text path maps a note into. | `FileContent` | dashboard/src/data/files.ts:51-59 |
| The L9 notes client (`listNotes`/`readNote`) this view consumes. | "export interface NoteEntry" | dashboard/src/data/notes.ts:10-10 |
| The shell that hosts the takeover + lifts its selection. | "export type CockpitView" | dashboard/src/cockpit/Cockpit.tsx:65-65 |
| The entry surface (compact list + references) that opens this reader. | "export function TaskNotes" | dashboard/src/panels/TaskNotes.tsx:146-146 |
| The unchanged L9 serving endpoints behind the client. | "def _walk_notes" | mcp/src/agents_remember/serving/notes.py:70-70 |
| The component test suite. | "function stubNotesApi" | dashboard/src/panels/notes-reader/NotesReaderViewer.test.tsx:29-29 |

## Current L5I Maintenance

The controlled Notes Reader is memoized as a persistent cockpit view. Shell view switches with
unchanged route props no longer reconstruct its reader subtree, while its own selected-note state
and data reads remain unchanged.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-24T13:17:17Z — Curator: documented the persistent-reader memo boundary; verification
  fields remain pre-commit.

- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, finding 2): render the "Showing the first 2 MiB"
  truncation banner (`notes-trunc-banner`) above the DualPane when a note is `truncated && markdown` —
  DualPane's banner lives only in `CodeSide`, which markdown (the dominant note type) never reaches, so the
  banner is added here for that case (CodeSide's exact wording/style). Component test asserts the banner
  for a truncated markdown note and its absence for a normal one. Verification metadata pinned until
  closeout stamps the L18 commit.
- 2026-07-07T14:00+02:00 — Created for agent-orchestration L17: the Notes Reader takeover on the file-viewer
  chrome — a notes-tree rail (highlight-follows-selection, reports/ included) + a content pane that REUSES
  `DualPane` (markdown as a partnerless overview, text through CodeSide, binary placeholder). Controlled by
  `CockpitShell` (selection lifted so it survives back/forward). Server contract unchanged. Verification
  metadata pinned until closeout stamps the L17 commit.
