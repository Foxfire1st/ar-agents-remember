# dashboard/src/data/files.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/files.ts`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`       |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
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
  available. (L10-L68)
- `FilesApiError` carries the HTTP status plus the server's `status` string code so the UI can show
  the precise reason. (L72-L80)
- `getJson<T>` is the shared transport: it `fetch`es a URL and, on a non-ok response, reads the body's
  `status` field (falling back to `statusText`) and throws a `FilesApiError`. As of L4 (D6) `getJson` and
  the `qs` query-string builder are **exported** so the L3 change-set client (`data/changeset.ts`) reuses
  the same fetch wrapper + serving error idiom. (L82-L92)
- `fetchRepos`, `listDir`, `readFile`, `resolveForward`, and `resolveReverse` each take a trailing
  `base` arg, build their query string with `qs` (`URLSearchParams`), and delegate to `getJson`. The
  two onboarding helpers differ only by the `direction=forward|reverse` query param. (L91-L124)

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Typed result contracts mirror the L1 endpoints' camelCase JSON (catalog, dir listing, file content, forward/reverse pairing). | L10-L68 | [files.ts](files.ts) |
| `getJson` maps every non-ok response to a thrown `FilesApiError` carrying the server status code. | L72-L89 | [files.ts](files.ts) |
| Five `base`-arg GET helpers build the `/repos`, `/list`, `/read`, and `/onboarding` (forward+reverse) URLs. | L91-L124 | [files.ts](files.ts) |
| The serving layer defines the endpoints and maps domain errors to the status idiom this client surfaces. | L298-L332 | [serving/files.py](agents-remember/mcp/src/agents_remember/serving/files.py) |
| `FileViewer` orchestrates `fetchRepos`/`readFile`/`resolveForward`/`resolveReverse` and renders `FilesApiError.code`. | L11-L21, L112, L162-L214 | [FileViewer.tsx](agents-remember/dashboard/src/panels/file-viewer/FileViewer.tsx) |
| `useFilesTree` calls `listDir` per directory level to lazy-load each tree side. | L11, L47 | [useFilesTree.ts](agents-remember/dashboard/src/panels/file-viewer/useFilesTree.ts) |
| `FileTree` consumes the `DirEntry` and `Scope` types. | L8 | [FileTree.tsx](agents-remember/dashboard/src/panels/file-viewer/FileTree.tsx) |
| `DualPane` consumes the `FileContent` type for its code side. | L8 | [DualPane.tsx](agents-remember/dashboard/src/panels/file-viewer/DualPane.tsx) |
| The vitest contract test pins the endpoint URLs and the `FilesApiError` mapping. | L1-L35 | [files.test.ts](files.test.ts) |
| House-style sibling client: `base` arg, typed results, no store mutation. | — | [stream.ts](stream.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

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
