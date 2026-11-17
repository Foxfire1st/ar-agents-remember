# dashboard/src/data/notes.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

`notes.test.ts` is the unit suite for the notes data layer (`data/notes.ts`): the
folder/read URL construction, the shared `FilesApiError` mapping, and the
single-request reference resolution.

## Code Commentary

### Logic

Three cases in the single `data/notes client` describe block use the sibling suite’s fetch-stub
idiom, with `vi.unstubAllGlobals` after each test:

- **client** — `listFolder`/`readNote` build exactly
  `/api/notes/folder?repo&master&path&offset` and `/api/notes/read?repo&master&path` (path
  URL-encoded); a non-ok response rejects with the shared `FilesApiError`.
- **resolveNoteReferences** — one POST carries the document’s references; a valid answer supplies
  one path and one null. The case checks the retained path map, POST URL, method and JSON request body.

### Conventions

Pure unit tests — no component rendering, no store; fetch is stubbed per test.

### Invariants And Boundaries

The suite checks folder/read URL construction, the valid reference-map POST, and a shared
`FilesApiError` rejection for a non-ok read response. It supplies no malformed-answer or rendered-UI
assertions, so it does not establish a guarantee about every link the UI can render.

## Evidence

### Cross-Repo References

No meaningful cross-repo references found.

A stubbed-fetch unit suite; nothing crosses repositories.

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The folder/read client functions under test. [1]
- The single-request reference resolver under test. [2]
- The sibling client suite's shared fetch-stub idiom. [3]


