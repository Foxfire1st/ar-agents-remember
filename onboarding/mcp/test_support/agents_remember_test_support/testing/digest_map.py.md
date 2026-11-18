# mcp/test_support/agents_remember_test_support/testing/digest_map.py

## Governing Overview

[Overview](overview.md)

## Purpose

Provides digest-map assertion helpers over the composed authored and generated map.

## Code Commentary

The helpers check source ranges, hashes, ordering and coverage, digest places and clauses, evidence associations and audience unions. Retired unit bindings retain their historical checks. Clause coverage calls `scripts/instruction_renewal/digest.py::clause_coverage_error`, a repository renewal-tooling helper, so that facet shares implementation rather than supplying an independent second algorithm.

## Relationships

Instruction map tests load the joined view through this support. The authored map owns semantic units and audiences; the renewal planner owns generated current bindings.

## Evidence


- Evidence, retirement and audience checks remain separately expressed. [2]

### Repo-Internal References (renewed)

- Assertions cover source bindings and digest places; clause coverage calls the repository renewal helper clause_coverage_error. [1]
