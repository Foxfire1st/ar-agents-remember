# mcp/tests/test_quality_evidence_helper_invariants.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_evidence_helper_invariants.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T16:54+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Proves quality evidence identity and selector helpers.

## Code Commentary

### Logic

The cases cover candidate tree, attempt nonce, environment identity, causal report ordering, exact
selection metadata, formatter-safe controlled retry-evidence mutations, and the low-fan-out
product-scenario owner invariant. The mutation proof
extracts and executes only `_append_comment` from its AST, avoiding an import of the scenario CLI;
that keeps the test from falsely acquiring ownership of every fixture path in the CLI catalog.
The candidate-identity example pins the project runtime as CPython `3.13.15`, so the invariant
demonstrates that runtime provenance participates in the environment identity carried by quality
evidence instead of preserving the superseded Python 3.12 example.

### Conventions

Tests execute production owners and use shared builders only for canonical setup. Scenario-specific
differences remain in the test so fixtures do not become a parallel implementation.

### Invariants And Boundaries

- The suite preserves loud negative cases and exact identity/refusal assertions; it does not obtain
  green through a fallback, allowlist, or weakened production threshold.
- Dagger owns certifying execution. Any direct execution remains bounded diagnostic evidence only.
- Helper extraction must remain dependency-neutral: importing the whole retry scenario module here
  would make lifecycle consumer discovery correctly add every scenario fixture to this test.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required for this repository-owned test contract. | `_value` | mcp/tests/test_quality_evidence_helper_invariants.py:1-117 |

## Repo-Internal References

The test file is direct evidence for the production boundary named above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The selected scenarios and assertions implement this test unit's forcing proof. | `_value` | mcp/tests/test_quality_evidence_helper_invariants.py:1-117 |
| The actual comment mutator executes in isolation and preserves Ruff-valid module spacing. | `test_retry_route_python_comment_mutation_is_formatter_safe` | mcp/tests/test_quality_evidence_helper_invariants.py:65-96 |
| The product matrix scenario cannot drift back to a central high-fan-out owner. | `test_retry_product_scenario_uses_the_seed_low_fan_out_owner` | mcp/tests/test_quality_evidence_helper_invariants.py:99-124 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_value` | mcp/tests/test_quality_evidence_helper_invariants.py:1-117 |

## Update History

- 2026-08-29T16:54+02:00 — Updated the candidate-identity forcing example to the canonical
  project-owned CPython 3.13.15 runtime and documented its environment-evidence role.
- 2026-08-27T20:45+02:00 — Added an AST-only invariant binding the product retry scenario to the
  designated low-fan-out seed owner without importing the scenario catalog.
- 2026-08-27T20:16+02:00 — Added dependency-neutral execution of the real retry comment helper
  after importing its scenario catalog created false fixture-consumer ownership.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
