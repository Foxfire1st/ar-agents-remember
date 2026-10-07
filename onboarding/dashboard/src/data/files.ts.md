# dashboard/src/data/files.ts

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
- cit:([`getJson`, `FilesApiError`, `qs`], dashboard/src/data/files.ts:76-84; dashboard/src/data/files.ts:90-97; dashboard/src/data/files.ts:104-104) is the shared transport: it `fetch`es a URL and, on a non-ok response, reads the body's
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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Typed result contracts mirror the L1 endpoints' camelCase JSON (catalog, dir listing, file content, forward/reverse pairing). [1]
- `getJson` maps every non-ok response to a thrown `FilesApiError` carrying the server status code. [2]
- Five `base`-arg GET helpers build the `/repos`, `/list`, `/read`, and `/onboarding` (forward+reverse) URLs. [3]
- The serving layer registers the four `/api/files/*` endpoints this client calls. [4]
- `run_scoped` maps domain errors to the status idiom this client surfaces (`unknown-repo`/`unknown-scope` 404, `bad-path` 400, `not-found` 404). [5]
- `FileViewer` orchestrates `fetchRepos`/`readFile`/`resolveForward`/`resolveReverse` and renders `FilesApiError.code`. [6]
- The File Viewer's tree loader calls `listDir` per directory level from the shared adapter. [7]
- `FileTree` consumes the `DirEntry` and `Scope` types. [8]
- `DualPane` consumes the `FileContent` type for its code side. [9]
- The vitest contract test pins the endpoint URLs and the `FilesApiError` mapping. [10]
- House-style sibling client: `base` arg and typed results. Unlike this request/response client, `stream.ts` is stateful: it applies snapshots/deltas and connection status directly to the stream store. [11]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
