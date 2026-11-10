# mcp/test_support/agents_remember_test_support/testing/capsule_budget_snapshot.py

## Governing Overview

[overview](overview.md)

## Purpose

The module freezes the measured sizes, approved limits, history and decision fingerprints, and one later per-detail budget decision of the historical capsule-budget registry `skills/l-01-agent-lifecycles/capsule-budgets.json`. `mcp/tests/test_role_capsule_budgets.py` and `mcp/tests/test_role_capsule_budgets_d694.py` read it.

## Code Commentary

Measurements stay separate from limits: a measured size may exceed its limit, and the budget test must then report the overage. The registry test fingerprints the registry's decision and history sections against these constants and compares the exact single-detail decision.

The file is itself frozen: `capsule_budget_d694.py` and `capsule_budget_d695.py` assert its SHA-256 equals the `historicalSnapshotSha256` named in their records, so any edit fails those checks.

## Evidence

- Measured sizes are kept apart from approved limits. [1]
- The history and decision fingerprints are fixed constants. [2]
- One later decision raises a single step-detail budget. [3]
- The current checker binds this file by its SHA-256. [4]
