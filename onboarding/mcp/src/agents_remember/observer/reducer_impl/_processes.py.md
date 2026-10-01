# mcp/src/agents_remember/observer/reducer_impl/_processes.py

## Governing Overview

[overview](../overview.md)

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

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.

## L23 Lineage Reduction

Reduction classifies `source-lineage-blocked` as preflight and validates either
dict or model lineage facts into the Engine Process projection. Invalid routing
is not repaired here; the reducer only carries the plane's source facts.
