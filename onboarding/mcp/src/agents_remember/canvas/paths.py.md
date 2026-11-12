# mcp/src/agents_remember/canvas/paths.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Owns where a task, its presenter attempts and a presenter's working folders live, and the admission each path gets. It refuses a segment that could leave its directory and a target whose physical path leaves its root.

## Code Commentary

- `path_segment` refuses anything that could leave the directory it names; `guard_path` refuses a target with a symlinked component below the root or one resolving outside it.
- `task_root`, `presenter_root` and `presenter_working_root` fix the ordering of a page's working folder: repository, task, leaf, page, attempt.
- `design_text_source` resolves the repository's own design text else the shipped default, and `_read_design` reads it within a byte ceiling; an oversized text yields no bytes at all.

## Evidence

- A path segment that could leave its directory is refused. [1]
- A symlinked component below the root or a target resolving outside it is refused. [2]
- The design text in force is the repository's own text or the shipped default. 

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/paths.py::design_text_source - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976. Retired means the anchor no longer stands, not that the cited subject was deleted.
