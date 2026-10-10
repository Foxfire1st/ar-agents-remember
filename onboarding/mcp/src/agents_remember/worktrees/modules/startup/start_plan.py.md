# mcp/src/agents_remember/worktrees/modules/startup/start_plan.py

## Governing Overview

[Nearest governing route overview](../overview.md)

## Purpose

Request-local enclosure plan values, unchanged contract projections and ordinary preview/block results. It carries already validated authority and creates none.

## Code Commentary

`StartContractPlan` holds the derived leaf and the same request's owner-validated preview-only parent. The builder supplies `None` on actual apply; the wrapper is neither a durable contract nor an activation/source reservation.

`_PreparedStartEnclosure` and `_StartEnclosurePlan`, the memory/provider blocked results, `_contract_after_memory_start`, and `_preview_start_enclosure` live here without a duplicate implementation. Block results retain the same recovery actions and wire fields. No code path rewrites a contract to the removed `disabled` mode or writes a new contract in it: `_contract_after_memory_start` only reconciles the external base commit, carrying a genuine `reconciledMemoryBaseCommit` onto the existing contract projection. Preview uses the existing `ensure_worktree` dry-run and returns ordinary prepared results, preserving memory/provider plans.

Authority remains with the existing master-series constructor/admission and durable transaction owners. These local values do not authorize actual apply or another parent-series caller.

## Evidence

- No disabled projection; only the external base reconciles [6]
- Same request's validated preview-only parent [7]
- Memory blocks retain recovery action and fields [8]
- Preview uses the dry-run worktree owner [9]
