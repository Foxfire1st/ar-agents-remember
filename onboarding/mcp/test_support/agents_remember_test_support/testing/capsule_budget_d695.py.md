# mcp/test_support/agents_remember_test_support/testing/capsule_budget_d695.py

## Governing Overview

[overview](overview.md)

## Purpose

The module checks capsule word budgets against the current record `skills/l-01-agent-lifecycles/capsule-budgets-current.json`. It is imported by `mcp/tests/test_role_capsule_budgets.py`, `mcp/tests/test_role_capsule_budgets_d694.py`, `mcp/tests/test_knowledge_bootstrap_procedure.py` and `instruction_consistency.py`.

## Code Commentary

The loader, the current view and `current_budget_findings` each assert the record's canonical JSON fingerprint, which is a hash of the record itself, so any edit to the budget record renews it in the same change; `current_capsule_ceiling` is re-exported from `capsule_budget_d694.py`. The population check requires the declared step-detail list to be unique and equal to the measured and limited details, the linked ordinary templates to be exactly the four fixed file, entity-catalog, repo-overview and route-overview templates, the two populations to be disjoint, ordinary templates to carry measurements but no word limit, and the step-detail ceiling to be 2500.

Source findings classify details and templates from `composition-manifest.json` (`step_detail` true or false), report stale ordinary-template sizes without capping them, and reuse the area and source predicates of `capsule_budget_d694.py`. `current_budget_findings` also asserts the SHA-256 of the frozen registry, `capsule_budget_snapshot.py`, the d694 record, `capsule_budget_d694.py` and `core/digest-map.json` against the record, and that the digest map's `maximumWords` equals the record's digest ceiling.

## Evidence

- The linked ordinary template population is fixed. [1]
- Populations, uncapped ordinary templates and the 2500-word detail ceiling are asserted. [2]
- Detail and template classification is read from the composition manifest. [3]
- Frozen owners and the current digest map are bound by hash before findings are collected. [4]
