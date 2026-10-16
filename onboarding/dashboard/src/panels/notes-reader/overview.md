# dashboard/src/panels/notes-reader/ — Notes Reader Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/notes-reader/`             |

## Governing Overview

[dashboard/src/panels overview](../overview.md)

## Purpose

`notes-reader/` provides the task-artifact reading screen: coordination notes, registered requirement packets, recorded task reports, supplied role reports, and the whole decision log. Cockpit opens the task-artifact screen as a full-bleed takeover. The compact `TaskNotes` surface remains an entry point through its Notes explorer link, resolved references, and recorded reports; task-reader prose can open registered requirements through the same takeover.

The screen shares the File Viewer's `DualPane` content primitive and the rail-and-pane layout pattern used by the Change-Set Viewer. Notes and requirements have selection rails; reports and the whole decision log use the content area without a rail.

## Hot Path Summary

The whole decision log shares the task-page authored row, newest-first recorded-time ordering and oldest-based authored numbering. Product records contribute to neither authored counts nor numbers; a muted counted end disclosure retains them unnumbered. Exact/prefix text provenance remains classification, not an impossibility guarantee against authored collisions.

An entry surface opens a typed artifact target in Cockpit. Notes load folders lazily through `ExplorerTree`; requirements load their task-document-selected flat listing. Selection updates the controlled target and fetches the selected content for `DualPane`. Recorded reports fetch their scoped report, supplied reports render directly, and decisions render their supplied log. The screen header and `data-artifact-kind` identify the artifact kind; Back hides the retained takeover.

## Construction

`NotesReaderViewer.tsx` dispatches the discriminated `TaskArtifactReaderTarget`. `useNotesFolderCache.ts` owns the retained folder store, stable paging callbacks, fill/vanish recovery and LRU protection; NotesTree wires it to the shared ExplorerTree. Notes use `data/notes.ts` to request one folder at a time from `/api/notes/folder` and an opened file from `/api/notes/read`. Reference resolution belongs to the entry surface and uses one `POST /api/notes/resolve` request for the document's references. Requirements use `data/requirements.ts` and the target's task-document selector to call `/api/requirements/list` and `/api/requirements/read`.

The notes rail reuses `ExplorerTree`. It opens ancestors of the selected note, fetches successive folder parts until that note is found or the folder is exhausted, and offers a synthetic row to load another part. A vanished folder clears its cached entries and preserves the server's reason. The folder cache refreshes access order and attempts least-recently-used eviction above 32 folders, protecting the open note's ancestor folders and the folder being inserted. It can exceed 32 when no eligible eviction candidate remains. Requirements use a separate flat button rail populated from their listing.

Fetched notes, requirements, and reports share `DualPane`: markdown occupies its partnerless markdown pane, other text uses its read-only `FilePane`, and binary content produces a byte-count placeholder. `NotePane` supplies local failure and empty/loading placeholders and adds the truncation banner for truncated markdown.

A `task-report` target fetches its recorded report through `readRoleReport`, using the role, request ID, and task-document reference. A supplied `role-report` renders the content already passed to the component. The decisions target renders the supplied whole log, with authored rows newest-first and product records in a separate muted counted end disclosure.

Cockpit owns the target and selection callbacks. Selecting a note clears folder-open mode; selecting a requirement changes its path. Back hides the takeover without clearing its target, and Cockpit retains the reader mounted with `display: none`. A mode-bar change, node opening, or Change-Set opening also hides it. Retention preserves component state while that reader remains mounted; it is not browser-history persistence.

The local notes API fixture recognizes `/api/task-document`, looks up the requested path in the dashboard's native `tasks` map and returns that entry's `summary`, or a 404 with null when it is absent. The cockpit fixture is seeded through the shared `projection`, `taskEntry` and `taskSummary` builders with a native reference, stage and activity; it does not rebuild an analytics.taskDocuments/series world or supply a fallback master for an unknown path. This describes fixture construction, not the production endpoint contract or executed verification.

## Invariants And Boundaries

- The notes routes read coordination files without mutating them. Server-side selector checks and path confinement govern access; folder replies have stable ordering and at most 200 entries per part, and note content is binary-tolerant and capped for display at 2 MiB. The extracted cache owns folder reads and the screen keeps content reads via `data/notes.ts`, rather than mutating the dashboard store.
- Notes, requirements, and report content reuse `DualPane`; the decisions log has its own list rendering. The notes tree reuses `ExplorerTree`, while requirements have a flat rail. There is no second bespoke notes content reader or notes tree.
- Requirement references resolve against registered requirement entries before notes references are considered. A reference containing a requirement address cannot fall through to a note target.
- The reader uses Panda CSS for its local styling. Its header contains the Back button; the note rail header is sticky. The inherited intent is no CSS animation (GSAP/Motion only); the reused DualPane currently has a CSS background transition. This is an implementation/intent discrepancy, not authority here to withdraw that wider policy.
- Kind-aware screen headings and open-path labels do not imply fully kind-aware status text: `NotePane` still says “Select a note from the tree.” when content is absent, and its failure text distinguishes notes from everything else as “requirement.”

## Retained Status Metadata

The current source-backed Notes Reader integration is recorded by the repository-local references below. This retained status sentence does not establish a verified lifecycle or review state.

## Evidence

- The read-only notes routes. [1]
- The same-origin notes client (`listFolder`/`readNote`/`resolveNoteReferences`). [2]
- The reused File Viewer content pane maps both notes and requirement packets to markdown/code/placeholder rendering. [3]
- Cockpit defines the note-opening callback. [4]

- Cockpit defines the note-selection callback. [5]

- Cockpit renders NotesReaderViewer. [6]
- TaskNotes resolves registered requirement references first; a requirement address never falls through to a note target. [7]

- The task-body fixture returns the path-addressed native entry summary or 404; the cockpit seed uses canonical native wire fixture builders. [8]
