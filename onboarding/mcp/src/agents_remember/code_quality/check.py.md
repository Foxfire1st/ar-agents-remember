# mcp/src/agents_remember/code_quality/check.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/code_quality/check.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c`                      |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`check.py` provides the remembered source quality suite entrypoint for
Agents Remember development.

## Code Commentary

### Logic

The module runs a fixed sequence of development checks from the source checkout:
`ruff check`, Pyright with the root project config, Radon cyclomatic
complexity, Radon maintainability index, pytest with coverage JSON, and
CRAP-Calculator over the generated coverage report.

The default CLI is:

```text
python -m agents_remember.code_quality.check
```

CRAP scores are visible every run, but the CRAP threshold is report-only by
default because the current repository already has known high-score legacy
functions. Passing `--fail-on-crap-threshold` turns that report into a hard
gate.

### Invariants And Boundaries

- The wrapper is a fixed quality suite, not a generic shell command surface.
- Subprocess commands use the active Python executable and fixed module names.
- Pyright uses `--project .` and the same configured source/test paths as the
  other source quality commands.
- pytest coverage JSON is generated into a temporary file unless the caller
  explicitly supplies `--coverage-json`.
- CRAP-Calculator runs in-process from the generated coverage JSON.
- Existing high CRAP pressure is report-only unless the caller opts into the
  threshold gate.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CRAP-Calculator owns function-level CRAP scoring and rendering. | [crap_calculator.py](agents-remember-md/mcp/src/agents_remember/code_quality/crap_calculator.py) |
| Unit tests cover fixed command composition including Pyright, failure propagation, missing coverage JSON, and optional CRAP threshold gating. | [test_code_quality_check.py](agents-remember-md/mcp/tests/test_code_quality_check.py) |
| Repo tool guidance points agents to this wrapper for full local source quality checks. | [system/tools.md](agents-remember-md/system/tools.md) |

## Update History

- 2026-05-28T19:52+02:00: Updated after Pyright joined the fixed source quality wrapper.
- 2026-05-24T06:30+02:00: Created the source quality suite wrapper that runs Ruff, Radon, pytest coverage, and CRAP-Calculator.
