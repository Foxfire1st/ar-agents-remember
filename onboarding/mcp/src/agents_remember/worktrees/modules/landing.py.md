# mcp/src/agents_remember/worktrees/modules/landing.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/modules/landing.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-14T17:20+02:00|
| lastVerifiedCommitHash | `47570cd827428c171613c8cb01e01f0b1cb26f73` |
| lastVerifiedCommitDate | 2026-09-20T01:58:41+02:00|
| governingOverview      | `overview.md`                              |

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

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `status_payload` calls `landing_refs` and emits its result as the `landing` block. | `status_payload`; `_status_payload_with_landing`; "def _status_payload_with_landing" | mcp/src/agents_remember/worktrees/modules/guidance.py:563-573; mcp/src/agents_remember/worktrees/modules/guidance.py:501-509 |
| The `LandingRefNode` schema the emitted dicts map onto + the `EngineProcessNode.landing` field. | `LandingRefNode` | mcp/src/agents_remember/observer/projection.py:956-978 |
| The reducer composer that reads `status["landing"]` into the node. | "landing=[LandingRefNode" | mcp/src/agents_remember/observer/reducer_impl/_processes.py:304 |
| The shared `run_git` runner supplies the `safe.directory` override, DEVNULL stdin, the `GIT_DIR`-family scrub, and its local timeout default; both probes here override that default through `GitRunnerOptions(timeout=...)`. | `GIT_REPOSITORY_SELECTOR_ENV`; `GIT_LOCAL_TIMEOUT_SECONDS`; `git_environment`; `run_git` | mcp/src/agents_remember/kernel/git_command.py:149-213; mcp/src/agents_remember/kernel/git_command.py:93 |
| The bounded off-tick caller: `LandingStateRefresher(observe=landing_refs)`, and the `unobserved_landing_refs` shape the recurring projection renders instead. | `LandingStateRefresher`; "observe: LandingObserver = landing_refs" | mcp/src/agents_remember/serving/projections/landing_state.py:148-352 |

## Update History
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 2 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `landing.py.md:26` (status_payload, landing_refs(contract)) — re-read the claim against the current source: the construct moved, and the range was re-derived from its real extent in the file the claim already cites; `landing.py.md:140` (status_payload, _status_payload_with_landing) — re-read the claim against the current source: the construct moved, and the range was re-derived from its real extent in the file the claim already cites.
- 2026-09-18T19:51:00+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the three enforced `citation_anchor_absent_from_range` rows in this document** (one table row, three anchors). The row cited `guidance.py:493-495` and `guidance.py:431-483` — the tail of `base_freshness` and part of `_pre_integration_phase` — for `status_payload` and `_status_payload_with_landing`; the definitions this leaf's moves left in the file sit at `563-565` and `501-503`, so the row's two source cells now cite those. The claim, all three anchors and the rest of the row are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "def status_payload"; "landing_refs(contract)" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:563-563; mcp/src/agents_remember/worktrees/modules/guidance.py:565-565. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): added mcp/src/agents_remember/worktrees/modules/guidance.py:493 to the row 136 of this card as the citation for `status_payload`: no cited file carried the construct, and the checker named line(s) [493] in this file as its live location; added mcp/src/agents_remember/worktrees/modules/guidance.py:495 to the row 140 of this card as the citation for `landing_refs`: no cited file carried the construct, and the checker named line(s) [495] in this file as its live location; re-pointed `GIT_LOCAL_TIMEOUT_SECONDS` in the row 139 of this card from mcp/src/agents_remember/kernel/git_command.py:55-64 to mcp/src/agents_remember/kernel/git_command.py:93, the extent of the construct the claim is about (the checker named line(s) [93, 128, 229] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `status_payload` in the row 136 of this card from mcp/src/agents_remember/worktrees/modules/guidance.py:431-433 to mcp/src/agents_remember/worktrees/modules/guidance.py:493-494, the extent of the construct the claim is about (the checker named line(s) [493] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `_status_payload_with_landing` in the row 136 of this card from mcp/src/agents_remember/worktrees/modules/guidance.py:493-494 to mcp/src/agents_remember/worktrees/modules/guidance.py:431-433, the extent of the construct the claim is about (the checker named line(s) [431, 490, 495] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `status_payload` in the row 136 of this card from mcp/src/agents_remember/worktrees/modules/guidance.py:495 to mcp/src/agents_remember/worktrees/modules/guidance.py:493-494, the extent of the construct the claim is about (the checker named line(s) [493] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `status_payload` in the row 136 of this card to mcp/src/agents_remember/worktrees/modules/guidance.py:493-494, the extent the claim is about (the checker named line(s) [493] as the live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): clamped mcp/src/agents_remember/worktrees/modules/guidance.py:496 to mcp/src/agents_remember/worktrees/modules/guidance.py:495, the range the cited construct now occupies
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (residue citation pass): re-derived the source
  range of 4 claim(s) whose anchor no longer sat in its cited range and normalised 3 further
  range(s) from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`). No claim wording was changed to fit an anchor; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base `7317108b`): `_remote_branch` and `_default_branch` now pass their probe bound as `GitRunnerOptions(timeout=_PROBE_TIMEOUT_SECONDS)`, the timeout keyword having become a field of the runner's one options object; the 8-second class each probe names is unchanged and still overrides the runner's 300s local default. Re-derived the anchors the migration shifted (`_remote_branch` 47-66 → 47-68, `_default_branch` 69-90 → 71-94, `_pr_for` 93-150 → 97-154, the `gh` occurrence L106 → L110, the `landing_active` caller lines L237/L268 → L241/L272, and the runner row `33-42; 70-70; 76-82; 85-151` → `55-64; 92-92; 140-146; 149-213`).
- 2026-09-13T14:32+02:00 — Curator citation repoint after the contract-scoped atomic-series activation re-keying shifted `modules/guidance.py`: `def status_payload` now resolves at `guidance.py:502-502`, the `landing_refs(contract)` call at `guidance.py:504-504`, and `_status_payload_with_landing` at `guidance.py:440-441`, so both affected rows were rebound. Claim wording unchanged.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: "def status_payload", "landing_refs(contract)", `_status_payload_with_landing`, `status_payload` repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:410-462, mcp/src/agents_remember/worktrees/modules/guidance.py:472-472, mcp/src/agents_remember/worktrees/modules/guidance.py:472-474, mcp/src/agents_remember/worktrees/modules/guidance.py:474-474. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-04T14:41:21+02:00 — 260731-EFA-L6 S18-B01 closing same-reviewer correction: added exact call and gh-argv anchors and rebound the gh subprocess behavior to its complete call-and-arguments source extent under the adversarial verdict, then the exact scoped fixer/check passed.
- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 8 citation items; scoped citation check now passes.
- 2026-07-31T21:34+02:00 — 260731-EFA-L3 curator: the earlier L3 entry below described the
  `GIT_DIR`-family scrub as something only the two git probes gained, and said the `gh` probe merely
  "still inlines its own `subprocess.run` … with the same 8-second bound and DEVNULL stdin". `_pr_for`
  now also passes `env=git_environment()` cit:(["env=git_environment()"], mcp/src/agents_remember/worktrees/modules/landing.py:128-128), so all three probes run scrubbed. Rewrote that
  paragraph to say so and to give the reason from the code's own comment — `gh` resolves the
  repository *through* git, so an inherited `GIT_DIR` would have it list another repository's PRs
  under this branch's name — plus the fact that the package-wide AST sweep cannot cover it
  (`_spawns_git` matches `PurePosixPath(head).name == "git"`, and
  `test_a_program_that_merely_starts_with_git_is_not_git` pins `/usr/bin/gh` as a non-offender), so
  `test_landing.py::test_the_gh_probe_does_not_inherit_the_repository_selectors` asserts it directly.
  Added the matching invariant. Two further claims were false against current code and were fixed:
  the gate was named `_landing_active` but the function is `landing_active` (L34-L44, no underscore,
  callers L237/L268), and Purpose still said the probe "re-fires every projector tick (~1s)" — it
  does not, `landing_refs` is reached only by the interactive `status_payload` cit:(["def status_payload"], mcp/src/agents_remember/worktrees/modules/guidance.py:503-503) and by `LandingStateRefresher(observe=landing_refs)` at
  `LANDING_REFRESH_INTERVAL_SECONDS = 30.0`, while the recurring projection renders
  `unobserved_landing_refs`. Corrected "the package's **first** `gh` use" to "only" (one occurrence
  in `src/`, L106). Verified `_PROBE_TIMEOUT_SECONDS = 8` and the DEVNULL/timeout claims still hold
  on all three probes; verified `run_git`'s default is still `GIT_LOCAL_TIMEOUT_SECONDS = 300`.
- 2026-07-31T21:34+02:00 — 260731-EFA-L3 curator: the earlier L3 entry below described the
  `GIT_DIR`-family scrub as something only the two git probes gained, and said the `gh` probe merely
  "still inlines its own `subprocess.run` … with the same 8-second bound and DEVNULL stdin". `_pr_for`
  now also passes `env=git_environment()` cit:(["env=git_environment()"], mcp/src/agents_remember/worktrees/modules/landing.py:128-128), so all three probes run scrubbed. Rewrote that
  paragraph to say so and to give the reason from the code's own comment — `gh` resolves the
  repository *through* git, so an inherited `GIT_DIR` would have it list another repository's PRs
  under this branch's name — plus the fact that the package-wide AST sweep cannot cover it
  (`_spawns_git` matches `PurePosixPath(head).name == "git"`, and
  `test_a_program_that_merely_starts_with_git_is_not_git` pins `/usr/bin/gh` as a non-offender), so
  `test_landing.py::test_the_gh_probe_does_not_inherit_the_repository_selectors` asserts it directly.
  Added the matching invariant. Two further claims were false against current code and were fixed:
  the gate was named `_landing_active` but the function is `landing_active` (L34-L44, no underscore,
  callers L237/L268), and Purpose still said the probe "re-fires every projector tick (~1s)" — it
  does not, `landing_refs` is reached only by the interactive `status_payload` cit:(["def status_payload"], mcp/src/agents_remember/worktrees/modules/guidance.py:503-503) and by `LandingStateRefresher(observe=landing_refs)` at
  `LANDING_REFRESH_INTERVAL_SECONDS = 30.0`, while the recurring projection renders
  `unobserved_landing_refs`. Corrected "the package's **first** `gh` use" to "only" (one occurrence
  in `src/`, L106). Verified `_PROBE_TIMEOUT_SECONDS = 8` and the DEVNULL/timeout claims still hold
  on all three probes; verified `run_git`'s default is still `GIT_LOCAL_TIMEOUT_SECONDS = 300`.
- 2026-07-31T20:52+02:00 — 260731-EFA-L3 curator: `_remote_branch` and `_default_branch` no longer
  inline `subprocess.run([...])`; both call `kernel.git_command.run_git(repo, [...],
  timeout=_PROBE_TIMEOUT_SECONDS)`. The old commentary ("Three git/gh probes ... run with
  `stdin=subprocess.DEVNULL`") described a subprocess call this file no longer makes, so it now
  names the shared runner, the `GIT_DIR`-family scrub the probes gained, and why the explicit
  `timeout=` matters (`run_git` defaults to `GIT_LOCAL_TIMEOUT_SECONDS = 300`; this probe needs 8).
  The Bounded invariant now records that `subprocess.TimeoutExpired` is a `SubprocessError` and so
  is already absorbed by both probes' `except (OSError, subprocess.SubprocessError)` into
  `missing`/`"main"`. Re-pointed the runner reference row from `modules/git.py` (which no longer
  defines a runner to mirror) to `kernel/git_command.py`. Verification metadata pinned until
  closeout stamps the L3 commit.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: retained landing probe semantics for bounded background observation and repaired the landing-ref commentary; unavailable facts remain planned/missing rather than invented.

- 2026-06-21T05:30+02:00 — Slice 5l P2 (landing-arc probe hardening, so the dashboard follows a REAL remote landing): added `_default_branch` (origin default via `git ls-remote --symref origin HEAD`, fallback `"main"`) and `_main_ref` — the protected target `origin/<base>` is now probed **directly** via `_remote_branch` (base = PR `baseRefName` or `_default_branch`), visible across the whole landing window before any PR and even when `gh` is absent, its `state` tracking whether THIS work landed (`merged`/`planned`/`unknown`, tip in `detail`). This replaces the PR-base-derived origin-main that used to live in `_pr_ref` (now `pr`-only). `_pr_for` requests + returns `createdAt`/`mergedAt`, and `_pr_ref` adds an `at` = gh's milestone time (mergedAt once merged, else createdAt). `landing_refs` hoists the single `_pr_for` lookup then appends `_main_ref` + `_pr_ref`. Module docstring notes the per-tick (~1s) re-probe needs no milestone hook. Verification metadata pinned until closeout stamps the 05l-P2 code commit.
- 2026-06-18T08:51+02:00 — Created for slice 5h H1: best-effort successful-landing arc observation (`git ls-remote` branch tips + best-effort `gh` PR state, timeout-bounded, `stdin=DEVNULL`, gated to the landing window, honest `factState`). Verification metadata pinned until closeout stamps the 5h code commit.
