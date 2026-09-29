# mcp/src/agents_remember/cli/knowledge_write_route.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_write_route.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T23:27:43+02:00 |
| lastVerifiedCommitHash | `46ca74302e76cf40fb6370ea9ece16d8fa719f00`|
| lastVerifiedCommitDate | 2026-09-30T00:07:49+02:00|
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
  relative to the task root. Since MIK-R11 the request also carries `decisions=leaf_decisions(contract)`:
  `leaf_decisions` binds the task owner's `tasks/leaf_decisions.leaf_decision_refusal` to the contract's
  task root and leaf, so a planned `dropped` row's cited decision is resolved at write time through the
  strict leaf lookup (ruling F1). `run_wave_write` binds none, so a wave refuses a `dropped` planned row.
- `run_wave_write` (`knowledge-bootstrap`): a bootstrap has no leaf, so it writes as the wave `--wave` names
  (`[A-Za-z0-9._-]`); its history file is `knowledge/history/<wave>.json` (MIK-R07 rule 8); the task is
  the bootstrap scope (architect ruling 2).
- `unconverted_write_refusal` (MIK-R24 rule 9): for a leaf contract whose memory worktree is **unconverted**,
  it asks `worktrees/knowledge_crossing.unconverted_line_refusal` whether the official memory branch's tip
  is already converted. If it is, `knowledge-ingest` prints the refusal, naming the crossing sync, and exits
  refused before the database route reads anything. Otherwise it returns `None` and the database route runs
  as before. **Inert until the official line is converted (architect ruling, 2026-09-29):** no line is
  converted before MIK-R37, so no run changes today.
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
| The database-only flags refused by name. | `_DATABASE_ONLY` | mcp/src/agents_remember/cli/knowledge_write_route.py:43-50 |
| The layout-marker test. | `is_converted` | mcp/src/agents_remember/cli/knowledge_write_route.py:55-58 |
| The rule 9 write refusal for an unconverted leaf tree whose official line is converted. | `unconverted_write_refusal`; `unconverted_line_refusal` | mcp/src/agents_remember/cli/knowledge_write_route.py:61-71; mcp/src/agents_remember/worktrees/knowledge_crossing.py:163-195 |
| The owner from the contract and `task.json`. | `leaf_owner` | mcp/src/agents_remember/cli/knowledge_write_route.py:95-107 |
| The task owner's decision resolver for the leaf (MIK-R11). | `leaf_decisions`; `leaf_decision_refusal` | mcp/src/agents_remember/cli/knowledge_write_route.py:136-140 |
| The leaf route, which binds that resolver. | `run_leaf_write`; "decisions=leaf_decisions(contract)" | mcp/src/agents_remember/cli/knowledge_write_route.py:143-175 |
| The wave route. | `run_wave_write` | mcp/src/agents_remember/cli/knowledge_write_route.py:178-212 |
| The ingest dispatch on the loaded contract. | `run` | mcp/src/agents_remember/cli/knowledge_ingest.py:673-709 |
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
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** The `run_leaf_write` Logic bullet now names `leaf_decisions`, the task owner's decision resolver bound per leaf (architect ruling 2026-09-29T22:35:34 F1: the strict lookup); a wave binds none. One row added and the leaf-route row reworded; ranges re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): Added the MIK-R24 rule 9 `unconverted_write_refusal` to Logic, with its ruling (inert until the official line is converted), and added its row. Re-measured the six existing rows, which were one to fourteen lines off after MIK-R12 and this leaf.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
