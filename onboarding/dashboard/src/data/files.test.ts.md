# dashboard/src/data/files.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Vitest contract test for the `data/files` client. It stubs the global `fetch` and asserts that each
helper builds the exact L1 endpoint URL (with encoded query params) and that a non-ok response is
mapped to a thrown `FilesApiError` carrying the server status code.

## Code Commentary

### Logic

- `stubFetch(payload, ok, status)` installs a `vi.fn` `fetch` returning a minimal `Response`-shaped
  object (`ok`, `status`, `statusText`, async `json`); `afterEach` unstubs all globals.
  (cit:([`stubFetch`], dashboard/src/data/files.test.ts:23-29))
- The first case calls all five helpers once and asserts the recorded URLs: bare `/api/files/repos`,
  the `list` / `read` query strings (note the `%2F`-encoded `path`), and `direction=forward` /
  `direction=reverse` for the two onboarding calls. (cit:(["direction=forward"], dashboard/src/data/files.test.ts:34-47))
- The second case stubs a 400 `{status: "bad-path"}` response and asserts `listDir` rejects with a
  `FilesApiError` instance. (cit:([`FilesApiError`], dashboard/src/data/files.test.ts:49-52))

### Invariants And Boundaries

- Pure unit test: it never opens a network connection — `fetch` is fully stubbed — so it pins the
  client's URL construction and error mapping, not server behavior.
- It asserts URL strings and the thrown error type only; the serving layer's own tests own response
  semantics.
- Globals are restored after every test so stubs never leak across cases.

### 2026-07-24 Curator Delta

Tests now prove shared repository-catalog reads, shared rejection followed by a fresh retry, and an
abort-aware hung socket whose timeout releases the slot.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Stubs `fetch` and unstubs globals after each test. [1]
- Asserts the catalog / list / read / onboarding URLs (including `%2F` path encoding and `direction`). [2]
- Asserts a non-ok response throws `FilesApiError`. [3]
- Subject under test: the helpers, result types, and `FilesApiError` mapping pinned here. [4]
- Contract counterpart: the serving layer emits the 404/400 status codes this test stubs. [5]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
