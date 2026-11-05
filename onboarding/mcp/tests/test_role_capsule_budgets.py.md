# mcp/tests/test_role_capsule_budgets.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Enforces recorded budgets for every yielded capsule and declared step file, with separate absolute word ceilings. Growth, a new role and a new operation are same-change decisions recorded with the raised or added budget. The test bounds sizes; it does not check decision provenance — that is evidenced by the registry's decisions_L101 and the decision records.

## Code Commentary

**Historical source account, superseded by the current clause below:** `matrix_keys` yields every role/operation capsule the landed source matrix produces plus the launcher's. `compiled_size` counts fresh whitespace-split words of the compiled instruction text, seals excluded; it is the bounded quantity, not the formula input. The key check covers both the capsule matrix and every declared detail. The shared guard requires each stored budget to equal `min(ceil(size_words*11/10), ceiling)` from stored size_words, actual size to fit that budget, and actual size, stored size and budget all to fit the 3700 capsule or 2500 step-file ceiling. Step size is the full source text, not the compiled inline stream. [Historical source custody: `mcp/tests/test_role_capsule_budgets.py` blob `17d6acd1f48bded76920424ca5fe5b1de2e153b0` at code base `59b01fb8f72a38d2d27f9c37b8b9ca2513fd3fa0`; this is no current implementation claim.]

## Current audience, delivery and evidence contract

The mutation case patches the real measurement inputs and calls `test_no_capsule_exceeds_its_recorded_budget` itself. It supplies a good control then over-budget, live/stored-size ceiling and missing-detail failures. The guard is a size/registry check, not a meaning classifier or evidence that decision provenance was validated.

Absolute capsule ceilings are 4631 words for Architect, 4513 for Manager, 4000 for Curator/Reviewer/Bootstrap and 3700 for other roles. Step details have a 2500-word ceiling and the separately delivered every-role digest has a 1100-word ceiling. Registry completeness, capped eleven-tenths budgets and exact/over-limit mutation controls apply independently. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
- Registry keys equal the yielded capsule matrix and declared step-file set. Anchor: Current substantive owner; original historical evidence remains in the memory base [Past-epoch source caption, detached from live reference 1. Recorded citation custody: mcp/tests/test_role_capsule_budgets.py blob 48690c63a4419d730945f1c08d02e5f551ba6180 (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The budget registry test requires capsule keys to equal the manifest-derived role/operation/launcher matrix, detail keys to equal every declared detail source, and the digest entry to have exactly size_words and budget_words.


- The shared guard bounds capsule and detail words under their capped eleven-tenths budgets and absolute ceilings. Anchor: Current substantive owner; original historical evidence remains in the memory base [Past-epoch source caption, detached from live reference 2. Recorded citation custody: mcp/tests/test_role_capsule_budgets.py blob 48690c63a4419d730945f1c08d02e5f551ba6180 (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The shared budget guard rejects missing/orphan entries, any actual/stored/budget size over its supplied ceiling, a budget different from min(ceil(stored size_words*11/10),ceiling), and actual size over budget. capsule_ceiling selects Architect4631, Manager4513, Curator/Reviewer/Bootstrap4000 and3700 for other roles; the caller separately guards details2500 and the shared digest1100.

- Measures fresh render_instructions whitespace words for the role/operation/launcher matrix and complete source text for every declared detail. Exact registry keys forbid missing/orphan entries. Each stored budget is min(ceil(stored size_words*11/10), ceiling); actual size, stored size and budget must each stay within 3700 capsule/2500 detail ceilings and actual size fit budget. Seed controls invoke the same real guard with mutated inputs, not a duplicate implementation. Anchor: Current test/support source [Past-epoch source caption, detached from live reference 3. Recorded citation custody: mcp/tests/test_role_capsule_budgets.py blob 48690c63a4419d730945f1c08d02e5f551ba6180 (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The tests measure whitespace-split words from freshly rendered capsule instructions and complete declared detail sources, plus the separately delivered every-role digest. Exact registry keys reject omissions and orphans. The same capped eleven-tenths guard applies to role-specific capsule ceilings (Architect4631, Manager4513, Curator/Reviewer/Bootstrap4000, otherwise3700), details2500 and digest1100; mutation controls invoke the real guard with changed inputs at and beyond those limits.

- The budget registry test requires capsule keys to equal the manifest-derived role/operation/launcher matrix, detail keys to equal every declared detail source, and the digest entry to have exactly size_words and budget_words. [1]
- The shared budget guard rejects missing/orphan entries, any actual/stored/budget size over its supplied ceiling, a budget different from min(ceil(stored size_words*11/10),ceiling), and actual size over budget. capsule_ceiling selects Architect4631, Manager4513, Curator/Reviewer/Bootstrap4000 and3700 for other roles; the caller separately guards details2500 and the shared digest1100. [2]
- The tests measure whitespace-split words from freshly rendered capsule instructions and complete declared detail sources, plus the separately delivered every-role digest. Exact registry keys reject omissions and orphans. The same capped eleven-tenths guard applies to role-specific capsule ceilings (Architect4631, Manager4513, Curator/Reviewer/Bootstrap4000, otherwise3700), details2500 and digest1100; mutation controls invoke the real guard with changed inputs at and beyond those limits. [3]

- Absolute capsule ceilings are 4631 words for Architect, 4513 for Manager, 4000 for Curator/Reviewer/Bootstrap and 3700 for other roles. Step details have a 2500-word ceiling and the separately delivered every-role digest has a 1100-word ceiling. Registry completeness, capped eleven-tenths budgets and exact/over-limit mutation controls apply independently. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [4]
