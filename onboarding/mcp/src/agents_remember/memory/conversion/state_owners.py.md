# mcp/src/agents_remember/memory/conversion/state_owners.py

## Governing Overview

[Governing overview](../overview.md)

## Purpose

Finds the old write owner and builds the conversion's attribution and durable review-fact verdict references from stored evidence.

## Evidence

- Origin and history supply candidate ownership for a legacy revision. [1]
- The conversion attribution preserves the known owner and explains unresolved identity. [2]

- `review_fact` applies `_durable_verdict_ref` and `_report_tail` to normalize worktree `role-reports` and absolute report paths into durable `notes/reports/<rel>` references without filesystem access, leaving empty tails, `..` traversal segments, URLs, and non-report paths unchanged. [3]
