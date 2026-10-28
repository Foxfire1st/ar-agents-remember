# dashboard/src/data/changeset.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Same-origin browser client for the L3 read-only change-set API. It exposes typed helpers over the three
GET endpoints (`/api/changeset/task`, `/file-diff`, `/master`), returns camelCase-typed results, and
uses the shared `qs` query builder with its own `getChangeSetJson` refusal-preserving transport.
A failure throws `ReviewTransportError`, carrying the route's refusal details. URL-keyed conditional results belong to the dashboard store; the viewer retains its selection-local render state.

`data/changeset.ts` is the same-origin client for the read-only change-set API: typed results, a thrown `ReviewTransportError` carrying the route's refusal, and bounded store-owned HTTP history. W03 added recorded-comparison support. `TaskChangeset` still optionally echoes the comparison number and its four trees, and `comparisonFileDiff` remains the per-file reader. The unused `comparisonChangeset` list helper is removed from this module; that is not removal of the server's comparison-list route.
## Code Commentary

### Logic

`masterChangeset` accepts typed options and serializes `includeLeaves` only when a caller sets it
explicitly (`options.includeLeaves !== undefined`), so omitting it leaves the server's own default — the
full response with per-leaf summaries — in force. **260921-ICR-L33 changed who asks for what, not this
client:** both of the dashboard's master-net readers (`panels/changeset/ChangeSetViewer.tsx` and
`panels/detail-panel/changeSetBar.tsx`) now use `loadChangeSet`, whose master URL sets `includeLeaves: true`, because R33.2 makes the
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

`ChangeSetAddress` is the shared list address (`repo` plus optional `scope`, `master`, `leaf`, `mode`, `generation`, `comparison`). Private `listUrl` selects comparison/leaf first, then master, then scope: comparison lists still reuse `/api/changeset/task` with the numbered `comparison` parameter and omit `mode`. Master addresses always include the leaf breakdown and carry generation pins. `peekChangeSet` reads the store’s cached list by that URL; `loadChangeSet` uses the same URL through the conditional-read owner. The viewer's initial list request and the detail-panel counters use this shared list API. The typed helpers also remain active: in a non-comparison working leaf view, `useWorkingChangesetPoll` calls `leafChangeset(repo, master, leaf, 'working')` every 2.5 seconds and independently refreshes the selected file diff. The shared address API does not replace that working-mode poll.

Typed data contracts and GET readers:

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
  and delegate to this module's `getChangeSetJson`.
- L4a leaf helpers: `leafChangeset(repo, master, leaf, mode, base?)` and
  `leafFileDiff(repo, master, leaf, kind, path, mode, base?)`, where `mode: LeafMode` (`"committed" |
  "working"`). They ride the **same** `/api/changeset/task` and `/file-diff` routes with a `leaf` + `mode`
  query (so the server's `leaf > master > scope` selector picks the leaf view), and `leafChangeset` returns
  the `TaskChangeset` shape (the server's extra `mode` echo is harmless), so the viewer renders it unchanged.

### Conventions

Reuses the L1 files client's house style: a `base = ""` same-origin default, typed return values, the
shared `qs` query builder, refusal-preserving `getChangeSetJson`, thrown `ReviewTransportError`, and bounded store-owned HTTP history. The
interfaces mirror `serving/changeset.py`'s dict shapes exactly.

### Invariants And Boundaries

Transport plus store-owned conditional list/file history — never interprets diff content; it maps HTTP to typed results or a
thrown `ReviewTransportError` (including 404 `unknown-repo`/`unknown-scope`/`not-found` — e.g. a
completed task whose worktree is gone — and 400 `bad-path`) and stops there. Same-origin by default; the
FastAPI dashboard server owns repo/scope resolution and path safety.

`TaskChangeset` carries optional `comparison` and `trees` (`codeBase`, `codeTip`, `memoryBase`, `memoryTip`), so a comparison answer uses the task shape with its identity attached. `FileDiff.kind` remains the existing `code` | `memory` discriminator. `comparisonFileDiff` calls the file-diff endpoint with `comparison` as its selector (the server refuses a `mode` combination). The removed `comparisonChangeset` helper is not a current export. Existing scope, leaf and master readers retain their request shapes.

## Current Behavior

the change-set client now carries an owner signal. `getChangeSetJson(url, signal)` passes it to the store's conditional resource (`cache.load(url, decodeChangeSetJson, url, signal)`) and rethrows an `AbortError` unchanged instead of wrapping it as a network failure; `loadChangeSet(target, signal)` exposes the same signal. A read its page abandoned therefore leaves no error on that owner. A live same-key owner keeps the shared fetch and its retained result; the pending entry is removed and the fetch aborted only when the last waiter leaves. This supersedes the sentence that the client only throws `ReviewTransportError`: an aborted read is not a transport failure.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Generation pins, the published generation identity, and the `committed`/`working` leaf-row state the master client threads and mirrors. [1]
- Typed result contracts mirror the L3 endpoints' camelCase JSON (changed files, counters, file-diff, master accumulation), and (260921-ICR-L25) the leaf view's `state`/`stateDetail` pair that keeps an unrecorded range apart from a measured-empty one. [2]

- The `base`-arg GET helpers build the `/task`, `/file-diff`, `/master` URLs via the shared `qs`.


- Change-set reads use qs and their own refusal-preserving getChangeSetJson, throwing ReviewTransportError rather than discarding refusal detail. [4]


- The serving layer that defines the endpoints + response shapes this client mirrors.

- The viewer's initial list request uses loadChangeSet, while its non-comparison working-leaf poll still calls leafChangeset and refreshes an active diff every 2.5 seconds. 


- `DetailPanel`’s change-set button restores cached data through `peekChangeSet` and reads counters through `loadChangeSet`.


- The vitest contract test pins the endpoint URLs + the `FilesApiError` mapping. [8]



- List addresses share one URL builder and store-backed peek/load API; the comparison list reuses the task endpoint with a number and no mode.

Retired at the fifth freeze d59c3493: dashboard/src/data/changeset.ts:176-184 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit c861abfeff33c9ef8f1ca066604c8f971b613361; dashboard/src/data/changeset.ts:186-196 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit c861abfeff33c9ef8f1ca066604c8f971b613361. Retired means the anchor no longer stands, not that the cited subject was deleted [13]


### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
- A comparison answer is the task shape plus identity [9]
- File diffs name which half of the comparison they read [10]
- The comparison file diff adds kind and path [12]

- Retired at the fifth freeze d59c3493: dashboard/src/data/changeset.ts:167-167 - the bytes it recorded now occur 12 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/serving/changeset.py:735-735 - the bytes it recorded now occur 9 times in the file, so no single home can be named and it is not given to the likelier one; dashboard/src/panels/detail-panel/changeSetBar.tsx:83-103 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 04729d84383a6787afe84ed33183fdc457a20f6e; dashboard/src/panels/changeset/ChangeSetViewer.tsx:252-298 - the bytes it cited (252-298) now occur 2 times in the file, so no single home can be named. Retired means the anchor no longer stands, not that the cited subject was deleted.

## Retirements

- Retired at the fifth freeze d59c3493: dashboard/src/data/changeset.ts:176-184 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit c861abfeff33c9ef8f1ca066604c8f971b613361; dashboard/src/data/changeset.ts:186-196 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit c861abfeff33c9ef8f1ca066604c8f971b613361. Retired means the anchor no longer stands, not that the cited subject was deleted.