# mcp/src/agents_remember/tasks/task_facts.py

## Governing Overview

[Tasks overview](overview.md)

## Purpose

Provides a shared, read-only O(N) index of task identities, kinds, and terminal statuses across live and archived coordination task folders for deferral validation, gate checks, report-only flags, and reader state derivation.

## Code Commentary

### Logic

- `TaskFact(task_id, kind, status, master_id, archived)` exposes `is_master` (`kind == "master"`) and case-insensitive `is_terminal` against `RESOLVED_MASTER_ROW_STATUSES`.
- `load_task_facts(coordination_root, repo_name=None)` scans live task folders via `iter_task_folders` and then archived folders under `0_archive/` (`_iter_archive_folders`, skipping `notes`, `enclosures`, and `requirements` directories), reading canonical task JSON via `read_task_doc` with raw JSON fallback (`_read_raw_task_json`).
- Live task documents take precedence over archived copies, and standalone sub-task documents take precedence over summary entries in a master's `subTasks[]`.

## Relationships

- Shared by `application/knowledge_writer/deferrals.py`, `application/knowledge_gate/deferrals.py`, `application/knowledge_reader/deferrals.py`, and `memory_quality/dependent_flags.py`.

## Evidence

- `load_task_facts` indexes live and archived canonical task documents once per run with live-over-archive and standalone-over-summary precedence. [1]
