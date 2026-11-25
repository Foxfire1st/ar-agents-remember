# mcp/tests/test_retry_selection.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused pure regression proof for the dependency-owned retry-selection pytest hook.

## Code Commentary

### Logic

The first positive case supplies two collected items and one explicit affected module, then proves
the hook retains only that item and reports the other through `pytest_deselected`. The second
passes a mock of a successful Pytest collection report for a zero-body shared-definition module and checks
that this exact observed module is valid without executing an unrelated body. The refusal case
proves empty configuration, parent-directory escape, and a genuinely uncollected module all fail
loudly.

### Conventions

- Tests invoke the hook directly with typed mocks; they do not create a second pytest route.

### Invariants And Boundaries

- A green test proves exact partition/refusal logic, not Dagger retry persistence or acceptance.
- The zero-body case supplies a passing collection-report fixture; touching a file alone is not
  evidence that Pytest collected it.
- Wrapper integration and coverage reuse require a separate witness.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository-owned unit contract.

No relevant external documentation was configured.

### Repo-Internal References

The implementation and explicit lane declaration are the load-bearing same-repository owners.

- The hook narrows executable items after canonical collection and distinguishes passing zero-body collection from an absent path. [1]
- The suite checks narrow selection, a mocked successful zero-body collection report and three refusal inputs: an empty configured list, a parent-directory path and an uncollected module. [2]

### Cross-Repo References

No meaningful cross-repository boundary is involved.

Temporary paths and mocks remain local to the test process.

### Repo-Internal References (continued)

- The `unit-regression` lane selects `mcp/tests/test_retry_selection.py`. [3]
