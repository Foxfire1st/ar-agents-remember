# dashboard/src/data/notes.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/notes.test.ts`               |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T02:00+02:00                           |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`       |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`notes.test.ts` is the unit suite for the L9 notes data layer (`data/notes.ts`): the
list/read URL construction, the shared `FilesApiError` mapping, and the
`resolveNoteReference` resolution rules.

## Code Commentary

### Logic

Two describe blocks in the `data/files.test.ts` idiom (a `stubFetch` that answers a
fixed payload, `vi.unstubAllGlobals` after each test):

- **client** — `listNotes`/`readNote` build exactly
  `/api/notes/list?repo&master` and `/api/notes/read?repo&master&path` (path
  URL-encoded); a non-ok response rejects with the shared `FilesApiError`.
- **resolveNoteReference** — the resolution table: a `notes/`-prefixed reference with
  trailing prose resolves to the notes-relative path; a nested `reports/…` path resolves
  with or without the `notes/` prefix; an unambiguous bare filename resolves; an
  AMBIGUOUS bare filename (same basename in two folders) does not; a code-path reference
  (`serving/files.py`, `panels/DetailPanel.tsx`) does not; plain prose and an empty note
  list do not.

### Conventions

Pure unit tests — no component rendering, no store; fetch is stubbed per test.

### Invariants And Boundaries

The suite pins the conservative posture: resolution returns `undefined` for anything
not provably one existing note, so the UI can never render a dead or guessed link.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| A stubbed-fetch unit suite; nothing crosses repositories. | — | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The module under test. | [data/notes.ts](agents-remember/dashboard/src/data/notes.ts) |
| The sibling client suite whose stub idiom this mirrors. | [data/files.test.ts](agents-remember/dashboard/src/data/files.test.ts) |

## Update History

- 2026-07-06T02:00+02:00 — Created for agent-orchestration L9: 8 unit tests over the
  notes client URLs, the shared error mapping, and the `resolveNoteReference` rules
  (prefix/nested/bare-filename hits; ambiguity, code paths, and plain prose stay
  unresolved). Verification metadata pinned until closeout stamps the L9 commit.
