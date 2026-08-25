# mcp/src/agents_remember/testing/unsafe_effects.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/unsafe_effects.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Maps every closed unsafe effect family to its stable direct-lane refusal explanation.

## Code Commentary

### Logic

`UNSAFE_EFFECT_RULES` contains exactly one human-actionable reason for each
`UnsafeEffectFamily`. `unsafe_family_reason` renders the canonical message and refuses an invalid
registry rather than inventing a generic answer.

### Conventions

Concrete audited effects live in the cohort manifest. This module owns vocabulary and guidance, not
repository-wide import/call inference.

### Invariants And Boundaries

- Every enum member has exactly one rule and no duplicate family exists.
- Unknown effects refuse in eligibility; they are never treated as safe because absent here.
- Adding a family requires manifest, classifier, and forcing-proof updates.

### Todos

None.

## Docs References

No external documentation owns the unsafe-family taxonomy.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One reason exists for each of the eight protected effect families. | `UNSAFE_EFFECT_RULES` | mcp/src/agents_remember/testing/unsafe_effects.py:11-57 |
| Manifest files declare their reviewed effect families. | "effects = []" | mcp/tests/python-direct-cohort.toml:24-29 |

## Cross-Repo References

No cross-repository policy is imported.

## Update History

- 2026-08-25T01:56+02:00 — Narrowed this owner to the closed family/reason registry after removing
  speculative whole-repository analysis.
- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
