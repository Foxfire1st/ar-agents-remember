# dashboard/src/data/changeset.ts

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

`masterChangeset` accepts typed options and serializes `includeLeaves` only when a caller sets it
explicitly (`options.includeLeaves !== undefined`), so omitting it leaves the server's own default — the
full response with per-leaf summaries — in force. **260921-ICR-L33 changed who asks for what, not this
client:** both of the dashboard's master-net readers (`panels/changeset/ChangeSetViewer.tsx` and
`panels/detail-panel/changeSetBar.tsx`) now pass `includeLeaves: true`, because R33.2 makes the
per-leaf breakdown part of what a master's net must show. The `false` path is retained and still
pinned by this module's own contract test; it is simply no longer the choice either reader makes, so
the older phrasing here — that the option exists "when a caller needs only the coherent series net
range" — is now a statement about the API rather than about the product.

### 260921-ICR-L13 — Generation pins and the published generation

The master client is now generation-bound. `MasterNetPins` (four optional wire params —
`codeBase`/`codeTip`/`memoryBase`/`memoryTip`) freezes a request to the listed generation;
unset pins are omitted from the query so the request selects the declared integrated result.
`MasterNetGeneration` (four commits + `digest`) is what the list response publishes, beside
`currentness` and `scope: "integrated"`; leaf rows carry optional
`state: "committed" | "working"`. cit:(["export interface MasterChangeset {"], dashboard/src/data/changeset.ts:76-76)
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
  the NET series `code`/`memory` as plain `ChangedFile[]` + `counters`) (cit:(["export interface MasterChangeset {"], dashboard/src/data/changeset.ts:76-76)).
- **`TaskChangeset` also carries the leaf view's own `state`/`stateDetail` (260921-ICR-L25), and they
  exist to keep an UNRECORDED range apart from a MEASURED EMPTY one.** `state?: "recorded" |
  "unrecorded"` and `stateDetail?: string` mirror the server's `state`/`stateDetail` on
  `LeafChangeSet`: a `committed` read of a live leaf has no landed commit to read yet, the server
  answers that state in the body rather than with a `404` (a `404` for a state the bar probes on
  **every** live leaf is a console error the accepted criterion counts — register B6), and the client
  carries the server's own sentence to the reader **verbatim rather than summarising it here**. Both
  fields are optional because the enclosure-scoped `taskChangeset` and the master read do not publish
  them. The consequence lives one file up: `changeSetBar.tsx` renders `unrecorded` as its own state
  and **withholds the `+0 −0` total**, because a zero of nothing is not a measurement.
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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Generation pins, the published generation identity, and the `committed`/`working` leaf-row state the master client threads and mirrors. [1]
- Typed result contracts mirror the L3 endpoints' camelCase JSON (changed files, counters, file-diff, master accumulation), and (260921-ICR-L25) the leaf view's `state`/`stateDetail` pair that keeps an unrecorded range apart from a measured-empty one. [2]
- Three `base`-arg GET helpers build the `/task`, `/file-diff`, `/master` URLs via the shared `qs`. [3]
- Reuses the L1 files client's shared `getJson`/`qs` transport + `FilesApiError`. [4]
- The serving layer that defines the endpoints + response shapes this client mirrors. [5]
- `ChangeSetViewer` orchestrates `taskChangeset`/`fileDiff`/`masterChangeset` + renders `FilesApiError.code`. [6]
- `DetailPanel`'s change-set button fetches counters via `taskChangeset`/`masterChangeset`. [7]
- The vitest contract test pins the endpoint URLs + the `FilesApiError` mapping. [8]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
