# mcp/src/agents_remember/serving/projections/snapshots_impl/_task_consolidation.py

## Governing Overview

[serving projections overview](../overview.md)

## Purpose

Projects a consolidation task document's `consolidationList` and live per-subject outcomes from the task's memory worktree history into `TaskConsolidationNode` and folds those rows into the document's `body_revision`.

## Code Commentary

`consolidation_fields(doc, body_revision, *, preview)` calls `task_consolidation_node(doc)`; if `doc.consolidationList` is `None`, it returns `(None, body_revision)` unchanged. Otherwise it hashes `body_revision` plus canonical JSON of the full `TaskConsolidationNode` (including every row) into a SHA-256 revision so changes in the memory worktree outside the task tree trigger dashboard refetches, and strips `rows` to `None` when `preview=True` while preserving aggregate counts. `task_consolidation_node` resolves the task's memory worktree and owner ID (`contract.leaf_id or contract.task_name`) through `doc.seriesContractPath` via `load_contract`, tracking every file read inside `body_input(...)`. `_subjects` builds a deduplicated ordered list of subjects: listed families, listed rules, then members read from each family's JSON record in `knowledge/families/`. `_history_rows` loads and merges all attempts matching `owner_history_attempt` under `knowledge/history/` via `merged_leaf_history`, returning `{}` if no history file exists yet and `None` on parse/IO failure (setting `memoryRead=False` and leaving all outcomes `open`). `_outcome` maps dispositions: `stands` or `no_impact` -> `"stands"`, `"unresolved"` -> `"unresolved"`, absent row -> `"open"`, and any other disposition -> `"corrected"`.

## Relationships

Called by `mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py` (`consolidation_fields`) when projecting task document summaries and bodies. Produces `TaskConsolidationNode` and `TaskConsolidationRowNode` models from `observer.projection_task_documents`, rendered on the frontend by `dashboard/src/panels/detail-panel/consolidationBlock.tsx`. Depends on `serving.projections.task_body_generation.body_input`, `worktrees.worktree_contract.load_contract`, and `models.knowledge_files.{documents,history,records}`.

## Evidence

- `consolidation_fields` folds the full serialized `TaskConsolidationNode` into a SHA-256 `body_revision` and drops `rows` only on `preview=True`, leaving non-consolidation documents untouched. [1]
- `task_consolidation_node` reads the task's memory worktree and history, builds per-subject rows and outcome counts, and records whether memory was readable in `memoryRead`. [2]
- `_subjects` emits each subject once in deterministic order: listed families, listed rules, then members discovered from each listed family's record. [3]
- `_outcome` classifies history rows as `"open"` (missing), `"stands"` (`stands`/`no_impact`), `"unresolved"` (`unresolved`), or `"corrected"` (any other disposition). [4]
