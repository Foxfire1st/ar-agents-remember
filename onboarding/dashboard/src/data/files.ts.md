# dashboard/src/data/files.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Same-origin browser client for the L1 read-only files API. It exposes typed helpers over the five JSON GET
endpoints the serving layer publishes (`/api/files/repos`, `/list`, `/read`, `/resolve`, `/onboarding`), returns
camelCase-typed results, and throws a `FilesApiError` on any non-ok response. Fetch, cancellation and JSON-decoding failures can propagate separately. It holds no state — the
File Viewer panel owns its own component state and calls these helpers directly.

## Code Commentary

### Logic

The module is data contracts, six endpoint helpers and repository-path normalization:

- Result interfaces (`RepoCatalog`, `DirListing`, `FileContent`, `FileResolution`, and the `ForwardPairing` /
  `ReversePairing` onboarding pairings) mirror the serving JSON shape one-for-one; `Scope` is a string
  that is either `"mainline"` or a worktree-group basename. The `ReversePairing` union has three
  variants — `"sidecar"` (partner code path + `exists`), `"none"`, and `"overview"`. The
  `"overview"` variant carries the doc body itself: `{ scope; onboardingPath; kind: "overview"; route;
  body: string | null }` so a partnerless overview/entities/index doc
  can be rendered by the file reader without a second fetch; `body` is `null` when no markdown is
  available. cit:([`ReversePairing`], dashboard/src/data/files.ts:83-87)
- cit:([`FilesApiError`], dashboard/src/data/files.ts:91-99) carries the HTTP status plus the server's `status` string code so the UI can show
  the server status code.
- cit:([`getJson`, `FilesApiError`, `qs`], dashboard/src/data/files.ts:110-123; dashboard/src/data/files.ts:91-99; dashboard/src/data/files.ts:125-126) is the shared transport: it `fetch`es a URL and, on a non-ok response, reads the body's
  `status` field (falling back to `statusText`) and throws a `FilesApiError`. `getJson` and
  the `qs` query-string builder are **exported**. Files, notes and requirements share this decoder;
  the change-set client shares `qs` and uses its own refusal-preserving `getChangeSetJson`.
- `fetchRepos`, `listDir`, `readFile`, `resolvePath`, `resolveForward` and `resolveReverse` each take a trailing
  `base` arg and delegate to `getJson`. Parameterized URLs use `qs` (`URLSearchParams`); the
  two onboarding requests differ by the `direction=forward|reverse` query param.
- `FileContent` carries optional `mediaType` and `tooLarge`. `FileResolution` declares existence and
  path, with optional kind, language and media type. `resolvePath` asks `/api/files/resolve` in the
  selected repository and scope.
- `resolveRepositoryPath` strips fragment and query, decodes the path and resolves it against the
  document directory or repository root. It rejects schemes, protocol-relative addresses, invalid
  encoding, NUL and traversal above the root.

### Conventions

Follows the dashboard data-client house style shared with `data/stream.ts` and `data/terminal.ts`: a
`base = ""` same-origin default, typed return values, `FilesApiError` for returned HTTP failures, and no store
mutation. Query strings are always built via `URLSearchParams` so path/scope values are encoded.

### Invariants And Boundaries

- Read-only transport and lexical path normalization. This module never mutates a store and never interprets onboarding content; it maps
  HTTP to typed results or a thrown `FilesApiError` and stops there.
- `status: "missing"` onboarding metadata is a normal placeholder the viewer renders, not a failure —
  a non-ok HTTP response becomes `FilesApiError`, while fetch, cancellation and decoding failures
  can propagate separately.
- The serving layer is the source of truth for the error idiom this client surfaces: 404
  `unknown-repo` / `unknown-scope` / `not-found`, 400 `bad-path`.
- Same-origin by default; the FastAPI dashboard server owns repo/scope resolution and path safety.



`fetchRepos` shares only concurrent boot reads and bounds its transport at 10 seconds.
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

- `getJson` maps every non-ok response to a thrown `FilesApiError` carrying the server status code.





- Six base-argument GET helpers build the repository catalog, directory listing, content read, path-resolution and forward/reverse onboarding URLs: fetchRepos, listDir, readFile, resolvePath, resolveForward and resolveReverse. [3]




- The serving layer registers the read-only files catalog, listing, content, media-bytes, path-resolution and onboarding-pairing routes consumed by the viewer. [4]



- `run_scoped` maps domain errors to the status idiom this client surfaces (`unknown-repo`/`unknown-scope` 404, `bad-path` 400, `not-found` 404). [5]

- `FileViewer` orchestrates `fetchRepos`/`readFile`/`resolveForward`/`resolveReverse` and renders `FilesApiError.code`. [6]
- The File Viewer's tree loader calls `listDir` per directory level from the shared adapter. [7]
- `FileTree` consumes the `DirEntry` and `Scope` types. [8]



- `DualPane` consumes the `FileContent` type for its code side. Source caption: `FileContent` [9]


- The vitest contract test pins the endpoint URLs and the `FilesApiError` mapping.

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.



## Retirements
