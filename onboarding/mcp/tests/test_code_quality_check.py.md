# mcp/tests/test_code_quality_check.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_code_quality_check.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T04:28+02:00                     |
| lastVerifiedCommitHash | `c1dc5056ffa45cc7fe1af66a6d5c38497fbfa5f6`                      |
| lastVerifiedCommitDate | 2026-07-31T04:58:22+02:00|
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

### Repository-Gate Parity After The Hook Split (260731-EFA-L1)

Two tests hold the local gates to the wrapper, and the split between them matters.

`test_repository_gates_use_default_strict_wrapper` scans the files that must literally contain
`agents_remember.code_quality.check` and must not contain `fail-on-crap-threshold`. That list is
now `.githooks/_gate.sh` and `.github/workflows/quality-checks.yml` — **not** the two hook files.
The hooks no longer inline the wrapper command; both `exec` the shared tiered body, and the full
tier is where the wrapper runs. The fix was to follow the indirection, not to drop the assertion.

`test_git_hooks_delegate_to_the_shared_tiered_gate` closes the hole that indirection would
otherwise open: `.githooks/pre-commit` must contain `exec "$hook_dir/_gate.sh" fast` and
`.githooks/pre-push` must contain `exec "$hook_dir/_gate.sh" full`. Together the two tests still
prove every repository gate reaches the wrapper with no threshold opt-out, while pinning the tier
each hook is wired to — so a pre-commit silently promoted to the full tier (the cost that trained
the `--no-verify` habit) or a pre-push silently demoted to the fast tier both fail here.

### Invariants And Boundaries

- Tests verify command order and fixed module selection without shelling out,
  including that Pyright receives the configured source/test paths and active
  interpreter path.
- Fixed check failures make the wrapper return nonzero.
- Missing coverage JSON makes the CRAP step fail.
- CRAP threshold hits fail the default wrapper, and the parser exposes no
  report-only or strict opt-in mode.
- Repository-gate fixtures prove the shared tiered hook body and CI both invoke
  the same default wrapper command, and separately that each hook is wired to
  its intended tier (`pre-commit` → `fast`, `pre-push` → `full`). The wrapper
  itself runs in the full tier and in CI; the fast tier runs the generated-copy
  checks plus ruff and Pyright.
- The wrapper threads an environment to the runner whose `PYTHONPATH` leads with
  this checkout's source import root, so the gate measures the current checkout.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The source quality wrapper owns the fixed Ruff, Pyright, Radon, pytest, and CRAP-Calculator sequence. | [check.py](agents-remember/mcp/src/agents_remember/code_quality/check.py) |
| CRAP-Calculator owns the function scoring used by the wrapper. | [crap_calculator.py](agents-remember/mcp/src/agents_remember/code_quality/crap_calculator.py) |
| The shared tiered hook body scanned by the parity test; the full tier invokes the wrapper. | [_gate.sh](agents-remember/.githooks/_gate.sh) |
| The two hooks whose tier arguments the delegation test pins. | [pre-commit](agents-remember/.githooks/pre-commit); [pre-push](agents-remember/.githooks/pre-push) |
| CI runs the same wrapper on every branch push and pull request. | [quality-checks.yml](agents-remember/.github/workflows/quality-checks.yml) |

## Update History

- 2026-07-31T04:28+02:00 — 260731-EFA-L1 split the hooks into a fast staged-content tier and a full
  pre-push tier over a shared `.githooks/_gate.sh`. `test_repository_gates_use_default_strict_wrapper`
  now scans `_gate.sh` and the CI workflow instead of the two hook files, which no longer inline the
  wrapper command; the new `test_git_hooks_delegate_to_the_shared_tiered_gate` pins each hook to its
  tier so neither can be silently promoted or demoted. Corrected this card's claim that pre-commit
  invokes the wrapper. Verification metadata pinned to the pre-leaf source authority until closeout
  stamps the code commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: documented mandatory default
  threshold failure, removal of the strict opt-in surface, and repository-gate command parity;
  verification remains pinned until the code commit.

- 2026-06-08T12:06+02:00: Added coverage that the Pyright command includes
  `--pythonpath` and the active interpreter path, matching the linked-worktree
  quality gate fix. Verification metadata stays pinned until closeout.
  task/runtime-asset-canonical-sync branch.
- 2026-06-02T10:35+02:00: Added a test that the wrapper threads this checkout's source import root first onto `PYTHONPATH` (preserving any pre-existing value); the fake runners now take the `env` argument. Verification metadata stays pinned until closeout. fix/quality-gate-worktree-local branch.
- 2026-05-28T19:52+02:00: Updated after source quality wrapper tests began asserting Pyright command wiring.
- 2026-05-24T06:30+02:00: Created unit coverage for the source quality suite wrapper.
