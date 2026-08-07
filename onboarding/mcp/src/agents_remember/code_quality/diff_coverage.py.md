# mcp/src/agents_remember/code_quality/diff_coverage.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/code_quality/diff_coverage.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T16:10+02:00                     |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

`diff_coverage.py` is **the binding coverage gate**. It scores the lines this change
touched against the coverage JSON `pytest` has already written, and fails the wrapper
when any of them never ran. It is the last enforcing step of
`python -m agents_remember.code_quality.check`, added by 260731-EFA-L2 (requirement
L2-R7). Before it, no coverage number in this repository could fail anything except CRAP.

It measures nothing itself. `check.py` runs pytest once with `--cov-report=json`, CRAP
reads that report, and this module reads the same report — so the aggregate, CRAP and the
diff floor are three readings of one measurement rather than three runs that can disagree.

## Code Commentary

### Why The Floor Is 100%, And Why No Lower Number Was Available

This is the fact most likely to be argued with later, so the derivation is recorded in the
module docstring and repeated here.

- **The aggregate cannot be the gate.** 88k lines of tests against 44,697 measured
  statements means a large share of the package executes simply by being imported. On
  2026-07-31 the suite reported **87.16%** (90.17% statements, 76.52% branches) over 434
  files. One newly added, entirely untested 20-line function moves that by **0.04
  percentage points** — below the resolution of any threshold anyone would set, and below
  the run-to-run wobble of a suite that starts subprocesses. An aggregate pin is satisfied
  by import-time execution and cannot see a single change, which is the only thing a
  pre-merge gate is for.
- **A floor below 100% is a per-change budget for untested code, and the budget grows
  with the change.** At floor `X`, a change of `N` units may carry `floor((1 - X) * N)`
  uncovered ones. Measured on this repository: of the last 40 commits on `main`, 31 touch
  `mcp/src/agents_remember` — p25 46 added source lines, median 234, p75 532, max 10,549.
  Against the median 234 units the budget is **23 uncovered units at 90%**, 11 at 95%, 4
  at 98%. The median function here is about **9 statements** (44,697 statements across
  4,672 scored functions), so **90% lets an entire untested function land inside an
  average change**, and 95% lets one land inside any change past 180 units — above the
  observed median. Only 100% means the same thing for a 3-line change and a 300-line one.
- **The lower bound rules the popular numbers out without any budget argument.** A floor
  at or below the tree's own aggregate (87.16%) passes any change that is merely average,
  so the tree can never improve and drifts down as the code grows. That disqualifies 80
  and 85 outright.
- **What arming it cost is stated rather than hidden.** Against this branch's merge base
  on 2026-07-31: 5,302 changed measurable units, 4,899 covered — 92.40% — leaving 403
  uncovered across 71 files. The floor was **not** set to 93% to make that green. 172 of
  the 403 are lines whose exact text also appears among the diff's removed lines (code
  relocated by the parameter-object and complexity refactors and by the whole-tree
  `ruff format` in `00e8379`); 231 are new content. **The gate does not subtract the
  relocated ones** — a carve-out for "lines that moved" is an exemption list with a
  different name, and a change that moves uncovered code into a new home owns it on
  arrival. All 403 were cleared; the leaf's final run reported 5498/5498 = 100.00%.

`DEFAULT_DIFF_COVERAGE_FLOOR = 100.0`. `--diff-floor` exists on the wrapper's parser and
is what the failure probes use to prove the arithmetic; it is not an operational dial.

### The Unit Being Counted

A *unit* is a measurable statement **or a branch arc leaving a changed line** — Coverage.py's
own accounting, and the same one `crap_calculator` uses. `tally_file` intersects the changed
line set with `executed_lines`, `missing_lines`, and the arcs whose **source** line is
changed (`executed_branches`, `missing_branches`). A changed line carrying no statement — a
comment, a blank, a continuation — contributes nothing at all rather than counting as
covered.

Because it reuses `crap_calculator.load_coverage_by_path`, the branch requirement is
inherited: a coverage report produced without `[tool.coverage.run] branch = true` is
**refused**, not silently degraded to statements.

### Base Resolution Is Printed, Never Assumed

A gate that silently picks its own comparison point can be made to certify nothing by
picking the wrong one, so `BaseResolution` carries both the revision and *how it was
chosen*, and `render` prints both on every run next to the verdict.

`resolve_base` tries, in order (`candidate_sources`), taking the **merge base** with the
first that resolves:

| Order | Revision | Why it earns its place |
| --- | --- | --- |
| 1 | `--diff-base` | The flag wins over everything, including the environment. A value that is not a commit raises `DiffScopeError` rather than falling through. |
| 2 | `AR_GATE_DIFF_BASE` | The one way to say it outright. A leaf worktree branched from a series branch is the case git cannot infer — `main` is not its source and it has no upstream — so `.githooks/_gate.sh` and the closeout path pass this. |
| 3 | `GITHUB_BASE_REF` | A pull request states its own base; tried as `origin/<ref>` then `<ref>`. This is what CI uses. |
| 4 | `@{upstream}` | Git's own record of where the branch came from, when one is configured. |
| 5 | `origin/HEAD`, then `main` | The default branch, the source for anything cut from it. |

When nothing resolves — an orphan branch, a first commit, a clone with no remote and no
`main` — the base becomes git's **empty tree** (`EMPTY_TREE`,
`4b825dc642cb6eb9a060e54bf8d69288fbee4904`), so every tracked line is a changed line and
the floor applies to all of it. That is deliberately the strict reading of "nothing to
compare against"; it is **not** a fourth state and it is not a skip.

### Four Reported States, None Of Which Pass Silently

| State | Meaning | Floor applies |
| --- | --- | --- |
| `measured` | Changed Python lines sit inside the measured packages. | yes — and every uncovered line and untaken arc is **named** |
| `no-changed-lines` | The diff against the base is empty. | no; says so |
| `no-python-changes` | Files changed, none of them Python. | no; says so |
| `no-measurable-changes` | Python changed, but no changed line is inside a measured package (tests, `scripts/`, provider images). | no; the files and their changed-line counts are listed |

`state_for_empty_diff` exists purely to tell the middle two apart — collapsing them into a
single "skipped" is how a gate stops being readable. `unmeasured_header`/`unmeasured_files`
list the unscored Python on **every** run, including successful ones, because an unscored
file nobody prints is indistinguishable from a covered one.

### Findings Are Named, Not Counted

`render` prints `uncovered line <path>:<n>` and `untaken branch <path>:<src> -> <dst>` for
every finding, with `describe_destination` rendering Coverage.py's negative destination as
`exit`. The percentage alone trains people to add any test until the number moves; the list
says which line has never run, which is the only actionable form. The report also states
outright that there is no exemption list — each finding is cleared by a test that reaches
it, or by deleting the code.

### Diff Parsing

`changed_python_lines` runs `git diff --unified=0 --no-color --no-ext-diff
--diff-filter=ACMR <base> -- '*.py'` — **base-to-working-tree, no second revision**, because
the working tree is what the suite just imported and measured, so the post-image line
numbers index the same content the coverage report describes.

`parse_unified_diff` is split out from the git call on purpose: its two guards (a `+++`
header that is not `+++ b/<path>`, and a `@@` line the `HUNK` pattern does not match) are
reachable only from malformed input, and `mcp/tests/test_diff_coverage.py` drives them
directly. A guard no test can reach is a guard nobody can show is right.

### Every Git Call Goes Through `_git`, On The Package's One Runner

`_git` is this module's only spawn point. It has exactly **three** callers — `run_git`,
`revision_exists` and `merge_base` — and `changed_python_lines` / `state_for_empty_diff` reach it
through `run_git`:

```python
def _git(project_root: Path, arguments: list[str]) -> subprocess.CompletedProcess[str]:
    try:
        return git_command.run_git(project_root, ["-c", "core.quotePath=false", *arguments])
    except (OSError, subprocess.SubprocessError) as error:
        raise DiffScopeError(f"git command failed (git {' '.join(arguments)}): {error}") from error
```

Three facts are packed into that helper.

- **`core.quotePath=false` is this gate's own requirement and stays.** Without it git octal-escapes
  non-ASCII paths in `diff` output, and `parse_unified_diff` stops recognising the very files it is
  supposed to score — silently, as "no changed lines".
- **The spawn itself belongs to `kernel.git_command.run_git`**, which strips the `GIT_DIR`-family
  repository selectors (`GIT_REPOSITORY_SELECTOR_ENV`) before running. That is not tidiness here.
  The full tier runs from the `pre-push` hook and git exports `GIT_DIR` to its hooks, so of every
  git call site in the package this gate's were the ones most certain to meet the variables they
  did not strip — and a redirected `git diff` makes this module certify the coverage of a different
  repository than the one being pushed.
- **The conversion of "git could not run" into `DiffScopeError` lives in `_git`, so all three
  callers get it by construction rather than by three copies.** `run_git` used to own that
  conversion alone while `revision_exists` and `merge_base` called this helper bare, and moving
  onto the shared runner made that difference load-bearing: the runner **bounds** every call
  (`GIT_LOCAL_TIMEOUT_SECONDS` = 300s) where the old inline `subprocess.run` had no timeout at all,
  and it passes `cwd=repo_root`, so a `project_root` that does not exist raises `FileNotFoundError`
  out of `subprocess.run` before git is ever started — where the old `git -C <path>` with no `cwd=`
  merely exited non-zero and those two answered `False` / `None`. `subprocess.TimeoutExpired` and
  `FileNotFoundError` are caught here as `SubprocessError` and `OSError`, so a wedged or unstartable
  git is this gate's own typed error from every entry point.

`run_git` is kept as the public, *raising* wrapper, and it now owns only the **other** failure half.
`kernel.git_command.run_git` returns a `CompletedProcess` with `check=False`, so `run_git` raises
`DiffScopeError` on an explicit `completed.returncode != 0`, carrying the exit code and git's
`stderr`. `revision_exists` and `merge_base` still read `returncode` directly, because a missing
revision and an unresolvable merge base are **answers, not failures** — converting those would turn
every ordinary negative into a gate crash, which is what
`test_a_git_that_ran_and_said_no_is_still_an_answer_not_an_error` pins.

## Invariants And Boundaries

- **The floor is 100% and lowering it is a policy change, not a tuning change.** Anything
  below it is a budget for untested code that grows with the size of the change; anything
  at or below 87.16% passes a merely average change.
- This module **scores** an existing coverage report. It never runs pytest and never
  measures coverage itself.
- It inherits `crap_calculator`'s refusal of a statement-only report. Turning
  `[tool.coverage.run] branch` off breaks this step loudly rather than softening it.
- There is no exemption list, no ignore file, and no carve-out for relocated lines. A
  moved uncovered line is owned by the change that moved it.
- The base used is printed on every run, always, including on success.
- No merge base means the empty tree, i.e. the whole tree — never a skip.
- Only the `measured` state can fail. The other three report and pass, and each says which
  of them it is.
- It lives **inside** the wrapper rather than beside it, so it reaches the pre-push hook,
  closeout and CI through the one command they already run. A separate invocation is a
  gate somebody has to remember, which is the same as not having one.
- Every git call goes through `_git`, and therefore through `kernel.git_command.run_git`. Do not
  spawn `git` in this module: it runs from the `pre-push` hook where `GIT_DIR` is exported, and an
  unstripped selector points the diff at another repository.
  `test_git_command.py::SingleRunnerTests` fails the build if a second runner appears.
- `-c core.quotePath=false` must stay on every call this module makes. It is what keeps
  `parse_unified_diff` able to see non-ASCII paths; losing it degrades the gate to silence rather
  than to an error.
- A git failure is a `DiffScopeError`, never an empty diff. An empty diff means `no-changed-lines`,
  which passes — so a failure that returned one would be a silent pass.
- **The three wrappers must agree on which failures are this gate's error.** The
  `OSError` / `subprocess.SubprocessError` conversion belongs to `_git`. Moving it back up into
  `run_git` alone lets a wedged git (`TimeoutExpired`, from the runner's 300s bound) or a missing
  `project_root` (`FileNotFoundError`, from the runner's `cwd=`) escape `revision_exists` and
  `merge_base` untyped. `test_diff_coverage.py::BaseResolutionTests::test_the_three_git_wrappers_agree_on_which_failures_are_this_gate_s_error`
  fails if any of the three stops converting.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wrapper's `run_diff_coverage` step, the `--diff-base`/`--diff-floor` flags, and the single pytest coverage run this module reads. | `run_diff_coverage` | mcp/src/agents_remember/code_quality/check.py:396-439 |
| `load_coverage_by_path`, `FileCoverage`, and the refusal of a report without branch data, all reused here. | `load_coverage_by_path`; `FileCoverage` | mcp/src/agents_remember/code_quality/crap_calculator.py:41-59; mcp/src/agents_remember/code_quality/crap_calculator.py:113-132 |
| Unit tests for base resolution order, the four states, the malformed-diff guards, and the named-findings report. `BaseResolutionTests::test_the_three_git_wrappers_agree_on_which_failures_are_this_gate_s_error` drives all three wrappers against a missing root and against a patched `git_command.run_git` raising `TimeoutExpired`; `::test_a_git_that_ran_and_said_no_is_still_an_answer_not_an_error` keeps a missing revision and an absent merge base as `False` / `None`. | `BaseResolutionTests` | mcp/tests/test_diff_coverage.py:81-254; mcp/tests/test_diff_coverage.py:221-255 |
| `[tool.coverage.run] branch = true`, without which this step refuses to score. | "branch = true" | pyproject.toml:68-70 |
| The full hook tier that runs the wrapper, and the note telling leaf branches to export `AR_GATE_DIFF_BASE`. | `AR_GATE_DIFF_BASE` | CONTRIBUTING.md:112-112 |
| CI checkout uses `fetch-depth: 0` so a merge base exists; a shallow clone would silently degrade this step to the empty tree. | "fetch-depth: 0" | .github/workflows/quality-checks.yml:34-34 |
| The contributor-facing statement of the floor and why it is 100%. | `### The coverage floor is on your diff, not on the tree` | CONTRIBUTING.md:95-131 |
| `run_git` — the runner `_git` calls — strips `GIT_REPOSITORY_SELECTOR_ENV`, keeps stdin on `DEVNULL`, and bounds every call with the local/remote/metadata timeout classes. | `run_git`; `GIT_REPOSITORY_SELECTOR_ENV` | mcp/src/agents_remember/kernel/git_command.py:33-42; mcp/src/agents_remember/kernel/git_command.py:85-151 |
| `QualityGateGitTests` points `GIT_DIR` at a decoy repository and proves `diff_coverage.run_git` still reads the repository it was handed, and that a non-repository and an unrunnable git both surface as `DiffScopeError`. | `QualityGateGitTests` | mcp/tests/test_git_command.py:328-390 |

## Update History

- 2026-08-04T18:07+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 8 citation rows with exact anchors (definition identifiers, quoted config literals, and the exact-level CONTRIBUTING heading) and ledger-verified ranges across crap_calculator, test_diff_coverage, pyproject, _gate.sh, quality-checks.yml, CONTRIBUTING, git_command, and test_git_command; the fixer normalized the CONTRIBUTING section extent. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-31T21:20+02:00 — 260731-EFA-L3 curator (second pass): the fix worker moved the
  `OSError`/`SubprocessError` → `DiffScopeError` conversion out of `run_git` and **into `_git`**
  after the entry below was written, so the card's account of the failure split was wrong.
  Corrected three claims in "Every Git Call Goes Through `_git`": (1) the quoted `_git` body no
  longer matched the source — it now carries the `try` / `except (OSError, subprocess.SubprocessError)`
  that raises `DiffScopeError`; (2) "four git call sites" was wrong — `_git` has exactly three
  callers (`run_git`, `revision_exists`, `merge_base`), with `changed_python_lines` /
  `state_for_empty_diff` reaching it through `run_git`; (3) the card credited `run_git` with both
  failure halves, when `run_git` now retains only the `completed.returncode != 0` branch and the
  "could not run" half is shared by all three. Recorded why it moved: the shared runner bounds
  every call at `GIT_LOCAL_TIMEOUT_SECONDS` = 300s where the old inline call had no timeout, and
  passes `cwd=repo_root`, so a missing `project_root` raises `FileNotFoundError` before git starts
  where the old `git -C <path>` merely exited non-zero — both would have escaped `revision_exists`
  and `merge_base` untyped. Added the matching invariant and named the two new
  `BaseResolutionTests` regressions in the `test_diff_coverage.py` reference row. No citation
  ranges to repair: this card's reference table carries source paths only.

- 2026-07-31T20:48+02:00 — 260731-EFA-L3 curator: this module's git calls were consolidated onto
  the package's one runner and the card said nothing about them. Added "Every Git Call Goes Through
  `_git`, On The Package's One Runner": the new private `_git` helper keeps `-c core.quotePath=false`
  (this gate's own requirement — without it `parse_unified_diff` cannot see non-ASCII paths) and
  delegates the spawn to `kernel.git_command.run_git`, which strips the `GIT_DIR`-family selectors.
  That matters most here: the full tier runs from `pre-push`, where git exports `GIT_DIR`, so an
  unstripped `git diff` would have scored a different repository than the one being pushed. Also
  recorded the failure conversion (`check=True`/`CalledProcessError` → explicit `returncode != 0`
  plus `OSError`/`subprocess.SubprocessError`, which now includes the runner's timeout) and why
  `revision_exists`/`merge_base` still read `returncode` directly. Added four invariants and the
  `git_command.py` / `test_git_command.py` reference rows. No citation ranges in this card point
  into a file this leaf changed — its reference table carries source paths only.

- 2026-07-31T16:10+02:00 — Created for 260731-EFA-L2 (requirement L2-R7). Records the new
  binding coverage gate: the changed-lines floor of 100% with the measured derivation that
  rules out 80/85/90/95, the unit definition (statements plus branch arcs leaving a changed
  line), the printed base-resolution chain ending at the empty tree, the four reported
  states, and the named-findings report with no exemption list. Verification metadata is
  pinned to the leaf's reformat commit until closeout stamps the code commit.
