# dashboard/src/panels/notes-reader/NotesReaderViewer.test.tsx

## Governing Overview

[overview.md](overview.md)

## Purpose

Vitest + Testing Library coverage for the L17 Notes Reader. It covers the two leaf-required axes plus the
content pane and the cockpit takeover wiring, and it absorbs the note-CONTENT rendering cases (markdown /
text fallback / binary placeholder) that used to live in `TaskNotes.test.tsx` before the inline reader was
retired.


## 260831-CCR-L23 Requirements-Artifact Cases

L23 re-tagged every existing render with `kind="notes"` and added a
`requirements artifact reader` describe block: a stub serving
`/api/requirements/{list,read}` proves the viewer shows the requirements root
(`data-artifact-kind="requirements"`, title `requirements · <master>`,
open-path `requirements/<path>`) and renders the exact selected packet's markdown
over the real `/api/requirements/read` URL.

## Role-Report Kind Case

The suite also renders the `role-report` kind and pins that the supplied report's body, file name and
truncation notice appear in the shared pane with no rail (MIK-R75 rule 4).

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

Fetch is stubbed per-URL (`/api/notes/list`, `/api/notes/read`; a `{repos:[]}` fallback keeps the hidden
File Viewer layer happy). No real network, no store mutation beyond the seeded projection. The seed
must stay cast-free: a fixture that cannot fail when the projection contract moves stops describing the
contract the day it moves.

## Evidence

### Cross-Repo References

No meaningful cross-repo references found.

A frontend component test; nothing crosses repositories.

### Repo-Internal References

- The component under test. [1]
- The shell driven by the takeover-wiring test. [2]
- `masterDoc` and `seedMaster` — the cast-free seed and its `satisfies WorkspaceProjection`. [3]
- The seed task document is checked against the generated TaskDocNode. [4]
- Analytics requires agentPickups and expectationRows arrays, along with the other projected collections. [5]
- The seeded snapshot satisfies the generated workspace contract. [6]
- The seed derives metrics through the shared lifecycle rollup helper. [7]
