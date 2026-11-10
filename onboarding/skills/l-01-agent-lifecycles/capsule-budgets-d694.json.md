# skills/l-01-agent-lifecycles/capsule-budgets-d694.json

## Governing Overview

[overview](overview.md)

## Purpose

A frozen predecessor of `capsule-budgets-current.json`: the exact measured limits, measurements and source sizes of one earlier approved size table, kept so the current record can prove what it grew from.

## Code Commentary

It uses the same `ar-role-capsule-budget-current/v1` schema as the current record. It holds 38 capsules, including the removed Designer and Strategist roles, 32 step details under the earlier flat `reference/` file names, ceilings of Architect 4,631, Manager 4,513, Curator 4,177, Reviewer and Bootstrap 4,000 and other roles 3,700, a 2,700-word step ceiling and a 1,474-word digest ceiling, with new-source budgets for the task-document reference and seven templates. Its scope says later growth returns to the Architect for the developer.

It does not describe the delivered texts and is not edited: `capsule-budgets-current.json` binds its SHA-256 in `predecessorD694Sha256`, and the predecessor-layer tests in `mcp/tests/test_role_capsule_budgets_d694.py` exercise its rejection rules on copies.

## Evidence

- Schema, decision scope and frozen hashes. [1]
- Capsule and step-detail limits, including Designer and Strategist rows and flat reference names. [2]
- Ceilings and new-source budgets. [3]
- The current record binds this file by hash. [4]
