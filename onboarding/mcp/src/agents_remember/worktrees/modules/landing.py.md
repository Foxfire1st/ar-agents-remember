# mcp/src/agents_remember/worktrees/modules/landing.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Best-effort observation of the **successful-landing arc** for the Engine Room (slice 5h; hardened
5l P2): the remote/PR refs a worktree retires into when it lands cleanly — `origin/<feat>`,
`origin/<base>` (the landing target), the PR, and the external memory source branch. When `landing_refs(contract)`
returns a list it becomes the status payload's `landing` block, and `reducer._engine_process`
composes that onto `EngineProcessNode.landing`.

Two callers reach the probe, and neither is the projection tick: the interactive `status_payload`
cit:(["def status_payload", "landing_refs(contract)"], mcp/src/agents_remember/worktrees/modules/guidance.py:541-543), and `serving/projections/landing_state.LandingStateRefresher`, which holds it as
`observe: LandingObserver = landing_refs` and runs its sweep loop with the default
`LANDING_REFRESH_INTERVAL_SECONDS = 30.0` and `LANDING_REFRESH_CONCURRENCY = 4`. In serving, page interest and the per-contract due schedule decide which contracts are probed. The
recurring projection reads retained landing observations or renders `unobserved_landing_refs`;
it does not call these remote/PR probes inline. So the arc still follows a **real remote landing** live
(push → PR open → PR merge) without a milestone hook, but off the tick and bounded.

## Code Commentary

Within one landing sweep, identical repository/ref ls-remote observations share their answers, including expected probe failures. Unexpected computation exceptions escape to the observation boundary, and a waiter has its own bounded timeout. The next sweep probes afresh because a remote is mutable. This bounds duplicate work without making the remote an immutable object or changing exact participant/PR/ref semantics.

`landing_refs(contract)` returns `None` until the worktree reaches the **landing window**
(`landing_active` — closeout-completed, or integration started, or cleanup begun; its callers
`landing_refs` and `unobserved_landing_refs` share this gate) — there is nothing
pushed/merged/carried to observe before that, and the gate keeps the polling status payload
network-free for the whole build phase. Once active it returns one dict per participant, each with a
`kind`/`label`/`state` and an honest `factState`.

The branch and PR probes are **timeout-bounded at `_PROBE_TIMEOUT_SECONDS = 8`**
cit:([`_PROBE_TIMEOUT_SECONDS`], mcp/src/agents_remember/worktrees/modules/landing.py:36-36). Both
run with `stdin=subprocess.DEVNULL` so a subprocess never inherits the stdio MCP transport's
protocol pipe (GitHub #49), and both run without the `GIT_DIR` family in their environment. Only the route differs:

The branch probe calls the shared `kernel.git_command.run_git` runner cit:([`_probe_remote_branch`], mcp/src/agents_remember/worktrees/modules/landing.py:174-190). The shared runner's
safe-directory and environment-isolation behavior is captured in the runner table below. It passes
`GitRunnerOptions(timeout=_PROBE_TIMEOUT_SECONDS)` **explicitly** cit:([`_probe_remote_branch`], mcp/src/agents_remember/worktrees/modules/landing.py:174-190), which is the load-bearing part: `run_git`'s default
is the local class `GIT_LOCAL_TIMEOUT_SECONDS = 300`, and this probe sits on the
interactive/refresher path where 8 seconds is the whole point.

The gh probe still inlines its own `subprocess.run` — `gh` is not git, so it cannot go through
`run_git` — with the same 8-second bound, DEVNULL stdin, and scrubbed environment cit:(["def _pr_for", "result = subprocess.run(", "\"gh\"", "subprocess.DEVNULL", "text=True", "env=git_environment()"], mcp/src/agents_remember/worktrees/modules/landing.py:193-193; mcp/src/agents_remember/worktrees/modules/landing.py:204-206; mcp/src/agents_remember/worktrees/modules/landing.py:224-228). That is not defensive symmetry: `gh` resolves *which
repository it is talking about* through git, so an inherited `GIT_DIR` would have it list another
repository's pull requests under this worktree's branch name, and the landing arc would report a PR
belonging to a repository the worktree never touched. `cwd=repo` does not outrank the selectors for
`gh` any more than it does for git. `"gh"` is the package's **only** non-git spawn that reads a
repository (the single occurrence in `src/`, L206), which is why it takes the same scrubbed
environment by hand. The current `_pr_for` source explicitly passes `env=git_environment()`; the branch probe
uses `run_git` with the same selector scrub.

- `_remote_branch(repo, branch)` runs `git ls-remote --heads origin <branch>` (reliable). It returns
  `("observed", sha)` when the branch is on origin, `("observed", None)` when origin was reachable
  but the branch is not pushed yet (→ `planned`), and `("missing", None)` when the probe could not
  run (offline / no origin). `_branch_ref` turns that into a `pushed` / `planned` / `unknown` state.
The branch probe queries the remote directly with `ls-remote --heads`, so **no `git fetch`** is needed.
- cit:([`_pr_for`], mcp/src/agents_remember/worktrees/modules/landing.py:193-250) runs a best-effort `gh pr list --head <head> --state all --json …`
  — the package's only `gh` use. `None` (gh absent/unauthed/errored) → the PR ref renders `unknown` with `factState: missing`;
  `{}` (gh ran, no PR) → `absent` with `factState: observed` when the recorded strategy is nonempty and not `pr`, otherwise `planned`; populated results retain the PR's number/state/url/base **plus gh's own
  `createdAt`/`mergedAt`** (slice 5l P2; `mergedAt` is JSON `null` on an open PR so it is coerced via
  `or ""`).

`_main_ref(repo, pr, target)` probes the landing target `origin/<base>` **directly** via
`_remote_branch` — `base` is the PR's `baseRefName` when present, otherwise the supplied contract source branch, otherwise `main`. So
`origin/<base>` is observable across the **whole** landing window: before any PR, and even when `gh`
is absent (the probe is `ls-remote`, independent of gh). Its `state` tracks whether **this** work
landed — `merged` once the PR is merged, else `planned` when origin is reachable (a pre-merge target
reads honestly as `planned`, never a misleading `tip`/done), else `unknown`; the current target tip
rides along in `detail`. `_pr_ref` emits only the `pr` ref.

`_pr_ref(pr, contract)` renders the PR participant and (slice 5l P2) adds an `at` field = gh's own milestone
time — `mergedAt` once merged, else `createdAt` — so the open→merged transition carries its timing;
`at` is omitted for the gh-absent / no-PR placeholders; populated PR rows carry the milestone time or explicit None.

`landing_refs` hoists the single `_pr_for` lookup (the PR drives both its own ref and the origin-main
merged state) and then appends `_main_ref(...)` followed by `_pr_ref(...)`. Both the feature-branch probe and the PR head lookup use `contract.code_work_branch`; the target passed to `_main_ref` is `contract.code_source_branch`.

An unobserved participant has state `unknown` and `factState: missing`; an observed absent branch is `planned`, while an observed PR absence distinguishes the recorded route — so the cockpit never animates a planned PR as a live one. For a mid-series worktree whose work branch is pushed and whose landing strategy is not yet recorded, a successful empty PR lookup shows the work branch `pushed`, `origin/<base>` `planned` (observed directly), and the PR `planned`.

### Observer ownership

The existing landing probe remains the bounded remote observation primitive, but recurring projection does not call it inline. The background observer retains its planned/missing failure semantics and exact contract identity while interactive commands continue to request fresh facts.

## Invariants And Boundaries

- **Best-effort + honest:** branch/PR facts distinguish missing/unknown from observed/planned; planned is a participant state for an observed not-yet outcome, not a factState value. `_main_ref` falls back to `main` only when neither an observed PR base nor the supplied contract source names a target. The projection's `_safe_status_payload` returns `None` for unavailable local status; a landing-snapshot merge failure keeps that local status.
- **Network-gated:** `landing_refs` returns `None` outside the landing window, so the build-phase
  `worktree_status` poll stays network-free (unlike the always-fetch-free `freshness`, this path
  *does* hit the network, hence the gate).
- **Bounded:** every probe carries an explicit 8-second timeout and `stdin=DEVNULL` (the #49
  guard). The branch probe calls `kernel.git_command.run_git` with
  `GitRunnerOptions(timeout=_PROBE_TIMEOUT_SECONDS)` rather than inheriting its 300-second local default. A stall stays inside the honesty rule: `run_git` raises
  `subprocess.TimeoutExpired`, which is a `subprocess.SubprocessError`, so the existing
  `except (OSError, subprocess.SubprocessError)` in the branch probe turns it into `("missing", None)` instead of letting it escape into `status_payload`.
- **Every spawn here is repository-scoped by argument, never by environment:** both probe implementations run
  with the `GIT_DIR` family stripped — the branch probe via `run_git`, the `gh` probe via an explicit
  `env=git_environment()`. A future probe added to this module inherits nothing: it must either go
  through `run_git` or pass `env=git_environment()` itself.
- **Additive contract:** the emitted `landing` list maps 1:1 onto `LandingRefNode`; absent ⇒
  `EngineProcessNode.landing` defaults to `[]`.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References


- `status_payload` calls `landing_refs` and emits its result as the `landing` block. [1]


- The `LandingRefNode` schema the emitted dicts map onto + the `EngineProcessNode.landing` field. [2]
- The reducer composer that reads `status["landing"]` into the node. [3]


- The bounded off-tick caller: `LandingStateRefresher(observe=landing_refs)`, and the `unobserved_landing_refs` shape the recurring projection renders instead.  Anchor: "observe: LandingObserver = landing_refs" [5]


- The remote-branch probe passes its timeout to the shared Git runner. The pull-request probe passes the same timeout and scrubbed environment to its own gh process. [4]
