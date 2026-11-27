# mcp/src/agents_remember/memory/knowledge_index/consolidation_outcomes.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Derives the per-`(record_id, revision_read)` consolidation outcome (`kept`, `corrected`, `merged`, `retired`, `unresolved`) from consolidation tasks' history files and live/retired records for the index's writer-metrics table.

## Code Commentary

`OUTCOME_COLUMNS` maps the five `Outcome` literals to writer-table column names (`consolidationKept`, `consolidationCorrected`, `consolidationMerged`, `consolidationRetired`, `consolidationUnresolved`). `consolidation_outcomes(histories, records)` first collects all predecessor IDs named in any `InvariantRecord.supersedes` (so merges and splits register as `merged`), then scans only history files with non-empty `consolidation_subjects` and only `InvariantRow`/`FamilyRow` rows carrying a non-`None` `revision`. `_outcome` maps `unresolved` -> `"unresolved"`, `changed` -> `"corrected"`, retiring rows (`retired`, or `deleted` with `effect == "retire"`) -> `"merged"` if superseded else `"retired"`, and all other rows -> `"kept"`. For `"corrected"`, the outcome is attributed to the revision read (`row.revision - 1`, skipped if `< 1`); for all other outcomes, to `row.revision`. When multiple passes touch the same `(record, revision)`, `_WEIGHT` breaks ties so terminal outcomes (`corrected`/`merged`/`retired`: 2) override `unresolved` (1), which overrides `kept` (0), with equal-weight later passes overwriting earlier ones. Whether a `kept` revision reads consolidated is checked by the caller (`writer_table.py`).

## Relationships

Imported by `memory/knowledge_index/writer_table.py` (`OUTCOME_COLUMNS`, `Outcome`, `consolidation_outcomes`) and `memory/knowledge_index/query.py` (`OUTCOME_COLUMNS`, `Outcome`). Depends on `models.knowledge_files.history`, `models.knowledge_files.history_consolidation.UNRESOLVED`, and `models.knowledge_files.records`.

## Evidence

- `OUTCOME_COLUMNS` maps the five `Outcome` literals to writer-table column names, and `_WEIGHT` ranks `corrected`/`merged`/`retired` above `unresolved` above `kept`. [1]
- `consolidation_outcomes` filters to history files with `consolidation_subjects`, attributes `corrected` rows to `row.revision - 1` (requiring `>= 1`), and resolves multi-pass conflicts by `_WEIGHT`. [2]
- `_outcome` classifies `unresolved`, `changed` (`corrected`), retiring rows into `merged` (when superseded by an `InvariantRecord`) or `retired`, and all other rows as `kept`. [3]
