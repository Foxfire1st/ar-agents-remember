# dashboard/src/data/files.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/files.test.ts`               |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-29T09:06+02:00                           |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`       |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Vitest contract test for the `data/files` client. It stubs the global `fetch` and asserts that each
helper builds the exact L1 endpoint URL (with encoded query params) and that a non-ok response is
mapped to a thrown `FilesApiError` carrying the server status code.

## Code Commentary

### Logic

- `stubFetch(payload, ok, status)` installs a `vi.fn` `fetch` returning a minimal `Response`-shaped
  object (`ok`, `status`, `statusText`, async `json`); `afterEach` unstubs all globals. (L5-L13)
- The first case calls all five helpers once and asserts the recorded URLs: bare `/api/files/repos`,
  the `list` / `read` query strings (note the `%2F`-encoded `path`), and `direction=forward` /
  `direction=reverse` for the two onboarding calls. (L16-L29)
- The second case stubs a 400 `{status: "bad-path"}` response and asserts `listDir` rejects with a
  `FilesApiError` instance. (L31-L34)

### Invariants And Boundaries

- Pure unit test: it never opens a network connection — `fetch` is fully stubbed — so it pins the
  client's URL construction and error mapping, not server behavior.
- It asserts URL strings and the thrown error type only; the serving layer's own tests own response
  semantics.
- Globals are restored after every test so stubs never leak across cases.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Stubs `fetch` and unstubs globals after each test. | L5-L13 | [files.test.ts](files.test.ts) |
| Asserts the catalog / list / read / onboarding URLs (including `%2F` path encoding and `direction`). | L16-L29 | [files.test.ts](files.test.ts) |
| Asserts a non-ok response throws `FilesApiError`. | L31-L34 | [files.test.ts](files.test.ts) |
| Subject under test: the helpers, result types, and `FilesApiError` mapping pinned here. | L72-L124 | [files.ts](files.ts) |
| Contract counterpart: the serving layer emits the 404/400 status codes this test stubs. | L298-L332 | [serving/files.py](agents-remember/mcp/src/agents_remember/serving/files.py) |

## Update History

- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): vitest contract test that stubs `fetch` and pins the `data/files` client's endpoint URLs and `FilesApiError` mapping. Verification metadata pinned to the task base until closeout stamps the L2 code commit.
