# dashboard/src/data/changeset.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/changeset.test.ts`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`       |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Vitest contract test for the `data/changeset` client. It stubs the global `fetch` and asserts that each
helper builds the exact L3 change-set endpoint URL (with encoded query params) and that a non-ok response
is mapped to a thrown `FilesApiError` carrying the server status code — the same idiom shared with the L1
`data/files` client.

## Code Commentary

### Logic

The URL contract tests cover the optional master `includeLeaves=false` query
shape alongside the existing task, file-diff, and leaf selectors, ensuring the
typed client does not silently drop the performance-critical flag.

- `stubFetch(payload, ok, status)` installs a `vi.fn` `fetch` returning a minimal `Response`-shaped
  object; `afterEach` unstubs globals. (L6-L14)
- The first case calls all three helpers and asserts the recorded URLs: `/api/changeset/task?repo&scope`,
  `/api/changeset/file-diff?...&kind=memory&path=...` (note the `%2F`-encoded path), and
  `/api/changeset/master?repo&master`. (L16-L30)
- An L4a case calls `leafChangeset` + `leafFileDiff` and asserts the leaf URLs ride the same `task` /
  `file-diff` routes with the `leaf` + `mode` query (`/api/changeset/task?...&leaf=...&mode=committed`,
  `/api/changeset/file-diff?...&leaf=...&kind=code&path=...&mode=working`).
- The last case stubs a 404 `{status: "not-found"}` (the completed-task / no-worktree path) and asserts
  `taskChangeset` rejects with a `FilesApiError` instance.

### Invariants And Boundaries

Pure unit test: `fetch` is fully stubbed (no network), pinning URL construction + error mapping, not
server behavior. Globals are restored after every case so stubs never leak.

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
| Stubs `fetch` and unstubs globals after each test. | L6-L14 | [changeset.test.ts](changeset.test.ts) |
| Asserts the task / file-diff / master URLs (including `%2F` path encoding). | L16-L30 | [changeset.test.ts](changeset.test.ts) |
| Asserts a non-ok (404) response throws `FilesApiError`. | L32-L35 | [changeset.test.ts](changeset.test.ts) |
| Subject under test: the helpers + result types + the shared error mapping. | L52-L69 | [changeset.ts](changeset.ts) |
| Contract counterpart: the serving layer emits the 404/400 codes this test stubs. | L38-L195 | [serving/changeset.py](agents-remember/mcp/src/agents_remember/serving/changeset.py) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-12T12:55+02:00 — 260712-TRH-L2: added the master query-shape assertion for `includeLeaves=false`; existing selector and error URL coverage remains intact. Verification metadata pinned until closeout stamps the L2 code commit.

- 2026-06-29T23:00+02:00 — L4a: added a case pinning the leaf URLs (`leafChangeset` + `leafFileDiff` ride
  the `task` / `file-diff` routes with a `leaf` + `mode` query). Verification metadata pinned until
  closeout stamps the L4a commit.
- 2026-06-29T16:40+02:00 — Created for operations-integration L4 (Change-Set Viewer): vitest contract
  test that stubs `fetch` and pins the `data/changeset` client's endpoint URLs and `FilesApiError`
  mapping. Verification metadata pinned to the task base until closeout stamps the L4 code commit.
