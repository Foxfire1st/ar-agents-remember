# mcp/tests/test_diff_coverage.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_diff_coverage.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural suite for `agents_remember.code_quality.diff_coverage` — the **100% per-diff
coverage floor** this leaf added. Every statement and branch arc on a changed line must be
exercised, and the failure names each uncovered line rather than reporting a percentage.

## The Method That Matters

Every test drives a **real throwaway git repository** rather than a stubbed diff. That is
deliberate and must not be undone: the gate's whole job is to read what git says changed,
and a fake `git diff` string proves only that the parser agrees with whoever wrote the
fixture — not that it agrees with git's hunk headers for an added file, a one-line
deletion, a rename, or a change that exists only in the working tree.

Module helpers: `git()`, `write()`, `coverage_report()` (a Coverage.py JSON report shaped
exactly like the wrapper's), and `seeded_repository()` (one committed module plus the
commit it was committed in).

There is exactly one patch in the file, and it is not a stubbed diff: the wrapper-agreement test
patches `diff_coverage.git_command.run_git` to raise `subprocess.TimeoutExpired`, because a git
that hangs for 300 seconds cannot be produced from a real repository inside a unit test. Its
other half — a missing project root — still uses the real runner.

## Code Commentary

### `BaseResolutionTests` — which commit "changed" is measured against

The precedence ladder, each rung tested: explicit base → `AR_GATE_DIFF_BASE` → the GitHub
Actions pull-request base → the configured upstream → the default branch → the empty tree.
An unknown explicit base is an **error, not a silent fallback**; a candidate with no shared
history is skipped rather than used; a first commit with no merge base compares against the
empty tree; a broken git invocation raises rather than reporting "nothing changed" (the
failure mode that would silently disable the floor).

The class also pins the seam between the module's three git wrappers, now that all of them go
through one `_git` on `kernel.git_command.run_git`:

- `test_the_three_git_wrappers_agree_on_which_failures_are_this_gate_s_error` drives `run_git`,
  `revision_exists` and `merge_base` twice over. First against a `project_root` that does not
  exist: the shared runner passes `cwd=`, so `subprocess.run` raises `FileNotFoundError` before
  git is started, where the old `git -C <missing>` merely exited non-zero and two of the three
  answered `False` / `None`. Then with `diff_coverage.git_command.run_git` patched to raise
  `subprocess.TimeoutExpired(cmd=["git"], timeout=300)` — a bound the old inline call did not
  have at all. All six calls must raise `DiffScopeError`. This is the regression against the
  conversion drifting back into `run_git` alone.
- `test_a_git_that_ran_and_said_no_is_still_an_answer_not_an_error` is its counterweight: on a
  real seeded repository, a known revision is `True`, `no-such-revision` is `False`, and
  `merge_base(root, "main")` is the seed commit. The conversion is for failures to *run* git;
  applying it to git's negatives would turn every ordinary "no" into a gate crash.

### `ChangedLineTests` — what counts as a changed line

Added, modified and renamed files all report their **new** line numbers. A pure deletion
contributes no changed lines and a deleted file is not a changed file — there is nothing
left to cover. Working-tree edits count, because they are what coverage measured. A
`/dev/null` post-image drops the file rather than keeping the previous one; an unparsable
hunk header is dropped rather than guessed at; non-Python changes are not collected.

### `MeasurementTests` — the verdict

Statements and branches are scored **together**. An uncovered changed line is *named*, not
only counted; an untaken branch on a changed line is named with its destination, and a
branch that leaves the function is reported as an exit. A changed line carrying no
statement is not counted as covered. A new module the suite never imports scores zero. An
empty diff says so rather than reporting a ratio, and a diff touching only non-Python files
is its own state. Changed Python outside the measured packages is named on every run. The
report states the base and the floor it was judged against. **A report without branch
measurement is refused** — the same fail-loud rule the CRAP reader carries.

### `WrapperIntegrationTests` — the floor as the gate runs it

Same coverage JSON, same exit code. A diff below the floor fails the wrapper; a diff at the
floor passes; a missing `coverage.json` fails instead of passing by default; an unusable
base fails the step rather than the process. The floor runs **inside** the wrapper rather
than beside it, and `--diff-base` / `--diff-floor` are real flags. The default is **zero
uncovered changed lines**.

## Invariants And Boundaries

- Real repositories only. Do not replace them with canned diff text. The single `patch.object`
  in the file stands in for a wedged git, which no real repository can produce on demand.
- Every failure mode fails **closed**: unknown base, broken git, missing coverage JSON, and
  statement-only coverage all fail rather than reporting a clean diff.
- `run_git`, `revision_exists` and `merge_base` must keep answering the same way about what is a
  failure (`DiffScopeError` for a git that could not run) and what is an answer (`False` / `None`
  for a git that ran and said no). Both halves are asserted, because either one alone can be
  satisfied by a change that breaks the other.
- The floor is per-diff, not per-file or per-project; it says nothing about total coverage.
- The floor lives in lifecycle-owned Dagger acceptance, where the closeout or integration
  operation supplies the exact accepted candidate and diff base. Host hooks and GitHub PR
  checks intentionally run deterministic non-test checks only.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test: base resolution, changed-line collection, and the measurement. | `resolve_base`; `changed_python_lines`; `measure` | mcp/src/agents_remember/code_quality/diff_coverage.py:145-173; mcp/src/agents_remember/code_quality/diff_coverage.py:176-197; mcp/src/agents_remember/code_quality/diff_coverage.py:289-317 |
| The wrapper that runs the floor as a step and exposes its two flags. | `run_diff_coverage`; "--diff-base"; "--diff-floor" | mcp/src/agents_remember/code_quality/check.py:59-61; mcp/src/agents_remember/code_quality/check.py:718-725; mcp/src/agents_remember/code_quality/check_cli.py:62-77 |
| The lifecycle-owned Dagger executor that carries the accepted candidate and diff base into the quality graph. | `run_clean_quality` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:112-193 |
| The runner `diff_coverage._git` delegates to, and the source of the 300s `GIT_LOCAL_TIMEOUT_SECONDS` bound and the `cwd=` the wrapper-agreement test exercises. | `GIT_LOCAL_TIMEOUT_SECONDS` | mcp/src/agents_remember/kernel/git_command.py:71-71 |
| The other side of the same seam: `QualityGateGitTests` proves a non-repository and an unrunnable git both reach `DiffScopeError` through `diff_coverage.run_git`, and points `GIT_DIR` at a decoy to prove the gate reads the repository it was handed. | `QualityGateGitTests` | mcp/tests/test_git_command.py:439-507 |

## 260824-PDLS Admission Boundary

Wrapper-integration configurations now receive the real test-session admission capability. Diff
coverage scoring is unchanged; diagnostic evidence cannot reach its measurement input.

## Update History

- 2026-08-24T21:23+02:00 — Added the typed admission precondition to wrapper fixtures.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 1 repeated path:start-end Citation objects from 1 same-claim citation group(s) at card line(s) 111; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 4 citation entries (8 findings); no Tier-3 findings.

- 2026-07-31T21:20+02:00 — 260731-EFA-L3 curator: `BaseResolutionTests` gained two tests this leaf
  and the card did not mention them. Added both to the `BaseResolutionTests` section:
  `test_the_three_git_wrappers_agree_on_which_failures_are_this_gate_s_error` (all three of
  `run_git` / `revision_exists` / `merge_base` must raise `DiffScopeError` for a missing
  `project_root` and for a patched `git_command.run_git` raising
  `TimeoutExpired(cmd=["git"], timeout=300)` — the two failures the shared runner introduced, since
  it passes `cwd=` and bounds every call where the old inline `git -C <path>` did neither) and
  `test_a_git_that_ran_and_said_no_is_still_an_answer_not_an_error` (a missing revision stays
  `False`, an absent merge base stays `None`). Qualified "The Method That Matters": the file is no
  longer patch-free, and the one `patch.object` is named along with why a real repository cannot
  produce a wedged git. Added the matching invariant and reference rows for `kernel/git_command.py`
  and `mcp/tests/test_git_command.py`. No citation ranges in this card — its reference table
  carries source paths only.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  changed-lines coverage floor suite. Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
