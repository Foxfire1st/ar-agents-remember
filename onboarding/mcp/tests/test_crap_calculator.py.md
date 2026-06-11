# mcp/tests/test_crap_calculator.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_crap_calculator.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T06:05+02:00                     |
| lastVerifiedCommitHash | `98af161a6c8d77f7dfc30457c9f6ab1c20e411ab`                      |
| lastVerifiedCommitDate | 2026-05-24T06:49:48+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_crap_calculator.py` verifies the source-development CRAP-Calculator
helper.

## Code Commentary

### Logic

The tests import `agents_remember.code_quality.crap_calculator` from `mcp/src`.
They verify the CRAP formula with coverage ratios, build a synthetic Python file
and Coverage.py JSON report to prove function-level Radon complexity can be
joined with coverage line spans, assert missing coverage files are treated as
zero coverage, and exercise file rollups plus table/JSON CLI rendering.

### Invariants And Boundaries

- These tests do not run pytest-cov; they feed synthetic coverage JSON directly
  into the calculator.
- The fixture stays temporary and does not require repository-wide coverage
  data.
- The tests protect function-level scoring first. File rollups and report
  rendering are covered as derived behavior so the helper can be used directly
  during refactor scouting.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CRAP-Calculator owns the formula, coverage matching, Radon integration, table output, and JSON output. | [crap_calculator.py](agents-remember/mcp/src/agents_remember/code_quality/crap_calculator.py) |

## Update History

- 2026-05-24T06:12+02:00: Updated after tests added rollup and CLI rendering coverage.
- 2026-05-24T06:05+02:00: Created unit coverage for CRAP-Calculator.
