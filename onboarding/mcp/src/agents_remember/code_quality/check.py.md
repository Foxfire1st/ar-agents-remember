# mcp/src/agents_remember/code_quality/check.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/code_quality/check.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-11T23:56+02:00               |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038` |
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

`check.py` is the Python quality wrapper executed inside the repository's pinned Dagger
quality graph. It decides what the Python rail certifies and what it merely reports, but it
is not an independent host-side acceptance gate: closeout and CI consume the Dagger graph's
single exported `clean-quality-results.json` result.

```text
dagger call quality --source=. --repository-bundle=<candidate.bundle> --mode=<targeted|full> --diff-base=<commit> reports export --path=<enclosure>/reports
```

## Code Commentary

#

- 260731-EFA-L7 (trace delta): the quality steps gained the enforcing `file-size` rail (armed via `pyproject.toml`'s `file_size_armed`), and the CRAP/coverage input scope now includes the configured test roots.
## Enforcing Steps Versus Report Steps

Every step is one of two kinds, and the distinction lives in the type rather than in
prose. `Step.report_note is None` means the step **enforces**: a non-zero exit is a finding
and fails the gate. A note means the step **reports**, and the note is printed into the
section header so nobody reads the output as enforcement.

The pytest step supplies the derived selection, coverage, and retry-proof context/append arguments.
Parallelism is not duplicated in this command builder: root pytest `addopts` owns `-n=auto`, so raw,
full, and targeted pytest runs inherit one default and `-n=0` remains an explicit diagnostic
override.

| Step | Kind | What it runs |
| --- | --- | --- |
| `ruff` | enforcing | `ruff check <every tracked .py>` — no `--select`, no `--extend-ignore` |
| `ruff-format` | enforcing | `ruff format --check <every tracked .py>` |
| `pyright` | enforcing | `pyright --project . --pythonpath <interpreter> <every tracked .py>` |
| `radon-cc` | **report** | `radon cc <packages> -s -n B --order SCORE` |
| `radon-mi` | **report** | `radon mi <packages> -s -n B` |
| `pytest` | enforcing | the derived suite under coverage, inheriting root pytest `-n=auto`, and emitting the coverage JSON |
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

**The full wrapper takes no path arguments at all, and it cannot be narrowed by hand.**
The one sanctioned narrowing is the leaf-edge `--targeted` contract (260731-EFA-L17) —
see the L17 section below — which derives its scope from the leaf's diff rather than
accepting caller-supplied paths.

The targeted branch preserves the repository's `file_size_armed` setting when it constructs the
targeted `CheckConfig`. File-size therefore remains an enforcing leaf rail; deriving a smaller path
set must never reset the policy bit to the dataclass default and turn violations into report-only
output.

#### Reading The Index Puts An Obligation On The Caller

Because `git ls-files` reads the *index*, this gate certifies **what is staged**, not what is on
disk — and since the wrapper takes no path arguments, it cannot be told otherwise. That places one
obligation on every caller: whatever the caller means this gate to certify has to be in the index
*before* it invokes the wrapper. 260731-EFA-L4 wrote that contract into `derive_scope`'s docstring.
It is the **only** part of this file L4 touched, and it changed no behaviour — 13 added lines, all
inside the docstring, zero executable lines altered.

The two tiers meet the obligation differently:

- The **pre-commit tier** gets it for free. There the staged content *is* the commit, so the index
  already names exactly what that tier certifies.
- The **closeout tier** does not, because it commits with `git add -A`. It therefore stages its
  whole worktree first: `worktrees/modules/closeout_staged_quality.py:gate_staged_code` runs
  `git reset --mixed HEAD` and then `git add -A`, and only then calls this wrapper. Until it did,
  every file a task **created** rather than edited went into the commit without ruff, pyright or
  the changed-lines floor reading a line of it, and a file the task **deleted** stayed in
  `ls-files` until the deletion was staged, so ruff was handed a path that no longer existed and
  took an `E902` for it. The docstring names the cost rather than describing it abstractly: L3's
  `abc7cbc` — the commit this card is pinned to — shipped four files that way.

**Widening the enumeration here would have been the wrong fix, twice over**, and the docstring says
so. Enumerating `--cached --others --exclude-standard` would redefine the pre-commit tier, making
ruff and pyright certify files deliberately held out of the commit; and it cannot reach
`run_diff_coverage` at all, because an untracked file has no diff against any base. The fix belongs
in the caller, and that is where it landed — this module's own logic is unchanged.

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

### 260731-EFA-L17 — The Two Contracts: Full And Targeted

The wrapper now speaks two contracts. `CheckConfig` (lines 70-84) gained the
`targeted`, `targeted_base`, and `targeted_scope` fields; `config_from_args`
(lines 677-711) maps `--targeted` / `--diff-base` / `--memory-cap-bytes` onto
them. `quality_steps` (lines 225-259) branches on the targeted plan:

- ruff/ruff-format/pyright run over the derived changed-file scope
  (`_fixed_steps`, lines 133-157);
- radon-cc/radon-mi consume the changed production module **files**
  (`_radon_report_steps`, lines 158-184) — this fixed the L17-round-2 finding
  where the report rails received package names that resolved to nothing at the
  repo root;
- pytest runs the derived test subset, or is omitted loudly when a targeted run
  derived none (`_pytest_step`, lines 185-203);
- the file-size rail is scoped to the leaf's changed paths in targeted mode
  (`_file_size_step`, lines 204-224);
- a targeted run with no changed Python files short-circuits to PASS with
  nothing for the leaf rails to certify (`run_quality_check`, lines 308-361).

Coverage.py instruments the top-level package root (the same proven shape as
the full wrapper) because per-module `--cov` on FastMCP/pydantic files crashed
collection; CRAP and diff-coverage still score the changed modules and the
leaf's own diff. `source_import_roots` (lines 264-294) now recovers the package
root when a coverage path is a file inside the package. Full runs may also run
under `--memory-cap-bytes` (RLIMIT_AS self-cap; see `code_quality.memory_cap`).

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
- Scope is derived, never passed: the full run takes no CLI path arguments, and
  the only sanctioned narrowing is `--targeted`'s change-set contract (changed
  files + reverse-import closure + derived test subset). No caller may hand the
  wrapper paths by hand.
- Scope is the **index**, so the caller owns what gets certified. The wrapper cannot be pointed at
  unstaged or untracked work, and a caller that commits with `git add -A` must stage before
  invoking it. Undo the `git reset --mixed` + `git add -A` in
  `closeout_staged_quality.py:gate_staged_code` and
  closeout silently returns to certifying only the files a task edited, reporting green on files no
  rail ever read.
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The changed-lines coverage floor this wrapper runs last, and the derivation of the 100% floor. | `DEFAULT_DIFF_COVERAGE_FLOOR` | mcp/src/agents_remember/code_quality/diff_coverage.py:1-5; mcp/src/agents_remember/code_quality/diff_coverage.py:30-30 |
| CRAP-Calculator owns function-level CRAP scoring, and is where Radon stays load-bearing. | `crap_score` | mcp/src/agents_remember/code_quality/crap_calculator.py:89-92; mcp/src/agents_remember/code_quality/crap_calculator.py:232-239 |
| Unit tests prove Radon is declared a report, that every enforcing step can fail, that the tool-signature exemption cannot widen, and that scope is derived rather than written down. | `RadonIsAReportNotAGateTests` | mcp/tests/test_code_quality_check.py:315-373 |
| An independent recomputation asserts the wrapper's real argument vectors reach every tracked Python file. | `test_every_tracked_python_file_is_linted_and_type_checked` | mcp/tests/test_gate_scope.py:152-173 |
| `run_git` — the one runner `git_ls_files` calls — strips `GIT_REPOSITORY_SELECTOR_ENV` and bounds every call with the local/remote/metadata timeout classes. | `GIT_REPOSITORY_SELECTOR_ENV` | mcp/src/agents_remember/kernel/git_command.py:33-42; mcp/src/agents_remember/kernel/git_command.py:70-73; mcp/src/agents_remember/kernel/git_command.py:85-92 |
| `QualityGateGitTests` points `GIT_DIR` at a decoy repository and proves `git_ls_files` still lists the repository it was handed, and that a non-repository and an unrunnable git both surface as `ScopeError`. | `QualityGateGitTests` | mcp/tests/test_git_command.py:391-453 |
| The shared tiered hook body derives the same `git ls-files` scope; the pre-push tier delegates to the wrapper's targeted contract, while `full` stays the manual/master-gate tier. | "git ls-files -z -- '*.py'" | .githooks/_gate.sh:72-72 |
| `[tool.pytest.ini_options] testpaths`, the selected complexity rules, and branch coverage are configured here. | "\"C901\", # Enforce [tool.ruff.lint.mccabe] max-complexity."; "branch = true"; "testpaths = [\"mcp/tests\"]" | pyproject.toml:6-18; pyproject.toml:67-70; pyproject.toml:110-124 |
| Repo instructions make the pinned Dagger graph the only acceptance environment, identify its exported result as authoritative, and explicitly refuse host test execution. | "dagger call quality --source=."; "single authoritative result"; "There is no host-test compatibility path" | AGENTS.md:148-161 |
| The closeout caller that satisfies this module's index obligation: `gate_staged_code` resets the index and stages the whole task worktree before invoking the wrapper with the leaf's targeted plan — and runs both worktree refusals before the reset, because `git reset` drops unmerged entries and `MERGE_HEAD`. | `gate_staged_code` | mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:77-129 |
| The optional settings-owned memory cap an explicitly constrained full run may use (`--memory-cap-bytes`); host-managed full runs do not call this planner. | `plan_capped_command` | mcp/src/agents_remember/kernel/primitives/memory_cap.py:92-130 |
| The targeted contract proofs: rail scoping, real radon input, and no-change short-circuit. | `TargetedScopeDerivationTests`, `TargetedWrapperRunTests` | mcp/tests/test_code_quality_targeted.py:142-359; mcp/tests/test_code_quality_targeted.py:360-630 |
| The command builder supplies derived test and coverage arguments; root pytest configuration owns automatic xdist workers. | "pytest_args = [sys.executable, \"-m\", \"pytest\", *test_args]"; "-n=auto" | mcp/src/agents_remember/code_quality/check.py:272-272; pyproject.toml:124-124 |

## 260731-EFA-L9 Change — Armed Layering Step

The wrapper's `quality_steps` now registers the `layering` step unconditionally
(cit:([`quality_steps`], mcp/src/agents_remember/code_quality/check.py:320-366)):
`code_quality/layering.py` reads `layers.toml [contract].order` and fails on rank violations,
package-pair cycles, undeclared top-level directories, and `from agents_remember import X` forms
resolving to no declared package. There is no baseline/allowlist; a green full wrapper now
requires zero layering violations.

## L23 Native Scratch Boundary

The quality CLI now forces transient tool state through the short native
`/tmp/arq` root and resets Python's process-wide `tempfile.tempdir` cache after
environment sanitization. Durable progress/test reports remain enclosure-owned;
the short scratch path prevents inherited WSL/UNC roots and Unix-socket length
limits from breaking otherwise-valid checks.

## Update History
- 2026-08-14T06:00+02:00 — L23 curator: reconciled the wrapper with the accepted Dagger-only
  quality boundary and the extracted staged-candidate gate owner; host invocation is diagnostic
  implementation detail, never a second acceptance gate. Verification metadata remains
  closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented the short native scratch root and cached-temp reset; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T07:15+02:00 — 260731-EFA-L24 curator: re-read the
  wrapper's optional self-cap path, corrected the moved planner range, and
  clarified that ordinary full runs are host-managed. Verification metadata
  remains pinned until closeout stamps L24.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: recorded that targeted configuration carries
  the repository file-size arm instead of falling back to the false dataclass default; updated
  shifted test citations after the responsibility splits.

- 2026-08-12T00:20+02:00 — Corrected ownership after `-n=auto` moved to root pytest `addopts`:
  this wrapper now contributes only derived test, coverage, and retry-proof arguments.
  Verification metadata remains pinned until closeout.

- 2026-08-11T23:56+02:00 — Recorded the single pytest rail's mandatory pytest-xdist `-n auto`
  execution; coverage and retry-proof arguments remain on the same command. Verification metadata
  remains pinned until closeout.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: recorded the armed layering step in the
  wrapper contract; the L9 change section above documents the rail. Verification metadata pinned
  until closeout stamps the L9 code commit.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the two contracts
  (full vs `--targeted`), the radon changed-file input fix, the derived test
  subset, the package-root coverage instrumentation, and the memory-cap flag;
  corrected the "no path arguments / no narrowing" claim to name `--targeted`
  as the only sanctioned narrowing; refreshed the closeout caller row to the
  post-L17 range. Verification metadata stays pinned until closeout stamps the
  260731-EFA-L17 commit.

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 curator (trace delta): body verified against the current code and updated (260731-EFA-L7 (trace delta): the quality steps gained the enforcing `file-size` rail (armed via `pyp...). Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: the file-size step (`file_size`) was added to the project-owned quality steps, armed via `pyproject.toml`'s `file_size_armed`; CRAP/coverage scope now includes the configured test roots. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized all 10 reference rows from
  markdown links to plain anchored sources (diff_coverage, crap_calculator, the four test suites,
  git_command, _gate.sh, pyproject.toml, AGENTS.md, closeout.py). Zero findings remain.

- 2026-08-01T09:40+02:00 — 260731-EFA-L4 curator: recorded the caller obligation that follows from
  reading the index. **Only this file's `derive_scope` docstring changed in L4 — 13 added lines, no
  deletions, zero executable lines; the wrapper's own logic is untouched.** The behaviour change is
  entirely in its caller: `worktrees/modules/closeout_staged_quality.py:gate_staged_code` now runs
  `git reset --mixed HEAD` + `git add -A` before invoking the wrapper, so files a task created (and
  deletions it made) are visible to ruff, pyright and the changed-lines floor where previously they
  were not. Added "Reading The Index Puts An Obligation On The Caller" under *Scope Is Derived From
  The Tree*, stating the pre-commit tier meets that obligation for free while the closeout tier had
  to be made to (the docstring records that L3's `abc7cbc` shipped four files ungated), and stating
  why widening this module's enumeration to `--cached --others --exclude-standard` was rejected:
  it would redefine the pre-commit tier and cannot reach `run_diff_coverage`, since an untracked
  file has no diff against any base. Added the matching invariant and one `closeout.py` reference
  row. Checked the card against `crap_calculator.py:83` — the body names no CRAP number, so nothing
  here contradicts `DEFAULT_CRAP_THRESHOLD = 20.0`. This card carries no line-range citations (its
  reference table is source paths only, two columns), so nothing needed re-anchoring. Verification
  metadata pinned until closeout stamps the commit.

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
