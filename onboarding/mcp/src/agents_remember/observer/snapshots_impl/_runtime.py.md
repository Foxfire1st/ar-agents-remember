# mcp/src/agents_remember/observer/snapshots_impl/_runtime.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/snapshots_impl/_runtime.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `2dea095cd68454a7a68893e37c07dbd8daa86d32`                                        |
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
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

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the owner-visible deadline
## 260713-TES-L5 Current Delta — Owner-Visible Deadline Surface

`read_expectation_rows` is surfacing only: the relay never evaluates expectation rows, and
verification is by expected product (owner work). `read_agent_pickups`' strict-read rationale
now names landing (not ack) as what a torn row blocks, matching the N16 vocabulary.

## Update History

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the owner-visible deadline
  surface — `read_expectation_rows` no longer claims an L2 predicate reads the store
  directly; the relay never evaluates expectation rows and verification is by expected
  product (owner work). The strict-read rationale in `read_agent_pickups` now names landing
  instead of ack as what a torn row blocks. Verification metadata pinned until closeout
  stamps the 260713-TES-L5 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
