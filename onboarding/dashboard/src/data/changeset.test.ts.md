# dashboard/src/data/changeset.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Vitest contract test for the `data/changeset` client. It stubs the global `fetch` and asserts that each
helper builds the exact L3 change-set endpoint URL with encoded query params. The test proves that a
non-ok response throws `FilesApiError`; the production clients and serving route separately own status
retention and the 400/404 response mapping.

## Code Commentary

### Logic

The URL contract tests cover the optional master `includeLeaves=false` query
shape alongside the existing task, file-diff, and leaf selectors, ensuring the
typed client does not silently drop the flag when a caller sets it. **260921-ICR-L33 note, because the
flag's story changed:** the R33.2 readers pass `includeLeaves: true` (and a contract case for that
spelling lives in the viewer's own suite), so `false` here pins a retained API path rather than the
path the product takes. The test file is byte-unchanged by that leaf, and this sentence described the
mechanism correctly before and after; the note exists so a reader does not infer the product's request
shape from the pinned flag.

- cit:([`stubFetch`, `afterEach`], dashboard/src/data/changeset.test.ts:6-12; dashboard/src/data/changeset.test.ts:14-14) installs a `vi.fn` `fetch`
  returning a minimal `Response`-shaped object and restores globals after each test.
- cit:(["includeLeaves=false"], dashboard/src/data/changeset.test.ts:16-32)
  covers the task, file-diff, and master URLs, including the optional `includeLeaves=false` selector:
  `/api/changeset/task?repo&scope`,
  `/api/changeset/file-diff?...&kind=memory&path=...` (note the `%2F`-encoded path), and
  `/api/changeset/master?repo&master`.
- cit:([`leafChangeset`, `leafFileDiff`], dashboard/src/data/changeset.test.ts:32-46) calls the leaf URLs on
  the same `task` / `file-diff` routes with the `leaf` + `mode` query.
- cit:(["not-found"], dashboard/src/data/changeset.test.ts:54-57) stubs a 404 `{status: "not-found"}`
  and asserts that `taskChangeset` rejects with a `FilesApiError` instance.
- cit:(["carries generation pins on the master URLs and omits unset pins"], dashboard/src/data/changeset.test.ts:59-77)
  pins the generation params on the master list and file-diff URLs (`codeBase`/`codeTip` carried,
  unset pins omitted so the request selects the declared integrated result).

### Invariants And Boundaries

Pure unit test: `fetch` is fully stubbed (no network), pinning URL construction + error mapping, not
server behavior. Globals are restored after every case so stubs never leak.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Stubs `fetch` and unstubs globals after each test. [1]
- Asserts the task / file-diff / master URLs (including `%2F` path encoding). [2]
- Asserts generation pins ride the master URLs and unset pins are omitted. [3]
- Asserts a non-ok (404) response throws `FilesApiError`. [4]
- The test imports and exercises taskChangeset and FilesApiError in its URL and error cases. [5]
- Contract counterpart: the serving layer emits the 404/400 codes this test stubs. [6]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
