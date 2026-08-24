# mcp/src/agents_remember/testing/hermetic_bootstrap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/hermetic_bootstrap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Creates the candidate-bound, Git-scrubbed, cache-isolated pytest process shared by diagnostic and
certifying routes.

## Code Commentary

`candidate_test_process` resolves the candidate and source root. `hermetic_pytest_environment`
reuses the kernel's native subprocess environment, removes repository selectors, pins
`PYTHONPATH`, applies disposable Git identity, and owns POSIX temp/cache roots.
`activate_current_pytest_environment` applies the same contract reversibly for root conftest.

## Invariants And Boundaries

- Both routes import the selected candidate, never an ambient editable install.
- Ambient Git selectors and developer identity do not reach tests.
- Cache/temp roots must be outside the candidate tree.
- Environment leases are idempotently reversible on every exit path.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate source root is validated explicitly. | `candidate_test_process` | mcp/src/agents_remember/testing/hermetic_bootstrap.py:50-59 |
| Child isolation is centralized. | `hermetic_pytest_environment` | mcp/src/agents_remember/testing/hermetic_bootstrap.py:62-84 |

## Update History

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
