# dashboard/src/panels/notes-reader/NotesReaderViewer.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/notes-reader/NotesReaderViewer.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T11:50+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

### Cockpit seed fixtures

`masterDoc()` + `seedMaster()` build the one-master projection the takeover cases select a row from.
Both are **typed against the mirror, not cast**: `masterDoc()` returns a `TaskDocNode` outright (its
trailing `as unknown as TaskDocNode` is gone) and `seedMaster()`'s projection ends in
`satisfies WorkspaceProjection`. That distinction matters more here than on a shared fixture, because
these are hand-written literals — the double cast was the only thing between them and the mirror, and
it made the seed immune to contract change: a new required `Analytics` field failed fifteen other
files and not this one. `metrics` is now `metricsFor([])` rather than a hand-listed bucket literal, so
a new lifecycle state adds a required bucket that this seed derives instead of missing.
(`Analytics.agentPickups` and `.expectationRows` are optional in the mirror, which is why the
deliberately short `analytics` literal still satisfies the type.)

### Invariants And Boundaries

Fetch is stubbed per-URL (`/api/notes/list`, `/api/notes/read`; a `{repos:[]}` fallback keeps the hidden
File Viewer layer happy). No real network, no store mutation beyond the seeded projection. The seed
must stay cast-free: a fixture that cannot fail when the projection contract moves stops describing the
contract the day it moves.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| A frontend component test; nothing crosses repositories. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component under test. | "export const NotesReaderViewer = memo(NotesReaderViewerImpl)" | dashboard/src/panels/notes-reader/NotesReaderViewer.tsx:274-274 |
| The shell driven by the takeover-wiring test. | "export function CockpitShell(" | dashboard/src/cockpit/Cockpit.tsx:858-858 |
| `masterDoc` and `seedMaster` — the cast-free seed and its `satisfies WorkspaceProjection`. | `masterDoc`; `seedMaster` | dashboard/src/panels/notes-reader/NotesReaderViewer.test.tsx:188-229 |
| `TaskDocNode`, `Analytics` with its optional `agentPickups`/`expectationRows`, `WorkspaceProjection`, and `metricsFor`. | `TaskDocNode`; `Analytics`; `WorkspaceProjection`; `metricsFor` | dashboard/src/types/projection.ts:92-106; dashboard/src/types/projection.ts:340-347; dashboard/src/types/projection.ts:484-510; dashboard/src/types/projection.ts:569-581 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 5 citation items; scoped citation check now passes.

- 2026-08-01T11:50+02:00 — 260731-EFA-L4 curator (citation pass): `types/projection.ts` adopted the
  server's state partition (`LIVE_STATES` + `TERMINAL_STATES` composed into `LIFECYCLE_STATES`), moving
  every anchor below it. Re-anchored the four inline ranges in the mirror row, each on its proving
  symbol: `TaskDocNode` L381-L410 → L418-L447, `Analytics` L626-L641 → L663-L678 (optional
  `agentPickups` L670 / `expectationRows` L672), `WorkspaceProjection` L674-L689 → L711-L726, and
  `metricsFor` L213-L220 → L250-L257. Table stayed two columns; no body claim changed.

- 2026-08-01T11:45+02:00 — 260731-EFA-L4 curator: the body described the rail, content pane, back and
  takeover cases but said nothing about the projection seed those takeover cases depend on, which is
  exactly where this leaf's change landed. Added the seed-fixture section: `masterDoc()` lost its
  `as unknown as TaskDocNode` and `seedMaster()` its `as unknown as WorkspaceProjection` in favour of
  `satisfies`, and `metrics` moved from a hand-listed bucket literal to `metricsFor([])`. Checked the
  thing that could have made that consequential — whether the newly-enforced typing changed any seeded
  value the takeover assertions read. It did not: the `masterDoc` literal is unchanged field-for-field
  (the cast was gratuitous over an already-complete node), and `metricsFor([])` is a superset of the old
  six-field literal, which no assertion here reads. Also verified why the short `analytics` literal
  still compiles under `satisfies` — `Analytics.agentPickups` and `.expectationRows` are optional in the
  mirror (cit:(["agentPickups", "expectationRows"], dashboard/src/types/projection.ts:93-93; dashboard/src/types/projection.ts:97-97)) — and recorded it, since that is the one thing that would otherwise look like a
  type error. Added the cast-free-seed boundary and two two-cell reference rows (this table is
  consistently two columns; the line ranges ride inside the Finding cell rather than adding a third).

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
