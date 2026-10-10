# skills/l-01-agent-lifecycles/capsule-budgets.json

## Governing Overview

[lifecycle overview](overview.md)

## Purpose

The decision-backed registry of all 38 role, operation and launcher capsule budgets: each budget equals ceil of its compiled instruction-word size times eleven over ten, recorded in the same change as the texts it measures.

## Code Commentary

Size is whitespace-split words of `render_instructions()`, task data and seals excluded. Growth, a new role and a new operation are each a decision recorded in the same change as the raised or added budget. The budget test fails when a capsule exceeds its budget, lacks one, or the registry names a capsule the manifest no longer yields.

## Evidence

- All 38 capsules carry ceil(raw*11/10) budgets recorded with the texts they measure. [1]

- The test bounds fresh compiled sizes by stored capsule budgets; decision recording is registry policy and is not checked by this test. [2]
