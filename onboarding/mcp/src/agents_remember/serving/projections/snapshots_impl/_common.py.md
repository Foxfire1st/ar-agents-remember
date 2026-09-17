# mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `997305a9ced4caea67edb826224bf0351264fd56`                                        |
| lastVerifiedCommitDate | 2026-09-17T19:54:27+02:00|
| governingOverview      | `../overview.md`                                          |

## Governing Overview

[serving projections overview](../overview.md)

## Purpose

Shared file-surface helpers for the observer snapshot readers. The readers split by responsibility (providers, runtime enclosures, analytical surfaces, task documents) share the task-document payload cache, the status payload TTL cache, and the small JSON/stat helpers collected here. No reader logic lives in this module; it is the common leaf the split modules import.

## Code Commentary

- `_TaskDocumentLifecycleMaps`
- `_iter_task_document_payloads`
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
