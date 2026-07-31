# mcp/src/agents_remember/code_quality/diff_coverage.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/code_quality/diff_coverage.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T16:10+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The wrapper's `run_diff_coverage` step, the `--diff-base`/`--diff-floor` flags, and the single pytest coverage run this module reads. | [check.py](agents-remember/mcp/src/agents_remember/code_quality/check.py) |
| `load_coverage_by_path`, `FileCoverage`, and the refusal of a report without branch data, all reused here. | [crap_calculator.py](agents-remember/mcp/src/agents_remember/code_quality/crap_calculator.py) |
| Unit tests for base resolution order, the four states, the malformed-diff guards, and the named-findings report. | [test_diff_coverage.py](agents-remember/mcp/tests/test_diff_coverage.py) |
| `[tool.coverage.run] branch = true`, without which this step refuses to score. | [pyproject.toml](agents-remember/pyproject.toml) |
| The full hook tier that runs the wrapper, and the note telling leaf branches to export `AR_GATE_DIFF_BASE`. | [_gate.sh](agents-remember/.githooks/_gate.sh) |
| CI checkout uses `fetch-depth: 0` so a merge base exists; a shallow clone would silently degrade this step to the empty tree. | [quality-checks.yml](agents-remember/.github/workflows/quality-checks.yml) |
| The contributor-facing statement of the floor and why it is 100%. | [CONTRIBUTING.md](agents-remember/CONTRIBUTING.md) |

## Update History

- 2026-07-31T16:10+02:00 — Created for 260731-EFA-L2 (requirement L2-R7). Records the new
  binding coverage gate: the changed-lines floor of 100% with the measured derivation that
  rules out 80/85/90/95, the unit definition (statements plus branch arcs leaving a changed
  line), the printed base-resolution chain ending at the empty tree, the four reported
  states, and the named-findings report with no exemption list. Verification metadata is
  pinned to the leaf's reformat commit until closeout stamps the code commit.
