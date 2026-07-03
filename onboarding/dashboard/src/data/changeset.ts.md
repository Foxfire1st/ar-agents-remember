# dashboard/src/data/changeset.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/changeset.ts`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-29T23:00+02:00                           |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`       |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Same-origin browser client for the L3 read-only change-set API. It exposes typed helpers over the three
GET endpoints (`/api/changeset/task`, `/file-diff`, `/master`), returns camelCase-typed results, and
reuses `data/files.ts`'s shared transport (`getJson`/`qs`) so the serving error idiom (a thrown
`FilesApiError`) is mapped once. It holds no state — the Change-Set Viewer owns its component state and
calls these helpers directly.

## Code Commentary

### Logic

Data contracts plus three fetch helpers:

- Result interfaces mirror the L3 JSON shape one-for-one: `ChangedFile` (`insertions`/`deletions` are
  `null` for binary; `status` is the git letter A/M/D/R; `hasSidecar?` on code files drives the L4
  code→sidecar split), `ChangeCounters` (`files`/`insertions`/`deletions`), `TaskChangeset`
  (`code`/`memory` + `counters`), `FileDiff` (`before`/`after` = `{content}` or `null` for an
  added/deleted file — feeds CodeMirror MergeView a/b), `MasterChangeset` (`leaves[]` per-leaf counters +
  the NET series `code`/`memory` as plain `ChangedFile[]` + `counters`). (L12-L50)
- `taskChangeset(repo, scope, base?)`, `fileDiff(repo, scope, kind, path, base?)`,
  `masterChangeset(repo, master, base?)`, and `masterFileDiff(repo, master, kind, path, base?)` (the series
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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Typed result contracts mirror the L3 endpoints' camelCase JSON (changed files, counters, file-diff, master accumulation). | L12-L50 | [changeset.ts](changeset.ts) |
| Three `base`-arg GET helpers build the `/task`, `/file-diff`, `/master` URLs via the shared `qs`. | L52-L69 | [changeset.ts](changeset.ts) |
| Reuses the L1 files client's shared `getJson`/`qs` transport + `FilesApiError`. | L82-L92 | [files.ts](files.ts) |
| The serving layer that defines the endpoints + response shapes this client mirrors. | L37-L196 | [serving/changeset.py](agents-remember/mcp/src/agents_remember/serving/changeset.py) |
| `ChangeSetViewer` orchestrates `taskChangeset`/`fileDiff`/`masterChangeset` + renders `FilesApiError.code`. | L152-L187 | [ChangeSetViewer.tsx](agents-remember/dashboard/src/panels/changeset/ChangeSetViewer.tsx) |
| `DetailPanel`'s change-set button fetches counters via `taskChangeset`/`masterChangeset`. | L573-L616 | [DetailPanel.tsx](agents-remember/dashboard/src/panels/DetailPanel.tsx) |
| The vitest contract test pins the endpoint URLs + the `FilesApiError` mapping. | L16-L36 | [changeset.test.ts](changeset.test.ts) |

## Update History

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
