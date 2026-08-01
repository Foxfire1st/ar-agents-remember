# test_landing.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_landing.py`                      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T09:52+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

Tests for the successful-landing arc observation (slice 5h; hardened 5l P2):
`worktrees/modules/landing.py`'s `landing_refs` and `_default_branch`. Pins the honesty contract — a
ref the probe cannot observe is `planned` or `missing`, never invented — plus the 5l-P2 direct
origin-main semantics, without touching the network or requiring `gh` (`subprocess.run` is mocked).
Since 260731-EFA-L3 it also pins the probe's **process boundary**: the `gh` spawn must not inherit
the `GIT_DIR`-family repository selectors. 9 tests across two classes (7 + 2), all green.

## Code Commentary

### Logic

`LandingRefsTests` builds a minimal `WorktreeContract` via the `_contract(tmp, **over)` helper (a real
`TemporaryDirectory` as `code_repo_path`/`memory_repo_path` so `repo.exists()` holds) and patches
`agents_remember.worktrees.modules.landing.subprocess.run`:

- `test_inactive_before_closeout_returns_none` — outside the landing window (`closeout_status`
  not-started, integration not-started, cleanup pending) `landing_refs` returns `None`.
- `test_observed_pushed_branch_and_open_pr` — `ls-remote` returns a sha and `gh` returns an OPEN PR:
  `origin-feat` is `pushed`/`observed`, the PR is `PR #128`/`open` and its `at` is gh's `createdAt`,
  and (5l P2) `origin-main` reads **`planned`** — an open PR has not landed yet, so the target is
  honestly planned, not a misleading `tip`/done.
- `test_merged_pr_marks_origin_main_merged_with_merged_at` (5l P2) — a MERGED PR: the PR `at` is gh's
  `mergedAt`, and `origin-main` is `merged` (this work landed in the protected target).
- `test_origin_main_probed_directly_before_any_pr` (5l P2) — gh returns `[]` (no PR yet) and the
  `--symref` probe resolves `main`: `origin-main` is still present, labelled `origin/main`, `planned`,
  with the tip in `detail` — proving the direct probe, not a PR-derived ref.
- `test_gh_absent_still_shows_origin_main_via_ls_remote` (5l P2) — `ls-remote` returns empty (origin
  reachable, branch not pushed) and `gh` raises `FileNotFoundError`: the PR ref degrades to `missing`,
  but `origin-main` stays `planned`/`observed` — visible independent of gh.
- `test_offline_probe_is_missing` — every probe returns a non-zero exit: `origin-feat`, the PR, **and**
  `origin-main` are all `missing` (origin-main `state` `unknown`).
- `test_the_gh_probe_does_not_inherit_the_repository_selectors` (260731-EFA-L3, L171-L195) — the one
  test here about the process boundary rather than the honesty axis. Its `fake` captures `cmd` **and
  every kwarg** into a list, so the spawn's `env=` can be inspected after the fact; it then sets all
  eight names of the imported `GIT_REPOSITORY_SELECTOR_ENV` at a decoy path via
  `patch.dict(os.environ, …)` and runs `landing_refs`. For each captured call whose argv head is
  `"gh"` it asserts the `env` is a dict, is **disjoint** from the selector tuple, and still contains
  `PATH` — a scrub that removed too much would leave `gh` unrunnable. The
  `self.assertTrue(gh_calls)` before the loop is what keeps it non-vacuous: a per-call loop over an
  empty list passes silently, which is exactly what would happen if the `gh` probe stopped running.
  The defect it encodes: `gh` resolves the repository through git, so an inherited `GIT_DIR` makes it
  list a different repository's PRs under this branch's name, and `cwd=repo` does not outrank that.
  This test is the *only* guard on that spawn — the package-wide AST sweep in `test_git_command.py`
  matches argv heads named `git`, and pins `/usr/bin/gh` as a non-offender.

`DefaultBranchTests` (5l P2) covers `_default_branch` in isolation: `test_parses_head_symref` asserts
the `ref: refs/heads/trunk\tHEAD` line parses to `trunk`, and `test_falls_back_to_main_on_probe_failure`
asserts a non-zero exit falls back to `"main"`.

### Conventions

`_completed(stdout, returncode)` builds a `subprocess.CompletedProcess`; the mocked `run` branches on
`"--symref" in cmd` (the `_default_branch` probe), then `"ls-remote" in cmd` + the branch name, to
answer the git default-branch / origin-main / origin-feat / `gh` probes. The honesty axis
(`observed`/`planned`/`missing`) is asserted via a `kind → ref` dict so order does not matter.

**Why one patch target still covers all three probes.** Every test patches
`agents_remember.worktrees.modules.landing.subprocess.run`, and since 260731-EFA-L3 the two git
probes do not call `subprocess.run` from this module at all — they call
`kernel.git_command.run_git`, which spawns from *its* module. The mocks still intercept them because
`landing.subprocess` and `git_command.subprocess` are the same stdlib module object, so patching the
`run` attribute through either name patches it for both (verified: under that patch,
`git_command.subprocess.run is` the mock). Worth knowing before moving the target to
`landing.run_git`, which would look equivalent and would silently stop covering the kernel runner's
own spawn kwargs. The same aliasing is what lets the new selector test observe a `gh` `env=` at all.

The probes' argv also changed shape without breaking these fixtures: the git spawns now arrive as
`["git", "-c", "safe.directory=<repo>", "ls-remote", …]`. The `fake` dispatchers survived because
every branch is a **membership** test (`"ls-remote" in cmd`, `"--symref" in cmd`) rather than an
index or a prefix match — a positional assertion here would have broken on the inserted `-c` pair.
`git_environment()` is *not* mocked, so the selector test exercises the real scrub against a real
`patch.dict`ed `os.environ`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The landing-arc observation under test (`landing_refs` + `_default_branch`), and the `_pr_for` `env=git_environment()` (L124) the selector test asserts. | [landing.py](agents-remember/mcp/src/agents_remember/worktrees/modules/landing.py) |
| The `WorktreeContract` dataclass the fixture builds. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| `GIT_REPOSITORY_SELECTOR_ENV` (imported, not restated — L21) and the `run_git` whose spawn the shared-module patch also intercepts. | [kernel/git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |
| The package-wide AST sweep that covers git spawns but deliberately not `gh`, which is why the `gh` property is asserted here instead. | [test_git_command.py](agents-remember/mcp/tests/test_git_command.py) |

## Series-Contract Notes

Landing tests continue to pin landing-state projection, with fixture contract paths updated from task-root contracts to leaf `series-contract.md` enclosures.

## Update History

- 2026-08-01T09:52+02:00 — 260731-EFA-L4 curator: No content impact: the whole diff is one
  fixture value, `_contract`'s `"workflow_kind": "chat"` becoming `"chat-task"`, forced by
  `WorkflowKind` narrowing to `Literal["chat-task", "light-task"]`
  (`worktrees/worktree_contract.py` L50). No test, class, mock, probe branch or assertion changed,
  and the card names no workflow kind anywhere — it claims the landing-window gate, the
  observed/planned/missing honesty axis, the origin-main semantics, the `gh` process boundary and
  the shared-`subprocess`-module patching argument, none of which the fixture value reaches.
  Re-verified every citation the L3 curator added against the current 218-line file, since they
  were the only thing here that could have drifted: `GIT_REPOSITORY_SELECTOR_ENV` is still imported
  at L21; `test_the_gh_probe_does_not_inherit_the_repository_selectors` still spans L171-L195
  (decorator at L171, the `assertIn("PATH", environment)` at L195); `_pr_for`'s
  `env=git_environment()` is still `landing.py` L124. Counted the tests: 9 across two classes,
  `LandingRefsTests` 7 + `DefaultBranchTests` 2, matching the Purpose line.

- 2026-07-31T21:38+02:00 — 260731-EFA-L3 curator: the suite gained
  `test_the_gh_probe_does_not_inherit_the_repository_selectors` (L171-L195) and the sidecar had not
  been touched this leaf, so it was stale in three places. "8 tests across two classes" is now 9
  (LandingRefsTests 7 + DefaultBranchTests 2) — counted, then confirmed by running the module: 9
  tests, all ok. Documented the new test (what it captures, the eight selectors from the imported
  `GIT_REPOSITORY_SELECTOR_ENV`, the disjoint-plus-`PATH` assertion, and the `assertTrue(gh_calls)`
  that keeps a per-call loop from passing vacuously). Added the Conventions note that matters most
  now that `_remote_branch`/`_default_branch` route through `kernel.git_command.run_git`: the
  existing `@patch("…landing.subprocess.run")` still intercepts them only because `landing.subprocess`
  and `git_command.subprocess` are the same module object (verified directly — under that patch
  `git_command.subprocess.run is` the mock), and the `fake` dispatchers survived the new
  `-c safe.directory=…` argv prefix only because they are membership tests, not positional ones.
  Added the `kernel/git_command.py` and `test_git_command.py` reference rows. No line ranges in this
  sidecar were wrong because it previously carried none; the ones added above are re-derived from
  the current file.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: landing tests were updated from `contract.md` fixtures to leaf `series-contract.md` fixtures while preserving landing-state expectations. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-21T05:30+02:00 — Slice 5l P2 (landing-arc probe hardening): updated for the new origin-main semantics — an open PR's `origin-main` is now `planned` (not `tip`), a merged PR's is `merged` — and added a direct origin-main probe before any PR (`test_origin_main_probed_directly_before_any_pr`), origin-main still visible when gh is absent (`test_gh_absent_still_shows_origin_main_via_ls_remote`), the merged-PR `at`=mergedAt / open-PR `at`=createdAt assertions, and a `DefaultBranchTests` class for `_default_branch` (symref parse + `"main"` fallback). Now imports `_default_branch`; 8 tests, all green. Verification metadata pinned until closeout stamps the 05l-P2 code commit.
- 2026-06-18T08:51+02:00 — Created for slice 5h H1: tests for `landing_refs` (the landing-window gate + the observed/planned/missing honesty across `ls-remote` + best-effort `gh`, subprocess mocked). Verification metadata pinned until closeout stamps the 5h code commit.
