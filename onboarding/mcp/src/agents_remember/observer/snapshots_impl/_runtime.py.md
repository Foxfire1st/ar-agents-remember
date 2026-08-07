# mcp/src/agents_remember/observer/snapshots_impl/_runtime.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/snapshots_impl/_runtime.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                        |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[overview](../../overview.md)

## Purpose

Runtime process-surface readers: enclosures, gates, inbox, expectations, engine facts. These readers describe the live worktree population -- enclosure contracts, gate state, agent inbox pickups, expectation rows, and the enriched engine process facts the Engine Room map renders. The git-backed ledger enrichment is imported from the analytical readers, which own the ledger window.

## Code Commentary

- `read_enclosures`
- `_enclosure_from_contract`
- `read_gates`
- `read_agent_pickups`
- `read_expectation_rows`
- `read_engine_process_facts`
- `refresh_engine_process_landing`
- `_safe_status_payload`
- `_cached_local_status`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/snapshots_impl/_runtime.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
