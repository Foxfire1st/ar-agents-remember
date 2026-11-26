# mcp/src/agents_remember/memory_quality/dependent_flags.py

## Governing Overview

[memory_quality route overview](overview.md)

## Purpose

Computes non-blocking `reportOnlyFindings` entries (`check: "dependent_flags"`) for task memory-quality checks without altering staleness computation, `ok`, or `findingCount`.

## Code Commentary

### Logic

- Exports `DEPENDENT_FLAGS_CHECK`, `DependentFlagScope`, `DependentFlagInputs`, and `collect_dependent_report_only_findings`.
- Emits four report-only finding kinds:
  1. `pre_base_stale_confirmation`: flags a leaf that confirmed an existing dependent without editing `record.document` (checked against the leaf's `B..C` diff and untracked files) when at least one `stands_on` link (record revision, file blob, or anchor content/refreshed anchor) was already stale at `B`, attaching `preBaseMovedLinks`.
  2. `deferral_lifted`: reports every `RecordRow` with `disposition == "deferral_lifted"` in the selected leaf's latest history attempt (or open/added histories when `owner` is unset).
  3. `deferral_orphaned`: warns on any open deferral (not created by `owner`) whose `condition.task` is terminal in `load_task_facts`.
  4. `deferral_due_warning`: warns on any open deferral (not created by `owner`) whose watched `condition.file` changed relative to `fileBlob` before `B` (`watched not in changed_files`).

## Relationships

- Called by `memory_quality/converted_check.py` (`converted_knowledge_check`) using `DependentFlagScope` supplied from `application/memory_quality/controller.py` through `memory_quality/check.py` (`DriftCheckContext`).
- Reads task facts via `tasks/task_facts.py` (`load_task_facts`).

## Evidence

- `collect_dependent_report_only_findings` emits `pre_base_stale_confirmation`, `deferral_lifted`, `deferral_orphaned`, and `deferral_due_warning` as non-blocking report-only findings. [1]
