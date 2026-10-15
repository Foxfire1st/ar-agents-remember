# mcp/tests/test_worklist_publication.py

## Governing Overview

[governing overview](overview.md)

## Purpose

F09/F13: the worklist publisher changes only different text.

## Code Commentary

The suite checks same document retains inode and times; missing unreadable or other text is atomically replaced; changed document replaces inode and publishes new text; unreadable existing file still uses atomic publication. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- F09/F13: the worklist publisher changes only different text. [1]
