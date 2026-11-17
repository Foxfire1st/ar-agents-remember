# mcp/test_support/agents_remember_test_support/testing/capsule_budget_d695.py

## Governing Overview

[overview](overview.md)

## Purpose

The module checks capsule word budgets against the current record `skills/l-01-agent-lifecycles/capsule-budgets-current.json`. It is imported by `mcp/tests/test_role_capsule_budgets.py`, `mcp/tests/test_role_capsule_budgets_d694.py`, `mcp/tests/test_knowledge_bootstrap_procedure.py` and `instruction_consistency.py`.

## Code Commentary

The loader reads the JSON record without authenticating a whole-current-record fingerprint. Measurements and their detail/template populations, source-size inventory and compiler-input revisions are read from `record["derived"]`; `current_measurements` holds capsule, step-detail, digest and ordinary-template measurements. The current view exposes measured membership without individual word budgets, and `current_capsule_ceiling` is re-exported from `capsule_budget_d694.py`. Population checks require unique declared details, matching detail measurements, disjoint ordinary-template membership and matching ordinary-template measurements. [5]

Source findings classify details and ordinary templates from the composed manifest, detect missing or stale measurements and source identities, and leave ordinary templates uncapped. Renewable population, measurement, source-identity and compiler-input findings end with `run mcp/.venv/bin/python scripts/renew-instructions.py`, using the shared renewal command. Current area findings compare fresh sizes with measurements and the authored capsule, detail and digest ceilings; an over-ceiling finding instead says that raising a ceiling is the developer's decision. [5] `_assert_history` authenticates the retained registry, snapshot helper, predecessor record and predecessor helper; it does not authenticate the current digest map or require equality with the map's word maximum.

## Evidence

- The ordinary-template population matches the composed manifest classification. [1]

- Detail and template populations are checked separately, and ordinary templates have measurements without a detail ceiling. [2]

- Detail and template classification is read from the composed manifest. [3]

- The retained registry, snapshot helper, predecessor record and predecessor helper are authenticated as frozen history. [4]

### Repo-Internal References (renewed)

- Current measurements and inventories live under record["derived"]. Renewable population, measurement and source findings name the shared renewal command; exceeding an authored ceiling instead names the developer's decision to raise it. [5]
