# dashboard/src/data/notes.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

`notes.test.ts` is the unit suite for the notes data layer (`data/notes.ts`): the
folder/read URL construction, the shared `FilesApiError` mapping, and the
single-request reference resolution.

## Code Commentary

### Logic

Two describe blocks in the `data/files.test.ts` idiom (a `stubFetch` handler by URL,
`vi.unstubAllGlobals` after each test):

- **client** — `listFolder`/`readNote` build exactly
  `/api/notes/folder?repo&master&path&offset` and `/api/notes/read?repo&master&path` (path
  URL-encoded); a non-ok response rejects with the shared `FilesApiError`.
- **resolveNoteReferences** — one POST carries the document's references and answers each
  with a path or null; the client maps answered paths and throws on a malformed answer.

### Conventions

Pure unit tests — no component rendering, no store; fetch is stubbed per test.

### Invariants And Boundaries

The suite pins the client contract: folder/read URLs, one POST for references, and a
rejection on malformed answers, so the UI can never render a dead or guessed link.

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


