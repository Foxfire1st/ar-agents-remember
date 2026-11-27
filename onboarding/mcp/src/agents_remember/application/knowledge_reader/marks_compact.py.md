# mcp/src/agents_remember/application/knowledge_reader/marks_compact.py

## Governing Overview

[application](../overview.md)

## Purpose

Pure compact row projection for dependent records (`view="dependent"` with `compact=True` and `view="impact"` dependents), stripping 40-character blob hashes and repeated prose so stale-dependent verification stays compact.

## Code Commentary

- `compact_dependent_row` retains `id`, `document`, `state`, `deferred` (bool), `confirmedUncommitted` (bool), and an integer `movedLinks` count instead of full moved-link objects and blob hashes.
- Truncates `confirmed.commit` to 10 characters as `confirmedCommit` and includes `confirmedTask` when non-empty.
- `_aggregate_conditions` deduplicates and sorts `deferrals[*].condition.task` and `condition.file`; `compact_dependent_row` emits a single string for one distinct value or a sorted list for multiple values (`conditionTask`, `conditionFile`), omitting the key when empty.
- `compact_dependent_rows` projects a sequence of dependent rows via `compact_dependent_row`.

## Relationships

- Re-exported by `application/knowledge_reader/marks.py` and called by `application/knowledge_impact.py` (`compact_dependent_rows`); tested in `mcp/tests/test_kno_r07_knowledge_queries.py`.
- Pure stdlib module with no internal repository dependencies.

## Evidence

- `compact_dependent_row` omits blob hashes and boilerplate prose, shortens `confirmedCommit` to 10 characters, and emits an integer `movedLinks` count. [1]
- `_aggregate_conditions` deduplicates and sorts task and file conditions across multiple deferrals. [2]
