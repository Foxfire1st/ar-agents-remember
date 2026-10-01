# mcp/src/agents_remember/worktrees/modules/landing.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Best-effort observation of the **successful-landing arc** for the Engine Room (slice 5h; hardened
5l P2): the remote/PR refs a worktree retires into when it lands cleanly — `origin/<feat>`,
`origin/<base>` (the protected target), the PR, and `origin/mem-main`. When `landing_refs(contract)`
returns a list it becomes the status payload's `landing` block, and `reducer._engine_process`
composes that onto `EngineProcessNode.landing`.

Two callers reach the probe, and neither is the projection tick: the interactive `status_payload`
cit:(["def status_payload", "landing_refs(contract)"], mcp/src/agents_remember/worktrees/modules/guidance.py:571-571; mcp/src/agents_remember/worktrees/modules/guidance.py:573-573), and `observer/landing_state.LandingStateRefresher`, which holds it as
`observe: LandingObserver = landing_refs` and sweeps landing-active contracts on its own
`LANDING_REFRESH_INTERVAL_SECONDS = 30.0` cadence with `LANDING_REFRESH_CONCURRENCY = 4`. The
recurring projection never spawns anything: it renders `unobserved_landing_refs` until the
refresher's latest observation replaces it. So the arc still follows a **real remote landing** live
(push → PR open → PR merge) without a milestone hook, but off the tick and bounded.

## Code Commentary

`landing_refs(contract)` returns `None` until the worktree reaches the **landing window**
(`landing_active`, L34-L44 — closeout-completed, or integration started, or cleanup begun; the name
carries no leading underscore, and its only two callers are `landing_refs` L241 and
`unobserved_landing_refs` L272, so both shapes share one gate) — there is nothing
pushed/merged/carried to observe before that, and the gate keeps the polling status payload
network-free for the whole build phase. Once active it returns one dict per participant, each with a
`kind`/`label`/`state` and an honest `factState`.

Three probes back the observation, all **timeout-bounded at `_PROBE_TIMEOUT_SECONDS = 8`**
cit:([`_PROBE_TIMEOUT_SECONDS`], mcp/src/agents_remember/worktrees/modules/landing.py:31-31), all
run with `stdin=subprocess.DEVNULL` so a subprocess never inherits the stdio MCP transport's
protocol pipe (GitHub #49), and — since 260731-EFA-L3 — **all three** run without the `GIT_DIR`
family in their environment. Only the route differs:

The two git probes call the shared `kernel.git_command.run_git` runner cit:([`_remote_branch`, `_default_branch`], mcp/src/agents_remember/worktrees/modules/landing.py:47-68; mcp/src/agents_remember/worktrees/modules/landing.py:71-94). The shared runner's
safe-directory and environment-isolation behavior is captured in the runner table below. Both pass
`GitRunnerOptions(timeout=_PROBE_TIMEOUT_SECONDS)` **explicitly** cit:([`_remote_branch`, `_default_branch`], mcp/src/agents_remember/worktrees/modules/landing.py:47-68; mcp/src/agents_remember/worktrees/modules/landing.py:71-94), which is the load-bearing part: `run_git`'s default
is the local class `GIT_LOCAL_TIMEOUT_SECONDS = 300`, and this probe sits on the
interactive/refresher path where 8 seconds is the whole point.

The gh probe still inlines its own `subprocess.run` — `gh` is not git, so it cannot go through
`run_git` — with the same 8-second bound, DEVNULL stdin, and scrubbed environment cit:(["def _pr_for", "result = subprocess.run(", "\"gh\"", "subprocess.DEVNULL", "text=True", "env=git_environment()"], mcp/src/agents_remember/worktrees/modules/landing.py:97-97; mcp/src/agents_remember/worktrees/modules/landing.py:108-108; mcp/src/agents_remember/worktrees/modules/landing.py:110-110; mcp/src/agents_remember/worktrees/modules/landing.py:128-129; mcp/src/agents_remember/worktrees/modules/landing.py:131-132). That is not defensive symmetry: `gh` resolves *which
repository it is talking about* through git, so an inherited `GIT_DIR` would have it list another
repository's pull requests under this worktree's branch name, and the landing arc would report a PR
belonging to a repository the worktree never touched. `cwd=repo` does not outrank the selectors for
`gh` any more than it does for git. `"gh"` is the package's **only** non-git spawn that reads a
repository (the single occurrence in `src/`, L110), which is why it takes the same scrubbed
environment by hand. Note that the package-wide AST guard in `mcp/tests/test_git_command.py`
**cannot** see this: `_spawns_git` matches `PurePosixPath(head).name == "git"`, and
`test_a_program_that_merely_starts_with_git_is_not_git` pins `/usr/bin/gh` as a deliberate
non-offender. The property is therefore asserted directly, by
`test_landing.py::test_the_gh_probe_does_not_inherit_the_repository_selectors`, which sets all eight
selectors and requires the captured `gh` call's `env` to be disjoint from them while still carrying
`PATH`.

- `_remote_branch(repo, branch)` runs `git ls-remote --heads origin <branch>` (reliable). It returns
  `("observed", sha)` when the branch is on origin, `("observed", None)` when origin was reachable
  but the branch is not pushed yet (→ `planned`), and `("missing", None)` when the probe could not
  run (offline / no origin). `_branch_ref` turns that into a `pushed` / `planned` / `unknown` state.
- `_default_branch(repo)` (slice 5l P2) resolves origin's default branch by parsing the
  `ref: refs/heads/<x>` line of `git ls-remote --symref origin HEAD`, falling back to `"main"` on any
  failure. `ls-remote` queries the remote directly, so **no `git fetch`** is needed and a stale local
  tracking ref can never mislead it.
- cit:([`_pr_for`], mcp/src/agents_remember/worktrees/modules/landing.py:97-154) runs a best-effort `gh pr list --head <head> --state all --json …`
  — the package's only `gh` use. `None` (gh absent/unauthed/errored) → the PR ref renders `missing`;
  `{}` (gh ran, no PR) → `planned`; otherwise the PR's number/state/url/base **plus gh's own
  `createdAt`/`mergedAt`** (slice 5l P2; `mergedAt` is JSON `null` on an open PR so it is coerced via
  `or ""`).

`_main_ref(repo, pr)` (slice 5l P2) probes the protected target `origin/<base>` **directly** via
`_remote_branch` — `base` is the PR's `baseRefName` when a PR exists, else `_default_branch`. So
`origin/<base>` is observable across the **whole** landing window: before any PR, and even when `gh`
is absent (the probe is `ls-remote`, independent of gh). Its `state` tracks whether **this** work
landed — `merged` once the PR is merged, else `planned` when origin is reachable (a pre-merge target
reads honestly as `planned`, never a misleading `tip`/done), else `unknown`; the current main tip
rides along in `detail`. This **replaces** the old PR-base-derived origin-main that used to live
inside `_pr_ref` (which now emits only the `pr` ref).

`_pr_ref(pr)` renders the PR participant and (slice 5l P2) adds an `at` field = gh's own milestone
time — `mergedAt` once merged, else `createdAt` — so the open→merged transition carries its timing;
`at` is `None` for the gh-absent / no-PR placeholders.

`landing_refs` hoists the single `_pr_for` lookup (the PR drives both its own ref and the origin-main
merged state) and then appends `_main_ref(...)` followed by `_pr_ref(...)`.

Honesty rule (slice 5h; 5f §2): a ref the probe could not observe is `planned` or `missing`, never
invented — so the cockpit never animates a planned PR as a live one. For a mid-series worktree (no PR
opened yet) the live arc honestly shows the source `pushed`, `origin/<base>` `planned` (observed
directly), and the PR `planned`.

### 260712-TRH-L7 observer ownership

The existing landing probe remains the bounded remote observation primitive, but recurring projection no longer calls it inline. The background observer retains its planned/missing failure semantics and exact contract identity while interactive commands continue to request fresh facts.

## Invariants And Boundaries

- **Best-effort + honest:** every probe failure degrades to `factState: "missing"` / `"planned"`;
  nothing is faked. `status_payload`'s `_safe_status_payload` wrapper returns `None` on any crash, so
  a probe error never blanks the rest of the status.
- **Network-gated:** `landing_refs` returns `None` outside the landing window, so the build-phase
  `worktree_status` poll stays network-free (unlike the always-fetch-free `freshness`, this path
  *does* hit the network, hence the gate).
- **Bounded:** every probe carries an explicit 8-second timeout and `stdin=DEVNULL` (the #49
  guard). For the two git probes both now come from `kernel.git_command.run_git` —
  `_remote_branch` and `_default_branch` pass `GitRunnerOptions(timeout=_PROBE_TIMEOUT_SECONDS)`
  rather than inheriting its 300-second local default. A stall stays inside the honesty rule: `run_git` raises
  `subprocess.TimeoutExpired`, which is a `subprocess.SubprocessError`, so the existing
  `except (OSError, subprocess.SubprocessError)` in both probes turns it into `("missing", None)` /
  `"main"` instead of letting it escape into `status_payload`.
- **Every spawn here is repository-scoped by argument, never by environment:** all three probes run
  with the `GIT_DIR` family stripped — the git two via `run_git`, the `gh` one via an explicit
  `env=git_environment()`. A future probe added to this module inherits nothing: it must either go
  through `run_git` or pass `env=git_environment()` itself. Only the git spawns are covered by the
  package-wide AST sweep, so any non-git addition owes a direct test the way the `gh` probe has one.
- **Additive contract:** the emitted `landing` list maps 1:1 onto `LandingRefNode`; absent ⇒
  `EngineProcessNode.landing` defaults to `[]`.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- `status_payload` calls `landing_refs` and emits its result as the `landing` block. [1]
- The `LandingRefNode` schema the emitted dicts map onto + the `EngineProcessNode.landing` field. [2]
- The reducer composer that reads `status["landing"]` into the node. [3]
- The shared `run_git` runner supplies the `safe.directory` override, DEVNULL stdin, the `GIT_DIR`-family scrub, and its local timeout default; both probes here override that default through `GitRunnerOptions(timeout=...)`. [4]
- The bounded off-tick caller: `LandingStateRefresher(observe=landing_refs)`, and the `unobserved_landing_refs` shape the recurring projection renders instead. [5]
