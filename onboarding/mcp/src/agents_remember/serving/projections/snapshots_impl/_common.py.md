# mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py

## Governing Overview

[serving projections overview](../overview.md)

## Purpose

Shared file-surface helpers for the observer snapshot readers. The readers split by responsibility (providers, runtime enclosures, analytical surfaces, task documents) share the task-document payload cache, the status payload TTL cache, and the small JSON/stat helpers collected here. No reader logic lives in this module; it is the common leaf the split modules import.

This module also owns **the one canonical task-document enumeration** (`_iter_task_json`) and its
bounded companion (`_canonical_task_json_candidates`). The enumeration feeds every always-on reader
(`read_task_documents`, `read_series_documents`, the closeout-queue reader), so its cost is paid on
each projection pass. Since 260921-ICR-L42 it walks only the three canonical levels
`tasks/<repository>/<task>/` instead of recursively globbing every JSON under `tasks/` and
discarding most of the results.

## Code Commentary

- `_TaskDocumentLifecycleMaps`
- `_iter_task_document_payloads`
- `_iter_task_json` (since 260921-ICR-L42: lists the repository folders, then their task folders, then
  each task folder's `*.json` entries; drops archive and enclosure paths; sorts only what is left)
- `_canonical_task_json_candidates` (since 260921-ICR-L42: the enumeration restricted to named
  `<task>/<file>.json` tails under every repository folder. Only the named task folders are listed,
  and the result is exactly the enumeration's subset for those tails, in the same order. Its only
  caller is `_task_documents._graph_master_docs`)
- `_task_directories` (since 260921-ICR-L42: every `tasks/<repository>/<task>/` folder)
- `_outside_archive_and_enclosures` (since 260921-ICR-L42: the `0_archive` / `enclosures` path filter)
- `_walked_directories` (since 260921-ICR-L42: one `os.scandir` level. It keeps real directories only,
  skips symlinked ones with `is_dir(follow_symlinks=False)`, and treats an unreadable folder as empty)
- `_json_entries` (since 260921-ICR-L42: every entry named `*.json` in one folder, of any type. The
  reader accepts or refuses each one)
- `_read_json`
- `_as_int`
- `_as_float`
- `_text_or_none`
- `_report_label`
- `_file_age_seconds`
- `_current_phase_text`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py`.
- **`_iter_task_json` must return exactly the list the earlier recursive glob returned**, element for
  element and in order. That glob was `sorted(tasks_root.rglob("*.json"))`, filtered to depth 3
  and to paths outside `0_archive` and `enclosures`. Symlinked folders are not descended, which
  matches `rglob` on this Python. A symlinked *file* named `*.json` and a directory named `*.json` are
  still listed. Historical copies under `notes/` and report or enclosure folders are never reached,
  because the walk stops at the task folder. The enumeration test keeps the old comprehension inline
  as its reference.
- **`_canonical_task_json_candidates` is defined as a subset of `_iter_task_json`, not as a direct
  path build.** A naive `tasks/<ref.repository>/<ref.path>` probe would miss a master held in another
  repository folder under the same identity. It would also change which duplicate wins the last-wins
  join. The review's mutation M1 is exactly that probe, and the byte-identity test catches it.
- The walk adds no index, cache or store. `_iter_task_document_payloads` keeps its existing parse
  cache (`TaskDocumentPayloadCache`) unchanged. Since L42 the body read no longer calls it, so HTTP
  threads no longer prune or fill that cache.

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.
- The canonical enumeration: three listed levels, the archive/enclosure filter, and a sort over only the kept entries. [1]
- The named-tail probe, an exact same-order subset of the enumeration. [2]
- The two listed levels, descended the way `rglob` descends. [3]
- One listing level: real directories only; an unreadable folder contributes nothing. [4]
- The rationale for the removed summary bound, which is unchanged and now sits two lines lower. [5]
- Regression evidence: the enumeration equals the earlier recursive glob, including its exclusions and symlink behavior. [6]

## 260921-ICR-L42 Canonical-Depth Enumeration

Before this leaf, `_iter_task_json` did `sorted(tasks_root.rglob("*.json"))` and then kept only depth-3
paths outside the archive and enclosures. On the live corpus that meant walking about 34,000 JSON files
(3.1 GB, most under `notes/` and report folders) and sorting them, only to keep about 560. It cost
about 0.6 s per call and 14,282 `relative_to` calls in the task-document body profile. Because every
always-on projection pass calls it, that cost also competed with every concurrent HTTP read for the
GIL. The new walk lists only the three canonical levels and returns the same list. On the same corpus
it took 0.0056 s, against 0.6156 s before (task evidence, not a contract). The parse cache and the
payload schema filter are unchanged.

`_canonical_task_json_candidates` gives the on-demand body read what it needs: the enumeration entries
for named tails, at a cost that follows the names rather than the corpus. Keeping it defined through
the same `_task_directories` / `_json_entries` / `_outside_archive_and_enclosures` helpers is what makes
the subset exact. That is why the body read projects byte-identical bodies.

## L23 Final Candidate Disposition

Shared enclosure snapshot construction selects the latest validated lifecycle operation and projects
bounded task-addressed phase, timing, command, report, and failure guidance. Worker, lease, and
resume identities remain private to recovery.
