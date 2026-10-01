# mcp/test_support/agents_remember_test_support/testing/certifying_bootstrap.py

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Explicitly composes Dagger admission with the shared hermetic candidate process for certifying
pytest startup.

## Code Commentary

`prepare_certifying_pytest_bootstrap` requires admission first, then resolves the candidate
process, returning a typed pair. Root conftest receives this composition before it loads shared or
certifying-only plugins.

## Invariants And Boundaries

- Admission precedes candidate planning and collection.
- The diagnostic route cannot construct this result because it receives no admission capability.
- This module composes responsibilities; it does not reimplement either validator or bootstrap.

## Evidence

### Repo-Internal References

- Certifying composition orders admission before candidate process creation. [1]
