# mcp/src/agents_remember/worktrees/modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `mcp/src/agents_remember/worktrees/modules` |
| lastUpdated            | 2026-07-18T20:03+02:00 |
| lastVerifiedCommitHash | `7ca29c3b6dd2c0184253e2690f1ebe78c511573b` |
| lastVerifiedCommitDate | 2026-07-18T20:18:51+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Purpose

The `worktrees/modules` package contains the extracted implementation modules
behind the `git_worktree_manager.py` facade. It separates Git adapters, lifecycle
status guidance, start preparation, onboarding refresh, closeout, integration,
cleanup, lifecycle finalization, abandon, provider teardown, start-contract leaf-ref normalization, the typed cross-layer argument DTO, and CLI
argument wiring while preserving the public facade import path. Reopen is deliberately NOT here:
`task_reopen` lives in the tasks package (L11) because it reopens a task, and this route's start path
merely honors its `cleanup: reopened` tombstone (recreate fresh, restamp the leaf doc's lifecycle).

## Hot Path Summary

- `git.py` owns raw Git subprocess operations and small repository state checks,
  including `committed_changed_paths` (issue #83: the unverified committed
  range — tree-diff `base..HEAD` ∩ `verified..HEAD`) and the
  `commit_text_or_none` baseline reader behind the closeout body gates.
  **Operations-integration L3** adds `changed_files_with_counts(repo, base, head=None)`
  (+ `_rename_aware_path`) — the change-set primitive behind the serving change-set API
  (`serving/changeset.py`): per-file `{path, insertions, deletions, status}` via
  `git diff --numstat --name-status --find-renames`, KEEPING deletions and reporting
  counts (binary → `None`, untracked → `A`, rename → post-rename path), unlike the
  name-only `changed_*_paths`.
- `guidance.py` renders lifecycle phase and typed next-operation payloads. Its
  `lifecycle_guidance` checks the disposal states first: `cleanup == "completed"`
  → the `cleanup-completed` phase, and (slice 05l P1) `cleanup == "abandoned"` →
  a dedicated `abandoned` phase (`nextOperation: "done"`). Before the abandoned
  branch a torn-down worktree fell through to the `worktree-started` default, so
  the dashboard rendered it as fully active; the explicit phase lets the observer
  reducer (`_GUIDANCE_PHASE`) project the teardown for the 05k render. **Slice 09**
  removed the dirty-tree → `commit-approval-pending` branch (a visibility bug):
  `lifecycle_guidance` no longer infers a commit-approval gate from `git status`,
  so a dirty worktree falls through to its honest lifecycle-position phase
  (closeout-completed → `integration-pending`, etc.). `commit-approval-pending` is
  owned by the closeout preview (`closeout.py`) and, once the gate plane is adopted,
  by a raised `closeout-approval` `GateNode` — never the working tree; the unused
  `contract_has_worktree_changes` import was dropped. **Slice 05m**
  adds the public `carryover_done(contract) -> (done, carryoverDoneAt)`: it reads the
  OFFICIAL ledger (`memory_repo_path/memory.md` via `load_ledger`/`find_mapping`) to
  detect whether the landed code commit (`integrated_code_commit`, else `code_commit`)
  was carried home, returning the carry commit's `%cI` as the milestone (external-only;
  internal/disabled → `(True, "")`). `lifecycle_guidance` now splits the
  `integration_status == "completed"` branch on it — not carried → phase
  `carryover-pending` routing the existing `memory_carryover_apply` (carryover must run
  while the parked memory branch still exists), carried → `cleanup-pending` carrying
  `carryoverDoneAt`.
- `landing.py` (slice 5h; hardened 5l P2) observes the successful-landing arc
  best-effort — `git ls-remote` branch tips (`origin/<feat>`, `origin/mem-main`) +
  a best-effort `gh pr list`, all timeout-bounded and `stdin=DEVNULL` (the #49
  stdio-pipe guard), gated to the landing window (closeout-completed onward) so the
  status poll stays network-free during the build phase; `guidance.py`'s
  `status_payload` emits its result as the `landing` block, and the observer reducer
  composes it onto `EngineProcessNode.landing`. Probe failures degrade to
  `factState: "missing"` — never faked. **Slice 5l P2** hardens the probe so the
  dashboard can follow a REAL remote landing: the protected target `origin/<base>`
  is now probed **directly** via `ls-remote` (`_main_ref` + `_default_branch`,
  resolving origin's default branch from the remote HEAD symref, no `fetch`) —
  visible across the whole landing window before any PR and even when `gh` is
  absent, with its `state` honestly tracking whether THIS work landed
  (`merged`/`planned`/`unknown`) rather than merely whether main exists; and the PR
  ref carries gh's own open/merge timestamp (`at` = `mergedAt` once merged, else
  `createdAt`). It re-fires every projector tick (~1s), so no milestone hook is
needed for cadence.
260712-TRH-L7 changes the landing guidance boundary: `status_payload` remains the explicit
interactive fresh-probe surface, while `projected_status_payload` consumes only a pre-observed
immutable landing snapshot. The recurring projector therefore never invokes `git ls-remote` or
`gh` through guidance; missing and stale observations remain explicit.
- `start.py`, `start_contract.py`, `leaf_ref_start.py`, `closeout.py`, `integrate.py`, `cleanup.py`,
  `finalize.py`, and `abandon.py`
  own the named `c-09-git-worktree-manager` skill lifecycle operations.
  `start.py` calls `start_contract.build_start_contract` to resolve the requested leaf ref through the
  `worktrees/leaf_refs.py` task-tree resolver before any start write; accepted refs persist the canonical
  task doc id in the leaf contract, while no-match/ambiguous refs return a `WorktreeCommandResult`
  refusal naming the expected `<repo>/<master-folder>/<doc-id>` form and candidates. Standalone/light
  task roots resolve through their non-master `task.json` doc id, slug/folder, and enclosure aliases, and
  resolver indexing skips sibling JSON artifacts unless they carry the task-document schema marker. After
  that, `start.py` runs a synchronous
  provider preflight, writes the contract, and
  then launches provider setup in the background (GitHub #53): dry runs stay
  synchronous, real starts return `starting` within seconds, and
  `retry_provider_setup` relaunches a failed/stale setup on an existing
  contract. Before any worktree exists, `start.py` also runs the stale-base
  preflight (GitHub #54): source branches behind/diverged from their upstream
  block the start with `stale_base_choice` recoveries (`fast-forward` /
  `proceed-stale`), and a missing external memory source branch is
  auto-created at the official memory tip using the code branch name as
  template. For master tasks, `start_contract.py` creates or loads the root
  `series-contract.md` integration contract first, creates the integration branch from the protected/source
  branch, and then starts each leaf from that integration branch with its own
  `enclosures/<leaf-id>/series-contract.md`. `cleanup.py`/`abandon.py` refuse to tear down while a live
  (fresh-heartbeat) background setup owns the worktree. **Slice 05m** makes
  `cleanup.py` carryover-guarded and work-branch-retiring: `cleanup_result` now HARD-REFUSES
  (raises) when integration is completed but `guidance.carryover_done` is false (external
  memory) — cleanup deletes the parked memory branch carryover reads from, so the carry
  must run first; the proof is the official ledger, not a contract stamp. After the guard
  it retires work branches only after proving they are reachable from the contract's
  recorded source branch (`merge-base --is-ancestor work_branch source_branch`), then
  deletes them with `git branch -D`; this avoids Git's ambient `HEAD`/upstream merge
  target while preserving unmerged work branches as `kept_branches`. Task 14 corrected
  cleanup to operate on the just-finalized child edge only: it removes the task work
  branches (`code`, `memory`, optional `memory_integration`) and keeps parent/source
  branches for their own lifecycle edge. Cleanup
  dry-runs also model scheduled removals: registered worktrees and `provider-runtime/`
  are subtracted before the worktree group directory is classified, so a group that will
  become empty reports `would_remove` rather than `not-empty`; real cleanup still removes
  directories only after they are actually empty. Task 32 also makes cleanup reclaim the
  observer drift snapshot generated by the code worktree it is deleting: dry-runs report
  the exact snapshot under `drift_snapshots["code"]`, and real cleanup removes only that
  contract-owned repository/branch snapshot. `integrate.py` refuses while an undecided or policy-invalid `master-handover-approval` gate addressed to the integrating master exists anywhere in the workspace: the pure `handover_gate_guard` folds every gate log (`GateStore.all_current`) and matches gates by `enclosure` against the contract's `task_name`/`parent_task_name` — never the consuming contract's lifecycle — evaluating the controller-threaded configured policy (the master-exit seam consumer, mirroring the closeout gate; gateless stays additive). Since cycle 7 the guard is evaluated on the dry run too — reported (`handover_gate` in the preview, whose summary names `handover-gate-blocked` when the real run would refuse) but enforced only on the real run, with no contract mutation on the dry-run path — and the pure sibling `unmatched_handover_gate_warning` puts a `handover_gate_warning` (unmatched OPEN handover gates + a verify-the-enclosure-spelling note) on gateless dry-run/integrated payloads, so a typo'd exact-string address cannot fail open silently. It then performs the code and
  memory fast-forwards atomically: it pre-validates that both fast-forwards are
  possible before mutating either branch and rolls both heads back on any
  memory-side failure, so integration never lands a half-integrated state.
  `abandon.py` is the discard-without-integration sibling: it reclaims the
  isolated provider stack and removes worktrees/branches without requiring a
  prior integration.
- `finalize.py` owns the terminal `lifecycle_finalize_task` operation. It
  refuses until closeout and integration are complete, the landed code commit is
  an ancestor of the recorded local source branch, and external-memory carryover
  is done; then it runs or verifies cleanup and marks the leaf task plus
  immediate parent row `Completed` when task-document paths are supplied. The
  proof is one parent-child branch edge at a time. PR-gated flows are identical
  after the PR merge has been pulled locally, while squash-merge equivalence is
  not inferred by default.
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
  and is re-exported here. Closeout preview and apply also pass
  `context.storage` explicitly to route-index generation, preserving the same
  repository/path-rule authority used when the onboarding plan was resolved.
- The closeout worklist (issue #83) is `closeout.py`'s
  `closeout_changed_paths`: working tree ∪ the unverified committed range, so
  transported history (merges, pre-committed slices) gates and stamps like
  hands-on edits. The onboarding plan's two-tier split (`working_paths`) keeps
  missing-sidecar blocking on working-tree paths only; committed-range paths
  without onboarding surface as the non-blocking `unonboarded` report. Body
  gates baseline against `contract_memory_verified_commit` so memory work
  committed before closeout classifies honestly, and payload lists that scale
  with transported history are exposed as count + sample
  (`PATH_SAMPLE_LIMIT`). Slice 6b adds **server-side gate enforcement** to
  `closeout.py`: when the contract has a `lifecycle_id`, closeout refuses unless
  the lifecycle's `closeout-approval` gate is developer-approved or approved by
  a policy-valid delegated orchestration decision
  (`controlplane.evaluate_closeout_gate(..., policy=args.gate_policy)`), marks it `applied` on success, and
  reports a `closeout_gate` block; gateless lifecycles keep the chat commit gate.
  Task 30 adds the already-integrated re-closeout reset: closeout source-head
  validation accepts the recorded integrated tips, preview reports
  `integration_reopen.would_reopen`, and apply reopens `integration_status` only
  when the new code or memory-content commit is not yet on the recorded source
  branch. Clean no-op re-closeout keeps the completed integration state and does
  not duplicate an already-present ledger mapping.
- `args.py` defines the frozen `WorktreeArgs` cross-layer DTO that operation
  modules consume in place of `argparse.Namespace`; `from_namespace` builds it
  from partial CLI/controller namespaces with per-field defaults. It carries `parent_task` and `leaf_id`
  for nested active task-root and leaf-enclosure resolution.
- `cli.py` keeps command-line parsing and JSON print adapters out of operation
  modules and converts each parsed namespace into `WorktreeArgs` at the boundary.
  Its `heal-leaf-ids` subcommand (260712-PTS-L1) is the deliberate invocation seam for
  `worktree_contract.heal_contract_leaf_ids` (`--coordination-root`, `--dry-run`; prints the heal
  report JSON) and intentionally bypasses `WorktreeArgs` — the heal is a one-shot legacy leaf-id
  migration sweep, never a per-read side effect, now that `load_contract` is walk-free and never
  normalizes.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The package is imported through the public worktree manager facade. | [git_worktree_manager.py](agents-remember/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Focused worktree tests exercise the facade and operation payloads. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Finalizer tests cover landed-commit proof, cleanup blocking, dry-run, and task-document reconciliation. | [test_lifecycle_finalize.py](agents-remember/mcp/tests/test_lifecycle_finalize.py) |
| Closeout onboarding refresh uses resolved storage authority for deterministic route-index preview and apply. | [onboarding.py](agents-remember/mcp/src/agents_remember/worktrees/modules/onboarding.py); [route_index.py](agents-remember/mcp/src/agents_remember/kernel/route_index.py) |

## Update History
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: closeout route-index preview and apply now forward the
  resolved `context.storage` authority explicitly to the deterministic builder.
- 2026-07-12T19:55+02:00 — 260712-PTS-L1 route impact (small): `cli.py` gained the `heal-leaf-ids`
  subcommand — the explicit one-shot seam for `worktree_contract.heal_contract_leaf_ids` now that
  contract loads are walk-free and never normalize legacy leaf ids (detail in the `cli.py` and
  `worktree_contract.py` sidecars). The module split this overview describes is unchanged.
  Verification metadata pinned until closeout stamps the 260712-PTS-L1 commit.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: worktree guidance separates fresh interactive landing probes from projected status, which consumes only pre-observed landing facts.

- 2026-07-07T23:45+02:00 — 260707-HFX-L4R2 route impact: start leaf-ref resolution now accepts
  standalone/light `task.json` roots through doc-id/slug/folder aliases and the shared resolver skips
  non-task sibling JSON artifacts by schema marker while keeping malformed task docs loud. Verification
  metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4 route impact: worktree start contract construction and
  leaf-ref validation moved out of `start.py` into `start_contract.py`/`leaf_ref_start.py`, backed by
  the dedicated `worktrees/leaf_refs.py` resolver; accepted refs
  persist doc ids, and invalid refs refuse before start writes. Verification metadata pinned until
  closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T19:30+02:00 — No route impact: 260707-HFX-L2 refines `start.py`'s memory mtime sync
  in place — divergent-content files keep fresh checkout mtimes so the grepai watcher re-embeds
  exactly the delta instead of silently skipping it (detail in the start.py sidecar and the new
  `test_provider_index_lifecycle.py`). No module added; the modules route model is unchanged.
- 2026-07-07T18:40+02:00 — No route impact: 260703-L18 finding 7 implements `start.py`'s
  missing-ledger-mapping recovery `memory_choice="reconciliation"` (records the unmapped code base ->
  the ledger's memory content tip the way closeout ledger syncs do, then proceeds to a started worktree)
  and prunes the block to only executable choices (`custom` removed). It reuses the existing
  `memory_choice` arg and adds no module, so the modules route model this overview describes is unchanged
  (detail in the `start.py` file sidecar).
- 2026-07-07T06:10+02:00 — No route impact: PR #100 review fixes (merge `e358c4a`) hardened
  `start.py`'s `_reconcile_missing_mapping` with a memory-source-branch guard (refuses when the
  official memory repo is checked out elsewhere; detail in the start.py sidecar). No module added;
  the modules route model is unchanged. Post-merge onboarding refresh, developer-approved.
- 2026-07-06T03:30+02:00 — No route impact: 260703-L11 reviewed `guidance.status_payload`'s `code_worktree_exists`/`memory_worktree_exists` probes as the existence-reporting contract the new projection flags mirror; no file in this route changed — the stat happens in `observer/snapshots.py`.
- 2026-07-05T19:55+02:00 — 260703-L8 route impact (cycle 7, small): integrate's dry run now evaluates-and-reports the seam guard (`handover_gate` in the preview; enforcement stays real-run-only; no dry-run contract mutation, AR4-2), and the new pure `unmatched_handover_gate_warning` surfaces unmatched OPEN handover gates as a `handover_gate_warning` enclosure spelling check on gateless results (AR4-1b). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 — 260703-L8 route impact (cycle 6, small): the integrate seam guard is re-addressed — the pure `handover_gate_guard` folds every gate log (`GateStore.all_current`) and matches `master-handover-approval` gates by `enclosure` against the contract's `task_name`/`parent_task_name`, replacing the inert `contract.lifecycle_id` lookup; the configured policy now reaches it from the controller. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:24+02:00 — 260703-L8 route impact (cycle 5, small): `integrate_result` enforces the master-exit seam — an existing `master-handover-approval` gate must be policy-valid-approved (mirror of the closeout gate; gateless stays additive) or the run returns handover-gate-blocked. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:32+02:00 — No route impact: abandon docstring vocabulary updated to the `l-01-agent-lifecycles` orchestrator read-only/abandon exit; no behavior change (260703-L9).
- 2026-07-04T12:32+02:00 — 260703-L4 route impact: closeout preview/apply now
  threads the trusted gate policy through `WorktreeArgs` and evaluates
  `closeout-approval` through that policy, preserving human approvals while
  allowing only configured delegated orchestration approvals. Verification
  metadata pinned until closeout stamps the L4 commit.
- 2026-07-03T00:35+02:00 — L11 route impact: start's existing-contract branch recreates fresh for cleanup in {abandoned, reopened} and restamps the leaf doc's lifecycleId post-write; abandon's controller ends its anchored ambient lifecycle. The reopen implementation itself lives under tasks/.
- 2026-06-29T23:18+02:00 — No route impact: `start.py` now derives the recorded memory base from the memory source branch tip (`_memory_base_for_source`) instead of the repo HEAD; the module structure and route model are unchanged (detail in the start.py file sidecar; task 260629_post-landing-cleanup L3).
- 2026-06-29T15:30+02:00 — operations-integration L3: `git.py` gained `changed_files_with_counts` (+ `_rename_aware_path`), the counts/status change-set primitive (keeps deletions; binary → `None`; untracked → `A`; rename → post-rename path) feeding the L3 serving change-set API (`serving/changeset.py`). Refreshed the `git.py` Hot Path bullet. The module split this overview describes is unchanged. Verification metadata pinned to the task base until closeout stamps the L3 code commit.
- 2026-06-27T23:09+02:00 — Task 32 route impact: refreshed the `cleanup.py` hot-path paragraph for exact observer drift-snapshot reclamation during worktree cleanup, including dry-run reporting and the contract-owned repository/branch boundary. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T21:10+02:00 — Task 30: refreshed the closeout hot-path summary for
  already-integrated re-closeout behavior: integrated source tips are valid
  closeout bases, closeout previews expose pending integration reopen, apply
  reopens only for unlanded new code/memory content, and clean no-op re-closeout
  avoids duplicate ledger mapping. Verification metadata pinned until closeout
  stamps the task-30 code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: worktree modules now treat a master root `series-contract.md` as the integration branch contract and each leaf `enclosures/<leaf-id>/series-contract.md` as worktree material; `WorktreeArgs` carries `parent_task`/`leaf_id`, and finalization can archive completed root tasks. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T00:03+02:00 — Task 14 cleanup correction: refreshed the `cleanup.py` hot-path paragraph for child-edge cleanup. Cleanup still hard-guards on carryover and proves task work branches against the contract source branch before deleting them, but no longer retires parent/source branches; those branches are finalized by their own lifecycle edge.
- 2026-06-23T22:50+02:00 — Dashboard task 14: added `finalize.py` to the route model. The terminal finalizer proves one landed parent-child edge, runs or verifies cleanup, and marks the current task plus immediate parent row complete; PR-gated edges reduce to the same local ancestry proof after merge/pull, and squash equivalence is intentionally out of the default path. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T15:09+02:00 — Task 13 cleanup correctness: refreshed the `cleanup.py` hot-path paragraph for source-branch-proof work-branch deletion (`merge-base --is-ancestor work_branch source_branch`, then `branch -D`), preserved kept-branch reporting for unmerged work, separated the then-existing source-branch retirement path from task work-branch deletion, and noted dry-run directory classification now subtracts scheduled worktree/provider-runtime removals while real cleanup stays empty-dir-only. Task 14 later removed source-branch retirement from cleanup.
- 2026-06-23T07:25+02:00 — slice 09 (gate-signal adoption, S1 visibility fix): refreshed the `guidance.py` Hot Path bullet for the removal of the dirty-tree → `commit-approval-pending` branch — `lifecycle_guidance` no longer reads a commit-approval gate off `git status`; a dirty worktree falls through to its honest lifecycle-position phase (closeout-completed → `integration-pending`). The gate is owned by the closeout preview / a raised `closeout-approval` `GateNode`; the unused `contract_has_worktree_changes` import was dropped. The module split this overview describes is unchanged; detail in the `guidance.py` sidecar. Verification metadata pinned until closeout stamps the slice-09 code commit.
- 2026-06-21T06:40+02:00 — slice 05m (carryover-before-cleanup + work/source branch retirement): refreshed the `guidance.py` Hot Path bullet for the new public `carryover_done` (reads the official ledger to detect the carry; external-only) and the `integration_status == "completed"` split into the `carryover-pending` (routes `memory_carryover_apply`) vs `cleanup-pending` (carries `carryoverDoneAt`) phases; and the `cleanup.py` bullet for the carryover hard-guard (refuses cleanup before the carry, since it deletes the parked memory branch) plus the new `_retire_branch` / `delete_remote_branch_if_present` retirement of BOTH the worktree and (PR'd) source branches — local for code + memory, remote for the code source branch. Verification metadata pinned until closeout stamps the 05m code commit.
- 2026-06-21T05:30+02:00 — slice 05l P2 (landing-arc probe hardening): refreshed the `landing.py` Hot Path bullet for the direct `origin/<base>` probe (`_main_ref` + the new `_default_branch`, resolving origin's default via the remote HEAD symref with no `fetch`) — visible across the whole landing window before any PR and independent of `gh`, its `state` tracking whether THIS work landed rather than merely whether main exists — and the PR ref's new `at` timestamp (gh's mergedAt/createdAt). The probe re-fires every projector tick (~1s) so no milestone hook is needed. Carryover/cleanup lifecycle correctness is 05m's scope, not here. Detail in the `landing.py` sidecar. Verification metadata pinned until closeout stamps the 05l-P2 code commit.
- 2026-06-21T04:10+02:00 — slice 05l P1 (backend teardown visibility, Gap A): `guidance.py`'s `lifecycle_guidance` gained a `cleanup == "abandoned"` branch (right after `cleanup == "completed"`) returning a dedicated `abandoned` phase (`nextOperation: "done"`); before this an abandoned worktree fell through to the `worktree-started` phantom. The observer reducer maps the phase for the 05k teardown render. Detail in the `guidance.py` sidecar. Verification metadata pinned until closeout stamps the 05l-P1 code commit.
- 2026-06-18T12:10 — Task 6 slice 6b: `closeout.py` gained server-side gate enforcement (refuse unless the lifecycle's `closeout-approval` gate is developer-approved via `controlplane.evaluate_closeout_gate`; mark `applied`; `closeout_gate` payload). The module split this overview describes is unchanged. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T08:51+02:00 — slice 5h H1: added `landing.py` (best-effort successful-landing arc observation — `git ls-remote` branch tips + best-effort `gh` PR state, gated to the landing window) to this route; `guidance.py`'s `status_payload` emits its `landing` block. Detail in the file sidecars. Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-16T03:25 — No route impact: slice 5f S6 (§9) adds the happy-path start-progress emits to `start.py` (`_record_start_progress` at the `preflight` / `code-worktree` success points, closing the gap where only blocked early returns emitted); the modules route model this overview describes is unchanged (detail in the `start.py` file sidecar).
- 2026-06-15T19:35 — No route impact: slice 5e (§5.4) adds best-effort start-progress writes to `start.py` (`_record_start_block` / `_clear_start_block` at the pre-contract blocked returns); the modules route model this overview describes is unchanged (detail in the `start.py` file sidecar).
- 2026-06-13T18:45+02:00 — No route impact: slice 2c threads `lifecycle_id` through `args.py`/`start.py` (`_build_start_contract` stamps the observable-lifecycle contract anchor) and emits it from `guidance.py`'s `status_payload`; the modules route model this overview describes is unchanged (detail in the file sidecars).
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
