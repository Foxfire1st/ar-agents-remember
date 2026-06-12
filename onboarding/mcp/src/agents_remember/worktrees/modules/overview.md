# mcp/src/agents_remember/worktrees/modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `mcp/src/agents_remember/worktrees/modules` |
| lastUpdated            | 2026-06-12T19:06+02:00|
| lastVerifiedCommitHash | `6f1a7e9028d5d4858cf9c645f2448d5395fafc6a` |
| lastVerifiedCommitDate | 2026-06-12T19:52:16+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Purpose

The `worktrees/modules` package contains the extracted implementation modules
behind the `git_worktree_manager.py` facade. It separates Git adapters, lifecycle
status guidance, start preparation, onboarding refresh, closeout, integration,
cleanup, abandon, provider teardown, the typed cross-layer argument DTO, and CLI
argument wiring while preserving the public facade import path.

## Hot Path Summary

- `git.py` owns raw Git subprocess operations and small repository state checks,
  including `committed_changed_paths` (issue #83: the unverified committed
  range — tree-diff `base..HEAD` ∩ `verified..HEAD`) and the
  `commit_text_or_none` baseline reader behind the closeout body gates.
- `guidance.py` renders lifecycle phase and typed next-operation payloads.
- `start.py`, `closeout.py`, `integrate.py`, `cleanup.py`, and `abandon.py`
  own the named `c-09-git-worktree-manager` skill lifecycle operations.
  `start.py` runs a synchronous provider preflight, writes the contract, and
  then launches provider setup in the background (GitHub #53): dry runs stay
  synchronous, real starts return `starting` within seconds, and
  `retry_provider_setup` relaunches a failed/stale setup on an existing
  contract. Before any worktree exists, `start.py` also runs the stale-base
  preflight (GitHub #54): source branches behind/diverged from their upstream
  block the start with `stale_base_choice` recoveries (`fast-forward` /
  `proceed-stale`), and a missing external memory source branch is
  auto-created at the official memory tip using the code branch name as
  template. `cleanup.py`/`abandon.py` refuse to tear down while a live
  (fresh-heartbeat) background setup owns the worktree. `integrate.py` performs the code and
  memory fast-forwards atomically: it pre-validates that both fast-forwards are
  possible before mutating either branch and rolls both heads back on any
  memory-side failure, so integration never lands a half-integrated state.
  `abandon.py` is the discard-without-integration sibling: it reclaims the
  isolated provider stack and removes worktrees/branches without requiring a
  prior integration.
- `sync.py` (GitHub #54 sub-task D) owns `worktree_sync`: the mid-task base
  sync that fetches upstreams, requires the new code tip to be ledger-mapped at
  the official memory tip, merges the source branch into the code work branch
  (abort on conflicts), fast-forwards parked memory (or blocks with
  `memory_sync_choice` recoveries when local memory commits diverge), and
  advances the contract's recorded base pair with a `sync_log` entry.
  `guidance.py`'s fetch-free `freshness` block in `worktree_status` is the
  detection surface that recommends it.
- `provider_async.py` owns the background setup launch (daemon thread), the
  durable `setup-progress.json` under the worktree group's provider-runtime
  dir, the `worktree_status` providers projection (running / stale / ok /
  ready-with-failed-phases / failed + retryArgs), and the live-setup guard.
  The progress file format itself lives in `providers/setup_progress.py`.
- `provider_teardown.py` performs full-reclaim teardown of a worktree's
  isolated provider stack (Docker rm -f containers and networks derived from
  persisted settings, then rmtree the provider-runtime tree, reclaiming
  root-owned data via a docker chown when needed). Used by both `cleanup.py`
  and `abandon.py`.
- `onboarding.py` owns closeout-time onboarding metadata and entity fingerprint
  refresh planning, plus the four-case body/history gates
  (`classify_sidecar_updates` / `require_updated_sidecar_content` for file
  sidecars, `classify_route_overview_updates` /
  `require_updated_route_overview_content` for route overviews): a changed
  source's sidecar — and the route overview that is its **nearest governor** —
  must pair a meaningful body change with a new Update History entry, or carry
  an explicit `No content impact:` / `No route impact:` history entry.
  Ancestor-matched overviews are reported as `stamped_without_body_review`
  rather than gating. Previews and apply payloads surface marker-attested
  documents. Shared metadata/route parsing lives in `kernel/onboarding_doc.py`
  and is re-exported here.
- The closeout worklist (issue #83) is `closeout.py`'s
  `closeout_changed_paths`: working tree ∪ the unverified committed range, so
  transported history (merges, pre-committed slices) gates and stamps like
  hands-on edits. The onboarding plan's two-tier split (`working_paths`) keeps
  missing-sidecar blocking on working-tree paths only; committed-range paths
  without onboarding surface as the non-blocking `unonboarded` report. Body
  gates baseline against `contract_memory_verified_commit` so memory work
  committed before closeout classifies honestly, and payload lists that scale
  with transported history are exposed as count + sample
  (`PATH_SAMPLE_LIMIT`).
- `args.py` defines the frozen `WorktreeArgs` cross-layer DTO that operation
  modules consume in place of `argparse.Namespace`; `from_namespace` builds it
  from partial CLI/controller namespaces with per-field defaults.
- `cli.py` keeps command-line parsing and JSON print adapters out of operation
  modules and converts each parsed namespace into `WorktreeArgs` at the boundary.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The package is imported through the public worktree manager facade. | [git_worktree_manager.py](agents-remember/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Focused worktree tests exercise the facade and operation payloads. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-06-12T19:06+02:00 — Issue #83: closeout worklist covers the unverified committed range (`closeout_changed_paths` in `closeout.py`, `committed_changed_paths`/`commit_text_or_none` in `git.py`), the onboarding plan gained the two-tier `working_paths` split with the non-blocking `unonboarded` report, body gates baseline at `contract_memory_verified_commit`, and scaling payload lists are bounded to count + sample.
- 2026-06-11T06:47+02:00 — No route impact: issue #62 removed the direct-closeout functions from `closeout.py`, the `direct-closeout` CLI subcommand from `cli.py`, and the facade re-exports — closeout is worktree-only; the module split this overview describes is unchanged (detail in the file sidecars).
- 2026-06-10T09:56+02:00 — GitHub #54 sub-task D: added `sync.py` (worktree_sync mid-task base sync) and `guidance.py`'s fetch-free `freshness` status block; `args.py` gained `memory_sync_choice`.
- 2026-06-10T09:30+02:00 — GitHub #54 sub-task B: `start.py` gained the stale-base preflight (`stale_base_choice` recoveries) and the memory source branch auto-template; `args.py` gained `stale_base_choice`.
- 2026-06-10T07:35+02:00 — GitHub #53: added `provider_async.py` (background provider setup launch, progress projection, teardown guard); `start.py` split preflight from launch and writes the contract before launching; cleanup/abandon gained the live-setup guard.
- 2026-06-10T05:20+02:00 — Issue #56 sub-task 2: route overviews get the same body gate scoped to nearest-governing routes (`No route impact:` marker; ancestors report as `stamped_without_body_review`), surfaced in closeout previews and apply payloads.
- 2026-06-10T04:47+02:00 — Issue #56 sub-task 1: `onboarding.py`'s content gate became the four-case body/history classification with in-band `No content impact:` attestation, shared parsing helpers moved to `kernel/onboarding_doc.py` (facade re-exports kept), and closeout payloads surface attested sidecars.
- 2026-06-01T00:00+02:00 — Added `abandon.py` (discard without integration) and `provider_teardown.py` (full-reclaim Docker + rmtree teardown) to the Purpose and Hot Path Summary listings.
- 2026-05-31T12:30+02:00 — Documented the new `args.py` typed `WorktreeArgs` cross-layer DTO replacing `argparse.Namespace` and `integrate.py`'s atomic all-or-nothing fast-forward behavior (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created when `c-09-git-worktree-manager` skill worktree lifecycle logic was split into focused implementation modules.
