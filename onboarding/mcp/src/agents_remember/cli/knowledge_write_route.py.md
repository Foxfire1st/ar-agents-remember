# mcp/src/agents_remember/cli/knowledge_write_route.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_write_route.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T10:05:46+02:00 |
| lastVerifiedCommitHash | `cd3e943d740b490d391722389af0a6bca0ccf93e`|
| lastVerifiedCommitDate | 2026-09-29T10:38:08+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**The file-writer route of `knowledge-ingest` and `knowledge-bootstrap` (MIK-R12 rule 7).** Both
commands keep one spelling; the memory tree they write decides the writer. A **converted** tree (it holds
`knowledge/layout.json`) is written by `write_knowledge`; an **unconverted** tree keeps the database ingest
exactly as before. Until the cutover (MIK-R37) no production memory tree is converted, so no production run
changes (architect ruling 1).

## Code Commentary

### Logic

- `is_converted` tests the layout marker; `load_leaf_contract` loads the contract or returns `None` (the
  database route then reports why); `converted_contract` combines the two.
- `leaf_owner`: the leaf is the contract's `leaf_id` (else task name); the task is `task.json` `id`, else the
  leaf ID's prefix before `-L<n>`.
- `run_leaf_write` (`knowledge-ingest`): a blank `--authorization-ref` exits 2 with the database route's
  message; the database-only flags (`--candidate-directory`, `--baseline`, `--rebase-baseline`,
  `--publish-to`, `--publish`, `--expected-destination`) are refused **by name**, exit 2; an unreadable list
  exits 2; then `write_knowledge` writes into the contract's memory worktree, with the hand-off path
  relative to the task root.
- `run_wave_write` (`knowledge-bootstrap`): a bootstrap has no leaf, so it writes as the wave `--wave` names
  (`[A-Za-z0-9._-]`); its history file is `knowledge/history/<wave>.json` (MIK-R07 rule 8); the task is
  the bootstrap scope (architect ruling 2).
- Exit status: 0 written or planned, 1 refused (every problem in the report, nothing written), 2 invocation
  refused. `--json` prints `WriteReport.to_document()`.

### Conventions

- Imported by `cli/knowledge_ingest.py` and `cli/knowledge_bootstrap.py`; not registered as its own subcommand.

### Invariants And Boundaries

- No database write happens on this route, and no argument is silently ignored.
- `--commit` stays the commit word: without it the run plans, validates and reports.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The dispatch test and the two routes.

| Finding | Anchor | Source |
| --- | --- | --- |
| The database-only flags refused by name. | `_DATABASE_ONLY` | mcp/src/agents_remember/cli/knowledge_write_route.py:40-47 |
| The layout-marker test. | `is_converted` | mcp/src/agents_remember/cli/knowledge_write_route.py:52-55 |
| The owner from the contract and `task.json`. | `leaf_owner` | mcp/src/agents_remember/cli/knowledge_write_route.py:79-91 |
| The leaf route. | `run_leaf_write` | mcp/src/agents_remember/cli/knowledge_write_route.py:120-151 |
| The wave route. | `run_wave_write` | mcp/src/agents_remember/cli/knowledge_write_route.py:154-188 |
| The ingest dispatch on the loaded contract. | `run` | mcp/src/agents_remember/cli/knowledge_ingest.py:672-708 |
| The bootstrap dispatch on the admitted memory root. | `_run` | mcp/src/agents_remember/cli/knowledge_bootstrap.py:515-537 |
| Planning writes nothing; unconverted memory is not this route. | `test_a_planning_run_writes_nothing_and_unconverted_memory_is_not_this_route` | mcp/tests/test_knowledge_writer.py:440-457 |
| Blank authorization refused and recorded. | `test_the_leaf_file_route_refuses_a_blank_authorization_and_reports_it` | mcp/tests/test_knowledge_writer.py:601-611 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
