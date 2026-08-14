# dashboard/src/data/files.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/files.test.ts`               |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

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
| Stubs `fetch` and unstubs globals after each test. | `fetch` | dashboard/src/data/files.test.ts:23-31 |
| Asserts the catalog / list / read / onboarding URLs (including `%2F` path encoding and `direction`). | `direction` | dashboard/src/data/files.test.ts:45-46 |
| Asserts a non-ok response throws `FilesApiError`. | `FilesApiError` | dashboard/src/data/files.test.ts:49-52 |
| Subject under test: the helpers, result types, and `FilesApiError` mapping pinned here. | `FilesApiError` | dashboard/src/data/files.ts:76-84 |
| Contract counterpart: the serving layer emits the 404/400 status codes this test stubs. | `run_scoped` | mcp/src/agents_remember/serving/scope.py:207-227 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-04T17:52+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 8 citation findings. Converted the
  three Logic line-cite parentheticals and the L2 history cite to cit form — the first-case range moved
  to `files.test.ts:34-47` — and re-anchored + re-ranged the `FilesApiError` and `run_scoped` rows.
  Scoped recheck clean.

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 2 stale self-citations after the
  hung-socket helper was added above the fixtures. The `stubFetch` + `afterEach` setup moved
  L5-L13 -> L23-L31 (L5-L13 is now the import list), and the `FilesApiError` non-ok case moved
  L31-L34 -> L49-L52; both the prose and the Repo-Internal References rows were repointed.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation that moved
  out of `serving/files.py`. The 404/400 status-code idiom the test stubs is now emitted by
  `run_scoped` in the extracted `serving/scope.py`
  (cit:([`run_scoped`], mcp/src/agents_remember/serving/scope.py:207-227)), not by `serving/files.py`
  (which only registers routes and delegates); repointed both the link path and the range.

- 2026-07-24T13:17:50Z — Added repository-catalog single-flight and timeout coverage. Verification
  hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): vitest contract test that stubs `fetch` and pins the `data/files` client's endpoint URLs and `FilesApiError` mapping. Verification metadata pinned to the task base until closeout stamps the L2 code commit.
