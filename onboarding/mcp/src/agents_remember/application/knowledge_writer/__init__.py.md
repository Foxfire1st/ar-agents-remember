# mcp/src/agents_remember/application/knowledge_writer/__init__.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The package surface.

- The package's public surface: the owner, the report, the request and the one operation. [1]
- The one operation it exports. [2]
- The module map names the reconsideration rows and the task-document question (MIK-R14). [3]
- The module map names the requirement endpoints module (MIK-R13). [4]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
