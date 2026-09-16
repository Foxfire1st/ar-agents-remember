# mcp/tests/test_suite_budget.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_suite_budget.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:35:26+00:00 |
| lastVerifiedCommitHash | `9c8a7a42a3d761b13c462874c7b312313a11c0ae`|
| lastVerifiedCommitDate | 2026-09-13T19:56:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Proves selected-case budget admission without recursive pytest collection.

## Code Commentary

### Logic

Three parametrized cases feed the actual collection-finish hook a synthetic selected item population: 1000 unit/250 integration passes; 1001 unit or 251 integration raises UsageError requiring an explicit tradeoff. The marker-shaped item double classifies each already-collected item. This is boundary arithmetic and refusal evidence, not a second inventory scan or a real nested pytest session.

### Conventions

These are focused unit cases under the canonical evidence-lane manifest. Reuse their behavior
boundary when changing policy rather than adding duplicate metric or collection assertions.

### Invariants And Boundaries

Default budgets are 1000 unit and 250 integration collected cases (`260831-LOCR-L37` raised the integration ceiling 200 -> 250 on explicit developer authorization; this module pins the same numbers `pyproject.toml` declares, so the two can never drift silently). Coverage is diagnostic; production
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
| Proves selected-case budget admission without recursive pytest collection. | `test_selected_case_budgets` | mcp/tests/test_suite_budget.py:19-35 |

## Cross-Repo References

No cross-repository protocol is exercised by these unit cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external boundary is claimed. | N/A | N/A |

## Update History

- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 curator: recorded this leaf's case-budget change —
  `integration_case_budget` 200 -> 250 and therefore the third parametrization's refusal boundary
  201 -> 251, developer-authorized so dropped coverage could be written back. `pyproject.toml` owns
  the tradeoff statement; this module is the pin that the declared numbers are the enforced ones.
  Verification metadata remains closeout-owned; no acceptance claim.

- 2026-09-12T00:52:39+02:00 — 260831-LOCR-L29 curator: recorded this leaf's case-budget change — `integration_case_budget` 150 → 200 with the measured tradeoff in `pyproject.toml` (integration 150 cases + 31 subtests in 31.8 s; unit 795 + 145 in 56.0 s). The budget file is the only place that numeric contract lives, so the card's prose is unchanged and the citation was repointed to the current extent. Verification metadata remains closeout-owned.

- 2026-09-06T21:35:26+00:00 — Documented the actual d3610903 unit behavior and test-double limits without claiming an unrun verification pass.
