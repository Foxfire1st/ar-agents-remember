# dashboard/src/data/notes.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Same-origin browser client for the L9 read-only coordination-notes API
(`mcp/.../serving/notes.py`). It exposes typed
helpers over the folder endpoint (`/api/notes/folder`), the reference-resolution POST
(`/api/notes/resolve`) and the read GET (`/api/notes/read`), and reuses
`data/files.ts`'s shared transport (`getJson`/`qs`) so the serving error idiom (a thrown
`FilesApiError`) is mapped once. It holds no state — the task reader's notes view
(`panels/TaskNotes.tsx`) owns the listing state. Reference matching lives on the server;
opening a note is delegated to the task-artifact reader.

## Code Commentary

### Logic

- Result interfaces mirror the JSON shape one-for-one: `FolderEntry`
  (`name`/`path` notes-root-relative posix/`kind`/`size`/`language`), `NotesFolder`
  (`repo`/`master`/`path`/`entries[]`/`total`/`offset`/`limit`/`remaining`/`exists`/`reason`),
  `NoteContent` (`language: "binary"` means undecodable, content empty),
  `NoteResolution` (`reference`/`path`, null staying plain text).
- `listFolder(repo, master, path, offset, base?)` and `readNote(repo, master, path, base?)` build their
  query strings with `qs` and delegate to `getJson` (both imported from `./files`).
- `resolveNoteReferences(repo, master, references, base?)` POSTs the document's references
  in one request; the server answers each with a notes path or null, so the page never
  fetches the paths of all notes. Bare filenames resolve only at the notes root, never by
  a tree walk (Parent ruling L126-REFERENCE-FORMAT-RULING).
- The consuming `ReferenceList` now resolves requirement addresses first. An explicit
  requirement address is not passed to the notes resolver; ordinary note references still use
  this module's conservative matching rules.

> 260928-MIK-L126 removed the client pure resolver (`resolveNoteReference`, `PATH_TOKEN`):
> reference matching lives on the server (`resolveNoteReferences` above).

### Conventions

House style mirrors `data/files.ts` / `data/changeset.ts`: a `base` arg with a
same-origin default, camelCase-typed results, no store mutation.

### Invariants And Boundaries

Read-only: only GET URLs and one POST are ever built here. Resolution is conservative by design —
a bare filename that exists only in a sub-folder stays plain text rather than being guessed,
and the request carries only the paths the document names, never the paths of all notes.

### Todos

No task-independent follow-up was identified in the reviewed client/resolver behavior.

## Evidence

### Cross-Repo References

No meaningful cross-repo references found.

A same-origin browser client; nothing crosses repositories.

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The folder, resolve and read endpoints this client wraps. [1]

- The task page owns the Notes line and delegates reader opening. [3]

- The test suite for this module. [4]
- The shared transport (`getJson`, `qs`, `FilesApiError`) reused here. [2]
