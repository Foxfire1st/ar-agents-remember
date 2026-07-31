# mcp/src/agents_remember/code_quality/check.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/code_quality/check.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T16:10+02:00                     |
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7` |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

`check.py` is the quality gate. It is the command the pre-push hook, CI, and worktree
closeout run, and it is the single place that decides what the repository certifies and
what it merely reports.

```text
python -m agents_remember.code_quality.check
```

## Code Commentary

### Enforcing Steps Versus Report Steps

Every step is one of two kinds, and the distinction lives in the type rather than in
prose. `Step.report_note is None` means the step **enforces**: a non-zero exit is a finding
and fails the gate. A note means the step **reports**, and the note is printed into the
section header so nobody reads the output as enforcement.

| Step | Kind | What it runs |
| --- | --- | --- |
| `ruff` | enforcing | `ruff check <every tracked .py>` — no `--select`, no `--extend-ignore` |
| `ruff-format` | enforcing | `ruff format --check <every tracked .py>` |
| `pyright` | enforcing | `pyright --project . --pythonpath <interpreter> <every tracked .py>` |
| `radon-cc` | **report** | `radon cc <packages> -s -n B --order SCORE` |
| `radon-mi` | **report** | `radon mi <packages> -s -n B` |
| `pytest` | enforcing | the suite under coverage, emitting the coverage JSON |
| CRAP | enforcing | scored in-process from that JSON after the steps (`run_crap_calculator`) |
| diff-coverage | enforcing | scored in-process from the **same** JSON (`run_diff_coverage`) |

The last two do not measure anything again. `pytest` writes one coverage report and both
score it, so the aggregate, CRAP and the changed-lines floor are three readings of one
measurement rather than three runs that can disagree.

**Radon cannot fail this gate and never could.** `radon cc` and `radon mi` exit 0 whatever
they find, so `run_fixed_checks` was structurally incapable of failing on them while the
wrapper's help text, the CI step name, and `AGENTS.md` all listed them beside the checks
that can. The steps are kept, relabelled with `RADON_REPORT_NOTE` — *"report only: radon
exits 0 whatever it finds, so nothing below can fail the gate"* — and their header now says
so. A report step that exits non-zero *does* still fail the gate: for a tool that exits 0
on every finding, a non-zero exit means the tool itself broke, and `step_failure()` prints
exactly that sentence rather than "failed with exit code N".

Radon remains load-bearing outside the gate: `crap_calculator.py` imports
`radon.complexity.cc_visit` for the complexity term of every CRAP score.

### Nothing Here Is Exempt

There is **no baseline, ratchet, allowlist or grandfather file** in this gate — not for
complexity, not for CRAP, not for coverage.

A fifth `complexity-baseline` step used to sit beside `ruff`, holding `C901`, `PLR0911`,
`PLR0912` and `PLR0915` against `quality/complexity-baseline.txt`, and `ruff` was handed
`--extend-ignore` for exactly those codes so the two steps could not double-report the same
function. **All of that is gone**: the module, its data file, its test, the
`BASELINED_COMPLEXITY_RULES` tuple and the `--extend-ignore` routing. The 67 recorded
offenders were refactored rather than scheduled, so `ruff` enforces the four codes directly
and the only way past a finding is to fix the function.

The `ruff` step therefore carries a comment saying what its bare command line means:
anything routed off it is a rule the gate stops enforcing. Adding a flag there is the
single edit that would silently un-arm four complexity rules.

### Scope Is Derived From The Tree

There are no `DEFAULT_SOURCE_PATHS`/`DEFAULT_TEST_PATHS` constants, no positional
`source_paths` argument and no `--tests` option. `derive_scope(project_root)` builds a
frozen `GateScope`:

- `lint_paths` and `type_paths` — **every tracked Python file**, from
  `git ls-files -z -- '*.py'`. `git ls-files` reads the *index*, so a file is in scope the
  moment it is `git add`-ed, which is exactly the content the pre-commit tier certifies.
- `coverage_paths` — the tracked top-level importable packages (`top_level_packages`: a
  directory holding `__init__.py` whose parent is not itself a package). These are what
  `--cov` measures, what the Radon report covers, and what CRAP scores; their parents are
  the import roots pushed onto `PYTHONPATH`.
- `test_paths` — read from `[tool.pytest.ini_options] testpaths` in the root
  `pyproject.toml`, so the wrapper does not carry a second copy of where the suite lives.

Every failure mode raises `ScopeError` rather than degrading: `git ls-files` failing, a tree
with no tracked Python, no tracked top-level package, a missing `pyproject.toml`, or a
missing/empty `testpaths`. `main()` catches it, prints `gate scope could not be derived: …`,
and returns 1. An empty scope would make every step pass by certifying nothing, which is the
exact failure this module exists to prevent.

**The wrapper takes no path arguments at all.** There is no supported way to narrow what the
gate certifies.

#### The Scope Query Runs On The Package's One Git Runner

`git_ls_files` does not spawn `git` itself. It builds `["ls-files", "-z", "--", *patterns]` and
hands it to `agents_remember.kernel.git_command.run_git`, which strips the `GIT_DIR`-family
repository selectors (`GIT_REPOSITORY_SELECTOR_ENV`: `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`,
`GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`,
`GIT_PREFIX`) from the child environment before running.

That is load-bearing for *this* module in particular, and the source says why: **this gate runs
from the `pre-push` hook, and git exports `GIT_DIR` to its hooks.** An unstripped `ls-files` here
would derive the entire gate's scope — every path Ruff lints, Pyright types and coverage measures —
from whichever repository `GIT_DIR` named, so the wrapper would certify a tree nobody was pushing.
Of all the git call sites in this package, the gate's were the ones most certain to meet the
variables they did not strip.

The failure conversion moved with it. `run_git` returns a `CompletedProcess` with `check=False`, so
`git_ls_files` raises `ScopeError` on *both* halves: `except (OSError, subprocess.SubprocessError)`
for a git that cannot run at all — which also now covers `subprocess.TimeoutExpired`, since the
runner bounds every call (300s locally by default) — and an explicit `completed.returncode != 0`
branch that puts the exit code and git's `stderr` in the message. Neither can return an empty list.

### The Two Post-Suite Scorers

`run_crap_calculator` renders the fixed-length `--top` table, then — separately — lists
**every** function at or above the threshold, not the first `--top` of them, with the branch
coverage that would clear it (`crap_failure_line` inverts `crap = cc**2 * (1-c)**3 + cc`).
When the complexity term alone already reaches the threshold there is no such coverage, and
the line says "split it" instead of naming an impossible number. A gate that truncates its
own findings sends the reader back to run the tool by hand for the rest.

`run_diff_coverage` resolves the diff base, scores the changed lines, prints the base it
chose and every uncovered line by name, and fails only in the `measured` state. It lives
inside the wrapper rather than beside it so it reaches the pre-push hook, closeout and CI
through the one command they already run.

Both return 1 when `coverage_json` does not exist, so a pytest step that died without
writing a report cannot leave two enforcing rails silently satisfied.

### Existing Behaviour That Did Not Change

Each subprocess still runs with this checkout's source import roots first on `PYTHONPATH`
(`subprocess_env` / `source_import_roots`, fed from `scope.coverage_paths`). That makes
pytest import and measure *this* checkout's `agents_remember` rather than whatever an
editable install resolves to, so the gate behaves identically from the primary clone and
from any linked worktree. CRAP threshold enforcement is still mandatory in the default
command, with no report-only or strict opt-in surface. `coverage_path_context` still writes
the report to a temporary directory unless `--coverage-json` is given.

## Invariants And Boundaries

- The wrapper is a fixed quality suite, not a generic shell command surface.
- Scope is derived, never passed: no CLI path arguments exist, and no caller can narrow it.
- A step is enforcing unless it carries a `report_note`; only the two Radon steps carry one.
- A report step that exits non-zero still fails the gate, reported as a broken tool.
- The four complexity codes are enforced by `ruff` directly. Any `--select`/`--ignore`/
  `--extend-ignore` added to that step un-arms rules — that is what the deleted baseline
  step used to do on purpose.
- No baseline, ratchet, allowlist or exemption file exists anywhere in this gate, and the
  CLI help says so.
- Any scope derivation failure is fatal and exits 1; the gate never certifies an empty or
  guessed scope. A non-zero `git ls-files` and an unrunnable git both raise `ScopeError`; neither
  degrades to an empty scope.
- Scope is read through `kernel.git_command.run_git`, never through a local `subprocess.run`.
  This gate runs from the `pre-push` hook where `GIT_DIR` is exported, so a bare `git` spawn here
  would scope the whole gate to another repository. `test_git_command.py::SingleRunnerTests`
  fails the build if any module in the package spawns `git` itself.
- One pytest run produces one coverage report; CRAP and the diff floor both score that
  report and never re-measure.
- Every CRAP score at or above the configured threshold fails the default wrapper, and every
  offender is listed — not just the top `--top`.
- Every uncovered changed line fails the default wrapper, and every one is named.
- `--diff-base`/`--diff-floor` exist so the failure probes can drive the arithmetic; the
  floor is policy (100%), not a dial.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The changed-lines coverage floor this wrapper runs last, and the derivation of the 100% floor. | [diff_coverage.py](agents-remember/mcp/src/agents_remember/code_quality/diff_coverage.py) |
| CRAP-Calculator owns function-level CRAP scoring, and is where Radon stays load-bearing. | [crap_calculator.py](agents-remember/mcp/src/agents_remember/code_quality/crap_calculator.py) |
| Unit tests prove Radon is declared a report, that every enforcing step can fail, that the tool-signature exemption cannot widen, and that scope is derived rather than written down. | [test_code_quality_check.py](agents-remember/mcp/tests/test_code_quality_check.py) |
| An independent recomputation asserts the wrapper's real argument vectors reach every tracked Python file. | [test_gate_scope.py](agents-remember/mcp/tests/test_gate_scope.py) |
| `run_git` — the one runner `git_ls_files` calls — strips `GIT_REPOSITORY_SELECTOR_ENV` and bounds every call with the local/remote/metadata timeout classes. | [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |
| `QualityGateGitTests` points `GIT_DIR` at a decoy repository and proves `git_ls_files` still lists the repository it was handed, and that a non-repository and an unrunnable git both surface as `ScopeError`. | [test_git_command.py](agents-remember/mcp/tests/test_git_command.py) |
| The shared tiered hook body derives the same `git ls-files` scope and runs this wrapper as its full tier. | [_gate.sh](agents-remember/.githooks/_gate.sh) |
| `[tool.pytest.ini_options] testpaths`, the selected complexity rules, and branch coverage are configured here. | [pyproject.toml](agents-remember/pyproject.toml) |
| Repo instructions state the gate command, that it takes no path arguments, and that Radon reports. | [AGENTS.md](agents-remember/AGENTS.md) |

## Update History

- 2026-07-31T20:48+02:00 — 260731-EFA-L3 curator: `git_ls_files` no longer spawns `git` itself.
  It builds `["ls-files", "-z", "--", *patterns]` and calls
  `agents_remember.kernel.git_command.run_git`, the package's single runner, which strips the
  `GIT_DIR`-family selectors. The card documented the derived scope without ever saying which
  repository the derivation reads — and this gate runs from the `pre-push` hook, where git exports
  `GIT_DIR`, so that was the one omission that mattered. Added "The Scope Query Runs On The
  Package's One Git Runner" under *Scope Is Derived From The Tree*, recorded the changed failure
  conversion (`check=True`/`CalledProcessError` → explicit `returncode != 0` plus
  `OSError`/`subprocess.SubprocessError`, which now includes the runner's timeout), and added the
  two matching invariants and the `git_command.py` / `test_git_command.py` reference rows. No
  citation ranges in this card point into a file this leaf changed — its reference table carries
  source paths only.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 final state. **Retired this card's
  `complexity-baseline` step, its `BASELINED_COMPLEXITY_RULES` routing contract and the
  `ruff --extend-ignore` note**: the developer's no-deferral rule removed the baseline
  outright, so `ruff` now enforces `C901`/`PLR0911`/`PLR0912`/`PLR0915` directly and the
  module, data file, test and gate step no longer exist. Added the `diff-coverage` step as
  the eighth and binding one, recorded that CRAP and the floor score the *same* coverage
  report, and recorded that both fail when that report is missing. Verification metadata is
  pinned to the leaf's reformat commit until closeout stamps the code commit.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 gate honesty (mid-leaf): replaced the report-only
  Radon claim with the `Step.report_note` split, added `ruff format --check`, and replaced
  the scope constants and CLI path arguments with `derive_scope`.

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
