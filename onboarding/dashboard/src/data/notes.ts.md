# dashboard/src/data/notes.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/notes.ts`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-05T08:27+02:00 |
| lastVerifiedCommitHash | `ea35964985f30080488270e71ac81657ac40682b` |
| lastVerifiedCommitDate | 2026-09-05T06:48:29+02:00 |
| governingOverview | `overview.md` |

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

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| A same-origin browser client; nothing crosses repositories. | — | — |

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
| The serving endpoints this client wraps. | `list_notes`; `read_note` | mcp/src/agents_remember/serving/notes.py:104-112; mcp/src/agents_remember/serving/notes.py:115-139 |
| The shared transport (`getJson`, `qs`, `FilesApiError`) reused here. | `getJson`; `qs`; `FilesApiError` | dashboard/src/data/files.ts:76-84; dashboard/src/data/files.ts:90-97; dashboard/src/data/files.ts:99-100 |
| The task notes surface owns the listing and delegates reader opening; its reference list gives explicit requirement addresses precedence over note resolution. | `TaskNotes`; `ReferenceList` | dashboard/src/panels/TaskNotes.tsx:170-220; dashboard/src/panels/TaskNotes.tsx:75-129 |
| The test suite for this module. | "builds the list / read URLs"; "throws the shared FilesApiError on a non-ok response" | dashboard/src/data/notes.test.ts:17-26; dashboard/src/data/notes.test.ts:28-31 |

## Update History

- 2026-09-05T08:27+02:00 — L31 native curator: Retained the conservative notes resolver after reviewing TaskNotes and ReferenceList; documented requirement-address precedence and delegated reader opening, with exact consumer ranges. Reviewed against frozen code `ea35964985f30080488270e71ac81657ac40682b`; this records source verification, not gate acceptance.

- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 8 citation finding(s); scoped recheck clean.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-06T01:50+02:00 — Created for agent-orchestration L9 (friction F-M): the
  `/api/notes/{list,read}` client (`listNotes`/`readNote` over the shared
  `getJson`/`qs` transport) and the pure conservative `resolveNoteReference`
  (notes-relative path with optional `notes/` prefix, or unambiguous bare filename;
  everything else stays plain text). Verification metadata pinned until closeout stamps
  the L9 commit.
