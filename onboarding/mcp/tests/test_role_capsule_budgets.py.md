# mcp/tests/test_role_capsule_budgets.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Enforces the MIK-R101 rule 6 budget contract: every compiled capsule has exactly one recorded budget, and no capsule exceeds it. Growth, a new role and a new operation are same-change decisions recorded with the raised or added budget. The test bounds sizes; it does not check decision provenance — that is evidenced by the registry's decisions_L101 and the decision records.

## Code Commentary

`matrix_keys` yields every role/operation capsule the landed source matrix produces plus the launcher's. `compiled_size` counts fresh whitespace-split words of the compiled instruction text, seals excluded; it is the bounded quantity, not the formula input. The budget case requires registry keys to equal the matrix exactly; the exceedance case requires each stored budget to equal `ceil(size_words*11/10)` computed from the registry's stored size_words, and each fresh compiled size to fit inside it, with growth pointed at a same-change decision.

## Evidence

- Registry keys equal exactly the capsule matrix the source yields. [1]
- No fresh compiled capsule exceeds its recorded ceil(size_words*11/10) budget. [2]
