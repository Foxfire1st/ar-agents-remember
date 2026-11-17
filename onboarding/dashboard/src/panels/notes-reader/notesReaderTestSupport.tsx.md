# dashboard/src/panels/notes-reader/notesReaderTestSupport.tsx

## Governing Overview

[overview](overview.md)

## Purpose

Supplies shared typed answers and API fixtures for notes-reader tests.

## Code Commentary

The fixtures build entries and content, supply paged note folders, named missing responses, content reads, reference resolutions and task summaries. An optional resolution map names exact reference/path pairs. The requirement fixture supplies one registered requirement and its body.

## Relationships

NotesReaderViewer tests consume these fixtures. Empty fixture answers are controlled test inputs, not production fallbacks or broader path authority.

## Evidence

- Supplies shared typed answers and API fixtures for notes-reader tests. [1]
