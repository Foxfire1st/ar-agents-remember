# mcp/src/agents_remember/observer/reducer_impl/_processes.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/reducer_impl/_processes.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`                                        |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[overview](../../overview.md)

## Purpose

Engine Room process map: one node per worktree contract (slice 5e). Composed, not read: contract + status guidance join the worktree's provider stack and setup-progress boot sequence into the process node vocabulary. Pure and deterministic so the served projection and sim replay stay byte-identical.

## Code Commentary

- `_is_disposed`
- `build_engine_processes`
- `_start_process_node`
- `_engine_process`
- `_CodeRefs`
- `_MemoryRefs`
- `_code_refs`
- `_memory_refs`
- `_SetupFacts`
- `_setup_facts`
- `_provider_boot_nodes`
- `_expected_provider_roles`
- `_engine_runtime_state`
- `_ref_fact_state`
- `_process_phase`
- `_process_health`
- `_ProcessLanes`
- `_process_edges`
- `_materialize_edge_state`
- `_seed_edge_state`
- `_missing_facts`
- `_source_files`
- `_as_dict`
- `_str_or_none`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/reducer_impl/_processes.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## L23 Lineage Reduction

Reduction classifies `source-lineage-blocked` as preflight and validates either
dict or model lineage facts into the Engine Process projection. Invalid routing
is not repaired here; the reducer only carries the plane's source facts.

## Update History
- 2026-08-12T20:10+02:00 — L23 curator: documented strict lineage reduction and preflight phase mapping; verification remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
