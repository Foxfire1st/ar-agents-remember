# dashboard/src/panels/notes-reader/NotesReaderViewer.test.tsx

## Governing Overview

[notes-reader/ overview](overview.md)

## Purpose

`NotesReaderViewer.test.tsx` proves the notes-reader takeover: the reader appears only when a note is
opened, keeps the Operations rails while hidden, and stays mounted across Back and Forward like the
File Viewer.

## 260831-CCR-L23 Requirements-Artifact Cases

L23 re-tagged every existing render with `kind="notes"` and added a
`requirements artifact reader` describe block: a stub serving
`/api/requirements/{list,read}` proves the viewer shows the requirements root
(`data-artifact-kind="requirements"`, title `requirements · <master>`,
open-path `requirements/<path>`) and renders the exact selected packet's markdown
over the real `/api/requirements/read` URL.

## L126 Folder-Tree, Paging, Whole-Log and Task-Report Cases

Since L126 the suite additionally pins the one-folder-at-a-time tree and its
transports; the flat-list rail and `/api/notes/list` fetch prose below is
superseded for these cases (retained as history where it describes unchanged
takeover/content-pane behavior):

- **Tree** — one-level tree with closed folders on open; expand loads a folder's
  children; folders over the part ceiling show a next-part row; deep paths open
  to the note with the way folders open and the note marked.
- **Fill/vanish/cache** — fill-to-note, vanish (twice), and LRU-plus-pin cache
  cases.
- **Whole log** — two authored rows use shared numbering (`#2`, `#1`), short times, formatted decision/rationale and reading/block classes. Product records remain in a closed muted disclosure at the end, and opening it creates no authored decision row. Input bytes stay unchanged, fetch is not called and Back invokes the supplied callback. Empty, records-only and authored-only inputs assert row/disclosure presence. The mixed fixture is reversed into descending time order; the former independently unsorted whole-log case was removed, so this suite no longer independently establishes storage-order independence.
- **Folder callback stability** — an unrelated rerender does not refetch a retained folder; expanding another folder still performs the demanded load.
- **Task-report read** — exact task-report read by recorded identity; existing
  role-report preservation kept.
- **Transport** — folder (`/api/notes/folder`), read (`/api/notes/read`),
  single-request resolve (`/api/notes/resolve`), and reports
  (`/api/role-launch/reports`); no route walks the tree.

## Role-Report Kind Case

The suite also renders the `role-report` kind and pins that the supplied report's body, file name and
truncation notice appear in the shared pane with no rail (MIK-R75 rule 4).

## Code Commentary

### Logic

The two cases that assert the reader is absent initially and survives Back now mount
`CockpitShell initialView="operations"` because MIK-R79 made Chats the opening view. The reader
behavior asserted (absence, rails, mounted identity across Back) is unchanged.

### Conventions

Vitest + Testing Library; the notes API is stubbed per case.

### Invariants And Boundaries

The cases bind the notes reader's takeover and keep-alive behavior on the Operations context; they do
not assert the product tab list.

### Todos

No additional work is asserted by this card.

### 260707-HFX2-L13 Fetch-Fixture Compatibility

The notes-reader fetch stub now serves `/api/task-document` before its notes folder/read branches. The
notes viewer embeds task-reader flows whose `DetailPanel` dependency fetches full task bodies on
demand, so this branch preserves the suite's isolation while leaving notes API assertions unchanged.
(The `notes list/read branches` wording of the earlier era now reads folder/read; resolve and
reports branches serve the reference and report cases.)

### Logic

- **Rail** — one folder's entries at a time (the open folder's files and
  subfolders), with the open note highlighted; the highlight
  follows the controlled `path` prop (rerender moves `data-active`); a rail click calls `onSelectNote`.
  (The flat whole-list rail prose of the earlier era is superseded; see the L126
  section above.)
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

### Cockpit seed fixtures

`masterDoc()` + `seedMaster()` build the one-master projection the takeover cases select a row from.
Both are **typed against the mirror, not cast**: `masterDoc()` returns a `TaskDocNode` outright (its
trailing `as unknown as TaskDocNode` is gone) and `seedMaster()`'s projection ends in
`satisfies WorkspaceProjection`. That distinction matters more here than on a shared fixture, because
these are hand-written literals — the double cast was the only thing between them and the mirror, and
it made the seed immune to contract change: a new required `Analytics` field failed fifteen other
files and not this one. `metrics` is now `metricsFor([])` rather than a hand-listed bucket literal, so
a new lifecycle state adds a required bucket that this seed derives instead of missing.
`Analytics.agentPickups` and `.expectationRows` are required in the current generated mirror.
The local `seedMaster` literal supplies both as empty arrays, so it remains checked against
that contract.

### Invariants And Boundaries

Fetch is stubbed per-URL (folder `/api/notes/folder`, read `/api/notes/read`,
single-request resolve `/api/notes/resolve`, reports `/api/role-launch/reports`;
a `{repos:[]}` fallback keeps the hidden File Viewer layer happy). No real
network, no store mutation beyond the seeded projection. The seed
must stay cast-free: a fixture that cannot fail when the projection contract moves stops describing the
contract the day it moves. (The `/api/notes/list` fetch prose of the earlier
era is superseded; see the L126 section above.)

## Evidence

### Docs References

No domain documentation source is configured for this repository. The requirement packet
`MIK-R79@v1` (rule 16) fixes the opening view; it lives outside the code and memory repositories, so
it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Cross-Repo References

No cross-repo boundary is crossed by this file.

No meaningful cross-repo references found.

A frontend component test; nothing crosses repositories.

### Repo-Internal References


- Current whole-log assertions cover authored numbering/times/formatted text/rationale, muted counted product-record end disclosure, input preservation and no fetch; seeded cases are not execution. [8]


- The viewer routes takeover content through the shared pane without a second reader. [9]

- The current viewer integrates the extracted folder cache while retaining content kinds. [17]
- The shell driven by the takeover-wiring test. [18]
- `masterDoc` and `seedMaster` — the cast-free seed and its `satisfies WorkspaceProjection`. [19]
- The cast-free seed is typed against generated TaskDocNode; optional new task fields do not make omitted seed properties runtime-null values. [20]

- Analytics requires agentPickups and expectationRows arrays, along with the other projected collections. [21]
- The seeded snapshot satisfies the generated workspace contract. [22]
- The seed derives metrics through the shared lifecycle rollup helper. [23]
