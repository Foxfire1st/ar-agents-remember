# dashboard/src/data/notes.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/notes.ts`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T01:50+02:00                           |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`       |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Same-origin browser client for the L9 read-only coordination-notes API
(`mcp/.../serving/notes.py`), plus the pure reference→note resolver. It exposes typed
helpers over the two GET endpoints (`/api/notes/list`, `/api/notes/read`) and reuses
`data/files.ts`'s shared transport (`getJson`/`qs`) so the serving error idiom (a thrown
`FilesApiError`) is mapped once. It holds no state — the task reader's notes view
(`panels/TaskNotes.tsx`) owns its component state and calls these helpers directly.

## Code Commentary

### Logic

- Result interfaces mirror the L9 JSON shape one-for-one: `NoteEntry`
  (`name`/`path` notes-root-relative posix/`size`/`language`), `NotesListing`
  (`repo`/`master`/`notes[]`/`truncated` — the server's honest depth-cap flag),
  `NoteContent` (`language: "binary"` means undecodable, content empty).
- `listNotes(repo, master, base?)` and `readNote(repo, master, path, base?)` build their
  query strings with `qs` and delegate to `getJson` (both imported from `./files`).
- `resolveNoteReference(reference, notePaths)` is the pure resolver behind
  reference-link resolution: it extracts path-like tokens (`PATH_TOKEN` — contiguous
  path characters ending in a dotted extension, so surrounding prose never bleeds in),
  strips an optional `notes/` prefix, and returns the first token that names an existing
  note — by notes-relative path, or by an UNAMBIGUOUS bare filename (a basename matching
  exactly one note). Anything else returns `undefined`, so a non-matching reference
  stays plain text: never a dead link, never a guessed one.

### Conventions

House style mirrors `data/files.ts` / `data/changeset.ts`: a `base` arg with a
same-origin default, camelCase-typed results, no store mutation.

### Invariants And Boundaries

Read-only: only GET URLs are ever built here. Resolution is conservative by design — an
ambiguous bare filename (two notes with the same basename in different folders) resolves
to `undefined` rather than picking one.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| A same-origin browser client; nothing crosses repositories. | — | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The serving endpoints this client wraps. | [serving/notes.py](agents-remember/mcp/src/agents_remember/serving/notes.py) |
| The shared transport (`getJson`, `qs`, `FilesApiError`) reused here. | [data/files.ts](agents-remember/dashboard/src/data/files.ts) |
| The notes view consuming these helpers + the resolver. | [panels/TaskNotes.tsx](agents-remember/dashboard/src/panels/TaskNotes.tsx) |
| The test suite for this module. | [data/notes.test.ts](agents-remember/dashboard/src/data/notes.test.ts) |

## Update History

- 2026-07-06T01:50+02:00 — Created for agent-orchestration L9 (friction F-M): the
  `/api/notes/{list,read}` client (`listNotes`/`readNote` over the shared
  `getJson`/`qs` transport) and the pure conservative `resolveNoteReference`
  (notes-relative path with optional `notes/` prefix, or unambiguous bare filename;
  everything else stays plain text). Verification metadata pinned until closeout stamps
  the L9 commit.
