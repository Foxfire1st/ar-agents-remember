# mcp/test_support/agents_remember_test_support/code_quality/diff_coverage.py

## Governing Overview

[Quality support overview](overview.md)

## Purpose

Reports changed statements and branch arcs from the existing Coverage.py JSON. The same
measurement feeds aggregate coverage, CRAP and the changed-line report; this module does not run
pytest. Coverage percentages are diagnostic, with no delivery floor or required extra tests.

## Code Commentary

### Diagnostic Policy

`render` prints the resolved base, state, numerator/denominator, uncovered lines and untaken
branches. `DEFAULT_DIFF_COVERAGE_FLOOR` and `--diff-floor` no longer exist. A measured zero-percent
result remains useful evidence and does not fail delivery. Missing or malformed reports and Git
execution errors remain failures; this change does not turn absent evidence into a pass.

### The Unit Being Counted

A *unit* is a measurable statement **or a branch arc leaving a changed line** — Coverage.py's
own accounting, and the same one `crap_calculator` uses. `tally_file` intersects the changed
line set with `executed_lines`, `missing_lines`, and the arcs whose **source** line is
changed (`executed_branches`, `missing_branches`). A changed line carrying no statement — a
comment, a blank, a continuation — contributes nothing at all rather than counting as
covered.

Coverage-file lookup normalizes path identity with `casefold()` after repository-relative
canonicalization. This preserves exact reporting paths while preventing Windows path casing from
turning measured files into false unmeasured findings.

Because it reuses `crap_calculator.load_coverage_by_path`, the branch requirement is
inherited: a coverage report produced without `[tool.coverage.run] branch = true` is
**refused**, not silently degraded to statements.

### Base Resolution Is Printed, Never Assumed

A gate that silently picks its own comparison point can be made to certify nothing by
picking the wrong one, so `BaseResolution` carries both the revision and *how it was
chosen*, and `render` prints both on every run in the diagnostic output.

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
the report describes all of it. That is deliberately the strict reading of "nothing to
compare against"; it is **not** a fourth state and it is not a skip.

### Four Reported States, None Of Which Pass Silently

| State | Meaning | Reporting |
| --- | --- | --- |
| `measured` | Changed Python lines sit inside the measured packages. | every uncovered line and untaken arc is **named** |
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
says which line has never run, which is the only actionable form. These observations support behavioral judgment; an uncovered unit does not itself require a new
test or deletion of the source.
### Diff Parsing

`changed_python_lines` runs `git diff --unified=0 --no-color --no-ext-diff
--diff-filter=ACMR <base> -- '*.py'` — **base-to-working-tree, no second revision**, because
the working tree is what the suite just imported and measured, so the post-image line
numbers index the same content the coverage report describes.

`parse_unified_diff` is split out from the git call on purpose: its two guards (a `+++`
header that is not `+++ b/<path>`, and a `@@` line the `HUNK` pattern does not match) are
malformed-input refusals. Their presence is an implementation fact, not a claim that the
retired parser edge suite remains in the current test population.

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
the current wrapper return-code handling preserves.

## Invariants And Boundaries

- Percentage observations cannot fail delivery; report execution and integrity errors can.
- Statement-plus-arc accounting and the branch-measurement requirement remain unchanged.
- The base is always reported; an absent merge base uses the empty tree rather than a silent skip.
- All Git calls use `_git` and the canonical runner, preserving selector sanitization, bounded
  calls and `core.quotePath=false` for non-ASCII paths.
- Git startup/timeouts become `DiffScopeError`. A negative revision lookup remains an answer;
  a failed diff is never represented as an empty successful diff.
- Unmeasured files are visible and are not described as covered.

## Evidence

### Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.

- Canonical runner and typed startup/timeout failures [1]
- Explicit and inferred comparison-base resolution [2]
- Changed statements and source-line branch arcs [3]
- Measured/nonmeasurable states [4]
- All findings remain diagnostic without a floor [5]
