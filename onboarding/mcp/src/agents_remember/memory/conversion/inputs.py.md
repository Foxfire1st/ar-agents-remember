# mcp/src/agents_remember/memory/conversion/inputs.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Reads a memory tree to convert, from a working directory or a Git tree, and writes a finished
conversion (MIK-R24 rule 6).** Both readers return the same `MemoryInput`: the exact bytes of every file
under `knowledge/` and `onboarding/`, read by the validator's own tree readers (so the route-index cache
is excluded the same way), plus a readable path to the tree's `knowledge.sqlite` when it has one.

## Code Commentary

### Logic

- `memory_from_directory(root)` reads the working tree through `knowledge_tree_from_directory`, and
  takes `root/knowledge.sqlite` when it is a file.
- `memory_from_git(repository, treeish, scratch)` reads the tree through `knowledge_tree_from_git`. The
  database blob, if `<treeish>:knowledge.sqlite` exists, is copied to `scratch/<blob>.sqlite` (once per
  blob), because SQLite opens files, not blobs.
- `write_changed(root, changed)` writes each changed file through a sibling temporary file
  (`.<name>.converting`) and a rename, in path order.

### Conventions

- `DATABASE_NAME = "knowledge.sqlite"`, the legacy database's committed name.

### Invariants And Boundaries

- The database copy is only ever opened read-only (`legacy_db` opens with `SQLITE_OPEN_READONLY`).
- `write_changed` is called only after the whole converted tree validated, so a refused conversion writes
  nothing.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The two readers and the writer.

- A working tree and its database. [1]
- A Git tree, with its database blob copied to scratch. [2]
- Writing a finished conversion through a temporary file and a rename. [3]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
