# dashboard/src/data/changeset.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/changeset.ts`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-22T11:00:00+02:00 |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`       |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Same-origin browser client for the L3 read-only change-set API. It exposes typed helpers over the three
GET endpoints (`/api/changeset/task`, `/file-diff`, `/master`), returns camelCase-typed results, and
reuses `data/files.ts`'s shared transport (`getJson`/`qs`) so the serving error idiom (a thrown
`FilesApiError`) is mapped once. It holds no state — the Change-Set Viewer owns its component state and
calls these helpers directly.

## Code Commentary

### Logic

`masterChangeset` accepts typed options and serializes `includeLeaves=false`
when a caller needs only the coherent series net range. The default remains
the full response with per-leaf summaries, preserving callers that inspect
that breakdown.

### 260921-ICR-L13 — Generation pins and the published generation

The master client is now generation-bound. `MasterNetPins` (four optional wire params —
`codeBase`/`codeTip`/`memoryBase`/`memoryTip`) freezes a request to the listed generation;
unset pins are omitted from the query so the request selects the declared integrated result.
`MasterNetGeneration` (four commits + `digest`) is what the list response publishes, beside
`currentness` and `scope: "integrated"`; leaf rows carry optional
`state: "committed" | "working"`. cit:(["export interface MasterChangeset {"], dashboard/src/data/changeset.ts:59-59)
`masterChangeset` threads `options.pins` into the params; `masterFileDiff` takes `pins` so an
opened entry stays bound to its generation after the branch advances. This leaf only exposes
the pins and the per-view generation for R24's catalogue/drill-down to build on — no
catalogue or drill-down is implemented here.

Data contracts plus three fetch helpers:

- Result interfaces mirror the L3 JSON shape one-for-one: `ChangedFile` (`insertions`/`deletions` are
  `null` for binary; `status` is the git letter A/M/D/R; `hasSidecar?` on code files drives the L4
  code→sidecar split), `ChangeCounters` (`files`/`insertions`/`deletions`), `TaskChangeset`
  (`code`/`memory` + `counters`), `FileDiff` (`before`/`after` = `{content}` or `null` for an
  added/deleted file — feeds CodeMirror MergeView a/b), `MasterChangeset` (`leaves[]` per-leaf counters +
  the NET series `code`/`memory` as plain `ChangedFile[]` + `counters`) (cit:(["export interface MasterChangeset {"], dashboard/src/data/changeset.ts:45-45)).
- `taskChangeset(repo, scope, base?)`, `fileDiff(repo, scope, kind, path, base?)`,
  `masterChangeset(repo, master, options?, base?)`, and `masterFileDiff(repo, master, kind, path, base?)` (the series
  net before/after via `/file-diff?master=`) each build their query string with `qs` (`URLSearchParams`)
  and delegate to `getJson` (imported from `./files`).
- L4a leaf helpers: `leafChangeset(repo, master, leaf, mode, base?)` and
  `leafFileDiff(repo, master, leaf, kind, path, mode, base?)`, where `mode: LeafMode` (`"committed" |
  "working"`). They ride the **same** `/api/changeset/task` and `/file-diff` routes with a `leaf` + `mode`
  query (so the server's `leaf > master > scope` selector picks the leaf view), and `leafChangeset` returns
  the `TaskChangeset` shape (the server's extra `mode` echo is harmless), so the viewer renders it unchanged.

### Conventions

Reuses the L1 files client's house style: a `base = ""` same-origin default, typed return values, the
single shared `getJson`/`qs` transport, the shared thrown `FilesApiError`, and no store mutation. The
interfaces mirror `serving/changeset.py`'s dict shapes exactly.

### Invariants And Boundaries

Transport only — never mutates a store, never interprets diff content; it maps HTTP to typed results or a
thrown `FilesApiError` (the serving idiom: 404 `unknown-repo`/`unknown-scope`/`not-found` — e.g. a
completed task whose worktree is gone — and 400 `bad-path`) and stops there. Same-origin by default; the
FastAPI dashboard server owns repo/scope resolution and path safety.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Generation pins, the published generation identity, and the `committed`/`working` leaf-row state the master client threads and mirrors. | "export interface MasterNetPins"; "export interface MasterNetGeneration"; "export interface MasterChangeset {" | dashboard/src/data/changeset.ts:46-46; dashboard/src/data/changeset.ts:52-52; dashboard/src/data/changeset.ts:59-59 |
| Typed result contracts mirror the L3 endpoints' camelCase JSON (changed files, counters, file-diff, master accumulation). | "interface TaskChangeset" | dashboard/src/data/changeset.ts:26-26 |
| Three `base`-arg GET helpers build the `/task`, `/file-diff`, `/master` URLs via the shared `qs`. | "export const taskChangeset" | dashboard/src/data/changeset.ts:78-78 |
| Reuses the L1 files client's shared `getJson`/`qs` transport + `FilesApiError`. | "export const qs" | dashboard/src/data/files.ts:99-99 |
| The serving layer that defines the endpoints + response shapes this client mirrors. | "def register_changeset_routes" | mcp/src/agents_remember/serving/changeset.py:638-638 |
| `ChangeSetViewer` orchestrates `taskChangeset`/`fileDiff`/`masterChangeset` + renders `FilesApiError.code`. | "export function ChangeSetViewer" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:476-476 |
| `DetailPanel`'s change-set button fetches counters via `taskChangeset`/`masterChangeset`. | "masterChangeset(target.repo" | dashboard/src/panels/detail-panel/changeSetBar.tsx:52-52 |
| The vitest contract test pins the endpoint URLs + the `FilesApiError` mapping. | "builds the task / file-diff / master URLs" | dashboard/src/data/changeset.test.ts:17-32 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **the master client is generation-bound (120 → 155 lines).** The section above records `MasterNetPins`/`MasterNetGeneration`, the `generation`+`currentness`+`scope` mirror, the `state`-labelled leaf rows, and pins threaded through `masterChangeset`/`masterFileDiff` with unset pins omitted. **Citation accounting:** every row into this file was re-derived against the moved candidate (the insertion moved `taskChangeset` `:56` → `:78` and `MasterChangeset` `:45` → `:59`), and the three cross-file rows were re-derived against this candidate too (`register_changeset_routes` `:517` → `:638`, `ChangeSetViewer` `:424` → `:476`, the bar's `masterChangeset(` `:39` → `:52`). The reopened claim is retained with its range regenerated onto the declaration the anchor holds. The four mechanical projection bullets below that recorded the superseded ranges (`:517`, `:424`, `:421`, `:39`) are retired by this reading — they pointed at lines that no longer hold their anchors, and this entry is the curator-read evidence that replaces them. Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 7 table citations and 1 prose citation for the changeset contract and consumer path; fixer-generated ranges verified.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-12T12:55+02:00 — 260712-TRH-L2: added the typed master query options and `includeLeaves` serialization so dashboard net-range callers can omit expensive per-leaf summaries without changing the default response. Verification metadata pinned until closeout stamps the L2 code commit.

- 2026-06-29T23:00+02:00 — L4a: added the leaf helpers `leafChangeset(repo, master, leaf, mode, base?)` +
  `leafFileDiff(repo, master, leaf, kind, path, mode, base?)` and the `LeafMode` (`"committed" | "working"`)
  type. They ride the existing `/api/changeset/{task,file-diff}` routes with a `leaf` + `mode` query;
  existing helpers unchanged. Verification metadata pinned until closeout stamps the L4a commit.
- 2026-06-29T17:00+02:00 — L4 follow-up: added `masterFileDiff(repo, master, kind, path)` (the series net
  before/after via `/api/changeset/file-diff?master=`) and made `MasterChangeset.code/memory` plain
  `ChangedFile[]` (the net diff; dropped `leafCount`), so the series view is per-file inspectable.
  Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T16:40+02:00 — Created for operations-integration L4 (Change-Set Viewer): same-origin typed
  client for the L3 change-set API (`/api/changeset/task|/file-diff|/master`) reusing `data/files.ts`'s
  shared `getJson`/`qs` transport + `FilesApiError`, holding no store state. Verification metadata pinned
  to the task base until closeout stamps the L4 code commit.
