# scripts/instruction_renewal/budgets.py

## Governing Overview

[Overview](../../overview.md)

## Purpose

Measures the current instruction corpus and checks compiled capsule token counts against `COMPILED_CAPSULE_TOKEN_CEILINGS`.

## Code Commentary

Measurements cover the capsule matrix, lifecycle sources, and applicable detail and template populations, with source identities, compiler revisions, and per-capsule `o200k_base` token counts (`_measure_with_tokens`). Current word-size deltas are reported as notices from these measurements, while siloed word-ceiling enforcement is retired. A measured source size is not an approval or an individual item ceiling. `_check_ceilings` enforces the 37-key `COMPILED_CAPSULE_TOKEN_CEILINGS` from `agents_remember.application.role_capsules.wire_budget` via `evaluate_wire_token_ceilings`, raising `AuthorityError` whenever any matrix key is missing or exceeds its token ceiling.

## Relationships

The planner receives prospective generated facts before measuring final current carriers. The current budget document (`capsule-budgets-current.json`) keeps authored decisions and historical records separate from its generated freshness measurements, while active ceiling enforcement comes from `COMPILED_CAPSULE_TOKEN_CEILINGS` in `wire_budget.py`.

## Evidence

- `_measure_with_tokens` and `plan` record current populations, word-size notices, source identities, and compiled-capsule token counts. [1]
- `_check_ceilings` validates all 37 compiled capsule measurements against `COMPILED_CAPSULE_TOKEN_CEILINGS` and raises `AuthorityError` naming the developer's decision on missing keys or over-ceiling totals. [2]
