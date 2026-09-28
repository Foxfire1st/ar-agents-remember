# mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-09-28T16:27:45+02:00 |
| lastVerifiedCommitHash | `58e22246cc09ef0ee12095e284a111a475081c38`                                        |
| lastVerifiedCommitDate | 2026-09-28T16:46:12+02:00|
| governingOverview      | `../overview.md`                                          |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |
| The canonical enumeration: three listed levels, the archive/enclosure filter, and a sort over only the kept entries. | `_iter_task_json` | mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py:74-90 |
| The named-tail probe, an exact same-order subset of the enumeration. | `_canonical_task_json_candidates` | mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py:93-113 |
| The two listed levels, descended the way `rglob` descends. | `_task_directories` | mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py:116-126 |
| One listing level: real directories only; an unreadable folder contributes nothing. | `_walked_directories` | mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py:133-140 |
| The rationale for the removed summary bound, which is unchanged and now sits two lines lower. | "A task-document summary limit" | mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py:65-71 |
| Regression evidence: the enumeration equals the earlier recursive glob, including its exclusions and symlink behavior. | `test_enumeration_keeps_exactly_the_canonical_depth_documents_the_recursive_glob_kept` | mcp/tests/test_task_document_body_lookup.py:231-263 |

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

## Update History

- 2026-09-28T16:27:45+02:00 — 260921-ICR-L42 curator (uncommitted candidate tree `27409ea9f3320689c28c6a810c9a88afa288bbba` over code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): **the canonical enumeration became a bounded three-level walk with the same result, and a named-tail probe was added for the body read.** Registered the five new helpers in Code Commentary and stated the equivalence contract with the earlier recursive glob, the subset-not-path-build rule for the probe, and the unchanged parse cache. Added the L42 section and six reference rows. The summary-bound rationale comment moved from `63-69` to `65-71` because of the two new imports; its text is unchanged. No stamp was advanced; closeout owns it.
- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **both governing declarations repaired.** The field named `overview.md` and the body link named `overview.md`; each resolved card-relatively to nothing, and they did not agree with each other. Both now name `../overview.md`, the route-local overview of this card's own directory. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-09-16T14:20+02:00 — 260916-TDPU (`ar/260916-tdpu`, base `67b21aeb`) curator: **the module no
  longer carries any task-document summary bound.** `_bounded_task_document_payloads` and
  `_stat_mtime_ns` are deleted, so both are dropped from Code Commentary;
  `_iter_task_document_payloads` (`_common.py:42-60`) returns every canonical task document the
  reader enumerated. The rationale the removal records lives in the module's own comment at
  `_common.py:63-69`: the old `TASK_DOCUMENT_SUMMARY_LIMIT` (250 roots-plus-newest-leaves) evicted
  silently and untested, so an operator saw a master whose sub-task rows were not clickable with no
  diagnostic and no way to tell a missing document from an unreadable one. If a bound is ever
  reintroduced it must be larger, must announce its own truncation, and must offer a way to reach
  what it hid. This card's stated one-to-one mirror is what the two deleted rows had contradicted.
  Verification metadata remains closeout-owned; no verification stamp advanced.

- 2026-08-14T06:34+02:00 — L23 final candidate review: shared snapshot construction attaches the
  latest validated task-addressed lifecycle operation and keeps private worker/recovery identity out
  of the served projection. Verification remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
