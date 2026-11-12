# mcp/test_support/agents_remember_test_support/testing/hermetic_bootstrap.py

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

## Evidence

### Repo-Internal References

- Candidate source root is validated explicitly. [1]
- Child isolation is centralized. [2]
