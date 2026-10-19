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
- The design text in force is the repository's own text or the shipped default. [3]
