# mcp/src/agents_remember/code_quality/crap_calculator.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/code_quality/crap_calculator.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T06:05+02:00                     |
| lastVerifiedCommitHash | `98af161a6c8d77f7dfc30457c9f6ab1c20e411ab`                      |
| lastVerifiedCommitDate | 2026-05-24T06:49:48+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`crap_calculator.py` implements CRAP-Calculator, a development helper that
combines Radon cyclomatic complexity with Coverage.py JSON line data to report
function-level CRAP scores.

## Code Commentary

### Logic

The helper reads coverage JSON, indexes coverage by normalized file path, walks
the requested Python files, asks Radon for function and method complexity
blocks, intersects each block's line span with executable coverage lines, and
computes:

```text
CRAP = complexity^2 * (1 - coverage_ratio)^3 + complexity
```

The default table output shows the highest function scores plus a per-file
rollup. JSON output preserves function fields for downstream tooling. Missing
coverage data is treated as zero function coverage so unmeasured complex code
stays visible as risk.

### Invariants And Boundaries

- CRAP-Calculator consumes coverage data; it does not run pytest or coverage
  itself.
- Scores are function/method level. File rollups are summaries over function
  scores, not replacements for the function-level risk list.
- Radon and coverage are development dependencies; this helper should not be
  imported by MCP runtime paths.
- The user-facing helper name is `CRAP-Calculator`; the Python module remains
  import-safe as `crap_calculator`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Unit tests cover the CRAP formula, function-span coverage intersection, and missing coverage data behavior. | [test_crap_calculator.py](agents-remember-md/mcp/tests/test_crap_calculator.py) |
| The source quality suite wrapper runs CRAP-Calculator from pytest coverage JSON. | [check.py](agents-remember-md/mcp/src/agents_remember/code_quality/check.py) |
| Development tool guidance documents the source quality wrapper and CRAP-Calculator command flow. | [system/tools.md](agents-remember-md/system/tools.md) |

## Update History

- 2026-05-24T06:30+02:00: Updated after the source quality wrapper started running CRAP-Calculator as part of the remembered suite.
- 2026-05-24T06:05+02:00: Created CRAP-Calculator for function-level complexity plus coverage risk reporting.
