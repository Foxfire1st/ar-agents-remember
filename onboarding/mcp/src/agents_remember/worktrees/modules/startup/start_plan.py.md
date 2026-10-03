# mcp/src/agents_remember/worktrees/modules/startup/start_plan.py

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

Request-local enclosure plan values, unchanged contract projections and ordinary preview/block results. It carries already validated authority and creates none.

## Code Commentary

`StartContractPlan` holds the derived leaf and the same request's owner-validated preview-only parent. The builder supplies `None` on actual apply; the wrapper is neither a durable contract nor activation/source reservation.

`_PreparedStartEnclosure` and `_StartEnclosurePlan`, memory/provider blocked results, `_contract_after_memory_start` and `_preview_start_enclosure` moved from start.py without a duplicate implementation. Block results retain the same recovery actions and wire fields. Disabled memory is projected through `ContractCells(memory_mode="disabled")`; otherwise a genuine reconciled memory-base result updates the existing contract projection. Preview uses the existing ensure_worktree dry-run and returns ordinary prepared results, preserving memory/provider plans.

Authority remains with the existing master-series constructor/admission and durable transaction owners. These local values do not authorize actual apply or another parent-series caller. Startup-state no-materialization is scoped independently of the known generic ambient completion event.

## Evidence

No Domain Documentation source is configured in system/sources.md. These are current source/assertion anchors; the approved requirement and bound public receipts remain task artifacts.


- One internal value carries the same request's validated preview-only parent. [1]
- Moved memory-mode/base projection preserves its typed contract semantics. [2]
- Preview uses the existing dry-run worktree owner and ordinary result shape. [3]
- Memory blocks retain their existing recovery action/fields. [4]
- Provider blocks retain their existing recovery action/fields. [5]
