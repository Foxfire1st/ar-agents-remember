# mcp/tests/test_code_quality_check.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_code_quality_check.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-08T12:06+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                      |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_code_quality_check.py` verifies the fixed source quality suite wrapper.

## Code Commentary

### Logic

The tests import `agents_remember.code_quality.check` from `mcp/src` and use a
fake command runner to avoid launching Ruff, Pyright, Radon, or pytest subprocesses
during unit tests. The fake runner records command composition and writes a
synthetic coverage JSON report for the pytest step so the real
CRAP-Calculator path still executes. The runner now also receives the subprocess
environment, and one test asserts the wrapper puts this checkout's source import
root first on `PYTHONPATH` while preserving any pre-existing `PYTHONPATH` entry.
The command-composition test also asserts Pyright receives `--pythonpath` with
the active interpreter, which lets linked worktrees reuse the primary checkout
virtualenv without losing third-party import resolution.

### Invariants And Boundaries

- Tests verify command order and fixed module selection without shelling out,
  including that Pyright receives the configured source/test paths and active
  interpreter path.
- Fixed check failures make the wrapper return nonzero.
- Missing coverage JSON makes the CRAP step fail.
- CRAP threshold hits are report-only by default and fail only when
  `fail_on_crap_threshold` is enabled.
- The wrapper threads an environment to the runner whose `PYTHONPATH` leads with
  this checkout's source import root, so the gate measures the current checkout.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The source quality wrapper owns the fixed Ruff, Pyright, Radon, pytest, and CRAP-Calculator sequence. | [check.py](agents-remember/mcp/src/agents_remember/code_quality/check.py) |
| CRAP-Calculator owns the function scoring used by the wrapper. | [crap_calculator.py](agents-remember/mcp/src/agents_remember/code_quality/crap_calculator.py) |

## Update History

- 2026-06-08T12:06+02:00: Added coverage that the Pyright command includes
  `--pythonpath` and the active interpreter path, matching the linked-worktree
  quality gate fix. Verification metadata stays pinned until closeout.
  task/runtime-asset-canonical-sync branch.
- 2026-06-02T10:35+02:00: Added a test that the wrapper threads this checkout's source import root first onto `PYTHONPATH` (preserving any pre-existing value); the fake runners now take the `env` argument. Verification metadata stays pinned until closeout. fix/quality-gate-worktree-local branch.
- 2026-05-28T19:52+02:00: Updated after source quality wrapper tests began asserting Pyright command wiring.
- 2026-05-24T06:30+02:00: Created unit coverage for the source quality suite wrapper.
