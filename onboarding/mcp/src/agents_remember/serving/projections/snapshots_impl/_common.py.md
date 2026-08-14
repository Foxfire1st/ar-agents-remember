# mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `aeca9a2839c965218a61a3040e15cb84367ebeca`                                        |
| lastVerifiedCommitDate | 2026-08-14T13:35:55+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[serving projections overview](overview.md)

## Purpose

Shared file-surface helpers for the observer snapshot readers. The readers split by responsibility (providers, runtime enclosures, analytical surfaces, task documents) share the task-document payload cache, the status payload TTL cache, and the small JSON/stat helpers collected here. No reader logic lives in this module; it is the common leaf the split modules import.

## Code Commentary

- `_TaskDocumentLifecycleMaps`
- `_iter_task_document_payloads`
- `_bounded_task_document_payloads`
- `_stat_mtime_ns`
- `_iter_task_json`
- `_read_json`
- `_as_int`
- `_as_float`
- `_text_or_none`
- `_report_label`
- `_file_age_seconds`
- `_current_phase_text`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## L23 Final Candidate Disposition

Shared enclosure snapshot construction selects the latest validated lifecycle operation and projects
bounded task-addressed phase, timing, command, report, and failure guidance. Worker, lease, and
resume identities remain private to recovery.

## Update History
- 2026-08-14T06:34+02:00 — L23 final candidate review: shared snapshot construction attaches the
  latest validated task-addressed lifecycle operation and keeps private worker/recovery identity out
  of the served projection. Verification remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
