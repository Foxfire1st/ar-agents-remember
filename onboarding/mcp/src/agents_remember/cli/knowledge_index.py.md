# mcp/src/agents_remember/cli/knowledge_index.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_index.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:01:17+02:00 |
| lastVerifiedCommitHash | `ffd043f1354e94a7dcf435e10b4b7224495cbcba`|
| lastVerifiedCommitDate | 2026-09-29T08:30:03+02:00|
| governingOverview | `../../../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The adapter reuses the index package; it adds only argument handling and printing.

| Finding | Anchor | Source |
| --- | --- | --- |
| The command line and the exit statuses. | "Exit status: 0 for a complete index" | mcp/src/agents_remember/cli/knowledge_index.py:1-14 |
| Arguments. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_index.py:30-41 |
| The build or reuse, the JSON report and the exit status by state. | `run` | mcp/src/agents_remember/cli/knowledge_index.py:44-82 |
| Registration in the umbrella. | "knowledge-index" | mcp/src/agents_remember/cli/__main__.py:77-82 |
| The command reports the index and exits by state. | `test_the_command_reports_the_index_and_exits_by_state` | mcp/tests/test_knowledge_index.py:398-433 |

## Cross-Repo References

No meaningful cross-repo references found: the command reads the memory tree it is given.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
