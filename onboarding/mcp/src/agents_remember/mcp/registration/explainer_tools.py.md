# mcp/src/agents_remember/mcp/registration/explainer_tools.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The explainer seat's tool declarations in a light owner: authoring, admitted reads, read-only Git, knowledge records, grades and the one report to the architect.

## Code Commentary

- Declaring these loads no reader, writer or renderer: each body imports its service on the call, and the authoring class, its write guard and the source reader are resolved on every request rather than at registration.
- Registration order is part of the published surface — `knowledge_read` is registered after the six Git tools and the judgment and report instances after them, so a seat's discovery order is the one it has always published.
- `source` re-reads the packet on each call, so an Update's new packet needs no restart, and it takes a side and a relative path only: there is no repository, HEAD or revision argument.
- The judgment and report objects are built once on first call and kept, because each carries construction-time identity — the seat, its fingerprints, the tray paths — and a per-call rebuild would be a different object.
- The surfaces are bounded at the edge: reads answer 12000 characters at a time with the whole file's digest, listing stops at 400 entries and depth 4, search at 200 files and 50 matches, grades at 200 references, and `documentation` is authoring help that is never review evidence.

## Evidence

- The explainer's surface is supplied on the server the seat launch already built [1]
- Authoring tools refuse arbitrary file reads and write only under the environment's own folders [2]
- The Git tools read named objects and never a worktree path [3]
- Admitted reads are bounded per call rather than returning a whole file [4]
- A grade carries the binding it was made at and refuses when the environment left it [5]
- One report is filed per tray message, with no argument for the message's own text [6]
