# mcp/src/agents_remember/application/knowledge_reader/deferrals.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Projects stored `DependentRecord.deferrals` at read time against the selected code tree, coordination task facts, and reading leaf to derive each deferral's `age` and `state` (`open`, `due`, or `orphaned`) without mutating stored records.

## Code Commentary

### Logic

- Exports `derive_deferrals`, `infer_reading_leaf`, and `opened_code_files`.
- `infer_reading_leaf(selection)` returns `selection.leaf_id` when bound, or scans `knowledge/history/*.json` in the selected directory or Git revision and returns the leaf ID only when exactly one open (`closed: false`) history file exists.
- `_deferral_state` classifies each deferral in priority order: (1) `orphaned` when `condition.task` is terminal in `task_facts`; (2) `open` when `current_leaf == deferral.createdByLeaf` (excluding the creating leaf from both task-due and file-due states); (3) `due` when `current_leaf == condition.task` or `condition.file`'s observed blob differs from `fileBlob`; (4) `open` otherwise.
- `_format_age` formats elapsed UTC age as `<1h`, `<N>h`, or `<N>d` (or `"unknown"` on unparseable timestamps).

## Relationships

- Consumed by `application/knowledge_reader/marks.py` (`dependent_list` and `dependent_detail`) to surface derived deferral state in `knowledge_read` dependent and record views and in the dashboard Knowledge reader.
- Uses `tasks/task_facts.py` (`load_task_facts`) for terminal-task orphan derivation.

## Evidence

- `derive_deferrals` derives deferral age and `open`/`due`/`orphaned` state with creating-leaf exclusion. [1]
- `infer_reading_leaf` resolves the active reading leaf from `ReaderSelection.leaf_id` or a unique open leaf history file. [2]
