# test_landing.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_landing.py`                      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-21T05:30+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

Tests for the successful-landing arc observation (slice 5h; hardened 5l P2):
`worktrees/modules/landing.py`'s `landing_refs` and `_default_branch`. Pins the honesty contract — a
ref the probe cannot observe is `planned` or `missing`, never invented — plus the 5l-P2 direct
origin-main semantics, without touching the network or requiring `gh` (`subprocess.run` is mocked).
8 tests across two classes, all green.

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

`DefaultBranchTests` (5l P2) covers `_default_branch` in isolation: `test_parses_head_symref` asserts
the `ref: refs/heads/trunk\tHEAD` line parses to `trunk`, and `test_falls_back_to_main_on_probe_failure`
asserts a non-zero exit falls back to `"main"`.

### Conventions

`_completed(stdout, returncode)` builds a `subprocess.CompletedProcess`; the mocked `run` branches on
`"--symref" in cmd` (the `_default_branch` probe), then `"ls-remote" in cmd` + the branch name, to
answer the git default-branch / origin-main / origin-feat / `gh` probes. The honesty axis
(`observed`/`planned`/`missing`) is asserted via a `kind → ref` dict so order does not matter.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The landing-arc observation under test (`landing_refs` + `_default_branch`). | [landing.py](agents-remember/mcp/src/agents_remember/worktrees/modules/landing.py) |
| The `WorktreeContract` dataclass the fixture builds. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |

## Series-Contract Notes

Landing tests continue to pin landing-state projection, with fixture contract paths updated from task-root contracts to leaf `series-contract.md` enclosures.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: landing tests were updated from `contract.md` fixtures to leaf `series-contract.md` fixtures while preserving landing-state expectations. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-21T05:30+02:00 — Slice 5l P2 (landing-arc probe hardening): updated for the new origin-main semantics — an open PR's `origin-main` is now `planned` (not `tip`), a merged PR's is `merged` — and added a direct origin-main probe before any PR (`test_origin_main_probed_directly_before_any_pr`), origin-main still visible when gh is absent (`test_gh_absent_still_shows_origin_main_via_ls_remote`), the merged-PR `at`=mergedAt / open-PR `at`=createdAt assertions, and a `DefaultBranchTests` class for `_default_branch` (symref parse + `"main"` fallback). Now imports `_default_branch`; 8 tests, all green. Verification metadata pinned until closeout stamps the 05l-P2 code commit.
- 2026-06-18T08:51+02:00 — Created for slice 5h H1: tests for `landing_refs` (the landing-window gate + the observed/planned/missing honesty across `ls-remote` + best-effort `gh`, subprocess mocked). Verification metadata pinned until closeout stamps the 5h code commit.
