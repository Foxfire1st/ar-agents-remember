# mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`                                        |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[serving projections overview](overview.md)

## Purpose

Runtime process-surface readers: enclosures, gates, inbox, expectations, engine facts. These readers describe the live worktree population -- enclosure contracts, gate state, agent inbox pickups, expectation rows, and the enriched engine process facts the Engine Room map renders. The git-backed ledger enrichment is imported from the analytical readers, which own the ledger window.

## Code Commentary

L23 attaches the latest task-bound lifecycle-operation projection while building an enclosure snapshot, keeping dashboard status derived from durable operation state.

- `read_enclosures`
- `_enclosure_from_contract`
- `read_gates`
- `read_agent_pickups`
- `read_expectation_rows`
- `read_engine_process_facts`
- `refresh_engine_process_landing`
- `_safe_status_payload`
- `_cached_local_status`

`read_agent_pickups` projects entry, subject, and owner task-document references from inbox rows.
`read_expectation_rows` projects the expectation's `taskDocumentRef`; neither reader reconstructs
or publishes a leaf-key ownership field.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Updated runtime inbox and expectation projections to preserve canonical
  entry/subject/owner task-document identity end to end.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
