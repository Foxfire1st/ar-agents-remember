# dashboard/src/data/notes.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Same-origin browser client for the L9 read-only coordination-notes API
(`mcp/.../serving/notes.py`), plus the pure reference→note resolver. It exposes typed
helpers over the two GET endpoints (`/api/notes/list`, `/api/notes/read`) and reuses
`data/files.ts`'s shared transport (`getJson`/`qs`) so the serving error idiom (a thrown
`FilesApiError`) is mapped once. It holds no state — the task reader's notes view
(`panels/TaskNotes.tsx`) owns the listing state. Its reference list uses the resolver,
and opening a note is delegated to the task-artifact reader.

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
- The consuming `ReferenceList` now resolves requirement addresses first. An explicit
  requirement address is not passed to the notes resolver; ordinary note references still use
  this module's conservative matching rules.

### Conventions

House style mirrors `data/files.ts` / `data/changeset.ts`: a `base` arg with a
same-origin default, camelCase-typed results, no store mutation.

### Invariants And Boundaries

Read-only: only GET URLs are ever built here. Resolution is conservative by design — an
ambiguous bare filename (two notes with the same basename in different folders) resolves
to `undefined` rather than picking one.

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

- The serving endpoints this client wraps. [1]
- The shared transport (`getJson`, `qs`, `FilesApiError`) reused here. [2]
- The task notes surface owns the listing and delegates reader opening; its reference list gives explicit requirement addresses precedence over note resolution. [3]
- The test suite for this module. [4]
