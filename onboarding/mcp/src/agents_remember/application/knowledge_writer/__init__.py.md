# mcp/src/agents_remember/application/knowledge_writer/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T10:05:46+02:00 |
| lastVerifiedCommitHash | `cd3e943d740b490d391722389af0a6bca0ccf93e`|
| lastVerifiedCommitDate | 2026-09-29T10:38:08+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The curator writer for text knowledge (MIK-R12): the package front door.** Its docstring maps the six
modules and names the one operation; it re-exports `Owner`, `WriteReport`, `WriteRequest` and
`write_knowledge`, which is everything the CLI route (`cli/knowledge_write_route.py`) and the tests import.

## Code Commentary

### Logic

- `__all__` is exactly the four names above. The history check (`history_check.py`) is not listed in the
  docstring's module map, although the writer calls it; it is an internal step of `write_knowledge`.

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
| The package's public surface: the owner, the report, the request and the one operation. | `__all__` | mcp/src/agents_remember/application/knowledge_writer/__init__.py:27-27 |
| The one operation it exports. | `write_knowledge` | mcp/src/agents_remember/application/knowledge_writer/writer.py:76-118 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
