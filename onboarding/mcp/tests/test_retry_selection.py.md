# mcp/tests/test_retry_selection.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused pure regression proof for the dependency-owned retry-selection pytest hook.

## Code Commentary

### Logic

The first positive case supplies two collected items and one explicit affected module, then proves
the hook retains only that item and reports the other through `pytest_deselected`. The second
records a passing Pytest collection report for a zero-body shared-definition module and proves
that this exact observed module is valid without executing an unrelated body. The refusal case
proves empty configuration, parent-directory escape, and a genuinely uncollected module all fail
loudly.

### Conventions

- Tests invoke the hook directly with typed mocks; they do not create a second pytest route.
- The file is explicitly classified as `unit-regression` in the lane manifest.

### Invariants And Boundaries

- A green test proves exact partition/refusal logic, not Dagger retry persistence or acceptance.
- The zero-body case must supply Pytest's passing collection report; touching a file alone is not
  evidence that Pytest collected it.
- The real retry matrix remains the forcing proof for wrapper integration and coverage reuse.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository-owned unit contract.

No relevant external documentation was configured.

### Repo-Internal References

The implementation and explicit lane declaration are the load-bearing same-repository owners.

- The hook narrows executable items after canonical collection and distinguishes passing zero-body collection from an absent path. [1]
- The suite covers narrow selection, zero-body collection, and all configured-path refusal shapes. [2]
- The suite has explicit unit-regression membership. [3]

### Cross-Repo References

No meaningful cross-repository boundary is involved.

Temporary paths and mocks remain local to the test process.
