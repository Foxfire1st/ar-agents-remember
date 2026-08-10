# dashboard/src/panels/notes-reader/ — Notes Reader Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/notes-reader/`             |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-08-01T13:20+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src/panels overview](../overview.md)

## Purpose

`notes-reader/` is the **Notes Reader** (agent-orchestration L17): the L9 coordination-notes reading
experience rebuilt on the SAME full-view pattern the File Viewer / Change-Set Viewer use. It is a
task-scoped **takeover** — `CockpitShell` renders it full-bleed in place of the railed Operations body — and
it is the frontend consumer of the **unchanged** L9 read-only notes API (`GET /api/notes/{list,read}`,
served by `serving/notes.py`). It reuses the L2 File Viewer content primitive (`file-viewer/DualPane`, which
itself composes `FilePane` + `grammar/Markdown`) and the L4 Change-Set Viewer takeover chrome (sticky back
header + `react-resizable-panels` rail+pane). It **replaces** the retired inline `TaskNotes` reading pane;
the compact `TaskNotes` list + resolved references remain the ENTRY surfaces that open it.

## Route Model

- `NotesReaderViewer.tsx` — the screen. LEFT RAIL = the master's notes tree from `/api/notes/list`
  (`reports/` included), one clickable row per note (path + byte size) with the open note in an amber/cyan
  **active wash** (the Change-Set Viewer row idiom); the server's `truncated` flag surfaces a muted
  "beyond the list cap" hint. CONTENT PANE = the opened note (`/api/notes/read`) rendered by **reusing
  `DualPane`**: a markdown note takes DualPane's partnerless-markdown path (the File Viewer's route-overview
  treatment), a text note renders through DualPane's `CodeSide` (read-only CodeMirror), a binary note
  degrades to the byte-count placeholder; loading/failed show a local `note-status` placeholder. The view is
  **controlled** — the open `path` + rail `onSelectNote` are lifted to `CockpitShell`, so a rail click
  switches the pane in place and the selection survives back/forward (the reader stays mounted-hidden after
  Back, like the File Viewer). A sticky back link (`notes-reader-back`) restores the railed Operations body.

260707-HFX2-L13 changes only `NotesReaderViewer.test.tsx` in this child route. Its shared `fetch`
fixture now recognizes `/api/task-document` because the surrounding detail/task-reader composition
loads the visible task body on demand before or alongside notes requests. The production Notes Reader
component, its `/api/notes/{list,read}` transport, takeover state, and `DualPane` rendering are
unchanged; the fixture branch prevents the parent reader's new request from leaking into or
invalidating the notes-specific assertions.

## Invariants And Boundaries

- Read-only over the **unchanged** L9 `/api/notes/*` server contract (allow-listing, confinement,
  binary/oversize all stay server-side); no store mutation — the screen owns its own listing/content fetch
  via `data/notes.ts`.
- **No second bespoke reader** — the content pane IS the File Viewer's `DualPane`; only the flat notes rail
  (the ChangeSetViewer column idiom) and the takeover chrome are local. Panda CSS owns looks; no CSS
  animation (GSAP/Motion only — master invariant).
- Opened as a Cockpit **takeover** (rails hidden, full-bleed), not a standing mode-bar tab; Back — or a
  mode-bar switch / a node `open()` — hides it. Unlike the Change-Set takeover, the reader is retained
  mounted-hidden (not discarded) so its listing + selection persist.

## Hot Path Summary

The Notes Reader: a `TaskNotes` list row or a resolved reference opens a full-bleed takeover — a notes-tree
rail (highlight-follows-selection, reports/ included) over the L9 `/api/notes/list` → a content pane that
reuses `DualPane` (markdown as a partnerless overview, text through CodeSide, binary placeholder) over
`/api/notes/read`; rail clicks switch the pane in place, and Back restores the railed Operations view with
the reader kept mounted-hidden so selection survives.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The read-only notes routes. | `register_notes_routes`; `list_notes`; `read_note` | mcp/src/agents_remember/serving/notes.py:101-109; mcp/src/agents_remember/serving/notes.py:112-136; mcp/src/agents_remember/serving/notes.py:168-177 |
| The same-origin notes client (`listNotes`/`readNote`/`resolveNoteReference`). | `listNotes`; `readNote`; `resolveNoteReference` | dashboard/src/data/notes.ts:32-33; dashboard/src/data/notes.ts:35-41; dashboard/src/data/notes.ts:52-65 |
| The reused File Viewer content pane (markdown/code/placeholder). | "function noteAsFileContent("; "function dualPaneProps("; "<DualPane {...dualPaneProps(note)} split={false} />" | dashboard/src/panels/notes-reader/NotesReaderViewer.tsx:118-118; dashboard/src/panels/notes-reader/NotesReaderViewer.tsx:131-131; dashboard/src/panels/notes-reader/NotesReaderViewer.tsx:196-196 |
| Cockpit defines the note-opening callback. | "const openNotes = useCallback((target: NotesReaderTarget) => {" | dashboard/src/cockpit/Cockpit.tsx:526-526 |
| Cockpit defines the note-selection callback. | "const selectNote = useCallback(" | dashboard/src/cockpit/Cockpit.tsx:533-533 |
| Cockpit renders NotesReaderViewer. | "<NotesReaderViewer" | dashboard/src/cockpit/Cockpit.tsx:590-590 |
| TaskNotes resolves a note reference into a reader target. | "const target = resolveNoteReference(reference" | dashboard/src/panels/TaskNotes.tsx:83-83 |

## Current L5I Route State

The current source-backed Notes Reader integration is recorded by the repository-local references
above.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this route against the frontend-rail change set. No route impact: NotesReaderViewer.tsx changed only by behavior-preserving lint remediation.

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-08-01T13:20+02:00 — No route impact: 260731-EFA-L4's single change under this route is
  `NotesReaderViewer.test.tsx`, and the entire diff is one import plus the two cockpit-takeover seed
  helpers — `masterDoc()` dropped its trailing `as unknown as TaskDocNode` (the literal is otherwise
  unchanged field for field; the cast was gratuitous over an already-complete node), `seedMaster()`
  swapped `as unknown as WorkspaceProjection` for `satisfies WorkspaceProjection`, and its `metrics`
  moved from a hand-listed six-field literal to `metricsFor([])`. I read the whole diff: no `it(...)`
  body, no assertion, no `/api/notes/{list,read}` or `/api/task-document` fetch-stub branch, and no
  Notes Reader source changed. The route model this overview describes is expressed nowhere in that
  seed — the takeover state, the controlled `path` + `onSelectNote` lift to `CockpitShell`, the reused
  `DualPane` content paths, and the mounted-hidden retention are all driven by props and the stubbed
  notes API; the seeded projection exists only so the Operations sidebar has one selectable master row
  for the takeover cases to click. Checked the one way the retype could have been consequential:
  `metricsFor([])` is a superset of the literal it replaced (same `lifecycleCount: 0`, `totalTokens: 0`,
  empty `stalenessHistogram`, with the per-state buckets now derived from `ACTIVE_STATES` instead of
  hand-listed), and no assertion in this file reads `metrics` at all. Suite runs green. Verification
  metadata pinned until closeout stamps the commit.

- 2026-07-24T13:17:17Z — Curator: documented the persistent-reader memo boundary. Verification
  metadata remains pre-commit.

- 2026-07-10T01:27+02:00 — No route impact: reviewed 260707-HFX2-L13's changed
  `NotesReaderViewer.test.tsx` fixture. It now serves the parent detail reader's on-demand
  `/api/task-document` request, but no Notes Reader runtime source, notes endpoint, takeover state, or
  rendering invariant changed. Verification metadata remains pinned until closeout stamps the
  eventual L13 code commit.

- 2026-07-07T18:40+02:00 — No route impact: 260703-L18 finding 2 renders the "Showing the first 2 MiB"
  truncation banner above the DualPane for a truncated markdown note (DualPane's banner lives only in
  CodeSide, which the markdown path never reaches); the Notes Reader takeover this overview describes is
  unchanged (detail in the file sidecar).
- 2026-07-07T14:00+02:00 — Created for agent-orchestration L17 (Notes reader v2): the Notes Reader child
  route — a task-scoped takeover over the unchanged L9 `/api/notes/*` API (a notes-tree rail with
  highlight-follows-selection + reports/, a content pane that REUSES `DualPane`), replacing the retired
  inline `TaskNotes` reading pane; the compact `TaskNotes` list + references stay as the entry surfaces.
  Verification metadata pinned until closeout stamps the L17 commit.
