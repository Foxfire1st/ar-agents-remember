# mcp/src/agents_remember/memory/conversion/state_owners.py

## Governing Overview

[Governing overview](../overview.md)

## Purpose

Finds the old write owner and builds the conversion's attribution and durable review-fact verdict references from stored evidence. `_REPORT_MARKERS` and `_durable_verdict_ref` import `ROLE_REPORT_DIRECTORY`, `COLLECTED_REPORT_PARTS`, and `collected_report_ref` from `worktrees/role_reports.py` (downward `memory` -> `worktrees` dependency in `layers.toml`) while keeping `_report_tail`'s contract-less segment search and unchanged conversion behavior.

## Evidence

- Origin and history supply candidate ownership for a legacy revision. [1]
- The conversion attribution preserves the known owner and explains unresolved identity. [2]

- `review_fact` applies `_durable_verdict_ref` (via `role_reports.collected_report_ref`, `COLLECTED_REPORT_PARTS`, and `ROLE_REPORT_DIRECTORY`) and `_report_tail` to normalize worktree `role-reports` and absolute report paths into durable `notes/reports/<rel>` references without filesystem access, leaving empty tails, `..` traversal segments, URLs, and non-report paths unchanged. [3]
