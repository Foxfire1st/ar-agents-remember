# dashboard/src/data/files.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Vitest unit suite for the `data/files` client with stubbed `fetch`. It checks catalog/list/read URLs,
onboarding direction markers, a non-ok `FilesApiError` rejection, owned JSON cancellation, and
repository-catalog single-flight behavior.

## Code Commentary

### Logic

- `stubFetch(payload, ok, status)` installs a `vi.fn` `fetch` returning a minimal `Response`-shaped
  object (`ok`, `status`, `statusText`, async `json`); `afterEach` unstubs all globals.
  (cit:([`stubFetch`], dashboard/src/data/files.test.ts:24-30))
- The first case calls all five helpers once and asserts the recorded URLs: bare `/api/files/repos`,
  the `list` / `read` query strings (note the `%2F`-encoded `path`), and `direction=forward` /
  `direction=reverse` for the two onboarding calls. (cit:(["direction=forward"], dashboard/src/data/files.test.ts:34-47))
- The second case stubs a 400 `{status: "bad-path"}` response and asserts `listDir` rejects with a
  `FilesApiError` instance. (cit:([`FilesApiError`], dashboard/src/data/files.test.ts:49-52))

### Invariants And Boundaries

- Pure unit test: it never opens a network connection — `fetch` is fully stubbed — so it pins the
  client's URL construction and error mapping, not server behavior.
- The URL/error cases assert exact catalog/list/read URLs, onboarding direction markers and the
  thrown error type. Owned JSON cases assert that a pre-aborted owner sends nothing, caller and timeout
  cancellation propagate to the fetch signal, caller signal state is preserved, and no timer remains.
  Catalog single-flight cases assert concurrent sharing, shared rejection with fresh retry, a fresh read
  after success, and timeout release of a hung request. These are stubbed-fetch observations; the
  serving layer’s own tests own response semantics.
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
- Asserts a non-ok response throws `FilesApiError`. [3]
- Subject under test: the helpers, result types, and `FilesApiError` mapping pinned here. [4]
- Contract counterpart: the serving layer emits the 404/400 status codes this test stubs.

Anchor: `run_scoped` in serving/scope.py, whose 404 unknown-repo/unknown-scope/not-found and 400 bad-path responses were read at the candidate at 239-249 rather than shifted, so this re-point is a match on the idiom, not on the number.

Anchor: `run_scoped` in serving/scope.py, whose 404 unknown-repo/unknown-scope/not-found and 400 bad-path responses were read at the candidate at 239-249 rather than shifted, so this re-point is a match on the idiom, not on the number.

Anchor: `run_scoped` in serving/scope.py, whose 404 unknown-repo/unknown-scope/not-found and 400 bad-path responses were read at the candidate at 239-249 rather than shifted, so this re-point is a match on the idiom, not on the number.

Anchor: `run_scoped` in serving/scope.py, whose 404 unknown-repo/unknown-scope/not-found and 400 bad-path responses were read at the candidate at 239-249 rather than shifted, so this re-point is a match on the idiom, not on the number.



- Contract counterpart: the serving layer emits the 404/400 status codes this test stubs. [5]


### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## Retirements

- Anchor: `run_scoped` in serving/scope.py, whose 404 unknown-repo/unknown-scope/not-found and 400 bad-path responses were read at the candidate at 239-249 rather than shifted, so this re-point is a match on the idiom, not on the number.


Anchor: `run_scoped` in serving/scope.py, whose 404 unknown-repo/unknown-scope/not-found and 400 bad-path responses were read at the candidate at 239-249 rather than shifted, so this re-point is a match on the idiom, not on the number.

Anchor: `run_scoped` in serving/scope.py, whose 404 unknown-repo/unknown-scope/not-found and 400 bad-path responses were read at the candidate at 239-249 rather than shifted, so this re-point is a match on the idiom, not on the number.

Anchor: `run_scoped` in serving/scope.py, whose 404 unknown-repo/unknown-scope/not-found and 400 bad-path responses were read at the candidate at 239-249 rather than shifted, so this re-point is a match on the idiom, not on the number.

Anchor: `run_scoped` in serving/scope.py, whose 404 unknown-repo/unknown-scope/not-found and 400 bad-path responses were read at the candidate at 239-249 rather than shifted, so this re-point is a match on the idiom, not on the number.

- Asserts exact catalog/list/read URLs and the onboarding direction markers. [2]
- Owned JSON cases distinguish pre-abort, caller cancellation and timeout cancellation while clearing timers. [6]
- Catalog single-flight cases check sharing, shared rejection and retry, post-settlement reads and hung-read timeout release. [7]
