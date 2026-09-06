# mcp/tests/test_suite_budget.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_suite_budget.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:35:26+00:00 |
| lastVerifiedCommitHash | |
| lastVerifiedCommitDate | |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Proves selected-case budget admission without recursive pytest collection.

## Code Commentary

### Logic

Three parametrized cases feed the actual collection-finish hook a synthetic selected item population:1000 unit/150 integration passes;1001 unit or 151 integration raises UsageError requiring an explicit tradeoff. The marker-shaped item double classifies each already-collected item. This is boundary arithmetic and refusal evidence, not a second inventory scan or a real nested pytest session.

### Conventions

These are focused unit cases under the canonical evidence-lane manifest. Reuse their behavior
boundary when changing policy rather than adding duplicate metric or collection assertions.

### Invariants And Boundaries

Default budgets are 1000 unit and150 integration collected cases. Coverage is diagnostic; production
CRAP 20 triggers review without failing delivery. Full suites and whole-candidate review occur at
master completion. A green unit result is not a certification certificate.

### Todos

Verification metadata remains closeout-owned; this card records source inspection only.

## Docs References

No Domain Documentation source is configured; this behavior is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is needed. | N/A | N/A |

## Repo-Internal References

The exact functions below establish the tested boundary and its test doubles.

| Finding | Anchor | Source |
| --- | --- | --- |
| Proves selected-case budget admission without recursive pytest collection. | `test_selected_case_budgets` | mcp/tests/test_suite_budget.py:23-35 |

## Cross-Repo References

No cross-repository protocol is exercised by these unit cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external boundary is claimed. | N/A | N/A |

## Update History

- 2026-09-06T21:35:26+00:00 — Documented the actual d3610903 unit behavior and test-double limits without claiming an unrun verification pass.
