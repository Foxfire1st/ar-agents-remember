# dashboard/src/data/files.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/files.ts`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Same-origin browser client for the L1 read-only files API. It exposes typed helpers over the four GET
endpoints the serving layer publishes (`/api/files/repos`, `/list`, `/read`, `/onboarding`), returns
camelCase-typed results, and throws a `FilesApiError` on any non-ok response. It holds no state — the
File Viewer panel owns its own component state and calls these helpers directly.

## Code Commentary

### Logic

The module is data contracts plus five fetch helpers:

- Result interfaces (`RepoCatalog`, `DirListing`, `FileContent`, and the `ForwardPairing` /
  `ReversePairing` onboarding pairings) mirror the serving JSON shape one-for-one; `Scope` is a string
  that is either `"mainline"` or a worktree-group basename. The `ReversePairing` union has three
  variants — `"sidecar"` (partner code path + `exists`), `"none"`, and `"overview"`. As of L5 the
  `"overview"` variant carries the doc body itself: `{ scope; onboardingPath; kind: "overview"; route;
  body: string | null }` (it previously had only `route`), so a partnerless overview/entities/index doc
  can be rendered by the file reader without a second fetch; `body` is `null` when no markdown is
  available. cit:([`ReversePairing`], dashboard/src/data/files.ts:68-72)
- cit:([`FilesApiError`], dashboard/src/data/files.ts:76-84) carries the HTTP status plus the server's `status` string code so the UI can show
  the precise reason.
- cit:([`getJson`, `FilesApiError`, `qs`], dashboard/src/data/files.ts:76-84; dashboard/src/data/files.ts:90-97; dashboard/src/data/files.ts:99-100) is the shared transport: it `fetch`es a URL and, on a non-ok response, reads the body's
  `status` field (falling back to `statusText`) and throws a `FilesApiError`. As of L4 (D6) `getJson` and
  the `qs` query-string builder are **exported** so the L3 change-set client (`data/changeset.ts`) reuses
  the same fetch wrapper + serving error idiom.
- cit:([`fetchRepos`, `listDir`, `readFile`, `resolveForward`, `resolveReverse`], dashboard/src/data/files.ts:108-111; dashboard/src/data/files.ts:113-114; dashboard/src/data/files.ts:116-121; dashboard/src/data/files.ts:123-131; dashboard/src/data/files.ts:133-141) each take a trailing
  `base` arg, build their query string with `qs` (`URLSearchParams`), and delegate to `getJson`. The
  two onboarding helpers differ only by the `direction=forward|reverse` query param.

### Conventions

Follows the dashboard data-client house style shared with `data/stream.ts` and `data/terminal.ts`: a
`base = ""` same-origin default, typed return values, a single thrown status error, and no store
mutation. Query strings are always built via `URLSearchParams` so path/scope values are encoded.

### Invariants And Boundaries

- Transport only. This module never mutates a store and never interprets onboarding content; it maps
  HTTP to typed results or a thrown `FilesApiError` and stops there.
- `status: "missing"` onboarding metadata is a normal placeholder the viewer renders, not a failure —
  only a non-ok HTTP response becomes a throw.
- The serving layer is the source of truth for the error idiom this client surfaces: 404
  `unknown-repo` / `unknown-scope` / `not-found`, 400 `bad-path`.
- Same-origin by default; the FastAPI dashboard server owns repo/scope resolution and path safety.

### 2026-07-24 Curator Delta

`fetchRepos` now shares only concurrent boot reads and expires its transport after 10 seconds.
Settlement always clears the slot: a successful later read re-fetches, and an abort or rejection lets
the next caller retry rather than turning a single-flight into a cache or permanent wedge.

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
| Typed result contracts mirror the L1 endpoints' camelCase JSON (catalog, dir listing, file content, forward/reverse pairing). | `RepoCatalog`; `DirListing`; `FileContent`; `ForwardPairing`; `ReversePairing` | dashboard/src/data/files.ts:27-29; dashboard/src/data/files.ts:38-43; dashboard/src/data/files.ts:51-59; dashboard/src/data/files.ts:62-66; dashboard/src/data/files.ts:68-72 |
| `getJson` maps every non-ok response to a thrown `FilesApiError` carrying the server status code. | `getJson`; `FilesApiError` | dashboard/src/data/files.ts:76-84; dashboard/src/data/files.ts:90-97 |
| Five `base`-arg GET helpers build the `/repos`, `/list`, `/read`, and `/onboarding` (forward+reverse) URLs. | `fetchRepos`; `listDir`; `readFile`; `resolveForward`; `resolveReverse` | dashboard/src/data/files.ts:108-111; dashboard/src/data/files.ts:113-114; dashboard/src/data/files.ts:116-121; dashboard/src/data/files.ts:123-131; dashboard/src/data/files.ts:133-141 |
| The serving layer registers the four `/api/files/*` endpoints this client calls. | `register_files_routes` | mcp/src/agents_remember/serving/files.py:296-325 |
| `run_scoped` maps domain errors to the status idiom this client surfaces (`unknown-repo`/`unknown-scope` 404, `bad-path` 400, `not-found` 404). | `run_scoped` | mcp/src/agents_remember/serving/scope.py:207-227 |
| `FileViewer` orchestrates `fetchRepos`/`readFile`/`resolveForward`/`resolveReverse` and renders `FilesApiError.code`. | "function FileViewerImpl({ active = true }: { active?: boolean }) {"; "return e instanceof FilesApiError ? e.code : \"request failed\";" | dashboard/src/panels/file-viewer/FileViewer.tsx:205-205; dashboard/src/panels/file-viewer/FileViewer.tsx:112-112 |
| `useFilesTree` calls `listDir` per directory level to lazy-load each tree side. | `useFilesTree`; `listDir` | dashboard/src/panels/file-viewer/useFilesTree.ts:19-55 |
| `FileTree` consumes the `DirEntry` and `Scope` types. | `FileTree`; `DirEntry`; `Scope` | dashboard/src/panels/file-viewer/FileTree.tsx:44-96 |
| `DualPane` consumes the `FileContent` type for its code side. | `DualPane`; `FileContent` | dashboard/src/panels/file-viewer/DualPane.tsx:90-134 |
| The vitest contract test pins the endpoint URLs and the `FilesApiError` mapping. | `FilesApiError` | dashboard/src/data/files.test.ts:1-35 |
| House-style sibling client: `base` arg and typed results. Unlike this request/response client, `stream.ts` is stateful: it applies snapshots/deltas and connection status directly to the stream store. | "export function openConversationStream" | dashboard/src/data/conversation/stream.ts:209-209 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: rebound the stream-sibling row to
  the real `openConversationStream`; exact non-fixing check returns zero findings.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: corrected the sibling comparison: `stream.ts`
  mutates its store with snapshots, deltas, and connection state. The new range is explicit `:1-1`
  curator input.

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: repaired 8 table citations and 4 prose citations; left 1 contradicted house-style claim unresolved as Tier 3.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation that split when
  the serving-side error mapper left `serving/files.py`. The old `L298-L332` row asserted one file
  owned both halves; `_run` was renamed `run_scoped` and moved to `serving/scope.py` (now L207-L227,
  and it additionally maps `ValueError` from a malformed path to the same `bad-path` 400), while
  `register_files_routes` stayed in `files.py` at L291-L312. Split the row in two and verified both
  ranges by reading them.

- 2026-07-24T13:17:50Z — Added bounded single-flight repository-catalog behavior. Verification
  hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-06-30T00:00:00+02:00 — Operations Integration L5: the `ReversePairing` `"overview"` variant now carries the doc
  body — its shape became `{ scope; onboardingPath; kind: "overview"; route; body: string | null }`
  (previously had no `body`) — so the file reader can render an opened partnerless overview's markdown
  directly. Transport/contract-only; no fetch-helper behaviour change. Verification metadata pinned to the
  task base until closeout stamps the L5 code commit.
- 2026-06-29T16:40+02:00 — Operations Integration L4: exported the shared `getJson` transport + the `qs` query-string builder (`FilesApiError` was already exported) so the new L3 change-set client `data/changeset.ts` reuses one fetch wrapper + serving error idiom (D6); no behaviour change to the files client. Verification metadata pinned to the task base until closeout stamps the L4 code commit.
- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): same-origin typed client for the L1 read-only files API (`/api/files/repos|/list|/read|/onboarding`) that returns camelCase results and throws `FilesApiError` on non-ok, holding no store state. Verification metadata pinned to the task base until closeout stamps the L2 code commit.
