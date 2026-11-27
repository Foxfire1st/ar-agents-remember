# mcp/src/agents_remember/tasks/consolidation_list.py

## Governing Overview

[overview](overview.md)

## Purpose

Defines the `ConsolidationList` Pydantic schema and document-level kind guard for a task document's optional `consolidationList` field.

## Code Commentary

`ListedFamily` and `ListedRule` enforce `FAM-…` and `INV-…` ID syntax using `models.knowledge_files.ids.id_pattern` without reading knowledge trees (whether a listed ID exists in memory is evaluated later by the worklist). `ConsolidationList` (`extra="forbid"`, `populate_by_name=True`) holds optional `families` and `rules` lists with no size cap. Its `@model_validator(mode="after")` `_require_ids` refuses empty lists (directing callers to clear with `null`) and rejects duplicate IDs within either list. `listed_ids()` returns all listed IDs with families before rules. `check_consolidation_list(kind, listing)` refuses a non-`None` `consolidationList` on a `master` document so consolidation always runs on a leaf task.

## Relationships

Imported by `tasks/document.py` (`ConsolidationList`, `check_consolidation_list`), `tasks/render.py` (`ConsolidationList`), and `tasks/document_field_effects.py` (`ConsolidationList`). Pairs with `tasks/consolidation_task.py`, which checks list presence and determines leaf seat roles.

## Evidence

- `ListedFamily` and `ListedRule` validate family and invariant ID syntax using `id_pattern` without consulting knowledge records. [1]
- `ConsolidationList` forbids unknown keys, requires at least one listed ID and per-list uniqueness via `_require_ids`, and returns families-first IDs via `listed_ids()`. [2]
- `check_consolidation_list` rejects any non-`None` `consolidationList` on a `master` document. [3]
