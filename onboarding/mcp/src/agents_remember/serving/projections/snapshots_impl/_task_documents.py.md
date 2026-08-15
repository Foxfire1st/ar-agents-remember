# mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `28a66feae742bf02fe4b647388b220f921cc7007`                                        |
| lastVerifiedCommitDate | 2026-08-15T03:44:49+02:00|
| governingOverview      | `../overview.md`                                       |

## Governing Overview

[serving projections overview](../overview.md)

## Purpose

Task-document and series readers: summaries, full bodies, lifecycle binding. Task JSON is the source of truth (never the rendered markdown). These readers project task documents and the series checklist, resolve cross-folder lifecycle links, and hash full bodies for the on-demand body endpoint.

## Code Commentary

- `read_task_documents`
- `read_task_document_body`
- `_task_document_lifecycle_maps`
- `_task_doc_lifecycle_id`
- `_doc_enclosure_lifecycle`
- `read_series_documents`
- `_series_subtask_nodes`
- `_series_subtask_created_at`
- `_ref_lifecycle`
- `_task_step_nodes`
- `_task_doc_node`
- `_task_doc_body_revision`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: task snapshot hydration now carries explicit master
  nature and sprint graph, derives deterministic waves, and includes both fields in body revision identity.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
