# dashboard/src/panels/notes-reader/NotesReaderViewer.test.tsx

## Governing Overview

[notes-reader/ overview](overview.md)

## Purpose

`NotesReaderViewer.test.tsx` proves the notes-reader takeover: the reader appears only when a note is
opened, keeps the Operations rails while hidden, and stays mounted across Back and Forward like the
File Viewer.

## Role-Report Kind Case

The suite also renders the `role-report` kind and pins that the supplied report's body, file name and
truncation notice appear in the shared pane with no rail (MIK-R75 rule 4).

## Code Commentary

### Logic

The two cases that assert the reader is absent initially and survives Back now mount
`CockpitShell initialView="operations"` because MIK-R79 made Chats the opening view. The reader
behavior asserted (absence, rails, mounted identity across Back) is unchanged.

### Conventions

Vitest + Testing Library; the notes API is stubbed per case.

### Invariants And Boundaries

The cases bind the notes reader's takeover and keep-alive behavior on the Operations context; they do
not assert the product tab list.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The requirement packet
`MIK-R79@v1` (rule 16) fixes the opening view; it lives outside the code and memory repositories, so
it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The cases mount the shell explicitly on Operations. [8]
- The takeover the cases drive. [9]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
