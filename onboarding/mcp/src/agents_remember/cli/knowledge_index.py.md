# mcp/src/agents_remember/cli/knowledge_index.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**`agents-remember knowledge-index (--memory-root DIR | --repository REPO --revision REV) (--cache-dir DIR | --coordination-root DIR)`: build or reuse the derived knowledge index of one memory tree and report it (MIK-R23).** `--memory-root` indexes a working tree's current captured state; `--repository`/`--revision` indexes a Git tree read through objects. The index lands in `--cache-dir`, or in `<coordination-root>/runtime/knowledge-index`. The printed index path is a dataset the knowledge read tools accept as their `databasePath`.

## Code Commentary

### Logic

- `add_arguments` declares two required mutually exclusive groups: the source (`--memory-root` or `--repository`, with `--revision`) and the cache (`--cache-dir` or `--coordination-root`).
- `run` refuses `--repository` without `--revision` (exit 2), opens a `KnowledgeIndexCache`, calls `for_directory` or `for_git_tree`, and prints one JSON object: `key`, `path`, `reused`, `state`, `converted`, `problems`, the build's `records`/`entries`/`historyRows` counts (`null` on reuse) and `seconds`.
- A `MemoryTreeError` or `OSError` — including a cache location inside a Git working tree — prints `{"error": …}` and exits 2.

### Conventions

- Registered in `cli/__main__.py` with the umbrella's declarative `add_arguments` + `set_defaults(func=run)` pair.

### Invariants And Boundaries

- Exit status: 0 for a complete index, 1 for a partial one, 2 when the tree cannot be read.
- It only reads the tree; the index lives outside any Git working tree.
- The installed runtime does not call it before MIK-R37.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The adapter reuses the index package; it adds only argument handling and printing.

- The command line and the exit statuses. [1]
- Arguments. [2]
- The build or reuse, the JSON report and the exit status by state. [3]
- Registration in the umbrella. [4]
- The command reports the index and exits by state. [5]

### Cross-Repo References

No meaningful cross-repo references found: the command reads the memory tree it is given.

No cross-repo boundary is crossed by this file.
