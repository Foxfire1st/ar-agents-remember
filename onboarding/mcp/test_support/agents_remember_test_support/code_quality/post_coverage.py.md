# mcp/test_support/agents_remember_test_support/code_quality/post_coverage.py

## Governing Overview

[Quality support overview](overview.md)

## Purpose

`post_coverage.py` owns the two fast, in-process rails that can run only after pytest has emitted
branch coverage: function-level CRAP scoring and the changed-lines/branches diagnostic report. The
split keeps the command/orchestration module below the file-size soft limit without changing the
public `check.run_crap_calculator`, `check.crap_failure_line`, or `check.run_diff_coverage` aliases.

## Code Commentary

### Logic

`run_crap_calculator` refuses missing, vacuous, or invalid coverage and renders production scores.
Functions at or above the review threshold remain visible while returning success, with simpler
code, a meaningful behavioral test, or concise justified acceptance as possible responses.
`run_diff_coverage` prints the comparison base and measured statement/arc findings without a
percentage failure. Targeted runs with no production modules are explicitly not applicable.

### Invariants And Boundaries

- Both functions consume existing coverage JSON without rerunning tests.
- Metric values are diagnostic; missing or invalid evidence still fails.
- No coverage-floor configuration or coverage-clearing prescription remains.
- The read-only `CoverageRailConfig` is satisfied by the immutable wrapper configuration.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository-local quality policy.

No external domain contract governs these post-pytest calculations.

### Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.

- Report integrity failures versus diagnostic high scores [1]
- Locate findings without required coverage percentages [2]
- Diagnostic measured coverage and explicit nonmeasured states [3]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this module.

Both rails read only the current repository and the wrapper-produced artifact.
