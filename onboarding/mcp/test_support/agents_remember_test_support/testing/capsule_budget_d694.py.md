# mcp/test_support/agents_remember_test_support/testing/capsule_budget_d694.py

## Governing Overview

[overview](overview.md)

## Purpose

The module checks capsule word budgets against the frozen record `skills/l-01-agent-lifecycles/capsule-budgets-d694.json`, separate from the older registry and its snapshot. `mcp/tests/test_role_capsule_budgets.py` and `mcp/tests/test_role_capsule_budgets_d694.py` use it, and `capsule_budget_d695.py` reuses its area and source predicates.

## Code Commentary

The loader, the current view and `current_budget_findings` each first assert that the record's canonical JSON fingerprint equals the fixed value, so a changed record fails rather than being measured. `current_budget_findings` asserts the record's detail and linked-template populations, and that `capsule-budgets.json` and `capsule_budget_snapshot.py` match the SHA-256 values named in the record. It then returns findings for missing or stale budgets, sizes that differ from the recorded measurement, sizes above a limit, limits or sizes above the role or area ceiling, and approved sources whose identity, word count or compiler-input revision changed. A role's capsule ceiling is its own entry or `every_other_role`.

The module computes findings only; the tests decide what a finding means.

## Evidence

- The record must match a fixed canonical fingerprint. [1]
- Area findings cover missing, stale, over-limit and over-ceiling entries. [2]
- Approved sources are checked for identity, word count and compiler-input revision. [3]
- The full check asserts populations and the frozen registry and snapshot hashes before collecting findings. [4]
