# dashboard/src/data/taskArtifacts.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The discriminated task-artifact reader target shared by the cockpit takeover wiring
introduced by 260831-CCR-L23. One union type replaces the previous notes-only
`NotesReaderTarget` shape: a `notes` target opens a note file inside a
master's `notes/` tree, and a `requirements` target opens a requirement
packet inside the same master's task-local `requirements/` root (adding the
`document` selector the notes variant does not need). L126 adds two members:
a `task-report` target opening one recorded role report by its exact recorded
request/task identity, and a `decisions` target carrying the log's entries for
the whole-log page; the `notes` member's `path` is optional and a `folder` flag
opens directly on a folder (rule-3 root link, rule-5 explorer link), with the
rail showing the tree and the pane waiting for a selection.

## Code Commentary

### Logic

`TaskArtifactReaderTarget` is a discriminated union on `kind`:

- `{ kind: 'notes'; repo; master; path?; folder? }` — the pre-existing notes-open
  payload, now carrying an explicit `kind: 'notes'` tag. The open note's
  notes-relative path is absent when the reader opens on a folder (rule-3 root
  link, rule-5 explorer link); `folder` is set for root/explorer links.
- `{ kind: 'requirements'; repo; master; document; path }` — the new
  requirement-open payload; `document` is the canonical task-document
  reference that selects the requirement root server-side.
- `{ kind: 'task-report'; repo; master; role; requestId; taskRepository; taskPath }` —
  one recorded role report, addressed by the exact identity the product recorded
  at role start (never by a tree walk).
- `{ kind: 'decisions'; repo; master; title; decisions }` — the log's entries in
  time order as the page holds them; the whole-log page shows them newest first
  with product-written records muted.

The module is type-only: it exports the union and nothing executable. Consumers
(`Cockpit.tsx`, `DetailPanel.tsx`, `taskReader.tsx`,
`TaskNotes.tsx`, `NotesReaderViewer.tsx`) import it under the local alias
`NotesReaderTarget` so the callbacks keep their historical name while their
payload type is the shared artifact union.

### Conventions

Single shared type definition — no consumer re-declares the target shape, so adding a
future artifact kind is a one-file union extension.

### Invariants And Boundaries

The union discriminates on `kind` only; every consumer that branches on it must
handle all four members (a requirements target without `document` is not a valid
payload; a task-report target without the full recorded identity is not
addressable).

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured for this type-only module.

No relevant domain documentation was found.

### Repo-Internal References


- The cockpit takeover renders the reader with this target spread. [1]



- The task reader wraps its prose with the requirements provider that produces these targets. [2]


- The reader itself consumes the union (notes vs requirements listing/content). [3]



### Cross-Repo References

No cross-repository implementation boundary is owned here.

No applicable cross-repository source was found.
