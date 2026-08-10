# mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                                        |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
