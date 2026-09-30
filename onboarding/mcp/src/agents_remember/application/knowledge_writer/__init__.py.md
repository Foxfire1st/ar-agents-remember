# mcp/src/agents_remember/application/knowledge_writer/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:13:48+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The curator writer for text knowledge (MIK-R12): the package front door.** Its docstring maps nine
modules (`requirement_links` since MIK-R13; `reconsideration` and `open_questions` since MIK-R14) and names the one operation; it re-exports `Owner`, `WriteReport`, `WriteRequest` and
`write_knowledge`, which is everything the CLI route (`cli/knowledge_write_route.py`) and the tests import.

## Code Commentary

### Logic

- `__all__` is exactly the four names above. The history check (`history_check.py`) is not listed in the
  docstring's module map, although the writer calls it; it is an internal step of `write_knowledge`.
- Since MIK-R13 the module map names `requirement_links`: the requirement endpoints a run's records link, resolved
  by their owner and reported, never refused. Nothing is re-exported for it; the report carries its result.
- Since MIK-R14 the map names `reconsideration` (the `still_rejected` and `raise` rows: `raise` sets the decision
  `under_reconsideration` and appends a question for the developer; `still_rejected` refreshes the fired links) and
  `open_questions` (that question, appended to the leaf's task document through `task_doc`). Nothing is re-exported
  for them: the CLI route imports `open_questions` and `reconsideration.OpenQuestions` directly.

### Conventions

- Package imports are absolute (`agents_remember.application.knowledge_writer.<module>`).

### Invariants And Boundaries

- `knowledge-ingest` and `knowledge-bootstrap` reach this package only when the memory tree they write is
  **converted** (it holds `knowledge/layout.json`). Unconverted memory keeps the installed database ingest
  until the cutover (MIK-R37); the database modules (`application/knowledge_ingest.py`,
  `knowledge_curator_ingest.py`, `knowledge_bootstrap*.py`) are untouched, and their removal is MIK-R26's
  (L26).

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

The package surface.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package's public surface: the owner, the report, the request and the one operation. | `__all__` | mcp/src/agents_remember/application/knowledge_writer/__init__.py:33-33 |
| The one operation it exports. | `write_knowledge` | mcp/src/agents_remember/application/knowledge_writer/writer.py:98-155 |
| The module map names the reconsideration rows and the task-document question (MIK-R14). | `reconsideration`; `open_questions` | mcp/src/agents_remember/application/knowledge_writer/__init__.py:15-18 |
| The module map names the requirement endpoints module (MIK-R13). | `requirement_links` | mcp/src/agents_remember/application/knowledge_writer/__init__.py:13-14 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): **body updated for MIK-R14.** Purpose and Logic record that the docstring's module map now names nine modules, adding `reconsideration` and `open_questions` (nothing re-exported for them). One row added. The `__all__` row was projected by the installed fixer, and its generated bullet is kept. No verification stamp was advanced.
- 2026-09-30T10:05:30+00:00: Generated citation repair: `__all__` repointed to mcp/src/agents_remember/application/knowledge_writer/__init__.py:33-33. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): **body updated for MIK-R13.** Purpose and Logic record that the docstring's module map now names `requirement_links` (seven modules, not six); one row was added. No claim the fixer re-pointed was reworded. No verification stamp was advanced.
- 2026-09-30T01:07:55+00:00: Generated citation repair: `__all__` repointed to mcp/src/agents_remember/application/knowledge_writer/__init__.py:29-29. No content impact: mechanical anchor-range projection bound to citation source snapshot 8a187177fd97aa785f74b03e4a26914c71c4a09b0afe5ab323208b62b13057b0; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
