# mcp/tests/test_quality_diagnostics.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_diagnostics.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:35:26+00:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Proves that diagnostic metric findings remain visible without blocking delivery.

## Code Commentary

### Logic

Two tests inject a measured zero-percent diff result and a production CRAP score of 72. The real post-coverage reporting functions return zero while printing the findings and review threshold 20. Measurement/calculation are mocked; these cases prove result interpretation, not real Git diff parsing or actual coverage collection. They also reject a required-branch-coverage prescription.

### Conventions

These are focused unit cases under the canonical evidence-lane manifest. Reuse their behavior
boundary when changing policy rather than adding duplicate metric or collection assertions.

### Invariants And Boundaries

There is **no per-declaration default budget**: `mcp/tests/conftest.py` registers the two ini names with `addini` and carries no `default=`, and the enforced pair lives once, in the repository-root `pyproject.toml` under `[tool.pytest.ini_options]` — **2300 unit / 400 integration** when this was written; read it there, it moves. Coverage is diagnostic; production
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
| Proves that diagnostic metric findings remain visible without blocking delivery. | `test_low_coverage_is_reported_without_failing_delivery` | mcp/tests/test_quality_diagnostics.py:20-49 |
| Proves that diagnostic metric findings remain visible without blocking delivery. | `test_high_crap_requests_review_without_failing_delivery` | mcp/tests/test_quality_diagnostics.py:52-75 |

## Cross-Repo References

No cross-repository protocol is exercised by these unit cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external boundary is claimed. | N/A | N/A |

## Update History

- 2026-09-18T18:56+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **removed a budget claim from a diagnostic card that had no business carrying one.** The `### Invariants And Boundaries` sentence read "Default budgets are 1100 unit and 300 integration collected cases" — a statement about `mcp/tests/conftest.py`, on a card whose source is `test_quality_diagnostics.py`, and false twice over since `260915-KS-L23`'s item 12 removed those two declarations entirely: there are no per-declaration defaults now, and the enforced pair is **2300 / 400**, declared in the repository-root `pyproject.toml` under `[tool.pytest.ini_options]`. The sentence now states the no-default rule, where the pair actually lives, and that it moves. This card's own source is **unchanged** since its recorded verification commit (`git diff <stamp>..HEAD -- mcp/tests/test_quality_diagnostics.py` is empty and the file is clean in the working tree), so **no verification stamp is advanced or owed** — the corrected fact was never this file's.
- 2026-09-06T21:35:26+00:00 — Documented the actual d3610903 unit behavior and test-double limits without claiming an unrun verification pass.
