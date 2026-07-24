# mcp/src/agents_remember/code_quality/check.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/code_quality/check.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-24T14:31Z                     |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`                      |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

`check.py` provides the remembered source quality suite entrypoint for
Agents Remember development.

## Code Commentary

### Logic

The module runs a fixed sequence of development checks from the source checkout:
`ruff check`, Pyright with the root project config and active interpreter,
Radon cyclomatic
complexity, Radon maintainability index, pytest with coverage JSON, and
CRAP-Calculator over the generated coverage report.

The default CLI is:

```text
python -m agents_remember.code_quality.check
```

CRAP threshold enforcement is mandatory in the default command. After rendering
the score table, any function at or above the configured threshold makes the
wrapper return non-zero. The former strict opt-in setting and CLI option no
longer exist.

Each subprocess runs with this checkout's source import roots (the parent of
every configured source package, e.g. `mcp/src`) prepended to `PYTHONPATH` via
`subprocess_env`/`source_import_roots`. That makes pytest import and measure
coverage for *this* checkout's `agents_remember` rather than whatever an editable
install resolves to. Without it, running the gate from a git worktree imported
the primary clone's editable package, so coverage never matched the worktree's
files and every complex function scored as uncovered — inflating CRAP far past
the threshold and falsely failing the push. With it, the gate behaves identically
from the primary clone and from any worktree.

### Invariants And Boundaries

- The wrapper is a fixed quality suite, not a generic shell command surface.
- Subprocess commands use the active Python executable and fixed module names.
- Pyright uses `--project .`, `--pythonpath` pointing at the wrapper's active
  interpreter, and the same configured source/test paths as the other source
  quality commands. The explicit interpreter keeps linked worktrees usable when
  root Pyright config still names `.venv` relative to the checkout but the hook
  is intentionally running with the primary checkout's virtualenv.
- pytest coverage JSON is generated into a temporary file unless the caller
  explicitly supplies `--coverage-json`.
- CRAP-Calculator runs in-process from the generated coverage JSON.
- Every CRAP score at or above the configured threshold fails the default
  wrapper; callers cannot turn enforcement into a report-only result.
- Subprocesses receive an environment with this checkout's source roots first on
  `PYTHONPATH`, so the gate measures the current checkout regardless of where an
  editable install points; the `CommandRunner` signature carries that env.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CRAP-Calculator owns function-level CRAP scoring and rendering. | [crap_calculator.py](agents-remember/mcp/src/agents_remember/code_quality/crap_calculator.py) |
| Unit tests cover fixed command composition including Pyright, failure propagation, missing coverage JSON, mandatory CRAP threshold failure, and repository-gate command parity. | [test_code_quality_check.py](agents-remember/mcp/tests/test_code_quality_check.py) |
| Repo tool guidance points agents to this wrapper for full local source quality checks. | [system/tools.md](agents-remember/system/tools.md) |

## Update History

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: replaced the report-only/strict-opt-in
  contract with mandatory default CRAP failure, added the missing governing-overview backlink, and
  reconciled the test reference; verification remains pinned until the code commit.

- 2026-06-08T12:06+02:00: Pyright command composition now passes `--pythonpath`
  with the wrapper's active interpreter so linked worktrees can reuse the
  primary checkout virtualenv while still resolving third-party imports. The
  pre-push hook also prepends the current checkout's `mcp/src` before invoking
  the wrapper so the worktree version of this module runs. Verification metadata
  stays pinned until closeout. task/runtime-asset-canonical-sync branch.
- 2026-06-02T10:35+02:00: The wrapper now prepends this checkout's source import roots to `PYTHONPATH` for every quality subprocess (`subprocess_env`/`source_import_roots`) and threads that env through the `CommandRunner`. Fixes the gate falsely failing from a git worktree (it imported the primary clone's editable package, so coverage didn't match the worktree files and CRAP inflated). Verification metadata stays pinned until closeout. fix/quality-gate-worktree-local branch.
- 2026-05-28T19:52+02:00: Updated after Pyright joined the fixed source quality wrapper.
- 2026-05-24T06:30+02:00: Created the source quality suite wrapper that runs Ruff, Radon, pytest coverage, and CRAP-Calculator.
