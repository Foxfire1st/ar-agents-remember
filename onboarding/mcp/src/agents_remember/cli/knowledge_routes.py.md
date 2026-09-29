# mcp/src/agents_remember/cli/knowledge_routes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_routes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:49:57+02:00 |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`|
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**`agents-remember knowledge-routes MEMORY_ROOT --code CODE_ROOT [--code-commit REV] [--family FAM-ID ...] [--json]`: the curator's read-only view of family routes and their mechanical suggestion (MIK-R04 rule 3).** For each family record of the memory working tree it prints the family's routes, its route state and the suggestion labelled `mechanical`. It never writes a route; the curator places routes and writes them through the writer.

## Code Commentary

### Logic

- `add_arguments` declares `memory_root`, the required `--code`, `--code-commit`, the repeatable `--family` and `--json`.
- `run` parses the memory tree with `knowledge_tree_from_directory` and `parse_tree`. The code files a suggestion reads are the tracked and untracked, not ignored, files of `--code` (`_working_tree_files`, `git ls-files --cached --others --exclude-standard`), or with `--code-commit` the file set of `code_tree_from_git`. An unreadable input prints "cannot read the inputs" and returns 2.
- `_family_documents` builds, per family (filtered by `--family` when given), the family ID, path, status, routes, `_state_document` (`unrealizedFamily`, `routeUnassigned`, `routeless`, `uncovered`, `emptied`) and the suggestion's `to_document`.
- With `--json` it prints the documents; otherwise `_render` prints each family's states, uncovered paths, emptied routes, the suggestion, and root-level realization files ("realizations at the repository root (route .)"). A requested family that does not exist prints `unknown family: <ID>`; no families prints "no family records".

### Conventions

- Registered in `cli/__main__.py` with the umbrella's declarative `add_arguments` + `set_defaults(func=run)` pair.
- It reuses `family_routes`; it adds only input reading and printing.

### Invariants And Boundaries

- It only reads: the memory bytes are unchanged after a run (the CLI test asserts it).
- Exit status: 0 when the families are read, 2 when an input cannot be read.
- Before MIK-R37 the real memory worktree holds no family record, so the command answers "no family records".
- The human-readable output does not mark that the routes differ from the suggestion; the curator compares the two lists (review R1 finding 4, not required).

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The route design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`, §4.2) and the
requirement packet `MIK-R04@v2` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The adapter reuses the route logic; it adds only argument handling and printing.

| Finding | Anchor | Source |
| --- | --- | --- |
| The command's arguments. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_routes.py:39-50 |
| The working tree's tracked and untracked, not ignored, files. | `_working_tree_files` | mcp/src/agents_remember/cli/knowledge_routes.py:53-57 |
| Each family's routes, state and suggestion. | `_state_document`; `_family_documents` | mcp/src/agents_remember/cli/knowledge_routes.py:60-67; mcp/src/agents_remember/cli/knowledge_routes.py:92-112 |
| Reading, rendering, unknown families and the exit status. | `run`; `_render` | mcp/src/agents_remember/cli/knowledge_routes.py:115-137; mcp/src/agents_remember/cli/knowledge_routes.py:70-89 |
| The subcommand is registered. | `knowledge_routes` | mcp/src/agents_remember/cli/__main__.py:85-90 |
| The command offers the suggestion and writes nothing. | `test_the_routes_command_offers_the_suggestion_and_writes_nothing` | mcp/tests/test_knowledge_family_routes.py:415-445 |

## Cross-Repo References

No meaningful cross-repo references found: the command reads one memory working tree and one code checkout, both named by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): created this card for the new file MIK-R04 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
