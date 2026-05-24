# mcp/tests/test_code_quality_check.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_code_quality_check.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T06:30+02:00                     |
| lastVerifiedCommitHash | `98af161a6c8d77f7dfc30457c9f6ab1c20e411ab`                      |
| lastVerifiedCommitDate | 2026-05-24T06:49:48+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_code_quality_check.py` verifies the fixed source quality suite wrapper.

## Code Commentary

### Logic

The tests import `agents_remember.code_quality.check` from `mcp/src` and use a
fake command runner to avoid launching Ruff, Radon, or pytest subprocesses
during unit tests. The fake runner records command composition and writes a
synthetic coverage JSON report for the pytest step so the real
CRAP-Calculator path still executes.

### Invariants And Boundaries

- Tests verify command order and fixed module selection without shelling out.
- Fixed check failures make the wrapper return nonzero.
- Missing coverage JSON makes the CRAP step fail.
- CRAP threshold hits are report-only by default and fail only when
  `fail_on_crap_threshold` is enabled.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The source quality wrapper owns the fixed Ruff, Radon, pytest, and CRAP-Calculator sequence. | [check.py](agents-remember-md/mcp/src/agents_remember/code_quality/check.py) |
| CRAP-Calculator owns the function scoring used by the wrapper. | [crap_calculator.py](agents-remember-md/mcp/src/agents_remember/code_quality/crap_calculator.py) |

## Update History

- 2026-05-24T06:30+02:00: Created unit coverage for the source quality suite wrapper.
