# mcp/tests/test_role_capsule_budgets.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Enforces recorded budgets for every yielded capsule and declared step file, with separate absolute word ceilings. Growth, a new role and a new operation are same-change decisions recorded with the raised or added budget. The test bounds sizes; it does not check decision provenance — that is evidenced by the registry's decisions_L101 and the decision records.

## Code Commentary

`matrix_keys` yields every role/operation capsule the landed source matrix produces plus the launcher's. `compiled_size` counts fresh whitespace-split words of the compiled instruction text, seals excluded; it is the bounded quantity, not the formula input. The key check covers both the capsule matrix and every declared detail. The shared guard requires each stored budget to equal `min(ceil(size_words*11/10), ceiling)` from stored size_words, actual size to fit that budget, and actual size, stored size and budget all to fit the 3700 capsule or 2500 step-file ceiling. Step size is the full source text, not the compiled inline stream.

## Current audience, delivery and evidence contract

The mutation case patches the real measurement inputs and calls `test_no_capsule_exceeds_its_recorded_budget` itself. It supplies a good control then over-budget, live/stored-size ceiling and missing-detail failures. The guard is a size/registry check, not a meaning classifier or evidence that decision provenance was validated.

## Evidence


- Registry keys equal the yielded capsule matrix and declared step-file set. [1]


- The shared guard bounds capsule and detail words under their capped eleven-tenths budgets and absolute ceilings. [2]

- Measures fresh render_instructions whitespace words for the role/operation/launcher matrix and complete source text for every declared detail. Exact registry keys forbid missing/orphan entries. Each stored budget is min(ceil(stored size_words*11/10), ceiling); actual size, stored size and budget must each stay within 3700 capsule/2500 detail ceilings and actual size fit budget. Seed controls invoke the same real guard with mutated inputs, not a duplicate implementation. [3]
