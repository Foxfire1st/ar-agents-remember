# mcp/src/agents_remember/worktrees/modules/landing.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/modules/landing.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-21T05:30+02:00                     |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77` |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Best-effort observation of the **successful-landing arc** for the Engine Room (slice 5h; hardened
5l P2): the remote/PR refs a worktree retires into when it lands cleanly — `origin/<feat>`,
`origin/<base>` (the protected target), the PR, and `origin/mem-main`. `status_payload`
(`guidance.py`) calls `landing_refs(contract)` and, when it returns a list, emits it as the status
payload's `landing` block; `reducer._engine_process` composes that onto `EngineProcessNode.landing`.
The probe re-fires every projector tick (~1s), so it follows a **real remote landing** live (push →
PR open → PR merge) without a milestone hook for cadence.

## Code Commentary

`landing_refs(contract)` returns `None` until the worktree reaches the **landing window**
(`_landing_active`: closeout-completed, or integration started, or cleanup begun) — there is nothing
pushed/merged/carried to observe before that, and the gate keeps the polling status payload
network-free for the whole build phase. Once active it returns one dict per participant, each with a
`kind`/`label`/`state` and an honest `factState`.

Three git/gh probes back the observation, all **timeout-bounded** (`_PROBE_TIMEOUT_SECONDS`) and run
with `stdin=subprocess.DEVNULL` so a subprocess never inherits the stdio MCP transport's protocol
pipe (GitHub #49):

- `_remote_branch(repo, branch)` runs `git ls-remote --heads origin <branch>` (reliable). It returns
  `("observed", sha)` when the branch is on origin, `("observed", None)` when origin was reachable
  but the branch is not pushed yet (→ `planned`), and `("missing", None)` when the probe could not
  run (offline / no origin). `_branch_ref` turns that into a `pushed` / `planned` / `unknown` state.
- `_default_branch(repo)` (slice 5l P2) resolves origin's default branch by parsing the
  `ref: refs/heads/<x>` line of `git ls-remote --symref origin HEAD`, falling back to `"main"` on any
  failure. `ls-remote` queries the remote directly, so **no `git fetch`** is needed and a stale local
  tracking ref can never mislead it.
- `_pr_for(repo, head)` runs a best-effort `gh pr list --head <head> --state all --json …` — the
  package's **first** `gh` use. `None` (gh absent/unauthed/errored) → the PR ref renders `missing`;
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
- **Bounded:** both subprocess probes carry an explicit timeout and `stdin=DEVNULL` (the #49 guard).
- **Additive contract:** the emitted `landing` list maps 1:1 onto `LandingRefNode`; absent ⇒
  `EngineProcessNode.landing` defaults to `[]`.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `status_payload` calls `landing_refs` and emits its result as the `landing` block. | [guidance.py](agents-remember/mcp/src/agents_remember/worktrees/modules/guidance.py) |
| The `LandingRefNode` schema the emitted dicts map onto + the `EngineProcessNode.landing` field. | [projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The reducer composer that reads `status["landing"]` into the node. | [reducer.py](agents-remember/mcp/src/agents_remember/observer/reducer.py) |
| The `run_git` subprocess style the git probe mirrors (`safe.directory` + DEVNULL). | [git.py](agents-remember/mcp/src/agents_remember/worktrees/modules/git.py) |

## Update History
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: retained landing probe semantics for bounded background observation and repaired the landing-ref commentary; unavailable facts remain planned/missing rather than invented.

- 2026-06-21T05:30+02:00 — Slice 5l P2 (landing-arc probe hardening, so the dashboard follows a REAL remote landing): added `_default_branch` (origin default via `git ls-remote --symref origin HEAD`, fallback `"main"`) and `_main_ref` — the protected target `origin/<base>` is now probed **directly** via `_remote_branch` (base = PR `baseRefName` or `_default_branch`), visible across the whole landing window before any PR and even when `gh` is absent, its `state` tracking whether THIS work landed (`merged`/`planned`/`unknown`, tip in `detail`). This replaces the PR-base-derived origin-main that used to live in `_pr_ref` (now `pr`-only). `_pr_for` requests + returns `createdAt`/`mergedAt`, and `_pr_ref` adds an `at` = gh's milestone time (mergedAt once merged, else createdAt). `landing_refs` hoists the single `_pr_for` lookup then appends `_main_ref` + `_pr_ref`. Module docstring notes the per-tick (~1s) re-probe needs no milestone hook. Verification metadata pinned until closeout stamps the 05l-P2 code commit.
- 2026-06-18T08:51+02:00 — Created for slice 5h H1: best-effort successful-landing arc observation (`git ls-remote` branch tips + best-effort `gh` PR state, timeout-bounded, `stdin=DEVNULL`, gated to the landing window, honest `factState`). Verification metadata pinned until closeout stamps the 5h code commit.
